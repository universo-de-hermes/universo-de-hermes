"""
Puente entre Pepe y la agenda de CJ Medical.

Cambios frente a la versión anterior:

1. TOKEN. Manda `X-API-Token` en cada llamada. Sin esto, apenas la API pide
   autenticación, todo responde 401 y Pepe se queda mudo.

2. LOS ERRORES YA NO SE TRAGAN. Antes cada función hacía `return {}` cuando la
   API no respondía 200, así que si el cupo se ocupaba mientras conversaban,
   Pepe recibía un diccionario vacío y no tenía idea de por qué. Ahora todo
   devuelve {"ok": False, "error": "CUPO_TOMADO", "mensaje": "..."} y el modelo
   puede decirle al cliente qué pasó.

3. LOS SERVICIOS SE RESUELVEN CONTRA LA AGENDA, no contra una lista quemada.
   Si el administrador crea un servicio nuevo desde la web, Pepe lo encuentra
   sin tocar este archivo. El mapa de sinónimos queda solo como ayuda.

4. Cuando el nombre da para dos cosas, no adivina: devuelve las opciones para
   que Pepe pregunte.
"""
import difflib
import os
import time
import unicodedata
from typing import Optional

import httpx

AGENDA_API = os.environ.get("AGENDA_API", "http://127.0.0.1:8001").rstrip("/")
# OJO: este modulo se importa ANTES de que main.py llame a load_dotenv(),
# asi que leer el token aqui lo dejaba vacio para siempre y la agenda
# respondia 401 en cada llamada. Se lee en el momento de usarlo.
API_TOKEN = os.environ.get("API_TOKEN", "").strip()


def _token() -> str:
    return (os.environ.get("API_TOKEN") or API_TOKEN or "").strip()

TIMEOUT = float(os.environ.get("AGENDA_TIMEOUT", "20"))
# Cada cuánto se puede agendar: la agenda trabaja cada 30 minutos
# (9:00, 9:30, 10:00…), nunca en cuartos.
PASO_MINUTOS = int(os.environ.get("AGENDA_PASO", "30"))


def _cabeceras() -> dict:
    h = {"accept": "application/json"}
    tok = _token()
    if tok:
        h["X-API-Token"] = tok
    return h


MENSAJES = {
    "CUPO_TOMADO":      "Esa hora acaba de ocuparse.",
    "CUPO_APARTADO":    "Otra persona está tomando esa hora en este momento.",
    "FUERA_DE_HORARIO": "La especialista no atiende a esa hora en esa sede.",
    "ALMUERZO":         "Esa hora cae en el horario de almuerzo.",
    "CLIENTE_NO_EXISTE": "No encuentro ese cliente.",
    "HORA_INVALIDA":    "La hora de fin quedó antes que la de inicio.",
    "CITA_NO_EXISTE":   "Esa cita ya no existe.",
    "ESTADO_NO_EXISTE": "Ese estado no existe.",
    "FALTA_DOCUMENTO":  "Falta el número de documento del cliente.",
    "SIN_SESION":       "La agenda no reconoce el token de Pepe.",
    "SOLO_ADMIN":       "Pepe no tiene permiso para eso.",
}


def _fallo(texto: str, estado: int = 0) -> dict:
    """Traduce lo que devolvió la API a algo que el modelo pueda usar."""
    t = str(texto or "")
    for marca, amable in MENSAJES.items():
        if marca in t:
            return {"ok": False, "error": marca, "mensaje": amable}
    if estado == 401:
        return {"ok": False, "error": "SIN_SESION", "mensaje": MENSAJES["SIN_SESION"]}
    if estado == 403:
        return {"ok": False, "error": "SOLO_ADMIN", "mensaje": MENSAJES["SOLO_ADMIN"]}
    return {"ok": False, "error": "ERROR", "mensaje": t[:200] or "La agenda no respondió."}


async def _llamar(metodo: str, ruta: str, cuerpo: dict = None, params: dict = None):
    url = AGENDA_API + ruta
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as c:
            r = await c.request(metodo, url, json=cuerpo, params=params,
                                headers=_cabeceras())
    except Exception as e:
        return {"ok": False, "error": "SIN_CONEXION",
                "mensaje": f"No pude hablar con la agenda ({e.__class__.__name__})."}
    if r.status_code >= 400:
        detalle = ""
        try:
            j = r.json()
            detalle = j.get("detail") or j.get("error") or str(j)
        except Exception:
            detalle = r.text
        return _fallo(detalle, r.status_code)
    try:
        return {"ok": True, "datos": r.json()}
    except Exception:
        return {"ok": True, "datos": None}


