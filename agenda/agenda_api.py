"""
Agenda CJ Medical — API REST
============================
Corrige agenda_api_full.py. Lo que cambió y por qué:

1. PREFIJOS.  nginx hace `proxy_pass http://127.0.0.1:8001/` con barra final,
   y eso BORRA el `/api/`. Las rutas declaradas como "/api/v2/x" quedaban en
   404 desde el dominio (funcionaban solo llamando a localhost:8001 directo).
   Ahora todo se registra una vez y se monta en cuatro prefijos, así que
   responde igual por "/x", "/v2/x", "/api/x" y "/api/v2/x". Nada se rompe.

2. huecos/dia pasaba `paso=>` y el parámetro se llama `p_paso` → fallaba siempre.

3. Mover una cita insertaba en cita_bitacora(... notas) y esa columna no
   existe; la tabla usa `detalle jsonb` → 500 en cada movida.

4. Los bloqueos llamaban a agendar_cita con cliente nulo, y esa función exige
   cliente → nunca se creaban. Ahora se insertan como tipo='bloqueo'.

5. indicadores armaba "2026-09-31", que no es una fecha → error en todo mes
   de 30 días. Ahora usa aritmética de fechas.

6. La agenda del día hacía INNER JOIN con clientes y servicios, así que los
   bloqueos y las citas sin servicio desaparecían. v_agenda ya trae todo.

7. Las conexiones a Postgres nunca se cerraban: con el uso se agotan. Ahora
   cada consulta abre y cierra.

8. Los errores de negocio (CUPO_TOMADO, ALMUERZO, FUERA_DE_HORARIO…) salían
   como 500 con traceback. Ahora salen como 409/400 con el mensaje.
"""
import base64
import hashlib
import hmac
import os
import secrets
from contextlib import contextmanager
from datetime import date, datetime, timedelta
from typing import List, Optional

import psycopg2
import psycopg2.extras
from fastapi import (APIRouter, Depends, FastAPI, HTTPException, Query,
                     Request, Response)
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

DATABASE_URL = os.environ.get(
    "DATABASE_URL", "postgresql://postgres@127.0.0.1:5432/cjmedical")

# Token para los servicios (Hermes). Se pone en la variable de entorno
# API_TOKEN del servicio; nunca se escribe en este archivo.
API_TOKEN = os.environ.get("API_TOKEN", "").strip()

# Desde qué sitios se puede llamar a la API con sesión. Por defecto solo el
# dominio de la agenda: con "*" cualquier página web podría hacer peticiones
# con la cookie de la recepcionista.
ORIGENES = [o.strip() for o in os.environ.get(
    "ORIGENES", "https://agenda.universojota.tech").split(",") if o.strip()]
COOKIE_SEGURA = os.environ.get("COOKIE_SEGURA", "1") != "0"
HORAS_SESION = int(os.environ.get("HORAS_SESION", "12"))

app = FastAPI(title="Agenda CJ Medical", version="3.1")
app.add_middleware(CORSMiddleware,
                   allow_origins=ORIGENES,
                   allow_origin_regex=".*" if ORIGENES == ["*"] else None,
                   allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])

rp = APIRouter()   # abierto: salud y entrada
r  = APIRouter()   # necesita sesión de operador (o el token de servicio)
ra = APIRouter()   # solo administrador

# ─────────────────────────────────────────────────────────── base de datos ──
MARCAS = ("CUPO_TOMADO", "CUPO_APARTADO", "FUERA_DE_HORARIO", "ALMUERZO",
          "CLIENTE_NO_EXISTE", "HORA_INVALIDA", "CITA_NO_EXISTE",
          "ESTADO_NO_EXISTE", "FALTA_DOCUMENTO", "FALTA_ESTADO_MOVIDO",
          "FECHA_INVALIDA", "ESPECIALISTA_NO_EXISTE", "SEDE_NO_EXISTE")


@contextmanager
def cursor():
    """Abre y CIERRA. La versión anterior dejaba la conexión abierta en cada
    request; con tráfico real Postgres se queda sin cupos."""
    conn = psycopg2.connect(DATABASE_URL)
    conn.autocommit = True
    try:
        with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
            yield cur
    finally:
        conn.close()


def traducir(e: Exception):
    """Un error de negocio no es un 500. Devuelve el código y el mensaje que
    el front y el agente saben interpretar."""
    txt = str(getattr(e, "pgerror", None) or e).strip().splitlines()[0]
    for m in MARCAS:
        if m in txt:
            codigo = 409 if m in ("CUPO_TOMADO", "CUPO_APARTADO") else 400
            return HTTPException(codigo, txt[txt.index(m):])
    if isinstance(e, psycopg2.errors.ExclusionViolation):
        return HTTPException(409, "CUPO_TOMADO: ya hay una cita en ese horario")
    return HTTPException(500, txt)


def todos(sql, params=()):
    with cursor() as cur:
        try:
            cur.execute(sql, params)
            return cur.fetchall()
        except Exception as e:
            raise traducir(e)


def uno(sql, params=(), falta="No encontrado"):
    with cursor() as cur:
        try:
            cur.execute(sql, params)
            fila = cur.fetchone()
        except Exception as e:
            raise traducir(e)
    if fila is None:
        raise HTTPException(404, falta)
    return fila


def ejecutar(sql, params=()):
    with cursor() as cur:
        try:
            cur.execute(sql, params)
        except Exception as e:
            raise traducir(e)
    return {"ok": True}


def hm(v):
    return str(v)[:5] if v is not None else None


# ──────────────────────────────────────────────────────── entrada y sesión ──
# Las contraseñas se guardan con PBKDF2-SHA256 y sal propia. Se usa solo la
# librería estándar a propósito: una dependencia menos que instalar en el VPS.
ITERACIONES = 210_000


def hash_clave(clave: str) -> str:
    if not clave or len(clave) < 8:
        raise HTTPException(400, "CLAVE_CORTA: la contraseña debe tener al menos 8 caracteres")
    sal = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", clave.encode(), sal, ITERACIONES)
    return "pbkdf2$%d$%s$%s" % (ITERACIONES, base64.b64encode(sal).decode(),
                                base64.b64encode(dk).decode())


def clave_correcta(clave: str, guardado: Optional[str]) -> bool:
    try:
        algo, it, sal, dk = (guardado or "").split("$")
        if algo != "pbkdf2":
            return False
        calc = hashlib.pbkdf2_hmac("sha256", (clave or "").encode(),
                                   base64.b64decode(sal), int(it))
        return hmac.compare_digest(calc, base64.b64decode(dk))
    except Exception:
        return False


def hash_token(t: str) -> str:
    return hashlib.sha256(t.encode()).hexdigest()


def abrir_sesion(usuario_id: str, agente: str = "") -> str:
    token = secrets.token_urlsafe(32)
    ejecutar("""insert into sesiones(token_hash, usuario_id, expira_en, agente)
                values(%s,%s,now() + (%s || ' hours')::interval, %s)""",
             (hash_token(token), usuario_id, HORAS_SESION, agente[:200]))
    ejecutar("update usuarios set ultimo_acceso = now() where id=%s", (usuario_id,))
    return token


