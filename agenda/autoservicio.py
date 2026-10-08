"""
Panel Clientes CJ — el autoservicio de recepción
================================================
La tablet de recepción: la clienta se agenda sola, avisa que llegó, reprograma
o cancela, sin ocupar a nadie.

Vive DENTRO de la agenda, no en el CRM. Eso trae tres cosas buenas:
no hay token que exponer (habla con Postgres por dentro), no hay un salto de
red por cada toque, y usa las mismas funciones de la base que ya usan la web
y Pepe — así nadie puede agendar algo que las otras dos considerarían
imposible.

Se conecta con dos líneas en `agenda_api.py`:

    from autoservicio import router as autoservicio_router      # arriba

    for _pre in ("", "/v2", "/api", "/api/v2"):                 # en el montaje
        ...
        app.include_router(autoservicio_router, prefix=_pre,
                           include_in_schema=_esquema)

Queda SIN sesión, como `rp`: es una tablet pública. Por eso mismo trae sus
propios candados (ver más abajo).

Lo que hay que saber para tocarlo
---------------------------------
1. LA SEDE LA DECIDE EL SERVIDOR. El navegador manda un apodo ("el-tesoro" /
   "bogota"), nunca un id. Cualquier otra cosa se rechaza: una tablet no
   agenda en la otra ciudad.

2. HORA DE COLOMBIA, SIEMPRE. El VPS corre en UTC. "Hoy", "mañana" y "esa
   hora ya pasó" se calculan con ahora_co(), nunca con datetime.now().
   Ojo: huecos_del_dia también descarta lo ya pasado, pero lo hace con el
   current_date de Postgres. Si esa base está en UTC, entre las 7 p. m. y la
   medianoche cree que ya es mañana y deja de filtrar. Por eso el filtro se
   repite aquí y no se confía en el de allá.

3. LOS ESTADOS SE BUSCAN POR NOMBRE. Nada de 'est-cumplido' quemado: si el
   dueño renombra "Llegó", esto sigue sirviendo.

4. LA DISPONIBILIDAD NO SE CALCULA A MANO. huecos_del_dia ya descuenta
   horario, horario puntual, almuerzo, citas y cupos apartados.

Variables de entorno (todas opcionales):

    AUTOSERVICIO_CLAVE   si se pone, la tablet abre
                         /autoservicio.html?sede=…&k=<clave> y la manda en
                         cada llamada. Sin ella la API no responde. Si no se
                         pone, queda abierta (más cómodo, menos seguro).
    AUTOSERVICIO_DATOS_COMPLETOS  1 para mostrarle a la clienta el celular y
                         el correo completos. Por defecto van tapados.
    AUTOSERVICIO_MINUTOS  cuántos minutos se aparta el cupo (8).
    AUTOSERVICIO_BD      dónde lleva la cuenta de cambios del día
                         (por defecto, autoservicio.db al lado de este archivo).
    AUTOSERVICIO_TOPE_CLIENTE  cuántas consultas por cédula se aceptan por
                         minuto y por IP (30). El script de prueba lo sube.
    AUTOSERVICIO_TOPE    lo mismo para el resto de llamadas (150).
    AUTOSERVICIO_ABIERTO 1 para que el panel funcione SIN abrirlo con usuario
                         y contraseña. Por defecto pide abrirlo.
    AUTOSERVICIO_DIAS    cuántos días dura abierta una tablet (30).
"""
import base64
import hashlib
import hmac
import os
import re
import secrets
import sqlite3
import sys
import time
import unicodedata
from datetime import date, datetime, timedelta, timezone
from typing import Optional

from fastapi import APIRouter, Query, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

CLAVE = os.getenv("AUTOSERVICIO_CLAVE", "").strip()
# La tablet se abre una vez con el usuario de la agenda y se queda abierta.
ABIERTO = os.getenv("AUTOSERVICIO_ABIERTO", "0") == "1"   # 1 = sin llave
DIAS_TABLETA = int(os.getenv("AUTOSERVICIO_DIAS", "30"))
DATOS_COMPLETOS = os.getenv("AUTOSERVICIO_DATOS_COMPLETOS", "0") == "1"
MIN_RESERVA = int(os.getenv("AUTOSERVICIO_MINUTOS", "2"))
# Cada cuántos minutos se ofrecen las horas. 15 es lo que usa la agenda, así
# que la tablet enseña exactamente los mismos cupos que ve recepción.
PASO = max(5, int(os.getenv("AUTOSERVICIO_PASO", "30")))
# Con paso de 30 se vuelve a lo de antes: solo en punto y y media.
SOLO_REDONDAS = PASO >= 30
CALL_CENTER = "+57 301 711 3464"
CANAL = "Autoservicio"                 # lo que separa el reporte "Quién agenda"

# La sede la resuelve el servidor. El navegador solo manda el apodo.
SEDES = {
    "el-tesoro": "sede-cj-medical-el-tesoro",
    "bogota":    "sede-cj-medical-bogota",
}
# Solo se usa si la sede no tiene la dirección cargada en la agenda.
DIRECCIONES = {
    "sede-cj-medical-el-tesoro": "Cra 25A #1a sur-45, LC 6100, "
                                 "Sótano 4 por la plaza de cines, Torre Norte, Medellín",
    "sede-cj-medical-bogota":    "Cra 11A #96-51, Edificio Oficity, "
                                 "Local 102, Chicó Norte, Bogotá",
}
# El largo que se acepta. Cubre cédula de ciudadanía, de extranjería, tarjeta
# de identidad y NIT. El pasaporte lleva letras y no se digita en el teclado
# numérico de la tablet: esa clienta pasa a recepción.
DOC_MIN, DOC_MAX = 6, 11
TIPOS_DOC = [("CC", "Cédula de ciudadanía"), ("CE", "Cédula de extranjería"),
             ("TI", "Tarjeta de identidad"), ("PA", "Pasaporte"), ("NIT", "NIT")]

router = APIRouter(tags=["autoservicio"])


# ──────────────────────────────── los ayudantes de la agenda ───────────────
# todos / uno / ejecutar viven en el módulo principal de la API. El archivo
# se llama distinto según la instalación (agenda_api.py en el VPS), así que en
# vez de quemar un import se busca el módulo que ya los tiene cargados. Si no
# apareciera ninguno, se abre una conexión propia con el mismo DATABASE_URL:
# así este archivo sirve igual suelto, para las pruebas.
_host = {"mod": None}


def _agenda():
    if _host["mod"] is not None:
        return _host["mod"]
    for mod in list(sys.modules.values()):
        if mod is None:
            continue
        if all(hasattr(mod, n) for n in ("todos", "uno", "ejecutar", "cursor")) \
           and hasattr(mod, "DATABASE_URL"):
            _host["mod"] = mod
            return mod
    _host["mod"] = _sueltos()
    return _host["mod"]