# ─────────────────────────────────────────────────── resolver nombres ──────
def _normal(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    return " ".join(s.lower().split())


# Sinónimos: cómo lo dice la gente → cómo se llama en la agenda.
# Es una ayuda, no la fuente de verdad: primero se busca en los servicios reales.
SINONIMOS = {
    "terapia": "terapias de revitalizacion",
    "terapia de revitalizacion": "terapias de revitalizacion",
    "revitalizacion": "terapias de revitalizacion",
    "masaje": "masaje de relajacion",
    "masaje relajante": "masaje de relajacion",
    "carbon": "carbon peel",
    "hidrafacial": "hidrofacial basica",
    "hidrafacial basico": "hidrofacial basica",
    "hidrafacial plus": "hidrafacial plus",
    "depilacion laser": "1 sesion zona m",
    "depilacion laser zona xs": "1 sesion zona xs",
    "depilacion laser zona s": "1 sesion zona s",
    "depilacion laser zona m": "1 sesion zona m",
    "depilacion laser zona l": "1 sesion zona l",
    "laser": "1 sesion zona m",
    "micropigmentacion": "remocion micropigmentacion 1 sesion",
    "remocion de micropigmentacion": "remocion micropigmentacion 1 sesion",
    "valoracion": "consulta medica",
    "valoracion inicial": "consulta medica",
    "valoracion inicial medica": "consulta medica",
    "control": "cita de control medico",
    "botox": "toxina - botox",
    "toxina": "toxina - botox",
    "radiofrecuencia": "radiofrecuencia fraccionada alta intensidad",
    "rf fraccionada": "radiofrecuencia fraccionada alta intensidad",
    "diseno de cejas": "diseno de cejas",
    "tintura de cejas": "tintura de cejas",
    "pestanas": "tintura de pestanas",
}

SINONIMOS_SEDE = {
    "bogota": "bogota", "chico": "bogota", "chico norte": "bogota",
    "medellin": "tesoro", "el tesoro": "tesoro", "tesoro": "tesoro",
    # El nombre completo de la sede y el sitio (el modelo puede repetirlos).
    "parque comercial el tesoro": "tesoro", "parque comercial": "tesoro",
    "c.c. el tesoro": "tesoro", "cc el tesoro": "tesoro",
    "centro comercial el tesoro": "tesoro",
    "cj medical - el tesoro": "tesoro", "cj medical el tesoro": "tesoro",
    "cjmedical el tesoro": "tesoro",
    "cj medical - bogota": "bogota", "cj medical bogota": "bogota",
    "cjmedical bogota": "bogota", "oficity": "bogota",
}

_cache = {"datos": None, "ts": 0.0}


async def datos(refrescar: bool = False) -> dict:
    """Maestros de la agenda, con caché de 5 minutos."""
    if not refrescar and _cache["datos"] and time.time() - _cache["ts"] < 300:
        return _cache["datos"]
    r = await _llamar("GET", "/datos")
    if not r["ok"]:
        return _cache["datos"] or {"sedes": [], "servicios": [],
                                   "estados": [], "especialistas": []}
    _cache["datos"] = r["datos"]
    _cache["ts"] = time.time()
    return _cache["datos"]


# Como el cliente nombra al personal: "la doctora Arias", "el Dr. Cueter".
TITULOS = {"dr", "dra", "doctor", "doctora", "sr", "sra", "senor", "senora",
           "don", "dona", "la", "el", "los", "las", "especialista", "medico",
           "medica", "profesional", "cosmetologa", "cosmetologo", "senorita"}


def _limpia_titulos(s: str) -> str:
    """«la doctora Arias» -> «arias». El cliente nombra a la gente con el
    titulo por delante y eso ensuciaba la comparacion."""
    return " ".join(w for w in _normal(s).split() if w not in TITULOS)


def _parecida(a: str, b: str) -> float:
    """Que tan parecidas son dos palabras. «julieth»/«julie» cuenta como
    igual (una empieza con la otra): el cliente escribe el nombre a su
    manera y en la agenda esta completo."""
    if a == b:
        return 1.0
    if not a or not b:
        return 0.0
    if len(a) >= 3 and len(b) >= 3 and (a.startswith(b) or b.startswith(a)):
        return 0.95
    return difflib.SequenceMatcher(None, a, b).ratio()


def _puntaje(consulta: str, nombre: str) -> float:
    """0.0 a 1.0. Mide cuanto de lo que dijo el cliente aparece en el
    nombre real, no si lo dijo completo.

    Antes exigia que TODAS las palabras coincidieran y dividia por el
    nombre mas largo: «jorge cueter» contra «JORGE RAMIRO CUETER GUZMAN»
    daba 0.25 (umbral 0.5) y Pepe le decia al cliente que esa especialista
    no existia. Ahora da 0.88.
    """
    c, n = _normal(consulta), _normal(nombre)
    if not c or not n:
        return 0.0
    if c == n:
        return 1.0
    if c in n or n in c:
        return 0.9 + min(len(c), len(n)) / max(len(c), len(n)) * 0.1
    pc, pn = c.split(), n.split()
    if not pc or not pn:
        return 0.0
    usadas, suma = set(), 0.0
    for w in pc:
        mejor, cual = 0.0, None
        for j, x in enumerate(pn):
            if j in usadas:
                continue
            s = _parecida(w, x)
            if s > mejor:
                mejor, cual = s, j
        if mejor >= 0.8:
            usadas.add(cual)
            suma += mejor
    cobertura = suma / len(pc)                  # cuanto de lo pedido aparece
    precision = suma / max(len(pc), len(pn))    # cuanto del nombre se uso
    return round(0.75 * cobertura + 0.25 * precision, 4)


def _variantes(nombres: str, apellidos: str) -> list:
    """Las formas en que la gente dice un nombre completo: «Jorge Cueter»,
    «Cueter», «Cueter Guzman», «Jorge Ramiro Cueter Guzman». El personal se
    conoce por el nombre corto y asi lo dice el cliente."""
    n = _normal(nombres).split()
    a = _normal(apellidos).split()
    v = []
    if n or a:
        v.append(" ".join(n + a))
    if n and a:
        v.append("%s %s" % (n[0], a[0]))
    if len(a) >= 2:
        v.append("%s %s" % (a[0], a[-1]))
    for w in n + a:
        if len(w) > 3:
            v.append(w)
    return [x for x in dict.fromkeys(v) if x]


async def resolver_servicio(texto: str) -> dict:
    """Devuelve {'ok':True,'id':…,'nombre':…} o, si hay varios parecidos,
    {'ok':False,'error':'AMBIGUO','opciones':[…]} para que Pepe pregunte."""
    d = await datos()
    servicios = d.get("servicios") or []
    if not servicios:
        return {"ok": False, "error": "SIN_DATOS",
                "mensaje": "No pude leer la lista de servicios."}
    consulta = _normal(texto)
    consulta = SINONIMOS.get(consulta, consulta)

    for s in servicios:                       # por id exacto
        if _normal(s["id"]) == consulta or s["id"] == texto:
            return {"ok": True, "id": s["id"], "nombre": s["nombre"],
                    "duracion": s.get("duracion")}

    marcados = sorted(
        ({"id": s["id"], "nombre": s["nombre"], "duracion": s.get("duracion"),
          "p": _puntaje(consulta, s["nombre"])} for s in servicios),
        key=lambda x: -x["p"])
    mejor = marcados[0]
    if mejor["p"] >= 0.99:
        return {"ok": True, **mejor}
    cerca = [m for m in marcados if m["p"] >= 0.55]
    if len(cerca) == 1:
        return {"ok": True, **cerca[0]}
    if len(cerca) > 1 and cerca[0]["p"] - cerca[1]["p"] > 0.2:
        return {"ok": True, **cerca[0]}
    if cerca:
        return {"ok": False, "error": "AMBIGUO",
                "mensaje": "Ese nombre puede ser varios servicios.",
                "opciones": [{"id": c["id"], "nombre": c["nombre"]} for c in cerca[:5]]}
    return {"ok": False, "error": "NO_EXISTE",
            "mensaje": f"No tengo un servicio que se llame «{texto}».",
            "opciones": [{"id": s["id"], "nombre": s["nombre"]} for s in servicios[:12]]}


async def resolver_sede(texto: str) -> dict:
    d = await datos()
    sedes = d.get("sedes") or []
    consulta = _normal(texto)
    consulta = SINONIMOS_SEDE.get(consulta, consulta)
    for s in sedes:
        if s["id"] == texto or consulta and consulta in _normal(s["id"] + " " + s["nombre"] + " " + (s.get("ciudad") or "")):
            return {"ok": True, "id": s["id"], "nombre": s["nombre"]}
    return {"ok": False, "error": "NO_EXISTE",
            "mensaje": f"No tengo una sede que se llame «{texto}».",
            "opciones": [{"id": s["id"], "nombre": s["nombre"]} for s in sedes]}


async def especialistas_para(servicio: str = None, sede: str = None) -> list:
    """Quienes pueden atender ese servicio en esa sede, con su nombre real.

    Es la lista que Pepe debe ofrecer. Antes salia de una lista quemada en
    el prompt y terminaba ofreciendo a alguien que no hace el servicio.
    """
    d = await datos()
    sede_id = servicio_id = None
    if sede:
        rs = await resolver_sede(sede)
        sede_id = rs.get("id") if rs.get("ok") else None
    if servicio:
        rv = await resolver_servicio(servicio)
        servicio_id = rv.get("id") if rv.get("ok") else None
    salida = []
    for e in (d.get("especialistas") or []):
        if not e.get("activo", True):
            continue
        if sede_id and sede_id not in (e.get("sedes") or []):
            continue
        svs = e.get("servicios") or []
        # sin servicios asignados = hace todos (misma regla que la web)
        if servicio_id and svs and servicio_id not in svs:
            continue
        salida.append({"id": e["id"],
                       "nombre": (str(e.get("nombres", "")) + " " +
                                  str(e.get("apellidos", ""))).strip()})
    return salida


async def resolver_especialista(texto: str, sede: str = None,
                                servicio: str = None) -> dict:
    """La especialista por nombre, como la dijo el cliente.

    Acepta el nombre corto («Dr. Cueter», «la doctora Arias», «Valentina»):
    se compara contra las formas en que se puede decir cada nombre real, no
    contra una lista quemada. Si se sabe la sede o el servicio, solo se mira
    entre quienes de verdad pueden atenderlos ahi.
    """
    if not texto:
        return {"ok": True, "id": None, "nombre": None}
    d = await datos()
    esp = [e for e in (d.get("especialistas") or []) if e.get("activo", True)]
    if not esp:
        return {"ok": False, "error": "SIN_DATOS",
                "mensaje": "No pude leer la lista del personal."}

    sede_id = servicio_id = None
    if sede:
        rs = await resolver_sede(sede)
        sede_id = rs.get("id") if rs.get("ok") else None
    if servicio:
        rv = await resolver_servicio(servicio)
        servicio_id = rv.get("id") if rv.get("ok") else None

    def _puede(e: dict) -> bool:
        if sede_id and sede_id not in (e.get("sedes") or []):
            return False
        svs = e.get("servicios") or []
        if servicio_id and svs and servicio_id not in svs:
            return False
        return True

    consulta = _limpia_titulos(texto) or _normal(texto)
    marcados = []
    for e in esp:
        nombre = (str(e.get("nombres", "")) + " " + str(e.get("apellidos", ""))).strip()
        p = max([_puntaje(consulta, v)
                 for v in _variantes(e.get("nombres", ""), e.get("apellidos", ""))] or [0.0])
        marcados.append({"id": e["id"], "nombre": nombre, "p": round(p, 4),
                         "puede": _puede(e)})
    marcados.sort(key=lambda x: -x["p"])

    aptos = [m for m in marcados if m["puede"]]
    if not aptos:
        return {"ok": False, "error": "NO_EXISTE",
                "mensaje": "No hay nadie que atienda eso ahi.",
                "opciones": [{"id": m["id"], "nombre": m["nombre"]}
                             for m in marcados[:6]]}

    if marcados[0]["p"] >= 0.6 and not marcados[0]["puede"]:
        # La reconozco, pero no hace ese servicio en esa sede. Se le dice
        # claro al cliente y se le ofrecen solo quienes si pueden.
        return {"ok": False, "error": "NO_LO_HACE",
                "mensaje": f"{marcados[0]['nombre']} no atiende eso ahi.",
                "quien_si": [{"id": m["id"], "nombre": m["nombre"]} for m in aptos[:6]],
                "nota": ("Dile al cliente que esa especialista no atiende ese "
                         "servicio en esa sede y ofrécele estas opciones TAL CUAL.")}

    mejor = aptos[0]
    empatados = [m for m in aptos if m["p"] >= 0.6 and mejor["p"] - m["p"] < 0.08]
    if len(empatados) > 1:
        return {"ok": False, "error": "AMBIGUO",
                "mensaje": "Hay mas de una especialista que se llama asi.",
                "opciones": [{"id": m["id"], "nombre": m["nombre"]} for m in empatados]}
    if mejor["p"] >= 0.6:
        return {"ok": True, "id": mejor["id"], "nombre": mejor["nombre"]}

    return {"ok": False, "error": "NO_EXISTE",
            "mensaje": f"No tengo a nadie registrado como «{texto}».",
            "opciones": [{"id": m["id"], "nombre": m["nombre"]} for m in aptos[:6]],
            "nota": ("Ofrécele al cliente estas opciones TAL CUAL. No inventes "
                     "que alguien «no está en esa ciudad»: si está en esta "
                     "lista, sí atiende ese servicio ahí.")}


def nombre_servicio(sid: str) -> str:
    for s in (_cache["datos"] or {}).get("servicios", []):
        if s["id"] == sid:
            return s["nombre"]
    return sid


def nombre_sede(sid: str) -> str:
    for s in (_cache["datos"] or {}).get("sedes", []):
        if s["id"] == sid:
            return s["nombre"]
    return sid


def nombre_especialista(eid: str) -> str:
    for e in (_cache["datos"] or {}).get("especialistas", []):
        if e["id"] == eid:
            return (str(e.get("nombres", "")) + " " + str(e.get("apellidos", ""))).strip()
    return eid


# ───────────────────────────────────────────────────────────── clientes ────
async def buscar_cliente(telefono: str = None, documento: str = None,
                         nombre: str = None) -> dict:
    r = await _llamar("POST", "/clientes/buscar",
                      {"telefono": telefono, "documento": documento, "nombre": nombre})
    if not r["ok"]:
        return r
    return {"ok": True, "clientes": r["datos"] or []}


async def crear_cliente(documento: str, primer_nombre: str, primer_apellido: str,
                        telefono: str = "", correo: str = "",
                        sede: str = None) -> dict:
    r = await _llamar("POST", "/clientes/crear", {
        "documento": documento, "primer_nombre": primer_nombre,
        "primer_apellido": primer_apellido, "telefono": telefono,
        "correo": correo or None, "sede": sede})
    if not r["ok"]:
        return r
    return {"ok": True, "cliente": r["datos"]}


async def actualizar_cliente(cliente_id: str, **campos) -> dict:
    """Corrige la ficha de un cliente que YA existe. Manda solo lo que cambia."""
    limpio = {k: v for k, v in campos.items() if v not in (None, "")}
    if not limpio:
        return {"ok": False, "error": "SIN_CAMBIOS",
                "mensaje": "No me dijiste qué dato hay que cambiar."}
    r = await _llamar("PUT", f"/clientes/{cliente_id}", limpio)
    if not r["ok"]:
        return r
    return {"ok": True, "cliente": r["datos"]}


async def citas_del_cliente(cliente_id: str) -> dict:
    r = await _llamar("GET", f"/clientes/{cliente_id}")
    if not r["ok"]:
        return r
    d = r["datos"] or {}
    proximas = [c for c in (d.get("citas") or [])
                if str(c.get("fecha", "")) >= time.strftime("%Y-%m-%d")]
    return {"ok": True, "cliente": d, "citas": proximas}


async def cita_del_cliente(cliente_id: str, fecha: str = None,
                           hora: str = None) -> dict:
    """La cita del cliente: la que coincida con fecha/hora, o la próxima.

    Sirve para confirmar, cancelar o mover sin depender del cita_id: el
    modelo no ve los resultados de sus herramientas entre mensajes, así que
    no se puede confiar en que se acuerde del id.
    """
    r = await citas_del_cliente(cliente_id)
    if not r["ok"]:
        return r
    citas = r["citas"] or []
    if fecha:
        del_dia = [c for c in citas if str(c.get("fecha"))[:10] == str(fecha)[:10]]
        if del_dia:
            citas = del_dia
    if hora:
        con_hora = [c for c in citas if str(c.get("inicio"))[:5] == str(hora)[:5]]
        if con_hora:
            citas = con_hora
    if not citas:
        return {"ok": False, "error": "CITA_NO_EXISTE",
                "mensaje": "Ese cliente no tiene citas próximas."}
    c = citas[0]
    return {"ok": True, "cita_id": c.get("cita_id") or c.get("id"),
            "fecha": str(c.get("fecha"))[:10],
            "hora": str(c.get("inicio"))[:5],
            "servicio": c.get("servicio"), "sede": c.get("sede"),
            "especialista": c.get("especialista"),
            "estado": c.get("estado")}


# ─────────────────────────────────────────────────────── horas y citas ────
async def horas_libres(servicio: str, sede: str, fecha: str = None,
                       dias: int = 7, especialista: str = None,
                       limite: int = 60) -> dict:
    """Horas libres reales. Si no se da fecha, busca en los próximos días."""
    sv = await resolver_servicio(servicio)
    if not sv["ok"]:
        return sv
    sd = await resolver_sede(sede)
    if not sd["ok"]:
        return sd
    ep = await resolver_especialista(especialista)
    if not ep["ok"]:
        return ep

    if fecha:
        r = await _llamar("POST", "/huecos/dia", {
            "fecha": fecha, "sede": sd["id"], "servicio": sv["id"],
            "especialista": ep["id"], "paso": PASO_MINUTOS})
    else:
        r = await _llamar("POST", "/huecos/buscar", {
            "desde": time.strftime("%Y-%m-%d"), "dias": dias,
            "sede": sd["id"], "servicio": sv["id"],
            "especialista": ep["id"], "paso": PASO_MINUTOS,
            "limite": limite})
    if not r["ok"]:
        return r

    # La agenda agenda cada 30 minutos: las citas empiezan en punto o y
    # media. La función de la base ya genera los candidatos cada
    # PASO_MINUTOS desde el inicio del horario, pero se filtra igual por si
    # algún horario de especialista empieza a una hora rara.
    def _en_punto_o_media(hora) -> bool:
        return str(hora or "").strip()[-2:] in ("00", "30")

    huecos = [h for h in (r["datos"] or [])
              if _en_punto_o_media(h.get("inicio"))]
    # agrupadas por día, con la especialista, para que Pepe ofrezca sin marear
    por_dia = {}
    vistas = set()
    for hu in huecos:
        f = str(hu["fecha"])[:10]
        # Dos especialistas libres a la misma hora: se ofrece una sola vez.
        clave = (f, str(hu["inicio"]))
        if clave in vistas:
            continue
        vistas.add(clave)
        por_dia.setdefault(f, []).append({
            "hora": hu["inicio"], "fin": hu["fin"],
            "especialista_id": hu["especialista_id"],
            "especialista": nombre_especialista(hu["especialista_id"]),
            "sede_id": hu["sede_id"]})
    return {"ok": True, "servicio": sv["nombre"], "servicio_id": sv["id"],
            "sede": sd["nombre"], "sede_id": sd["id"],
            "duracion": sv.get("duracion"),
            "dias": [{"fecha": f, "horas": por_dia[f]} for f in sorted(por_dia)]}


def _proximos_dias(dias: int) -> list:
    """Fechas de hoy en adelante, en formato AAAA-MM-DD.
    Se ancla a las 12:00 para que un cambio de hora no corra el día."""
    h = time.localtime()
    base = time.mktime((h.tm_year, h.tm_mon, h.tm_mday, 12, 0, 0, 0, 0, -1))
    return [time.strftime("%Y-%m-%d", time.localtime(base + i * 86400))
            for i in range(max(1, min(int(dias), 30)))]


async def horario_especialista(especialista: str, fecha: str = None,
                               dias: int = 7, sede: str = None,
                               servicio: str = None) -> dict:
    """¿Esta especialista trabaja ese día? ¿A qué horas tiene cupo?

    Sin fecha revisa los próximos `dias` y devuelve solo los días en que
    trabaja, para poder decir «el lunes no, pero el martes sí».
    """
    ep = await resolver_especialista(especialista)
    if not ep["ok"]:
        return ep
    sd = await resolver_sede(sede) if sede else {"ok": True, "id": None}
    if not sd["ok"]:
        return sd
    sv = await resolver_servicio(servicio) if servicio else {"ok": True, "id": None}
    if not sv["ok"]:
        return sv

    fechas = [fecha] if fecha else _proximos_dias(dias)
    salida = []
    for f in fechas:
        params = {"especialista": ep["id"], "fecha": f, "paso": PASO_MINUTOS}
        if sd.get("id"):
            params["sede"] = sd["id"]
        if sv.get("id"):
            params["servicio"] = sv["id"]
        r = await _llamar("GET", "/agenda-especialista", params=params)
        if not r["ok"]:
            return r
        d = r["datos"] or {}
        franjas = d.get("franjas") or []
        libres = [h.get("inicio") for h in (d.get("libres") or [])
                  if str(h.get("inicio", ""))[-2:] in ("00", "30")]
        if not franjas:
            # si preguntó por un día puntual hay que poder decir «no trabaja»
            if fecha:
                salida.append({"fecha": f, "trabaja": False})
            continue
        fr = franjas[0]
        alm = ("%s a %s" % (fr["alm_desde"], fr["alm_hasta"])
               if fr.get("alm_desde") and fr.get("alm_hasta") else None)
        salida.append({
            "fecha": f, "trabaja": True, "sede": fr.get("sede"),
            "horario": "%s a %s" % (fr.get("desde"), fr.get("hasta")),
            "almuerzo": alm, "libres": libres[:6],
            "hay_mas_horas": len(libres) > 6,
            "origen": fr.get("origen")})

    return {"ok": True, "especialista": ep["nombre"],
            "especialista_id": ep["id"],
            "consulta": fecha or ("próximos %d días" % len(fechas)),
            "dias": salida}


async def especialista_libre(sede_id: str, servicio_id: str, fecha: str,
                             hora: str) -> dict:
    """Quien esta libre a esa hora para ese servicio.

    Se usa cuando el cliente no pidio a nadie: antes Pepe tenia que nombrar
    una especialista y la inventaba (de ahi salio el «ESPECIALISTA_NO_
    DISPONIBLE: Valentina Baquero»).
    """
    r = await _llamar("POST", "/huecos/dia", {
        "fecha": fecha, "sede": sede_id, "servicio": servicio_id,
        "especialista": None, "paso": PASO_MINUTOS})
    if not r["ok"]:
        return r
    for h in (r["datos"] or []):
        if str(h.get("inicio"))[:5] == str(hora)[:5]:
            return {"ok": True, "especialista_id": h["especialista_id"],
                    "especialista": nombre_especialista(h["especialista_id"])}
    return {"ok": False, "error": "SIN_CUPO",
            "mensaje": "A esa hora ya no hay nadie libre para ese servicio."}


async def apartar_cupo(especialista_id: str, sede_id: str, fecha: str, hora: str,
                       servicio_id: str, referencia: str = "",
                       minutos: int = 5) -> dict:
    if not especialista_id:
        rl = await especialista_libre(sede_id, servicio_id, fecha, hora)
        if not rl["ok"]:
            return rl
        especialista_id = rl["especialista_id"]
    r = await _llamar("POST", "/cupos/apartar", {
        "especialista": especialista_id, "sede": sede_id, "fecha": fecha,
        "inicio": hora, "servicio": servicio_id, "minutos": minutos,
        "referencia": referencia})
    if not r["ok"]:
        return r
    return {"ok": True, "reserva": (r["datos"] or {}).get("id"),
            "vence": (r["datos"] or {}).get("expira_en")}


async def soltar_cupo(reserva: str) -> dict:
    return await _llamar("DELETE", f"/cupos/{reserva}")


async def agendar(cliente_id: str, especialista_id: str, sede_id: str,
                  fecha: str, hora: str, servicio_id: str,
                  notas: str = "", reserva: str = None,
                  canal: str = "Agente IA", por: str = "Pepe",
                  referencia: str = "") -> dict:
    if not especialista_id:
        rl = await especialista_libre(sede_id, servicio_id, fecha, hora)
        if not rl["ok"]:
            return rl
        especialista_id = rl["especialista_id"]
    if not reserva and referencia:
        # La reserva que el mismo aparto bloquea la cita si no se manda: la
        # funcion de Postgres la ve como de otra conversacion y responde
        # CUPO_APARTADO. Como el id no se puede recordar, se busca aqui por
        # la referencia (el telefono con el que se aparto).
        rv = await _llamar("GET", "/cupos/vigente",
                           params={"referencia": referencia, "fecha": fecha,
                                   "inicio": hora})
        if rv["ok"] and (rv["datos"] or {}).get("id"):
            reserva = rv["datos"]["id"]
    cuerpo = {"cliente_id": cliente_id, "especialista": especialista_id,
              "sede": sede_id, "fecha": fecha, "inicio": hora,
              "servicio": servicio_id, "canal": canal, "por": por,
              "notas": notas}
    if reserva:
        cuerpo["reserva"] = reserva
    r = await _llamar("POST", "/citas/agendar", cuerpo)
    if not r["ok"]:
        return r
    c = r["datos"] or {}
    return {"ok": True, "cita_id": c.get("id"), "fecha": str(c.get("fecha")),
            "hora": str(c.get("inicio"))[:5],
            "servicio": nombre_servicio(c.get("servicio_id")),
            "sede": nombre_sede(c.get("sede_id")),
            "especialista": nombre_especialista(c.get("especialista_id"))}


async def cambiar_estado(cita_id: str, estado_tipo: str, motivo: str = "") -> dict:
    """estado_tipo: 'abierto' | 'atendido' | 'ausente' | 'movido' | 'cancelado'.
    Se resuelve contra la tabla de estados, porque CJ Medical los renombra."""
    d = await datos()
    candidatos = [e for e in d.get("estados", [])
                  if e.get("tipo") == estado_tipo and e.get("activo", True)]
    if estado_tipo == "confirmado":
        candidatos = [e for e in d.get("estados", [])
                      if "confirm" in _normal(e.get("nombre", ""))]
    if not candidatos:
        return {"ok": False, "error": "ESTADO_NO_EXISTE",
                "mensaje": f"No hay un estado de tipo {estado_tipo}."}
    r = await _llamar("POST", "/citas/estado", {
        "cita_id": cita_id, "estado": candidatos[0]["id"],
        "por": "pepe", "motivo": motivo})
    if not r["ok"]:
        return r
    return {"ok": True, "estado": candidatos[0]["nombre"]}


async def confirmar(cita_id: str) -> dict:
    return await cambiar_estado(cita_id, "confirmado")


async def cancelar(cita_id: str, motivo: str = "") -> dict:
    return await cambiar_estado(cita_id, "cancelado", motivo)


async def reprogramar(cita_id: str, fecha: str, hora: str,
                      especialista_id: str = None, sede_id: str = None,
                      motivo: str = "") -> dict:
    r = await _llamar("POST", "/citas/reprogramar", {
        "cita_id": cita_id, "fecha": fecha, "inicio": hora,
        "especialista": especialista_id, "sede": sede_id,
        "motivo": motivo, "por": "pepe"})
    if not r["ok"]:
        return r
    c = r["datos"] or {}
    return {"ok": True, "cita_id": c.get("id"), "fecha": str(c.get("fecha")),
            "hora": str(c.get("inicio"))[:5],
            "servicio": nombre_servicio(c.get("servicio_id")),
            "sede": nombre_sede(c.get("sede_id")),
            "especialista": nombre_especialista(c.get("especialista_id"))}


async def citas_de_manana() -> dict:
    """Para los recordatorios del día anterior."""
    manana = time.strftime("%Y-%m-%d", time.localtime(time.time() + 86400))
    r = await _llamar("GET", "/citas", params={"fecha": manana, "limite": 500})
    if not r["ok"]:
        return r
    vivas = [c for c in (r["datos"] or [])
             if c.get("estado_tipo") == "abierto" and c.get("telefono")]
    return {"ok": True, "fecha": manana, "citas": vivas}