def quien_es(req: Request):
    """Devuelve quién está llamando, o None. Dos formas de identificarse:
    el token de servicio (Hermes) o la cookie de sesión (las personas)."""
    cabecera = (req.headers.get("x-api-token")
                or req.headers.get("authorization", "").replace("Bearer ", "")).strip()
    if API_TOKEN and cabecera and hmac.compare_digest(cabecera, API_TOKEN):
        return {"tipo": "servicio", "id": "hermes", "nombre": "Hermes",
                "rol": "operador", "canal": "WhatsApp"}

    token = req.cookies.get("sesion") or req.headers.get("x-sesion", "")
    if not token:
        return None
    fila = None
    with cursor() as cur:
        cur.execute("""select u.id, u.nombre, u.correo, u.rol, u.canal, u.sede_id,
                              u.activo, s.expira_en
                         from sesiones s join usuarios u on u.id = s.usuario_id
                        where s.token_hash = %s""", (hash_token(token),))
        fila = cur.fetchone()
    if not fila or not fila["activo"] or fila["expira_en"] < datetime.now():
        return None
    # se renueva sola mientras la persona esté trabajando
    ejecutar("""update sesiones
                   set visto_en = now(),
                       expira_en = now() + (%s || ' hours')::interval
                 where token_hash = %s""", (HORAS_SESION, hash_token(token)))
    return {"tipo": "usuario", "id": fila["id"], "nombre": fila["nombre"],
            "correo": fila["correo"], "rol": fila["rol"], "canal": fila["canal"],
            "sede_id": fila["sede_id"]}


def hay_usuarios() -> bool:
    return uno("""select count(*) as n from usuarios
                   where activo and clave_hash is not null""")["n"] > 0


def sesion(req: Request):
    """Cualquiera que ya entró: recepción, call center o Hermes."""
    a = quien_es(req)
    if a is None:
        # Mientras no exista ninguna persona registrada la agenda queda abierta,
        # para poder crear la primera desde el propio navegador. En cuanto haya
        # una, deja de estarlo.
        if not hay_usuarios():
            return {"tipo": "arranque", "id": "arranque", "nombre": "Sin registrar",
                    "rol": "admin", "canal": "Recepcionista"}
        raise HTTPException(401, "SIN_SESION: hay que entrar con usuario y contraseña")
    return a


def admin(a=Depends(sesion)):
    if a.get("rol") != "admin":
        raise HTTPException(403, "SOLO_ADMIN: esta parte es solo del administrador")
    return a


class LoginReq(BaseModel):
    correo: str
    clave: str


class ClaveReq(BaseModel):
    actual: Optional[str] = None
    nueva: str


class UsuarioReq(BaseModel):
    nombre: str
    correo: str
    rol: str = "operador"
    canal: str = "Recepcionista"
    sede_id: Optional[str] = None
    nota: Optional[str] = None
    activo: bool = True
    clave: Optional[str] = None