def _sueltos():
    """Plan B: los mismos ayudantes, con conexión propia. Solo se usa si este
    archivo corre fuera de la API (por ejemplo, en una prueba suelta)."""
    import psycopg2
    import psycopg2.extras
    from contextlib import contextmanager
    from fastapi import HTTPException

    url = os.environ.get("DATABASE_URL")
    if not url:
        raise RuntimeError("autoservicio: no encontré los ayudantes de la agenda "
                           "ni un DATABASE_URL con el que abrir la mía.")

    @contextmanager
    def cursor():
        conn = psycopg2.connect(url)
        conn.autocommit = True
        try:
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                yield cur
        finally:
            conn.close()

    def _todos(sql, params=()):
        with cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def _uno(sql, params=(), falta="No encontrado"):
        with cursor() as cur:
            cur.execute(sql, params)
            fila = cur.fetchone()
        if fila is None:
            raise HTTPException(404, falta)
        return fila

    def _ejecutar(sql, params=()):
        with cursor() as cur:
            cur.execute(sql, params)
        return {"ok": True}

    ns = type("AgendaSuelta", (), {})()
    ns.cursor, ns.todos, ns.uno, ns.ejecutar = cursor, _todos, _uno, _ejecutar
    ns.DATABASE_URL = url
    return ns


def todos(sql, params=()):
    return _agenda().todos(sql, params)


def uno(sql, params=(), falta="No encontrado"):
    return _agenda().uno(sql, params, falta)


def ejecutar(sql, params=()):
    return _agenda().ejecutar(sql, params)


# ───────────────────────────────────────────────── hora de Colombia ────────
CO = timezone(timedelta(hours=-5))          # Colombia no tiene horario de verano


def ahora_co() -> datetime:
    return datetime.now(timezone.utc).astimezone(CO)


def hoy_co() -> date:
    return ahora_co().date()


DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
         "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def fecha_larga(f) -> str:
    d = f if isinstance(f, date) else date.fromisoformat(str(f)[:10])
    return f"{DIAS[d.weekday()]} {d.day} de {MESES[d.month - 1]} de {d.year}"


def hora_12(hm: str) -> str:
    """'14:30' → '2:30 p. m.' — como lo lee una persona, no un sistema."""
    try:
        h, m = int(str(hm)[:2]), int(str(hm)[3:5])
    except ValueError:
        return str(hm)
    return f"{h % 12 or 12}:{m:02d} {'a. m.' if h < 12 else 'p. m.'}"


def como_dia(f) -> str:
    d = f if isinstance(f, date) else date.fromisoformat(str(f)[:10])
    h = hoy_co()
    if d == h:
        return "hoy"
    if d == h + timedelta(days=1):
        return "mañana"
    return fecha_larga(d)


# ───────────────────────────────────────────────────────── utilidades ──────
def solo_digitos(s) -> str:
    return re.sub(r"\D", "", str(s or ""))


def mismo_telefono(a, b) -> bool:
    """Por los últimos 10 dígitos: da igual +57 300…, 57300… o 300…."""
    a, b = solo_digitos(a)[-10:], solo_digitos(b)[-10:]
    return bool(a) and len(a) >= 7 and a == b


def tapar_telefono(t) -> str:
    d = solo_digitos(t)[-10:]
    return f"{d[:3]} ••• {d[-4:]}" if len(d) >= 7 else "•" * len(d)


def tapar_correo(c) -> str:
    c = str(c or "").strip()
    if "@" not in c:
        return ""
    usuario, dominio = c.split("@", 1)
    return f"{usuario[:2] if len(usuario) > 3 else usuario[:1]}•••@{dominio}"


def sin_tildes(s) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", str(s or "").lower())
                   if unicodedata.category(c) != "Mn")


# Palabras que no se capitalizan y siglas que van enteras en mayúscula.
MENORES = {"de", "del", "la", "las", "los", "y", "da", "do"}
# La base guarda los nombres en mayúscula y sin tildes («BOGOTA»). En pantalla
# eso se lee mal, y es lo primero que ve la clienta. Se reponen al mostrar; la
# base no se toca.
TILDES = {"bogota": "Bogotá", "medellin": "Medellín", "cali": "Cali",
          "pereira": "Pereira", "barranquilla": "Barranquilla",
          "cundinamarca": "Cundinamarca", "antioquia": "Antioquia",
          "chico": "Chicó", "bolivar": "Bolívar", "atlantico": "Atlántico"}
SIGLAS = {"cj", "cc", "ce", "ti", "pa", "nit", "sas", "ips", "eps", "dr", "dra",
          "d.c.", "dc"}


def titulizar(s) -> str:
    """Los datos vienen en MAYÚSCULA SOSTENIDA y así se leen mal en pantalla.
    «CJ MEDICAL EL TESORO» debe quedar «CJ Medical El Tesoro», no
    «Cj Medical El Tesoro»: la sigla se respeta."""
    t = str(s or "").strip()
    if not t:
        return ""
    salida = []
    for i, p in enumerate(t.lower().split()):
        if p in SIGLAS:
            salida.append(p.upper())
        elif p in TILDES:
            salida.append(TILDES[p])
        elif p in MENORES and i:
            salida.append(p)
        else:
            salida.append(p.capitalize())
    return " ".join(salida)


def nombre_cliente(c: dict) -> str:
    partes = [c.get("primer_nombre"), c.get("segundo_nombre"),
              c.get("primer_apellido"), c.get("segundo_apellido")]
    return titulizar(" ".join(p for p in partes if p)) or "—"


def correo_valido(c) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[a-zA-Z]{2,}$", str(c or "").strip()))


def hm(v) -> str:
    return str(v)[:5] if v is not None else ""


# ─────────────────────────────────────────────── errores con cara humana ───
class Problema(Exception):
    def __init__(self, codigo: str, mensaje: str, estado: int = 400):
        self.codigo, self.mensaje, self.estado = codigo, mensaje, estado
        super().__init__(mensaje)


# Lo que levanta la base, dicho como se lo diríamos a una clienta.
HUMANO = {
    "CUPO_TOMADO":      ("Esa hora se acabó de ocupar. Le mostramos las que quedan.", 409),
    "CUPO_APARTADO":    ("Alguien más está tomando esa hora en este momento. "
                         "Escoja otra, por favor.", 409),
    "FUERA_DE_HORARIO": ("La especialista no atiende a esa hora. Escoja otra.", 400),
    "ALMUERZO":         ("Esa hora cae en el almuerzo. Escoja otra, por favor.", 400),
    "ESPECIALISTA_NO_DISPONIBLE": ("Esa especialista ya no está libre a esa hora.", 409),
    "CLIENTE_NO_EXISTE": ("No encontramos sus datos. Por favor pase a recepción.", 404),
    "CITA_NO_EXISTE":   ("Esa cita ya no está en la agenda.", 404),
    "FALTA_DOCUMENTO":  ("Falta el número de documento.", 400),
    "HORA_INVALIDA":    ("Esa hora no es válida.", 400),
    "ESTADO_NO_EXISTE": ("No pudimos cambiar el estado de la cita.", 400),
}


