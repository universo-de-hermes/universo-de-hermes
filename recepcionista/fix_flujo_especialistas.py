#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arregla el flujo de especialistas y la sincronizacion del CRM.

BUG 1 — Pepe no reconocia a la especialista que el cliente pedia.
  El cliente pidio "Dr. Jorge Cueter". En la agenda esta como
  "JORGE RAMIRO CUETER GUZMAN". El puntaje comparaba palabras exactas y
  dividia por el nombre mas largo: 0.5 * 2 / 4 = 0.25, y el umbral era 0.5
  -> NO_EXISTE. Pepe, sin datos, se inventaba la razon: "no tengo
  registrado al Dr. Jorge Cueter en la sede de Medellin" (FALSO: si trabaja
  ahi) y despues ofrecia a Valentina Baquero, que ni hace ese servicio.
  Arreglo: se compara contra las formas en que se dice cada nombre real
  ("Jorge Cueter", "Cueter", "Cueter Guzman"), con tolerancia a nombres
  incompletos, y solo se mira entre quienes de verdad atienden ese servicio
  en esa sede.

BUG 2 — La tarjeta del CRM mostraba "Celular: —" y "Correo: —".
  El CRM guarda su propia copia del cliente (SQLite) y nadie la
  actualizaba: los datos los tenia la agenda (Postgres). Arreglo: cuando
  Pepe identifica al cliente por cedula, se sincroniza la ficha del CRM.