class UsuarioEditReq(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[str] = None
    rol: Optional[str] = None
    canal: Optional[str] = None
    sede_id: Optional[str] = None
    nota: Optional[str] = None
    activo: Optional[bool] = None
    clave: Optional[str] = None


def _usuario_publico(u: dict) -> dict:
    """Nunca sale el hash de la contraseña de este servidor."""
    return {k: v for k, v in u.items() if k != "clave_hash"}


@rp.post("/auth/login")
def login(req: LoginReq, respuesta: Response, peticion: Request):
    ejecutar("select limpiar_sesiones()")
    u = None
    with cursor() as cur:
        cur.execute("""select * from usuarios
                        where lower(correo) = lower(%s) and activo""", (req.correo,))
        u = cur.fetchone()
    # se compara igual aunque el correo no exista, para no delatar cuáles sí
    ok = clave_correcta(req.clave, u["clave_hash"] if u else None)
    if not u or not ok:
        raise HTTPException(401, "DATOS_INCORRECTOS: revisa el correo y la contraseña")
    token = abrir_sesion(u["id"], peticion.headers.get("user-agent", ""))
    respuesta.set_cookie("sesion", token, httponly=True, samesite="lax",
                         secure=COOKIE_SEGURA, max_age=HORAS_SESION * 3600, path="/")
    return {"usuario": _usuario_publico(u), "sesion": token}


@rp.get("/auth/yo")
def auth_yo(peticion: Request):
    a = quien_es(peticion)
    if a is None:
        if not hay_usuarios():
            # primera vez: todavía no hay nadie, hay que crear al administrador
            return {"sesion": False, "sin_usuarios": True}
        raise HTTPException(401, "SIN_SESION")
    return {"sesion": True, "usuario": a}


@rp.post("/auth/logout")
def logout(peticion: Request, respuesta: Response):
    token = peticion.cookies.get("sesion") or peticion.headers.get("x-sesion", "")
    if token:
        ejecutar("delete from sesiones where token_hash=%s", (hash_token(token),))
    respuesta.delete_cookie("sesion", path="/")
    return {"ok": True}


@r.post("/auth/clave")
def cambiar_clave(req: ClaveReq, a=Depends(sesion)):
    if a["tipo"] != "usuario":
        raise HTTPException(400, "Esta cuenta no usa contraseña")
    u = uno("select * from usuarios where id=%s", (a["id"],), "Usuario no encontrado")
    if not clave_correcta(req.actual or "", u["clave_hash"]):
        raise HTTPException(401, "DATOS_INCORRECTOS: la contraseña actual no coincide")
    ejecutar("update usuarios set clave_hash=%s where id=%s",
             (hash_clave(req.nueva), a["id"]))
    ejecutar("delete from sesiones where usuario_id=%s", (a["id"],))
    return {"ok": True, "mensaje": "Contraseña cambiada. Hay que entrar de nuevo."}


@ra.get("/usuarios")
def usuarios_list():
    return [_usuario_publico(u) for u in
            todos("select * from usuarios order by nombre")]


@ra.put("/usuarios/{uid}")
def usuario_guardar(uid: str, req: UsuarioEditReq):
    campos = {k: v for k, v in req.dict().items()
              if v is not None and k != "clave"}
    if req.rol and req.rol not in ("admin", "operador"):
        raise HTTPException(400, "El rol tiene que ser admin u operador")
    if req.clave:
        campos["clave_hash"] = hash_clave(req.clave)
    if not campos:
        raise HTTPException(400, "Nada que actualizar")
    existe = uno("select count(*) as n from usuarios where id=%s", (uid,))["n"]
    if existe:
        partes = ", ".join(f"{k}=%({k})s" for k in campos)
        campos["__id"] = uid
        ejecutar(f"update usuarios set {partes} where id=%(__id)s", campos)
    else:
        if not campos.get("nombre") or not campos.get("correo"):
            raise HTTPException(400, "Falta nombre o correo")
        cols = ", ".join(["id"] + list(campos))
        vals = ", ".join(["%(__id)s"] + [f"%({k})s" for k in campos])
        campos["__id"] = uid
        ejecutar(f"insert into usuarios({cols}) values({vals})", campos)
    # si se desactiva o se le cambia la clave, se le cierran las sesiones
    if req.activo is False or req.clave:
        ejecutar("delete from sesiones where usuario_id=%s", (uid,))
    return _usuario_publico(uno("select * from usuarios where id=%s", (uid,),
                                "Usuario no encontrado"))


@ra.delete("/usuarios/{uid}")
def usuario_borrar(uid: str):
    ejecutar("delete from sesiones where usuario_id=%s", (uid,))
    ejecutar("update usuarios set activo=false where id=%s", (uid,))
    return {"ok": True, "mensaje": "Usuario desactivado"}


# ────────────────────────────────────────────────────────────────── modelos ──
class ClienteCrear(BaseModel):
    documento: str; primer_nombre: str; primer_apellido: str
    telefono: str = ""; correo: Optional[str] = None; sede: Optional[str] = None


class ClienteEditar(BaseModel):
    documento: Optional[str] = None; primer_nombre: Optional[str] = None
    segundo_nombre: Optional[str] = None; primer_apellido: Optional[str] = None
    segundo_apellido: Optional[str] = None; telefono: Optional[str] = None
    correo: Optional[str] = None; sede_id: Optional[str] = None
    notas: Optional[str] = None
    tipo_doc: Optional[str] = None; ciudad: Optional[str] = None
    genero: Optional[str] = None; tipo_cliente: Optional[str] = None
    dia_nac: Optional[int] = None; mes_nac: Optional[int] = None


class BuscarCliente(BaseModel):
    telefono: Optional[str] = None
    documento: Optional[str] = None
    nombre: Optional[str] = None


class HuecosRequest(BaseModel):
    fecha: date; sede: Optional[str] = None
    especialista: Optional[str] = None; servicio: Optional[str] = None
    duracion: Optional[int] = None; paso: int = 15


class BuscarHuecosReq(BaseModel):
    desde: Optional[date] = None; dias: int = 14
    sede: Optional[str] = None; especialista: Optional[str] = None
    servicio: Optional[str] = None; duracion: Optional[int] = None
    paso: int = 15; limite: int = 40


class ApartarCupoReq(BaseModel):
    especialista: str; sede: str; fecha: date; inicio: str
    servicio: Optional[str] = None; minutos: int = 5; referencia: str = ""


class AgendarReq(BaseModel):
    cliente_id: str; especialista: str; sede: str; fecha: date
    inicio: str; servicio: Optional[str] = None; fin: Optional[str] = None
    canal: str = "WhatsApp"; por: str = ""
    notas: Optional[str] = None; reserva: Optional[str] = None


class CambiarEstadoReq(BaseModel):
    cita_id: str; estado: str; por: str = ""; motivo: Optional[str] = None


class ReprogramarReq(BaseModel):
    cita_id: str; fecha: date; inicio: str
    especialista: Optional[str] = None; sede: Optional[str] = None
    servicio: Optional[str] = None; motivo: str = ""; por: str = ""


class MoverCitaReq(BaseModel):
    fecha: Optional[date] = None; inicio: Optional[str] = None
    fin: Optional[str] = None; especialista_id: Optional[str] = None
    sede_id: Optional[str] = None; servicio_id: Optional[str] = None
    cliente_id: Optional[str] = None; notas: Optional[str] = None
    por: str = ""


class BloqueoReq(BaseModel):
    especialista: str; sede: str; fecha: date; inicio: str
    fin: str; motivo: str = "Bloqueo"; por: str = ""


class EspecialistaReq(BaseModel):
    nombres: str; apellidos: str = ""
    especialidad: Optional[str] = None
    color: Optional[str] = "#8A7C75"; activo: bool = True


class EspecialistaEditReq(BaseModel):
    nombres: Optional[str] = None; apellidos: Optional[str] = None
    especialidad: Optional[str] = None
    color: Optional[str] = None; activo: Optional[bool] = None


class EspecialistaUpsert(BaseModel):
    """Lo mismo, más las listas: así la agenda guarda la especialista completa
    (datos + sedes + servicios + horarios) en una sola llamada."""
    nombres: Optional[str] = None; apellidos: Optional[str] = None
    especialidad: Optional[str] = None; documento: Optional[str] = None
    correo: Optional[str] = None; telefono: Optional[str] = None
    color: Optional[str] = None; activo: Optional[bool] = None
    sedes: Optional[list] = None
    servicios: Optional[list] = None
    horarios: Optional[list] = None


class EspecialistaSedeReq(BaseModel):
    especialista_id: str; sede_id: str; activo: Optional[bool] = None


class EspecialistaServicioReq(BaseModel):
    especialista_id: str; servicio_id: str


class HorarioReq(BaseModel):
    especialista_id: str; dia: int; sede_id: str
    desde: str; hasta: str
    alm_desde: Optional[str] = None; alm_hasta: Optional[str] = None


class ServicioReq(BaseModel):
    nombre: str; duracion: int = 30; precio: Optional[float] = None
    codigo: Optional[str] = None; activo: bool = True


class ServicioEditReq(BaseModel):
    nombre: Optional[str] = None; duracion: Optional[int] = None
    precio: Optional[float] = None; codigo: Optional[str] = None
    activo: Optional[bool] = None


class SedeReq(BaseModel):
    nombre: str; ciudad: Optional[str] = None
    direccion: Optional[str] = None; telefono: Optional[str] = None
    hora_inicio: str = "09:00"; hora_fin: str = "19:00"
    puestos: int = 1; activo: bool = True


class SedeEditReq(BaseModel):
    nombre: Optional[str] = None; ciudad: Optional[str] = None
    direccion: Optional[str] = None; telefono: Optional[str] = None
    hora_inicio: Optional[str] = None; hora_fin: Optional[str] = None
    puestos: Optional[int] = None; activo: Optional[bool] = None


class EstadoReq(BaseModel):
    nombre: str; color: str = "#8A7C75"; tipo: str = "abierto"
    inicial: bool = False; transparente: bool = False
    orden: int = 50; activo: bool = True


# ──────────────────────────────────────────────────────────────── salud ────
@rp.get("/")
def raiz():
    return {"agenda": "CJ Medical", "version": "3.0"}


@rp.get("/health")
def health():
    try:
        with cursor() as cur:
            cur.execute("select count(*) as n from citas")
            n = cur.fetchone()["n"]
        return {"status": "ok", "db": "conectada", "citas": n}
    except Exception as e:
        return {"status": "error", "db": str(e)}


# ───────────────────────────────────────────── todo junto para la agenda ───
@r.get("/datos")
def datos():
    """Todo lo que la agenda web necesita al abrir, en LISTAS (antes venían
    como objetos indexados por id y el front no los reconocía)."""
    sedes = todos("""select id, nombre, codigo, ciudad, direccion, telefono,
                            hora_inicio, hora_fin, puestos, capacidad_dia,
                            dias_mes, activo
                       from sedes where activo order by nombre""")
    servicios = todos("""select id, nombre, codigo, duracion, precio, activo
                           from servicios where activo order by nombre""")
    estados = todos("""select id, nombre, color, tipo, inicial, transparente,
                              orden, activo
                         from estados where activo order by orden""")
    esp = todos("""
        select e.id, e.nombres, e.apellidos, e.especialidad, e.color, e.activo,
               coalesce((select array_agg(s.sede_id order by s.sede_id)
                           from especialista_sedes s
                          where s.especialista_id = e.id), '{}') as sedes,
               coalesce((select array_agg(x.servicio_id order by x.servicio_id)
                           from especialista_servicios x
                          where x.especialista_id = e.id), '{}') as servicios,
               coalesce((select json_agg(json_build_object(
                             'id', h.id, 'dia', h.dia, 'sedeId', h.sede_id,
                             'desde', to_char(h.desde,'HH24:MI'),
                             'hasta', to_char(h.hasta,'HH24:MI'),
                             'almDesde', to_char(h.alm_desde,'HH24:MI'),
                             'almHasta', to_char(h.alm_hasta,'HH24:MI'))
                             order by h.dia, h.desde)
                           from horarios h
                          where h.especialista_id = e.id), '[]') as horarios
          from especialistas e
         where e.activo
         order by e.nombres""")
    for s in sedes:
        s["hora_inicio"] = hm(s["hora_inicio"])
        s["hora_fin"] = hm(s["hora_fin"])
    return {"sedes": sedes, "servicios": servicios,
            "estados": estados, "especialistas": esp}


# ───────────────────────────────────────────────────────────── maestros ────
@r.get("/sedes")
def sedes_list():
    return todos("select * from sedes order by nombre")


@ra.post("/sedes")
def sedes_create(req: SedeReq):
    sid = "sede-cj-medical-" + req.nombre.lower().replace(" ", "-")[:40]
    ejecutar("""insert into sedes(id,nombre,ciudad,direccion,telefono,
                                  hora_inicio,hora_fin,puestos,activo)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
                on conflict(id) do update set nombre=excluded.nombre,
                  ciudad=excluded.ciudad, direccion=excluded.direccion,
                  telefono=excluded.telefono, hora_inicio=excluded.hora_inicio,
                  hora_fin=excluded.hora_fin, puestos=excluded.puestos,
                  activo=excluded.activo""",
             (sid, req.nombre, req.ciudad, req.direccion, req.telefono,
              req.hora_inicio, req.hora_fin, req.puestos, req.activo))
    return uno("select * from sedes where id=%s", (sid,), "Sede no encontrada")


@ra.put("/sedes/{sid}")
def sedes_update(sid: str, req: SedeEditReq):
    return _actualizar("sedes", sid, req, "Sede no encontrada", exige=("nombre",))


@ra.delete("/sedes/{sid}")
def sedes_delete(sid: str):
    n = uno("select count(*) as n from citas where sede_id=%s", (sid,))["n"]
    if n:
        ejecutar("update sedes set activo=false where id=%s", (sid,))
        return {"ok": True, "mensaje": "La sede tiene citas; quedó desactivada."}
    return ejecutar("delete from sedes where id=%s", (sid,))


@r.get("/servicios")
def servicios_list():
    return todos("select * from servicios order by nombre")


@ra.post("/servicios")
def servicios_create(req: ServicioReq):
    sid = "srv-" + req.nombre.lower().replace(" ", "-")[:50]
    ejecutar("""insert into servicios(id,nombre,codigo,duracion,precio,activo)
                values(%s,%s,%s,%s,%s,%s)
                on conflict(id) do update set nombre=excluded.nombre,
                  codigo=excluded.codigo, duracion=excluded.duracion,
                  precio=excluded.precio, activo=excluded.activo""",
             (sid, req.nombre, req.codigo, req.duracion, req.precio, req.activo))
    return uno("select * from servicios where id=%s", (sid,), "Servicio no encontrado")


@ra.put("/servicios/{sid}")
def servicios_update(sid: str, req: ServicioEditReq):
    return _actualizar("servicios", sid, req, "Servicio no encontrado", exige=("nombre",))


@ra.delete("/servicios/{sid}")
def servicios_delete(sid: str):
    n = uno("select count(*) as n from citas where servicio_id=%s", (sid,))["n"]
    if n:
        ejecutar("update servicios set activo=false where id=%s", (sid,))
        return {"ok": True, "mensaje": "El servicio tiene citas; quedó desactivado."}
    return ejecutar("delete from servicios where id=%s", (sid,))


@r.get("/estados")
def estados_list():
    """No existía: la agenda no tenía de dónde leer los estados."""
    return todos("select * from estados order by orden")


@ra.post("/estados")
def estados_create(req: EstadoReq):
    eid = "est-" + req.nombre.lower().replace(" ", "-")[:30]
    if req.inicial:
        ejecutar("update estados set inicial=false where inicial and id<>%s", (eid,))
    ejecutar("""insert into estados(id,nombre,color,tipo,inicial,transparente,
                                    orden,activo)
                values(%s,%s,%s,%s,%s,%s,%s,%s)
                on conflict(id) do update set nombre=excluded.nombre,
                  color=excluded.color, tipo=excluded.tipo,
                  inicial=excluded.inicial, transparente=excluded.transparente,
                  orden=excluded.orden, activo=excluded.activo""",
             (eid, req.nombre, req.color, req.tipo, req.inicial,
              req.transparente, req.orden, req.activo))
    return uno("select * from estados where id=%s", (eid,), "Estado no encontrado")


@ra.put("/estados/{eid}")
def estados_update(eid: str, req: EstadoReq):
    # solo puede haber un estado inicial; si este lo es, los demás dejan de serlo
    if req.inicial:
        ejecutar("update estados set inicial=false where inicial and id<>%s", (eid,))
    ejecutar("""insert into estados(id,nombre,color,tipo,inicial,transparente,orden,activo)
                values(%s,%s,%s,%s,%s,%s,%s,%s)
                on conflict(id) do update set nombre=excluded.nombre,
                  color=excluded.color, tipo=excluded.tipo,
                  inicial=excluded.inicial, transparente=excluded.transparente,
                  orden=excluded.orden, activo=excluded.activo""",
             (eid, req.nombre, req.color, req.tipo, req.inicial,
              req.transparente, req.orden, req.activo))
    return uno("select * from estados where id=%s", (eid,), "Estado no encontrado")


@ra.delete("/estados/{eid}")
def estados_delete(eid: str):
    return ejecutar("update estados set activo=false where id=%s", (eid,))


@r.get("/especialistas")
def especialistas_list():
    return todos("""
        select e.*,
               coalesce((select array_agg(s.sede_id order by s.sede_id)
                           from especialista_sedes s
                          where s.especialista_id=e.id), '{}') as sedes,
               coalesce((select array_agg(x.servicio_id order by x.servicio_id)
                           from especialista_servicios x
                          where x.especialista_id=e.id), '{}') as servicios
          from especialistas e order by e.nombres""")


@ra.post("/especialistas")
def especialistas_create(req: EspecialistaReq):
    base = (req.nombres + "-" + req.apellidos).lower().replace(" ", "-")[:60]
    eid = "esp-" + base
    ejecutar("""insert into especialistas(id,nombres,apellidos,especialidad,color,activo)
                values(%s,%s,%s,%s,%s,%s)
                on conflict(id) do update set nombres=excluded.nombres,
                  apellidos=excluded.apellidos,
                  especialidad=excluded.especialidad,
                  color=excluded.color, activo=excluded.activo""",
             (eid, req.nombres, req.apellidos, req.especialidad or "",
              req.color, req.activo))
    return uno("select * from especialistas where id=%s", (eid,), "Especialista no encontrada")


@ra.put("/especialistas/{eid}")
def especialistas_update(eid: str, req: EspecialistaUpsert):
    """Crea o actualiza, y deja sedes, servicios y horarios exactamente como
    vienen. La agenda web guarda la especialista completa de una sola vez;
    hacerlo con seis llamadas sueltas deja estados a medias si una falla."""
    base = {k: v for k, v in req.dict().items()
            if v is not None and k not in ("sedes", "servicios", "horarios")}
    existe = uno("select count(*) as n from especialistas where id=%s", (eid,))["n"]
    if existe:
        if base:
            partes = ", ".join(f"{k}=%({k})s" for k in base)
            base["__id"] = eid
            ejecutar(f"update especialistas set {partes} where id=%(__id)s", base)
    else:
        if not base.get("nombres"):
            raise HTTPException(400, "Falta nombres")
        base.setdefault("apellidos", "")
        cols = ", ".join(["id"] + list(base))
        vals = ", ".join(["%(__id)s"] + [f"%({k})s" for k in base])
        base["__id"] = eid
        ejecutar(f"insert into especialistas({cols}) values({vals})", base)

    if req.sedes is not None:
        ejecutar("delete from especialista_sedes where especialista_id=%s", (eid,))
        for s in req.sedes:
            ejecutar("""insert into especialista_sedes(especialista_id,sede_id)
                        values(%s,%s) on conflict do nothing""", (eid, s))
    if req.servicios is not None:
        ejecutar("delete from especialista_servicios where especialista_id=%s", (eid,))
        for s in req.servicios:
            ejecutar("""insert into especialista_servicios(especialista_id,servicio_id)
                        values(%s,%s) on conflict do nothing""", (eid, s))
    if req.horarios is not None:
        ejecutar("delete from horarios where especialista_id=%s", (eid,))
        for h in req.horarios:
            sede = h.get("sedeId") or h.get("sede_id")
            if not sede:
                continue
            ejecutar("""insert into horarios(especialista_id,dia,sede_id,desde,
                                             hasta,alm_desde,alm_hasta)
                        values(%s,%s,%s,%s,%s,%s,%s)""",
                     (eid, int(h.get("dia", 0)), sede,
                      h.get("desde") or "09:00", h.get("hasta") or "18:00",
                      h.get("almDesde") or h.get("alm_desde") or None,
                      h.get("almHasta") or h.get("alm_hasta") or None))
    return especialista_uno(eid)


def especialista_uno(eid: str):
    return uno("""
        select e.*,
               coalesce((select array_agg(s.sede_id order by s.sede_id)
                           from especialista_sedes s
                          where s.especialista_id=e.id), '{}') as sedes,
               coalesce((select array_agg(x.servicio_id order by x.servicio_id)
                           from especialista_servicios x
                          where x.especialista_id=e.id), '{}') as servicios
          from especialistas e where e.id=%s""", (eid,), "Especialista no encontrada")


@ra.delete("/especialistas/{eid}")
def especialistas_delete(eid: str):
    n = uno("""select count(*) as n from citas
                where especialista_id=%s and fecha>=current_date
                  and ocupa_cupo""", (eid,))["n"]
    if n:
        raise HTTPException(400, f"Tiene {n} citas futuras. Reasígnalas primero.")
    ejecutar("update especialistas set activo=false where id=%s", (eid,))
    return {"ok": True, "mensaje": "Especialista desactivada"}


@ra.post("/horarios")
def horarios_create(req: HorarioReq):
    return ejecutar("""insert into horarios(especialista_id,dia,sede_id,desde,
                                            hasta,alm_desde,alm_hasta)
                       values(%s,%s,%s,%s,%s,%s,%s)""",
                    (req.especialista_id, req.dia, req.sede_id, req.desde,
                     req.hasta, req.alm_desde or None, req.alm_hasta or None))


@ra.delete("/horarios/{hid}")
def horarios_delete(hid: int):
    return ejecutar("delete from horarios where id=%s", (hid,))


@ra.post("/especialista-sedes")
def especialista_sede(req: EspecialistaSedeReq):
    if req.activo is False:
        return ejecutar("""delete from especialista_sedes
                            where especialista_id=%s and sede_id=%s""",
                        (req.especialista_id, req.sede_id))
    return ejecutar("""insert into especialista_sedes(especialista_id,sede_id)
                       values(%s,%s) on conflict do nothing""",
                    (req.especialista_id, req.sede_id))


@ra.post("/especialista-servicios")
def especialista_servicio(req: EspecialistaServicioReq):
    return ejecutar("""insert into especialista_servicios(especialista_id,servicio_id)
                       values(%s,%s) on conflict do nothing""",
                    (req.especialista_id, req.servicio_id))


@ra.delete("/especialista-servicios/{especialista_id}/{servicio_id}")
def especialista_servicio_del(especialista_id: str, servicio_id: str):
    return ejecutar("""delete from especialista_servicios
                        where especialista_id=%s and servicio_id=%s""",
                    (especialista_id, servicio_id))


def _actualizar(tabla: str, ident: str, req, falta: str, exige=()):
    """PUT que crea si no existe. La agenda web guarda con el id que ella
    misma genera (`set(col/id, datos)`); si el PUT solo actualizara, un
    registro nuevo se perdería o quedaría con otro id."""
    # Un "" que llega del formulario no es un valor: se guarda como NULL.
    # Antes viajaba como '' y la clave foranea clientes_sede_id_fkey reventaba
    # con un 500 al crear un cliente sin "sede preferida" (el combo manda "").
    campos = {k: (None if v == "" else v)
              for k, v in req.dict().items() if v is not None}
    if not campos:
        raise HTTPException(400, "Nada que actualizar")
    existe = uno(f"select count(*) as n from {tabla} where id=%s", (ident,))["n"]
    if existe:
        partes = ", ".join(f"{k}=%({k})s" for k in campos)
        campos["__id"] = ident
        ejecutar(f"update {tabla} set {partes} where id=%(__id)s", campos)
    else:
        faltan = [c for c in exige if not campos.get(c)]
        if faltan:
            raise HTTPException(400, "Falta " + ", ".join(faltan))
        cols = ", ".join(["id"] + list(campos))
        vals = ", ".join(["%(__id)s"] + [f"%({k})s" for k in campos])
        campos["__id"] = ident
        ejecutar(f"insert into {tabla}({cols}) values({vals})", campos)
    return uno(f"select * from {tabla} where id=%s", (ident,), falta)


# ───────────────────────────────────────────────────────────── clientes ────
@r.post("/clientes/buscar")
def clientes_buscar(req: BuscarCliente):
    """Usa la función de la base, que normaliza el teléfono: da igual si llega
    +57 300…, 57300… o 300…."""
    return todos("select * from buscar_cliente(%s,%s,%s)",
                 (req.telefono, req.documento, req.nombre))


@r.post("/clientes/crear")
def clientes_crear(req: ClienteCrear):
    return uno("""select * from crear_cliente(p_documento=>%s,
                        p_primer_nombre=>%s, p_primer_apellido=>%s,
                        p_telefono=>%s, p_correo=>%s, p_sede=>%s)""",
               (req.documento, req.primer_nombre, req.primer_apellido,
                req.telefono, req.correo or "", req.sede))


@r.get("/clientes")
def clientes_list(buscar: Optional[str] = Query(None), limite: int = 100):
    if buscar:
        like = f"%{buscar}%"
        return todos("""select * from clientes
                         where documento ilike %s or telefono ilike %s
                            or (primer_nombre || ' ' || primer_apellido) ilike %s
                         order by primer_nombre limit %s""",
                     (like, like, like, limite))
    return todos("select * from clientes order by primer_nombre limit %s", (limite,))


@r.get("/clientes/{cid}")
def cliente_detail(cid: str):
    cli = uno("select * from clientes where id=%s", (cid,), "Cliente no encontrado")
    cli["citas"] = todos("""select * from v_historial_cliente
                             where cliente_id=%s limit 60""", (cid,))
    return cli


@r.put("/clientes/{cid}")
def cliente_update(cid: str, req: ClienteEditar):
    return _actualizar("clientes", cid, req, "Cliente no encontrado",
                       exige=("documento",))


# ─────────────────────────────────────────────────────────────── agenda ────
@r.get("/agenda/{sede_id}/{fecha}")
def agenda_dia(sede_id: str, fecha: date):
    """v_agenda ya trae cliente, teléfono, documento, especialista, servicio,
    estado y color. La versión anterior volvía a unir con INNER JOIN y los
    bloqueos (sin cliente) y las citas sin servicio desaparecían."""
    sql = """select id, fecha, to_char(inicio,'HH24:MI') as inicio,
                    to_char(fin,'HH24:MI') as fin, tipo, canal, notas, motivo,
                    ocupa_cupo, sede_id, sede, especialista_id,
                    especialista, especialista_corto, servicio_id, servicio,
                    duracion, cliente_id, cliente as cliente_nombre,
                    cliente_corto, documento, telefono,
                    estado_id, estado as estado_nombre, estado_tipo,
                    color as estado_color, asignada_por, creado_por
               from v_agenda where fecha=%s"""
    if sede_id and sede_id != "todas":
        return todos(sql + " and sede_id=%s order by inicio", (fecha, sede_id))
    return todos(sql + " order by sede_id, inicio", (fecha,))


@r.get("/citas")
def citas_list(fecha: Optional[str] = Query(None),
               desde: Optional[str] = Query(None),
               hasta: Optional[str] = Query(None),
               sede_id: Optional[str] = Query(None),
               limite: int = 500):
    cond, par = [], []
    if fecha:
        cond.append("fecha=%s"); par.append(fecha)
    if desde:
        cond.append("fecha>=%s"); par.append(desde)
    if hasta:
        cond.append("fecha<=%s"); par.append(hasta)
    if sede_id and sede_id != "todas":
        cond.append("sede_id=%s"); par.append(sede_id)
    w = (" where " + " and ".join(cond)) if cond else ""
    par.append(limite)
    return todos(f"select * from v_agenda{w} order by fecha, inicio limit %s", par)


@r.get("/citas/{cid}/bitacora")
def cita_bitacora(cid: str):
    return todos("select * from cita_bitacora where cita_id=%s order by ts", (cid,))


@r.post("/citas/agendar")
def agendar(req: AgendarReq):
    return uno("""select * from agendar_cita(p_cliente=>%s, p_especialista=>%s,
                        p_sede=>%s, p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                        p_fin=>%s, p_canal=>%s, p_por=>%s, p_notas=>%s,
                        p_reserva=>%s)""",
               (req.cliente_id, req.especialista, req.sede, req.fecha,
                req.inicio, req.servicio, req.fin, req.canal, req.por,
                req.notas or "", req.reserva),
               "No se pudo agendar")


@r.post("/citas/estado")
def cambiar_estado(req: CambiarEstadoReq):
    return uno("select * from cambiar_estado(%s,%s,%s,%s)",
               (req.cita_id, req.estado, req.por, req.motivo or ""),
               "Cita no encontrada")


@r.post("/citas/reprogramar")
def reprogramar(req: ReprogramarReq):
    return uno("""select * from reprogramar_cita(p_cita=>%s, p_fecha=>%s,
                        p_inicio=>%s, p_especialista=>%s, p_sede=>%s,
                        p_servicio=>%s, p_motivo=>%s, p_por=>%s)""",
               (req.cita_id, req.fecha, req.inicio, req.especialista,
                req.sede, req.servicio, req.motivo, req.por),
               "Cita no encontrada")


@r.post("/citas/bloqueo")
def cita_bloqueo(req: BloqueoReq):
    """agendar_cita() exige cliente, así que no servía para bloqueos.
    Un bloqueo es una cita tipo='bloqueo' sin cliente."""
    cid = uno("select 'b_' || replace(gen_random_uuid()::text,'-','') as id")["id"]
    ejecutar("""insert into citas(id,tipo,fecha,inicio,fin,especialista_id,
                                  sede_id,estado_id,canal,notas,creado_por)
                values(%s,'bloqueo',%s,%s,%s,%s,%s,
                       (select id from estados where inicial and activo limit 1),
                       'manual',%s,%s)""",
             (cid, req.fecha, req.inicio, req.fin, req.especialista,
              req.sede, req.motivo, req.por))
    return uno("select * from v_agenda where id=%s", (cid,), "No se pudo crear")


@r.put("/citas/{cid}")
def cita_update(cid: str, req: MoverCitaReq):
    """Mover o editar. La versión anterior escribía en cita_bitacora(...,notas)
    y esa columna no existe: cada movida terminaba en 500. El trigger de la
    tabla ya deja el rastro, así que aquí no hay que insertar nada."""
    campos = {k: v for k, v in req.dict().items()
              if v is not None and k != "por"}
    if not campos:
        raise HTTPException(400, "Nada que actualizar")
    partes = ", ".join(f"{k}=%({k})s" for k in campos)
    campos["__id"] = cid
    ejecutar(f"update citas set {partes} where id=%(__id)s", campos)
    return uno("select * from v_agenda where id=%s", (cid,), "Cita no encontrada")


@r.delete("/citas/{cid}")
def cita_delete(cid: str):
    """No borra: cancela. Una cita borrada se lleva el historial con ella."""
    return uno("""select * from cambiar_estado(%s,
                    (select id from estados where tipo='cancelado' and activo
                      order by orden limit 1), %s, %s)""",
               (cid, "agenda", "Anulada desde la agenda"), "Cita no encontrada")


# ─────────────────────────────────────────────────────── cupos y huecos ────
@r.post("/huecos/dia")
def huecos_dia(req: HuecosRequest):
    """El parámetro se llama p_paso, no paso: así estaba fallando siempre."""
    return todos("""select fecha, to_char(inicio,'HH24:MI') as inicio,
                           to_char(fin,'HH24:MI') as fin,
                           especialista_id, sede_id
                      from huecos_del_dia(p_fecha=>%s, p_sede=>%s,
                           p_especialista=>%s, p_servicio=>%s,
                           p_duracion=>%s, p_paso=>%s)""",
                 (req.fecha, req.sede, req.especialista, req.servicio,
                  req.duracion, req.paso))


@r.post("/huecos/buscar")
def huecos_buscar(req: BuscarHuecosReq):
    return todos("""select fecha, to_char(inicio,'HH24:MI') as inicio,
                           to_char(fin,'HH24:MI') as fin,
                           especialista_id, sede_id
                      from buscar_huecos(p_desde=>%s, p_dias=>%s, p_sede=>%s,
                           p_especialista=>%s, p_servicio=>%s, p_duracion=>%s,
                           p_paso=>%s, p_limite=>%s)""",
                 (req.desde or date.today(), req.dias, req.sede,
                  req.especialista, req.servicio, req.duracion,
                  req.paso, req.limite))


@r.post("/cupos/apartar")
def apartar(req: ApartarCupoReq):
    return uno("""select * from apartar_cupo(p_especialista=>%s, p_sede=>%s,
                        p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                        p_minutos=>%s, p_referencia=>%s)""",
               (req.especialista, req.sede, req.fecha, req.inicio,
                req.servicio, req.minutos, req.referencia),
               "No se pudo apartar")


@r.delete("/cupos/{reserva}")
def soltar(reserva: str):
    return {"ok": uno("select soltar_cupo(%s) as ok", (reserva,))["ok"]}


# ─────────────────────────────────────────────────────────── indicadores ───
@ra.get("/indicadores")
def indicadores(anio: int = None, mes: int = None):
    """Antes armaba '2026-09-31', que no es una fecha: reventaba en todo mes
    de 30 días."""
    hoy = date.today()
    anio = anio or hoy.year
    mes = mes or hoy.month
    if not 1 <= mes <= 12:
        raise HTTPException(400, "Mes fuera de rango")
    desde = date(anio, mes, 1)
    hasta = date(anio + (mes == 12), (mes % 12) + 1, 1) - timedelta(days=1)
    por_estado = todos("""
        select c.sede_id, s.nombre as sede, c.estado_id,
               e.nombre as estado, e.tipo as estado_tipo, e.color,
               count(*) as total
          from citas c
          left join sedes s on s.id=c.sede_id
          left join estados e on e.id=c.estado_id
         where c.fecha between %s and %s
         group by 1,2,3,4,5,6 order by 1,4""", (desde, hasta))
    por_dia = todos("""select fecha, count(*) as total,
                              count(*) filter (where ocupa_cupo) as ocupan
                         from citas where fecha between %s and %s
                        group by fecha order by fecha""", (desde, hasta))
    por_esp = todos("""
        select c.especialista_id, nombre_corto(e.nombres,e.apellidos) as especialista,
               count(*) as total,
               count(*) filter (where es.tipo='atendido') as realizadas,
               count(*) filter (where es.tipo='ausente')  as incumplidas,
               count(*) filter (where es.tipo='cancelado') as canceladas
          from citas c
          join especialistas e on e.id=c.especialista_id
          left join estados es on es.id=c.estado_id
         where c.fecha between %s and %s
         group by 1,2 order by 3 desc""", (desde, hasta))
    canal = todos("""select coalesce(nullif(canal,''),'Sin canal') as canal,
                            count(*) as total
                       from citas where fecha between %s and %s
                      group by 1 order by 2 desc""", (desde, hasta))
    return {"anio": anio, "mes": mes, "desde": str(desde), "hasta": str(hasta),
            "por_estado": por_estado, "por_dia": por_dia,
            "por_especialista": por_esp, "por_canal": canal}


# ────────────────── horarios por fecha puntual y bloqueos ──────────────────
# "Este lunes trabaja de 2 a 6, y el otro no." Si una especialista tiene filas
# en horarios_fecha para una fecha y sede, esas mandan ese día y el horario
# semanal se ignora. Sirve además para bloquear varios días de una sola vez
# (cita médica, incapacidad, vacaciones).

class HorarioFechaReq(BaseModel):
    especialista: str
    sede: str
    desde: date
    hasta: Optional[date] = None
    inicio: str
    fin: str
    alm_desde: Optional[str] = None
    alm_hasta: Optional[str] = None
    dias: Optional[List[int]] = None      # 0=domingo .. 6=sábado; null = todos
    nota: str = ""
    reemplazar: bool = True


class BloqueoRangoReq(BaseModel):
    especialista: str
    sede: str
    desde: date
    hasta: Optional[date] = None
    inicio: str
    fin: str
    motivo: str = "Bloqueo"
    dias: Optional[List[int]] = None
    por: str = ""


@r.get("/agenda-especialista")
def agenda_especialista(especialista: str = Query(...),
                        fecha: date = Query(...),
                        sede: Optional[str] = Query(None),
                        servicio: Optional[str] = Query(None),
                        paso: int = Query(30)):
    """¿Esta especialista trabaja ese día y a qué horas tiene cupo?

    Se usa cuando el cliente pregunta por alguien puntual. Con `huecos` solo no
    se puede distinguir «no trabaja» de «trabaja pero está llena», por eso se
    devuelven las dos cosas: las franjas de trabajo y las horas libres.
    """
    fila = None
    with cursor() as cur:
        cur.execute("""select id, trim(nombres || ' ' || apellidos) as nombre
                         from especialistas where id=%s""", (especialista,))
        fila = cur.fetchone()
        if not fila:
            # tambien acepta el nombre: «Valentina», «Valentina Baquero»
            cur.execute("""select id, trim(nombres || ' ' || apellidos) as nombre
                             from especialistas
                            where activo
                              and (nombres || ' ' || apellidos) ilike %s
                            order by length(nombres || ' ' || apellidos)
                            limit 1""", ("%" + especialista + "%",))
            fila = cur.fetchone()
    if not fila:
        raise HTTPException(404, "ESPECIALISTA_NO_EXISTE: no encontré a esa especialista")
    eid = fila["id"]

    franjas = todos("""select f.especialista_id, f.sede_id, s.nombre as sede,
                              to_char(f.desde,'HH24:MI')     as desde,
                              to_char(f.hasta,'HH24:MI')     as hasta,
                              to_char(f.alm_desde,'HH24:MI') as alm_desde,
                              to_char(f.alm_hasta,'HH24:MI') as alm_hasta,
                              f.origen
                         from franjas_del_dia(%s, %s, %s, %s) f
                         join sedes s on s.id = f.sede_id
                        order by f.desde""",
                    (fecha, sede, eid, servicio))

    libres = todos("""select to_char(inicio,'HH24:MI') as inicio,
                             to_char(fin,'HH24:MI')    as fin,
                             sede_id
                        from huecos_del_dia(p_fecha=>%s, p_sede=>%s,
                             p_especialista=>%s, p_servicio=>%s, p_paso=>%s)""",
                   (fecha, sede, eid, servicio, paso))

    return {"especialista_id": eid, "especialista": fila["nombre"],
            "fecha": fecha, "trabaja": bool(franjas),
            "franjas": franjas, "libres": libres}


@r.get("/horarios-fecha")
def horarios_fecha_list(especialista: Optional[str] = Query(None),
                        sede: Optional[str] = Query(None),
                        desde: Optional[date] = Query(None),
                        hasta: Optional[date] = Query(None),
                        limite: int = 1000):
    """Los horarios puntuales cargados, para pintarlos en el calendario.

    Va en `r` (operador), no en `ra` (admin): la agenda del día lo consulta
    cada vez que se abre una fecha, y quien la usa es la recepcionista. Si
    respondiera 403, la rejilla pintaría el horario semanal y ofrecería horas
    que la API después rechaza. Poner y quitar siguen siendo de admin.
    """
    return todos("""
        select hf.id, hf.especialista_id, hf.sede_id, hf.fecha,
               to_char(hf.desde,'HH24:MI')     as desde,
               to_char(hf.hasta,'HH24:MI')     as hasta,
               to_char(hf.alm_desde,'HH24:MI') as alm_desde,
               to_char(hf.alm_hasta,'HH24:MI') as alm_hasta,
               hf.nota,
               coalesce(nullif(trim(e.nombres || ' ' || e.apellidos),''),
                        e.id) as especialista,
               s.nombre as sede
          from horarios_fecha hf
          join especialistas e on e.id = hf.especialista_id
          join sedes         s on s.id = hf.sede_id
         where (%s::text is null or hf.especialista_id = %s::text)
           and (%s::text is null or hf.sede_id = %s::text)
           and (%s::date is null or hf.fecha >= %s::date)
           and (%s::date is null or hf.fecha <= %s::date)
         order by hf.fecha, hf.desde
         limit %s""",
        (especialista, especialista, sede, sede, desde, desde, hasta, hasta,
         max(1, min(limite, 3000))))


@ra.post("/horarios-fecha")
def horarios_fecha_crear(req: HorarioFechaReq):
    """Pone la misma franja en varias fechas del rango.

    `dias` filtra por día de la semana (0=domingo .. 6=sábado); si no se manda,
    se aplica a todos los días del rango. Devuelve una fila por fecha evaluada.
    """
    filas = todos("""select * from horario_fecha_rango(
                        %s::text, %s::text, %s::date, %s::date,
                        %s::time, %s::time, %s::time, %s::time,
                        %s::text, %s::text, %s::int[], %s::boolean)""",
                  (req.especialista, req.sede, req.desde,
                   req.hasta or req.desde, req.inicio, req.fin,
                   req.alm_desde or None, req.alm_hasta or None,
                   req.nota, "", req.dias, req.reemplazar))
    return {"ok": True,
            "puestas": len([f for f in filas if f.get("creado")]),
            "detalle": filas}


@ra.delete("/horarios-fecha/{hid}")
def horarios_fecha_borrar(hid: int):
    return ejecutar("delete from horarios_fecha where id=%s", (hid,))


@ra.delete("/horarios-fecha")
def horarios_fecha_borrar_rango(especialista: str = Query(...),
                                desde: date = Query(...),
                                hasta: Optional[date] = Query(None),
                                sede: Optional[str] = Query(None)):
    """Quita los horarios puntuales de una especialista en un rango de fechas.
    A partir de ahí vuelve a regir el horario semanal."""
    filas = todos("""delete from horarios_fecha hf
                      where hf.especialista_id = %s::text
                        and hf.fecha between %s::date and %s::date
                        and (%s::text is null or hf.sede_id = %s::text)
                      returning hf.id""",
                  (especialista, desde, hasta or desde, sede, sede))
    return {"ok": True, "borradas": len(filas)}


@r.post("/citas/bloqueo-rango")
def bloqueo_rango(req: BloqueoRangoReq):
    """Bloquea varias fechas de una vez, escogiendo horas y días.

    `dias` filtra por día de la semana (0=domingo .. 6=sábado); si no se manda,
    bloquea todos los días del rango. Las fechas donde ya hay una cita no se
    tocan: vuelven marcadas como «chocaron».
    """
    filas = todos("""select * from bloquear_rango(
                        %s::text, %s::text, %s::date, %s::date,
                        %s::time, %s::time, %s::text, %s::text, %s::int[])""",
                  (req.especialista, req.sede, req.desde,
                   req.hasta or req.desde, req.inicio, req.fin,
                   req.motivo, req.por, req.dias))
    return {"ok": True,
            "bloqueados": len([f for f in filas if f.get("creado")]),
            "chocaron": len([f for f in filas if not f.get("creado")]),
            "detalle": filas}


@r.get("/citas/bloqueos")
def bloqueos_list(desde: Optional[date] = Query(None),
                  hasta: Optional[date] = Query(None),
                  especialista: Optional[str] = Query(None),
                  limite: int = 500):
    """Los bloqueos cargados, para pintarlos en el calendario."""
    return todos("""
        select c.id, c.fecha, to_char(c.inicio,'HH24:MI') as inicio,
               to_char(c.fin,'HH24:MI') as fin, c.motivo,
               c.especialista_id, c.sede_id,
               coalesce(nullif(trim(e.nombres || ' ' || e.apellidos),''),
                        e.id) as especialista,
               s.nombre as sede
          from citas c
          join especialistas e on e.id = c.especialista_id
          join sedes         s on s.id = c.sede_id
         where c.tipo = 'bloqueo'
           and c.ocupa_cupo
           and (%s::date is null or c.fecha >= %s::date)
           and (%s::date is null or c.fecha <= %s::date)
           and (%s::text is null or c.especialista_id = %s::text)
         order by c.fecha, c.inicio
         limit %s""",
        (desde, desde, hasta, hasta, especialista, especialista,
         max(1, min(limite, 2000))))


# ───────────────────────────────────────────────────────────── montaje ─────
# nginx borra el "/api/" al hacer proxy_pass con barra final, así que la misma
# API queda colgada de cuatro prefijos. Da igual cómo la llamen: responde.
# Cada grupo con su nivel: rp abierto, r necesita haber entrado, ra es del
# administrador. Los cuatro prefijos porque nginx borra el "/api/".
for _pre in ("", "/v2", "/api", "/api/v2"):
    _esquema = (_pre == "")
    app.include_router(rp, prefix=_pre, include_in_schema=_esquema)
    app.include_router(r,  prefix=_pre, dependencies=[Depends(sesion)],
                       include_in_schema=_esquema)
    app.include_router(ra, prefix=_pre, dependencies=[Depends(admin)],
                       include_in_schema=_esquema)