def traducir(e: Exception) -> Problema:
    """La agenda ya devuelve HTTPException con la marca adentro; aquí solo se
    cambia el texto técnico por uno que una clienta pueda leer."""
    txt = str(getattr(e, "detail", None) or getattr(e, "pgerror", None) or e)
    for marca, (frase, estado) in HUMANO.items():
        if marca in txt:
            return Problema(marca, frase, estado)
    return Problema("AGENDA", "No pudimos completar la operación. "
                              "Por favor pase a recepción.", 500)


def mal(p: Problema) -> JSONResponse:
    return JSONResponse({"ok": False, "error": p.codigo, "mensaje": p.mensaje},
                        status_code=p.estado)


# ────────────────────────────────────── la puerta de una tablet pública ────
# La página no pide login. Dos candados baratos: una clave opcional que vive
# en la tablet, y un tope de intentos por IP para que nadie saque la base de
# clientas probando cédulas.
_golpes: dict = {}
# Consultar por cédula es lo único que sirve para pescar datos ajenos, así que
# ese grupo va más apretado. Una tablet real hace una o dos por clienta; mil
# por minuto es alguien probando números. Se puede ajustar sin tocar código.
TOPE = {"cliente": (int(os.getenv("AUTOSERVICIO_TOPE_CLIENTE", "30")), 60),
        "abrir":   (10, 60),          # adivinar contraseñas, despacio
        "otros":   (int(os.getenv("AUTOSERVICIO_TOPE", "150")), 60)}


def _de_donde(req: Request) -> str:
    reenviado = req.headers.get("x-forwarded-for", "")
    if reenviado:
        return reenviado.split(",")[0].strip()
    return req.client.host if req.client else "?"


def pasa_el_tope(req: Request, grupo: str = "otros") -> bool:
    tope, ventana = TOPE.get(grupo, TOPE["otros"])
    clave, ahora = (_de_donde(req), grupo), time.time()
    marcas = [t for t in _golpes.get(clave, []) if ahora - t < ventana]
    marcas.append(ahora)
    _golpes[clave] = marcas
    if len(_golpes) > 4000:                     # que no crezca para siempre
        for k in [k for k, v in _golpes.items() if not v or ahora - v[-1] > 600]:
            _golpes.pop(k, None)
    return len(marcas) <= tope


def clave_ok(req: Request, k: Optional[str] = None) -> bool:
    if not CLAVE:
        return True
    return (k or req.query_params.get("k") or req.headers.get("x-panel", "")) == CLAVE


def puerta(req: Request, k: Optional[str] = None, grupo: str = "otros",
           t: Optional[str] = None):
    # El tope primero y siempre: si se contara después de la clave, quien
    # estuviera probando claves no gastaría intentos.
    topado = not pasa_el_tope(req, grupo)
    if not clave_ok(req, k):
        raise Problema("CERRADO", "Esta tablet no está habilitada.", 403)
    if topado:
        raise Problema("MUCHOS_INTENTOS",
                       "Demasiados intentos. Espere un momento o pase a recepción.", 429)
    if ABIERTO:
        return None
    viva = tableta_viva(_token_de(req, t))
    if not viva:
        raise Problema("SIN_TABLETA",
                       "Esta tablet no está abierta. Pídale a recepción que la abra.", 401)
    return viva


def sede_de(apodo: Optional[str]) -> str:
    sid = SEDES.get(str(apodo or "").strip().lower())
    if not sid:
        raise Problema("SEDE", "Esta tablet no está configurada. "
                               "Avise a recepción.", 400)
    return sid


# ──────────────────────────────── el registro de cambios del día ───────────
# Lo lleva el propio panel (§4.11), en su propio archivo: así no hay que
# migrar nada en Postgres. Si se perdiera, lo único que pasa es que alguien
# podría hacer dos cambios el mismo día.
BD = os.getenv("AUTOSERVICIO_BD") or os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "autoservicio.db")


def _bd():
    conn = sqlite3.connect(BD, timeout=5)
    conn.row_factory = sqlite3.Row
    conn.execute("""create table if not exists cambios(
                      id integer primary key autoincrement,
                      documento text not null, dia text not null,
                      accion text not null, cita_id text, sede text,
                      ts text not null)""")
    conn.execute("create index if not exists cambios_dia on cambios(documento, dia)")
    return conn


def cambios_de_hoy(documento: str) -> int:
    try:
        with _bd() as conn:
            f = conn.execute("select count(*) as n from cambios "
                             "where documento=? and dia=?",
                             (solo_digitos(documento), hoy_co().isoformat())).fetchone()
            return f["n"] if f else 0
    except sqlite3.Error:
        return 0                     # si el archivo falla, no se le cierra la puerta


def anotar_cambio(documento: str, accion: str, cita_id: str, sede: str):
    try:
        with _bd() as conn:
            conn.execute("insert into cambios(documento,dia,accion,cita_id,sede,ts) "
                         "values(?,?,?,?,?,?)",
                         (solo_digitos(documento), hoy_co().isoformat(), accion,
                          cita_id, sede, ahora_co().isoformat(timespec="seconds")))
            conn.commit()
    except sqlite3.Error:
        pass


# ─────────────────────────────────────────── la llave de la tablet ────────
# La recepcionista abre la tablet UNA vez con el mismo correo y contraseña que
# usa en la agenda, y queda abierta hasta que alguien la cierre o se venza.
# La clienta nunca escribe una clave: si tuviera que hacerlo, el panel no
# serviría para lo que existe.
#
# Las contraseñas no se guardan aquí ni se copian: se comprueban contra el
# hash que ya tiene la tabla `usuarios` de la agenda. Quitarle el acceso a
# alguien es desactivarlo ahí, como siempre.
def _hash_token(t: str) -> str:
    return hashlib.sha256(t.encode()).hexdigest()


def clave_correcta(clave: str, guardado: Optional[str]) -> bool:
    """Mismo formato que la agenda: pbkdf2$iteraciones$sal$clave."""
    try:
        algo, it, sal, dk = (guardado or "").split("$")
        if algo != "pbkdf2":
            return False
        calc = hashlib.pbkdf2_hmac("sha256", (clave or "").encode(),
                                   base64.b64decode(sal), int(it))
        return hmac.compare_digest(calc, base64.b64decode(dk))
    except Exception:
        return False


def _tabla_tabletas(conn):
    conn.execute("""create table if not exists tabletas(
                      token_hash text primary key,
                      usuario    text not null,
                      nombre     text default '',
                      sede       text default '',
                      abierta_en text not null,
                      expira_en  text not null,
                      agente     text default '')""")