Uso:  python3 fix_flujo_especialistas.py
"""
import os
import shutil
import sys

BASE = "/root/universo/recepcionista"
MARCA = ".pre-especialistas.bak"

CAMBIOS = []
CRLF = {}


def leer(p):
    # main.py quedo guardado con saltos de linea de Windows (\r\n): si no se
    # normaliza, ninguna ancla coincide.
    with open(p, encoding="utf-8", newline="") as f:
        bruto = f.read()
    CRLF[p] = "\r\n" in bruto
    if CRLF[p]:
        print("  (aviso) %s usa saltos de linea CRLF" % os.path.basename(p))
    return bruto.replace("\r\n", "\n")


def escribir(p, t):
    if CRLF.get(p):
        t = t.replace("\n", "\r\n")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def respaldar(p):
    b = p + MARCA
    if not os.path.exists(b):
        shutil.copy2(p, b)
        print("  respaldo: %s" % os.path.basename(b))


def cambiar(t, viejo, nuevo, etiqueta):
    n = t.count(viejo)
    if n != 1:
        raise SystemExit("  X ancla '%s' aparece %d veces (se esperaba 1)" % (etiqueta, n))
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)
    return t.replace(viejo, nuevo)


# ══════════════════════════════════════════════ agenda_helper.py ═════════
AH = os.path.join(BASE, "agenda_helper.py")
print("\n== agenda_helper.py ==")
t = leer(AH)
respaldar(AH)

t = cambiar(
    t,
    "import os\nimport time\nimport unicodedata",
    "import difflib\nimport os\nimport time\nimport unicodedata",
    "import difflib",
)

VIEJO_PUNTAJE = '''def _puntaje(consulta: str, nombre: str) -> float:
    c, n = _normal(consulta), _normal(nombre)
    if not c or not n:
        return 0.0
    if c == n:
        return 1.0
    if c in n or n in c:
        return 0.8 + min(len(c), len(n)) / max(len(c), len(n)) * 0.15
    palabras_c, palabras_n = set(c.split()), set(n.split())
    comunes = palabras_c & palabras_n
    if not comunes:
        return 0.0
    return 0.5 * len(comunes) / max(len(palabras_c), len(palabras_n))
'''

NUEVO_PUNTAJE = '''# Como el cliente nombra al personal: "la doctora Arias", "el Dr. Cueter".
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
'''
t = cambiar(t, VIEJO_PUNTAJE, NUEVO_PUNTAJE, "_puntaje tolerante + _variantes")

VIEJO_RESOLVER = '''async def resolver_especialista(texto: str) -> dict:
    if not texto:
        return {"ok": True, "id": None, "nombre": None}
    d = await datos()
    esp = d.get("especialistas") or []
    marcados = sorted(
        ({"id": e["id"],
          "nombre": (str(e.get("nombres", "")) + " " + str(e.get("apellidos", ""))).strip(),
          "p": _puntaje(texto, str(e.get("nombres", "")) + " " + str(e.get("apellidos", "")))}
         for e in esp), key=lambda x: -x["p"])
    if marcados and marcados[0]["p"] >= 0.5:
        return {"ok": True, "id": marcados[0]["id"], "nombre": marcados[0]["nombre"]}
    return {"ok": False, "error": "NO_EXISTE",
            "mensaje": f"No tengo una especialista que se llame «{texto}».",
            "opciones": [{"id": m["id"], "nombre": m["nombre"]} for m in marcados[:6]]}
'''

NUEVO_RESOLVER = '''async def especialistas_para(servicio: str = None, sede: str = None) -> list:
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
'''
t = cambiar(t, VIEJO_RESOLVER, NUEVO_RESOLVER, "resolver_especialista + especialistas_para")

# apartar_cupo: si no hay especialista, la agenda escoge
VIEJO_APARTAR = '''async def apartar_cupo(especialista_id: str, sede_id: str, fecha: str, hora: str,
                       servicio_id: str, referencia: str = "",
                       minutos: int = 5) -> dict:
    r = await _llamar("POST", "/cupos/apartar", {'''
NUEVO_APARTAR = '''async def especialista_libre(sede_id: str, servicio_id: str, fecha: str,
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
    r = await _llamar("POST", "/cupos/apartar", {'''
t = cambiar(t, VIEJO_APARTAR, NUEVO_APARTAR, "apartar_cupo escoge especialista si no la hay")

VIEJO_AGENDAR = '''                  canal: str = "Agente IA", por: str = "Pepe") -> dict:
    cuerpo = {"cliente_id": cliente_id, "especialista": especialista_id,'''
NUEVO_AGENDAR = '''                  canal: str = "Agente IA", por: str = "Pepe") -> dict:
    if not especialista_id:
        rl = await especialista_libre(sede_id, servicio_id, fecha, hora)
        if not rl["ok"]:
            return rl
        especialista_id = rl["especialista_id"]
    cuerpo = {"cliente_id": cliente_id, "especialista": especialista_id,'''
t = cambiar(t, VIEJO_AGENDAR, NUEVO_AGENDAR, "agendar escoge especialista si no la hay")

escribir(AH, t)


# ══════════════════════════════════════════════ herramientas.py ══════════
HR = os.path.join(BASE, "herramientas.py")
print("\n== herramientas.py ==")
t = leer(HR)
respaldar(HR)

VIEJO_RC = '''    salida = {}
    for campo, tipo, etiqueta in (("especialista", "especialista", "la especialista"),
                                  ("sede", "sede", "la sede"),
                                  ("servicio", "servicio", "el servicio")):
        r = await _resolver_uno(a.get(campo) or a.get(campo + "_id"), tipo)
        if not r.get("ok"):
            return r
        if not r.get("id"):
            return {"ok": False, "error": "FALTA_" + tipo.upper(),
                    "mensaje": "Me falta %s para agendar." % etiqueta}
        salida[campo + "_id"] = r["id"]
    return {"ok": True, **salida}
'''
NUEVO_RC = '''    salida = {}
    # Primero la sede y el servicio: con eso se sabe quien puede atender.
    for campo, tipo, etiqueta in (("sede", "sede", "la sede"),
                                  ("servicio", "servicio", "el servicio")):
        r = await _resolver_uno(a.get(campo) or a.get(campo + "_id"), tipo)
        if not r.get("ok"):
            return r
        if not r.get("id"):
            return {"ok": False, "error": "FALTA_" + tipo.upper(),
                    "mensaje": "Me falta %s para agendar." % etiqueta}
        salida[campo + "_id"] = r["id"]
    # La especialista: si el cliente no pidio a nadie, la escoge la agenda
    # entre quienes esten libres. Antes era obligatoria y Pepe se la
    # inventaba ("ESPECIALISTA_NO_DISPONIBLE: Valentina Baquero").
    v = str(a.get("especialista") or a.get("especialista_id") or "").strip()
    if not v:
        salida["especialista_id"] = None
        return {"ok": True, **salida}
    if v.startswith("esp-"):
        salida["especialista_id"] = v
        return {"ok": True, **salida}
    r = await ag.resolver_especialista(v, sede=salida["sede_id"],
                                       servicio=salida["servicio_id"])
    if not r.get("ok"):
        return r
    salida["especialista_id"] = r["id"]
    return {"ok": True, **salida}
'''
t = cambiar(t, VIEJO_RC, NUEVO_RC, "_resolver_cita: especialista opcional y filtrada")

# Sincronizacion del CRM
VIEJO_FICHA = '''def _ficha(c: dict) -> dict:'''
NUEVO_FICHA = '''def _sincronizar_crm(ctx: dict, ficha: dict) -> None:
    """Deja la copia del cliente en el CRM igual a la de la agenda.

    La tarjeta del CRM mostraba «Celular: —» y «Correo: —» aunque Pepe ya
    tenia los datos: el CRM guarda su propia copia (SQLite) y nadie la
    actualizaba cuando Pepe identificaba al cliente por cedula. Nunca puede
    tumbar la conversacion: si falla, se sigue.
    """
    cid = ctx.get("client_id")
    if not cid:
        return
    campos = {}
    if ficha.get("nombre_completo"):
        campos["name"] = str(ficha["nombre_completo"]).strip()
    if ficha.get("telefono"):
        campos["phone"] = str(ficha["telefono"]).strip()
    if ficha.get("correo"):
        campos["email"] = str(ficha["correo"]).strip()
    if ficha.get("documento"):
        campos["document"] = str(ficha["documento"]).strip()
    if not campos:
        return
    try:
        from crm.database import update_client_data
        update_client_data(int(cid), **campos)
    except Exception as e:
        print("  (aviso) no pude sincronizar el CRM: %s" % e)


def _ficha(c: dict) -> dict:'''
t = cambiar(t, VIEJO_FICHA, NUEVO_FICHA, "_sincronizar_crm")

VIEJO_BUSCAR = '''            cl = r["clientes"]
            return {"ok": True, "encontrados": len(cl),
                    "clientes": [_ficha(c) for c in cl[:5]]}
'''
NUEVO_BUSCAR = '''            cl = r["clientes"]
            fichas = [_ficha(c) for c in cl[:5]]
            if fichas:
                _sincronizar_crm(ctx, fichas[0])
            return {"ok": True, "encontrados": len(cl), "clientes": fichas}
'''
t = cambiar(t, VIEJO_BUSCAR, NUEVO_BUSCAR, "buscar_cliente sincroniza el CRM")

VIEJO_REG = '''            c = r["cliente"] or {}
            return {"ok": True, "cliente_id": c.get("id"),
                    "nombre": " ".join(x for x in [c.get("primer_nombre"),
                                                   c.get("primer_apellido")] if x)}
'''
NUEVO_REG = '''            c = r["cliente"] or {}
            _sincronizar_crm(ctx, _ficha(c))
            return {"ok": True, "cliente_id": c.get("id"),
                    "nombre": " ".join(x for x in [c.get("primer_nombre"),
                                                   c.get("primer_apellido")] if x)}
'''
t = cambiar(t, VIEJO_REG, NUEVO_REG, "registrar_cliente sincroniza el CRM")

# ver_horas_libres: decirle a Pepe que cada hora trae su especialista
VIEJO_HORAS = '''                    "duracion_minutos": r["duracion"], "dias": dias,
                    "nota": "Ofrécele dos o tres, no la lista entera."}'''
NUEVO_HORAS = '''                    "duracion_minutos": r["duracion"], "dias": dias,
                    "nota": ("Ofrécele dos o tres, no la lista entera. Cada "
                             "hora trae la especialista que la tiene libre: si "
                             "el cliente no pidió a nadie, no la nombres, solo "
                             "agenda y la agenda le asigna esa misma.")}'''
t = cambiar(t, VIEJO_HORAS, NUEVO_HORAS, "ver_horas_libres explica la especialista")

# ── prompt ──
VIEJO_P7 = '''7. AGENDA. Recién cuando el cliente dijo que sí. Manda la especialista, la
   sede y el servicio por NOMBRE (como los dijo el cliente) y la cédula del
   cliente: la herramienta los busca sola, no necesitas acordarte de los
   ids. Si te devuelve un error, LEE el mensaje, corrige eso y vuelve a
   intentarlo; no le pases el problema al cliente.'''
NUEVO_P7 = '''7. AGENDA. Recién cuando el cliente dijo que sí. Manda la sede y el servicio
   por NOMBRE (como los dijo el cliente) y la cédula del cliente: la
   herramienta los busca sola, no necesitas acordarte de los ids. La
   especialista solo la mandas si el cliente pidió a alguien en particular;
   si no pidió a nadie, déjala vacía y la agenda le asigna a quien esté
   libre. Si te devuelve un error, LEE el mensaje, corrige eso y vuelve a
   intentarlo; no le pases el problema al cliente.'''
t = cambiar(t, VIEJO_P7, NUEVO_P7, "prompt paso 7: especialista opcional")

VIEJO_ESP = '''Nunca digas si alguien trabaja o no sin haber llamado a la herramienta: eso
no se adivina.'''
NUEVO_ESP = '''Nunca digas si alguien trabaja o no sin haber llamado a la herramienta: eso
no se adivina.

## Cómo se llaman las especialistas

El cliente las nombra como las conoce: «el Dr. Cueter», «la doctora Arias»,
«Valentina», «Diana». En la agenda están con el nombre completo. La
herramienta reconoce los dos, así que mándale el nombre TAL COMO lo dijo el
cliente: no lo completes, no lo traduzcas y no lo inventes.

- Si la herramienta no reconoce el nombre, te devuelve `opciones`: son las
  especialistas reales que sí pueden atender eso en esa sede. Ofrécelas TAL
  CUAL, con el nombre que te dio la herramienta.
- NUNCA te inventes la razón por la que no encontraste a alguien. Frases
  como «no está registrada en esa ciudad» son mentira y confunden al
  cliente: si está en la lista, atiende ahí.
- Solo se puede agendar un servicio con quien lo hace. Si el cliente pide a
  alguien que no hace ese servicio, la herramienta te dice quiénes sí: no
  insistas con la que él pidió.'''
t = cambiar(t, VIEJO_ESP, NUEVO_ESP, "prompt: nombres cortos y no inventar")

escribir(HR, t)


# ══════════════════════════════════════════════ main.py ═════════════════
MP = os.path.join(BASE, "main.py")
print("\n== main.py ==")
t = leer(MP)
respaldar(MP)

t = cambiar(
    t,
    '    contexto = {"telefono": telefono, "escalar": escalar}',
    '    contexto = {"telefono": telefono, "escalar": escalar,\n'
    '                "client_id": client_id}',
    "contexto de herramientas lleva client_id",
)

VIEJO_PERS = '''Bogotá — Chico Norte:
- Diana Carolina Ruiz — Cosmetóloga
- Dr. Jorge Cueter — Médico'''
NUEVO_PERS = '''Bogotá — Chico Norte:
- Diana Carolina Ruiz — Cosmetóloga
- Dr. Jorge Cueter — Médico

Así se conoce al personal y así lo dice el cliente. En la agenda están con
el nombre completo («Dr. Cueter» es JORGE RAMIRO CUETER GUZMAN, «Dra.
Julieth Arias» es JULIE VIVIANA ARIAS HERNANDEZ). Las herramientas reconocen
los dos. Si alguien aparece aquí, atiende: no inventes que «no está en esa
ciudad».'''
t = cambiar(t, VIEJO_PERS, NUEVO_PERS, "prompt: nombres cortos del personal")

escribir(MP, t)

print("\n%d cambios aplicados." % len(CAMBIOS))