def abrir_tableta(usuario: dict, sede: str, agente: str) -> dict:
    token = secrets.token_urlsafe(32)
    hasta = ahora_co() + timedelta(days=DIAS_TABLETA)
    with _bd() as conn:
        _tabla_tabletas(conn)
        conn.execute("""insert into tabletas(token_hash,usuario,nombre,sede,
                              abierta_en,expira_en,agente) values(?,?,?,?,?,?,?)""",
                     (_hash_token(token), usuario.get("correo") or usuario.get("id"),
                      usuario.get("nombre") or "", sede,
                      ahora_co().isoformat(timespec="seconds"),
                      hasta.isoformat(timespec="seconds"), (agente or "")[:200]))
        conn.execute("delete from tabletas where expira_en < ?",
                     (ahora_co().isoformat(timespec="seconds"),))
        conn.commit()
    return {"token": token, "hasta": hasta.date().isoformat(),
            "abierta_por": usuario.get("nombre") or usuario.get("correo")}


def tableta_viva(token: str) -> Optional[dict]:
    if not token:
        return None
    try:
        with _bd() as conn:
            _tabla_tabletas(conn)
            f = conn.execute("select * from tabletas where token_hash=?",
                             (_hash_token(token),)).fetchone()
    except sqlite3.Error:
        return None
    if not f or f["expira_en"] < ahora_co().isoformat(timespec="seconds"):
        return None
    return dict(f)


def cerrar_tableta(token: str):
    try:
        with _bd() as conn:
            _tabla_tabletas(conn)
            conn.execute("delete from tabletas where token_hash=?", (_hash_token(token),))
            conn.commit()
    except sqlite3.Error:
        pass


def _token_de(req: Request, t: Optional[str] = None) -> str:
    return (t or req.headers.get("x-tableta")
            or req.query_params.get("t") or "").strip()


def mensaje_limite() -> str:
    return (f"Ya realizó un cambio hoy. Comuníquese con el call center "
            f"{CALL_CENTER} o directamente en recepción.")


# ─────────────────────────────────────────────── lectura de la agenda ──────
def _sede_fila(sid: str) -> dict:
    fila = todos("""select id, nombre, ciudad, direccion, telefono
                      from sedes where id=%s""", (sid,))
    fila = fila[0] if fila else {}
    nombre = titulizar(fila.get("nombre") or "CJ Medical")
    # El campo ciudad viene como lo cargaron: «MEDELLIN - ANTIOQUIA»,
    # «BOGOTÁ D.C. - BOGOTA D.C.». Tal cual, en pantalla queda «Bogotá D.C. -
    # Bogotá D.C.» al lado de una sede que ya se llama Bogotá. Se parte por la
    # coma o el guion y se queda la primera parte, que es la ciudad.
    ciudad = titulizar(re.split(r"\s[-–]\s|,", str(fila.get("ciudad") or ""))[0])
    # Y si esa ciudad ya está en el nombre de la sede, no se repite. Se compara
    # por la PRIMERA palabra: la ciudad es «Bogotá D.C.» y la sede «CJ Medical -
    # Bogotá», que no se contienen una a la otra pero son la misma ciudad.
    clave = sin_tildes(ciudad).lower().split()
    if clave and clave[0] in sin_tildes(nombre).lower().split(" -"):
        ciudad = ""
    elif clave and clave[0] in sin_tildes(nombre).lower():
        ciudad = ""
    direccion = (fila.get("direccion") or "").strip()
    return {"id": sid, "nombre": nombre, "ciudad": ciudad,
            "direccion": direccion or DIRECCIONES.get(sid, ""),
            # para que recepción sepa de dónde salió la que ve la clienta
            "direccion_de": "agenda" if direccion else "código"}


def _estado_id(nombre: str) -> Optional[str]:
    """Por NOMBRE, nunca por id quemado (§4.14)."""
    objetivo = sin_tildes(nombre)
    for e in todos("select id, nombre from estados where activo"):
        if sin_tildes(e["nombre"]) == objetivo:
            return e["id"]
    return None


def _nombres_esp() -> dict:
    return {e["id"]: titulizar(f"{e.get('nombres','')} {e.get('apellidos','')}".strip())
            for e in todos("select id, nombres, apellidos from especialistas where activo")}


def servicio_activo(servicio_id: str) -> dict:
    """El servicio tiene que existir y estar activo. Un id inventado no puede
    colarse hasta agendar_cita."""
    fila = todos("select id, nombre, duracion from servicios where id=%s and activo",
                 (servicio_id,))
    if not fila:
        raise Problema("SERVICIO", "Ese servicio ya no está disponible. "
                                   "Por favor escoja otro o pase a recepción.", 400)
    return fila[0]


def exigir_que_lo_haga(especialista_id: str, servicio_id: str) -> None:
    """La misma regla de la agenda: sin servicios asignados hace todos; con
    servicios asignados, solo esos.

    huecos_del_dia ya filtra por aquí, así que en el camino normal esto nunca
    salta. Está para el camino anormal: una pantalla vieja que quedó abierta
    con una lista de antes, un reintento después de que recepción le cambió
    los servicios a alguien, o alguien mandando la petición a mano. Es barato
    y es lo único que garantiza que en la agenda no aparezca una especialista
    citada para algo que no realiza.
    """
    if not especialista_id or not servicio_id:
        return
    fila = todos("""select exists(select 1 from especialista_servicios
                                   where especialista_id=%s) as tiene,
                           exists(select 1 from especialista_servicios
                                   where especialista_id=%s and servicio_id=%s) as lo_hace""",
                 (especialista_id, especialista_id, servicio_id))
    f = fila[0] if fila else {}
    if f.get("tiene") and not f.get("lo_hace"):
        raise Problema("NO_LO_REALIZA",
                       "Esa profesional no realiza ese servicio. "
                       "Por favor escoja otra hora o pase a recepción.", 409)


def _huecos(sid: str, servicio: str, fecha: str) -> list:
    """Las horas libres de verdad. huecos_del_dia ya descuenta horario,
    horario puntual, almuerzo, citas y cupos apartados (§8.5).

    El paso es el MISMO que usa la agenda (15 minutos). Antes eran 30, y
    encima se dejaban solo las de en punto y y media: eso se veía bonito, pero
    de 27 servicios hay 18 que duran 15, 20 o 45 minutos, y a esos les escondía
    la mitad de los cupos. La clienta leía «no hay» en la tablet mientras
    recepción sí tenía dónde meterla. Con AUTOSERVICIO_PASO=30 se vuelve al
    comportamiento de antes, si algún día se prefiere lo redondo.

    Encima solo se quita lo que ya pasó, con hora de Colombia, porque el filtro
    de la base usa su propio current_date y el VPS está en UTC (§8.1)."""
    filas = todos("""select to_char(inicio,'HH24:MI') as inicio,
                            to_char(fin,'HH24:MI')    as fin,
                            especialista_id, sede_id
                       from huecos_del_dia(p_fecha=>%s, p_sede=>%s,
                            p_especialista=>null, p_servicio=>%s,
                            p_duracion=>null, p_paso=>%s)""",
                 (fecha, sid, servicio, PASO))
    corte = (ahora_co() + timedelta(minutes=20)).strftime("%H:%M")
    es_hoy = fecha == hoy_co().isoformat()
    return [f for f in filas
            if (not SOLO_REDONDAS or re.match(r"^\d{2}:(00|30)$", f["inicio"] or ""))
            and not (es_hoy and f["inicio"] < corte)]


def _cita_en_agenda(cid: str) -> dict:
    return uno("""select id, fecha, to_char(inicio,'HH24:MI') as inicio,
                         to_char(fin,'HH24:MI') as fin, sede_id, sede,
                         especialista_id, especialista, servicio_id, servicio,
                         cliente_id, estado_id, estado as estado_nombre,
                         estado_tipo, canal
                    from v_agenda where id=%s""", (cid,), "Cita no encontrada")


def _proxima_cita(cliente_id: str, sid: str) -> Optional[dict]:
    """La próxima cita viva de esa clienta EN ESTA SEDE.

    La de hoy sigue contando tres horas después de su hora: una clienta que
    llega veinte minutos tarde tiene que poder decir «ya llegué». Si se
    descartara apenas pasa la hora, ese botón nunca serviría para lo que
    existe."""
    hoy = hoy_co()
    limite = (ahora_co() - timedelta(hours=3)).strftime("%H:%M")
    filas = todos("""select id, fecha, to_char(inicio,'HH24:MI') as inicio,
                            sede_id, especialista_id, especialista,
                            servicio_id, servicio, estado as estado_nombre,
                            estado_tipo
                       from v_agenda
                      where cliente_id=%s and sede_id=%s and tipo='cita'
                        and fecha between %s and %s
                        and coalesce(estado_tipo,'abierto')='abierto'
                      order by fecha, inicio limit 12""",
                 (cliente_id, sid, hoy, hoy + timedelta(days=120)))
    for c in filas:
        if str(c["fecha"])[:10] == hoy.isoformat() and (c["inicio"] or "") < limite:
            continue
        return c
    return None


def _cita_para_pantalla(c: dict, sede: dict) -> dict:
    f = str(c.get("fecha"))[:10]
    return {"id": c.get("id"), "fecha": f, "fecha_larga": fecha_larga(f),
            "cuando": como_dia(f), "hora": hm(c.get("inicio")),
            "hora_larga": hora_12(hm(c.get("inicio"))),
            "servicio": titulizar(c.get("servicio") or "Su cita"),
            "servicio_id": c.get("servicio_id"),
            "especialista": titulizar(c.get("especialista") or ""),
            "especialista_id": c.get("especialista_id"),
            "sede": sede.get("nombre"), "direccion": sede.get("direccion"),
            "estado": titulizar(c.get("estado_nombre") or ""),
            "es_hoy": f == hoy_co().isoformat()}


def _pantalla_final(cid: str, titulo: str) -> dict:
    c = _cita_en_agenda(cid)
    sede = _sede_fila(c.get("sede_id"))
    f = str(c.get("fecha"))[:10]
    return {"titulo": titulo, "cita_id": c.get("id"),
            "servicio": titulizar(c.get("servicio") or ""),
            "fecha": f, "fecha_larga": fecha_larga(f), "cuando": como_dia(f),
            "hora": hm(c.get("inicio")), "hora_larga": hora_12(hm(c.get("inicio"))),
            "sede": sede["nombre"], "direccion": sede["direccion"],
            "especialista": titulizar(c.get("especialista") or ""),
            "estado": titulizar(c.get("estado_nombre") or "")}


# ═══════════════════════════════════════════════════════ los endpoints ═════
class AbrirReq(BaseModel):
    correo: str
    clave: str
    sede: Optional[str] = None
    k: Optional[str] = None


@router.post("/autoservicio/abrir")
def as_abrir(req: AbrirReq, request: Request):
    """La recepcionista abre la tablet con su propio usuario de la agenda.
    No se crea ninguna cuenta nueva ni se guarda ninguna contraseña aquí."""
    try:
        if not clave_ok(request, req.k):
            raise Problema("CERRADO", "Esta tablet no está habilitada.", 403)
        # Adivinar contraseñas se hace despacio o no se hace.
        if not pasa_el_tope(request, "abrir"):
            raise Problema("MUCHOS_INTENTOS",
                           "Demasiados intentos. Espere un minuto.", 429)
        sid = sede_de(req.sede)
        correo = str(req.correo or "").strip().lower()
        filas = todos("""select id, nombre, correo, rol, activo, clave_hash
                           from usuarios where lower(correo)=%s""", (correo,))
        u = filas[0] if filas else None
        # se compara igual aunque el correo no exista, para no delatar cuáles sí
        bien = clave_correcta(req.clave, u["clave_hash"] if u else None)
        if not u or not u.get("activo") or not bien:
            raise Problema("DATOS_INCORRECTOS",
                           "El correo o la contraseña no coinciden.", 401)
        abierta = abrir_tableta(u, sid, request.headers.get("user-agent", ""))
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    return {"ok": True, **abierta}


@router.post("/autoservicio/cerrar")
def as_cerrar(req: dict, request: Request):
    """Cierra esta tablet. Vuelve a pedir usuario y contraseña.

    Hay que traer la llave de la tablet para cerrarla, así que no se puede
    cerrar la de otra sede a ciegas; el tope está para que tampoco sirva para
    ir probando llaves."""
    # El tope se cuenta SIEMPRE, y antes de mirar la clave: si se evaluara
    # después, un `or` que corta dejaría sin tope justo el caso que importa,
    # que es alguien probando claves.
    topado = not pasa_el_tope(request, "abrir")
    if topado or not clave_ok(request, req.get("k")):
        return mal(Problema("CERRADO", "No disponible.", 403))
    cerrar_tableta(_token_de(request, str(req.get("t") or "")))
    return {"ok": True}


@router.get("/autoservicio/datos")
def as_datos(request: Request, sede: Optional[str] = Query(None),
             k: Optional[str] = Query(None), t: Optional[str] = Query(None)):
    """Lo que la tablet necesita al abrir: su sede, los servicios que de
    verdad se pueden hacer ahí, y los tipos de documento."""
    try:
        puerta(request, k, "otros", t)
        sid = sede_de(sede)
        esp = todos("""select e.id,
                              coalesce((select array_agg(x.servicio_id)
                                          from especialista_servicios x
                                         where x.especialista_id=e.id),'{}') as servicios
                         from especialistas e
                         join especialista_sedes s on s.especialista_id=e.id
                        where e.activo and s.sede_id=%s""", (sid,))
        # Una especialista SIN servicios asignados hace todos; con servicios
        # asignados, solo esos (§8.6).
        hace_todo = any(not (e.get("servicios") or []) for e in esp)
        puede = {s for e in esp for s in (e.get("servicios") or [])}
        servicios = [{"id": s["id"], "nombre": titulizar(s["nombre"]),
                      "duracion": s.get("duracion") or 30}
                     for s in todos("""select s.id, s.nombre, s.duracion
                                         from servicios s
                                         left join citas c on c.servicio_id = s.id
                                        where s.activo
                                        group by s.id, s.nombre, s.duracion
                                        /* Los mas pedidos primero: para
                                           encontrar «Toxina - Botox» habia que
                                           bajar 27 fichas en una tablet. */
                                        order by count(c.id) desc, s.nombre""")
                     if hace_todo or s["id"] in puede]
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    return {"ok": True, "sede": dict(_sede_fila(sid), apodo=sede),
            "servicios": servicios,
            "tipos_doc": [{"v": v, "t": t} for v, t in TIPOS_DOC],
            "call_center": CALL_CENTER, "hoy": hoy_co().isoformat()}


class DocReq(BaseModel):
    documento: str
    sede: Optional[str] = None
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/cliente")
def as_cliente(req: DocReq, request: Request):
    """Quién es y qué tiene. El celular y el correo salen tapados: la clienta
    reconoce si son los suyos, pero la pantalla no sirve para sacar la base
    de datos a punta de probar cédulas."""
    try:
        puerta(request, req.k, "cliente", req.t)
        doc = solo_digitos(req.documento)
        if not DOC_MIN <= len(doc) <= DOC_MAX:
            raise Problema("DOC", f"Un documento tiene entre {DOC_MIN} y {DOC_MAX} "
                                  "dígitos. Revíselo, por favor.", 400)
        sid = sede_de(req.sede)
        sede = _sede_fila(sid)
        encontrados = todos("select * from buscar_cliente(null,%s,null)", (doc,))
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))

    exacto = next((c for c in encontrados
                   if solo_digitos(c.get("documento")) == doc), None)
    if not exacto:
        return {"ok": True, "encontrado": False, "documento": doc}

    try:
        cita = _proxima_cita(exacto["id"], sid)
    except Exception:
        cita = None                 # no poder leer la cita no le impide agendar

    tel, correo = exacto.get("telefono") or "", exacto.get("correo") or ""
    return {"ok": True, "encontrado": True,
            "cliente": {"id": exacto["id"], "nombre": nombre_cliente(exacto),
                        "primer_nombre": titulizar(exacto.get("primer_nombre")),
                        "primer_apellido": titulizar(exacto.get("primer_apellido")),
                        "tipo_doc": exacto.get("tipo_doc") or "CC",
                        "documento": exacto.get("documento") or doc,
                        "telefono": tel if DATOS_COMPLETOS else tapar_telefono(tel),
                        "correo": correo if DATOS_COMPLETOS else tapar_correo(correo),
                        "tiene_telefono": bool(solo_digitos(tel)),
                        "tiene_correo": bool(correo)},
            "cita": _cita_para_pantalla(cita, sede) if cita else None,
            "puede_cambiar": cambios_de_hoy(doc) == 0,
            "mensaje_limite": mensaje_limite()}


class GuardarReq(BaseModel):
    cliente_id: Optional[str] = None
    documento: str
    tipo_doc: str = "CC"
    primer_nombre: str = ""
    primer_apellido: str = ""
    telefono: str = ""
    correo: str = ""
    sede: Optional[str] = None
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/cliente/guardar")
def as_guardar(req: GuardarReq, request: Request):
    """Crea la ficha o la actualiza. Al estar dentro de la agenda se llama
    directo a crear_cliente(), que SÍ recibe el tipo de documento — por la
    puerta HTTP había que mandarlo después con un PUT aparte."""
    try:
        puerta(request, req.k, "otros", req.t)
        sid = sede_de(req.sede)
        doc = solo_digitos(req.documento)
        nombre, apellido = req.primer_nombre.strip(), req.primer_apellido.strip()
        tel, correo = solo_digitos(req.telefono), req.correo.strip()
        tipo = (req.tipo_doc or "CC").strip().upper()

        # Todos son obligatorios (§4.3). Se avisa el primero que falte: en una
        # tablet se corrige de a uno, no de a cinco.
        if not doc:
            raise Problema("DOC", "Falta el número de documento.", 400)
        if not DOC_MIN <= len(doc) <= DOC_MAX:
            raise Problema("DOC", f"Un documento tiene entre {DOC_MIN} y {DOC_MAX} "
                                  "dígitos. Revíselo, por favor.", 400)
        if tipo not in dict(TIPOS_DOC):
            raise Problema("TIPO", "Escoja el tipo de documento.", 400)
        if len(nombre) < 2:
            raise Problema("NOMBRE", "Falta su nombre.", 400)
        if len(apellido) < 2:
            raise Problema("APELLIDO", "Falta su apellido.", 400)
        if len(tel) < 10:
            raise Problema("TELEFONO", "El celular debe tener 10 dígitos.", 400)
        if not correo_valido(correo):
            raise Problema("CORREO", "Revise el correo, por favor.", 400)

        if req.cliente_id:
            cli = uno("""update clientes set tipo_doc=%s, primer_nombre=%s,
                                primer_apellido=%s, telefono=%s, correo=%s
                          where id=%s returning *""",
                      (tipo, nombre.upper(), apellido.upper(), tel, correo,
                       req.cliente_id), "No encontramos su ficha.")
        else:
            cli = uno("""select * from crear_cliente(p_documento=>%s,
                              p_primer_nombre=>%s, p_primer_apellido=>%s,
                              p_telefono=>%s, p_correo=>%s, p_tipo_doc=>%s,
                              p_sede=>%s, p_por=>%s)""",
                      (doc, nombre, apellido, tel, correo, tipo, sid, CANAL),
                      "No pudimos registrarla.")
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    return {"ok": True, "cliente": {"id": cli.get("id"),
                                    "nombre": nombre_cliente(cli),
                                    "primer_nombre": titulizar(cli.get("primer_nombre"))}}


class HorasReq(BaseModel):
    sede: Optional[str] = None
    servicio: str
    fecha: str
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/horas")
def as_horas(req: HorasReq, request: Request):
    try:
        puerta(request, req.k, "otros", req.t)
        sid = sede_de(req.sede)
        fecha = date.fromisoformat(req.fecha[:10])
        if fecha < hoy_co():
            raise Problema("FECHA", "Esa fecha ya pasó.", 400)
        filas = _huecos(sid, req.servicio, fecha.isoformat())
        nombres = _nombres_esp()
    except ValueError:
        return mal(Problema("FECHA", "Esa fecha no es válida.", 400))
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))

    por_hora: dict = {}
    for f in filas:
        por_hora.setdefault(f["inicio"], set()).add(f["especialista_id"])
    horas = [{"hora": h, "hora_larga": hora_12(h), "cuantas": len(ids),
              "especialistas": [{"id": i, "nombre": nombres.get(i, "Especialista")}
                                for i in sorted(ids, key=lambda x: nombres.get(x, ""))]}
             for h, ids in sorted(por_hora.items())]
    return {"ok": True, "fecha": fecha.isoformat(),
            "fecha_larga": fecha_larga(fecha), "cuando": como_dia(fecha),
            "horas": horas}


class EspReq(BaseModel):
    sede: Optional[str] = None
    servicio: str
    fecha: str
    hora: str
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/especialistas")
def as_especialistas(req: EspReq, request: Request):
    try:
        puerta(request, req.k, "otros", req.t)
        sid = sede_de(req.sede)
        filas = _huecos(sid, req.servicio, req.fecha[:10])
        nombres = _nombres_esp()
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    ids = sorted({f["especialista_id"] for f in filas if f["inicio"] == req.hora[:5]},
                 key=lambda x: nombres.get(x, ""))
    return {"ok": True,
            "especialistas": [{"id": i, "nombre": nombres.get(i, "Especialista")}
                              for i in ids]}


class ReservaReq(BaseModel):
    sede: Optional[str] = None
    servicio: str
    fecha: str
    hora: str
    especialista: Optional[str] = None      # vacío = "me da igual"
    mio: Optional[str] = None    # la reserva que YA tiene apartada ella misma
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/reservar")
def as_reservar(req: ReservaReq, request: Request):
    """Aparta la hora mientras la clienta termina de decidir. Sin esto, otra
    persona la toma mientras ella escribe (§8.3)."""
    try:
        puerta(request, req.k, "otros", req.t)
        sid = sede_de(req.sede)
        # El servicio se valida ANTES de buscar horas: si no existe o
        # esta inactivo, el mensaje tiene que decir eso. Antes la busqueda
        # de horas iba primero y salia "esa hora se acabo de ocupar", que
        # es falso y confunde a la clienta.
        servicio_activo(req.servicio)
        esp = req.especialista
        if not esp:
            libres = [f for f in _huecos(sid, req.servicio, req.fecha[:10])
                      if f["inicio"] == req.hora[:5]]
            if not libres:
                raise Problema("CUPO_TOMADO", *HUMANO["CUPO_TOMADO"])
            esp = libres[0]["especialista_id"]
        exigir_que_lo_haga(esp, req.servicio)
        # Si esa hora ya la tiene apartada ELLA MISMA, no es que "alguien mas
        # la este tomando": se le devuelve la suya. Antes esto salia con un
        # mensaje falso que la asustaba y la mandaba a escoger otra hora sin
        # ninguna necesidad.
        r = None
        if req.mio:
            ya = todos("""select id, expira_en from reservas
                           where id=%s and especialista_id=%s and fecha=%s
                             and inicio=%s and expira_en > now()""",
                       (req.mio, esp, req.fecha[:10], req.hora[:5]))
            if ya:
                r = ya[0]
        if r is None:
            r = uno("""select * from apartar_cupo(p_especialista=>%s, p_sede=>%s,
                            p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                            p_minutos=>%s, p_referencia=>%s, p_canal=>%s)""",
                    (esp, sid, req.fecha[:10], req.hora[:5], req.servicio,
                     MIN_RESERVA, "autoservicio", CANAL), "No se pudo apartar")
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    # Los segundos que le quedan los calcula Postgres: expira_en viene SIN zona
    # y si los contara el navegador le sumaria 5 horas (la trampa de siempre).
    seg = uno("""select greatest(0,
                        ceil(extract(epoch from (expira_en - now())))::int) as s
                   from reservas where id=%s""", (str(r.get("id")),), "Sin reserva")
    return {"ok": True, "reserva": str(r.get("id")), "especialista": esp,
            "expira_en": str(r.get("expira_en")), "segundos": int(seg["s"] or 0)}


@router.post("/autoservicio/soltar")
def as_soltar(req: dict, request: Request):
    """Si la clienta se arrepiente o se va, el cupo vuelve a la agenda."""
    if not clave_ok(request, req.get("k")):
        return mal(Problema("CERRADO", "Esta tablet no está habilitada.", 403))
    r = str(req.get("reserva") or "")
    if r:
        try:
            todos("select soltar_cupo(%s)", (r,))
        except Exception:
            pass
    return {"ok": True}


class AgendarReq(BaseModel):
    cliente_id: str
    sede: Optional[str] = None
    servicio: str
    fecha: str
    hora: str
    especialista: str
    reserva: Optional[str] = None
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


def _confirmar_si_toca(cid: str, fecha: date):
    """Hoy o mañana → Confirmada sola. De pasado mañana en adelante se queda
    en Pendiente, que es donde recepción espera verla (§4.2)."""
    if fecha > hoy_co() + timedelta(days=1):
        return
    eid = _estado_id("Confirmado")
    if not eid:
        return
    try:
        todos("select * from cambiar_estado(%s,%s,%s,%s)", (cid, eid, CANAL, ""))
    except Exception:
        pass                      # la cita ya existe; el estado es lo secundario


@router.post("/autoservicio/agendar")
def as_agendar(req: AgendarReq, request: Request):
    try:
        puerta(request, req.k, "otros", req.t)
        sid = sede_de(req.sede)
        fecha = date.fromisoformat(req.fecha[:10])
        if fecha < hoy_co():
            raise Problema("FECHA", "Esa fecha ya pasó.", 400)
        servicio_activo(req.servicio)
        exigir_que_lo_haga(req.especialista, req.servicio)
        cita = uno("""select * from agendar_cita(p_cliente=>%s, p_especialista=>%s,
                           p_sede=>%s, p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                           p_canal=>%s, p_por=>%s, p_reserva=>%s)""",
                   (req.cliente_id, req.especialista, sid, fecha.isoformat(),
                    req.hora[:5], req.servicio, CANAL, CANAL, req.reserva or None),
                   "No se pudo agendar")
        _confirmar_si_toca(cita["id"], fecha)
        pantalla = _pantalla_final(cita["id"], "Su cita quedó agendada")
    except ValueError:
        return mal(Problema("FECHA", "Esa fecha no es válida.", 400))
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    return {"ok": True, "cita": pantalla}


# ───────────────────────────────────────────────────────── ya llegué ───────
def _cliente_y_cita(documento: str, cita_id: str, sid: str):
    """Comprueba que la cita sea de quien dice ser y de esta sede. Sin esto,
    mandar el id de una cita ajena tocaría la cita de otra persona."""
    doc = solo_digitos(documento)
    clientes = todos("select * from buscar_cliente(null,%s,null)", (doc,))
    exacto = next((c for c in clientes
                   if solo_digitos(c.get("documento")) == doc), None)
    if not exacto:
        raise Problema("CLIENTE_NO_EXISTE", *HUMANO["CLIENTE_NO_EXISTE"])
    cita = _proxima_cita(exacto["id"], sid)
    if not cita or cita["id"] != cita_id:
        raise Problema("CITA_NO_EXISTE",
                       "Esa cita ya no está disponible. Pase a recepción.", 404)
    return exacto, cita


class LlegadaReq(BaseModel):
    documento: str
    cita_id: str
    sede: Optional[str] = None
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/llegada")
def as_llegada(req: LlegadaReq, request: Request):
    """La clienta se anuncia. Recepción lo ve al instante en la agenda.
    No pide verificación y no gasta el cambio del día (§4.12)."""
    try:
        puerta(request, req.k, "otros", req.t)
        sid = sede_de(req.sede)
        cliente, cita = _cliente_y_cita(req.documento, req.cita_id, sid)
        if str(cita["fecha"])[:10] != hoy_co().isoformat():
            raise Problema("NO_ES_HOY", "Esa cita no es para hoy.", 400)
        eid = _estado_id("Llegó")
        if not eid:
            raise Problema("ESTADO", "No pudimos avisarle a recepción. "
                                     "Por favor dígaselo directamente.", 500)
        todos("select * from cambiar_estado(%s,%s,%s,%s)", (cita["id"], eid, CANAL, ""))
        pantalla = _pantalla_final(cita["id"], "Ya quedó anunciada")
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
    pantalla["nombre"] = titulizar(cliente.get("primer_nombre"))
    return {"ok": True, "cita": pantalla}


# ─────────────────────────────────────── reprogramar y cancelar ────────────
class CambioReq(BaseModel):
    documento: str
    cita_id: str
    accion: str                             # "reprogramar" | "cancelar"
    telefono: str = ""                      # el celular con el que quedó la cita
    sede: Optional[str] = None
    fecha: Optional[str] = None             # solo para reprogramar
    hora: Optional[str] = None
    especialista: Optional[str] = None
    servicio: Optional[str] = None          # vacío = se queda con el que tenía
    reserva: Optional[str] = None
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet


@router.post("/autoservicio/cambio")
def as_cambio(req: CambioReq, request: Request):
    """Dos candados antes de tocar una cita que ya existe: el celular con el
    que quedó (§4.9) y un solo cambio por día (§4.5)."""
    try:
        puerta(request, req.k, "cliente", req.t)
        accion = str(req.accion or "").lower()
        if accion not in ("reprogramar", "cancelar"):
            raise Problema("ACCION", "No entendimos qué desea hacer.", 400)
        doc = solo_digitos(req.documento)
        if cambios_de_hoy(doc):
            raise Problema("LIMITE_DIA", mensaje_limite(), 429)

        sid = sede_de(req.sede)
        cliente, cita = _cliente_y_cita(doc, req.cita_id, sid)
        if not mismo_telefono(req.telefono, cliente.get("telefono")):
            raise Problema("TELEFONO_NO_COINCIDE",
                           "Ese celular no coincide con el de la cita. "
                           "Por favor pase a recepción.", 403)

        if accion == "cancelar":
            eid = _estado_id("Cancelado")
            if not eid:
                raise Problema("ESTADO", "No pudimos cancelarla. Pase a recepción.", 500)
            # Cancelar es directo: no se le pregunta la razón (§4.13).
            todos("select * from cambiar_estado(%s,%s,%s,%s)",
                  (cita["id"], eid, CANAL, ""))
            pantalla = _pantalla_final(cita["id"], "Su cita quedó cancelada")
        else:
            if not (req.fecha and req.hora and req.especialista):
                raise Problema("FALTA", "Falta escoger el nuevo horario.", 400)
            fecha = date.fromisoformat(req.fecha[:10])
            if fecha < hoy_co():
                raise Problema("FECHA", "Esa fecha ya pasó.", 400)
            # Antes se mandaba siempre el servicio viejo. Si la clienta lo
            # cambiaba, la hora se apartaba con la duración del nuevo y la cita
            # nacía con la del viejo: dos duraciones distintas para el mismo
            # cupo. Ahora manda el que ella escogió, y se valida igual que al
            # agendar de cero.
            servicio = req.servicio or cita.get("servicio_id")
            servicio_activo(servicio)
            exigir_que_lo_haga(req.especialista, servicio)
            # reprogramar_cita deja la vieja en "Reprogramado" y crea la nueva:
            # el historial queda completo (§8.10).
            nueva = uno("""select * from reprogramar_cita(p_cita=>%s, p_fecha=>%s,
                                p_inicio=>%s, p_especialista=>%s, p_sede=>%s,
                                p_servicio=>%s, p_motivo=>%s, p_por=>%s,
                                p_canal=>%s, p_reserva=>%s)""",
                        (cita["id"], fecha.isoformat(), req.hora[:5],
                         req.especialista, sid, servicio,
                         "La clienta la movió desde el panel de recepción",
                         CANAL, CANAL, req.reserva or None), "No se pudo mover")
            _confirmar_si_toca(nueva["id"], fecha)
            pantalla = _pantalla_final(nueva["id"], "Su cita quedó reprogramada")
    except ValueError:
        return mal(Problema("FECHA", "Esa fecha no es válida.", 400))
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))

    anotar_cambio(doc, accion, cita["id"], sid)
    pantalla["nombre"] = titulizar(cliente.get("primer_nombre"))
    return {"ok": True, "cita": pantalla, "mensaje_limite": mensaje_limite()}


@router.get("/autoservicio/salud")
def as_salud(request: Request, k: Optional[str] = Query(None)):
    """Para saber si la agenda responde, sin necesidad de abrir la tablet."""
    try:
        topado = not pasa_el_tope(request)          # se cuenta siempre, ver arriba
        if topado or not clave_ok(request, k):
            raise Problema("CERRADO", "No disponible.", 403)
        abierta = tableta_viva(_token_de(request))
        return {"ok": True,
                "con_llave": not ABIERTO,
                "tablet_abierta": bool(abierta),
                "abierta_por": (abierta or {}).get("nombre") or None,
                "abierta_hasta": (abierta or {}).get("expira_en") or None,
                "hora_colombia": ahora_co().isoformat(timespec="seconds"),
                "servicios": len(todos("select id from servicios where activo")),
                "especialistas": len(todos("select id from especialistas where activo")),
                "estados": {n: _estado_id(n)
                            for n in ("Confirmado", "Llegó", "Cancelado")},
                "sedes": list(SEDES),
                # C. La dirección sale de la agenda; la del código es el
                # respaldo. Esto dice, por sede, cuál se le está mostrando a la
                # clienta — que es la que fotografía como comprobante.
                "direcciones": {apodo: {
                    "de": _sede_fila(sid).get("direccion_de"),
                    "dice": _sede_fila(sid).get("direccion")}
                    for apodo, sid in SEDES.items()},
                "con_clave": bool(CLAVE),
                "datos_completos": DATOS_COMPLETOS}
    except Problema as p:
        return mal(p)
    except Exception as e:
        return mal(traducir(e))
