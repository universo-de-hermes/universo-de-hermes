#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arregla el flujo de Pepe: no agendaba y mandaba al cliente para un asesor.

CAUSA 1 (por que no agendo): el servicio systemd no cargaba el .env y ademas
agenda_helper leia API_TOKEN al importarse, ANTES de que main.py llamara
load_dotenv(). Quedaba vacio -> la agenda respondia 401 en cada llamada.

CAUSA 2 (por que mando a un asesor): el prompt activo es SYSTEM_PROMPT (el
viejo de main.py) + BLOQUE_PROMPT. El viejo tiene 8 motivos de escalamiento,
incluidos "problema de pago" y "pregunta fuera de tu conocimiento", y reglas
como "Nunca confirmes una cita que no haya sido agendada por un asesor".

CAUSA 3 (nombre del cliente): el regex de nombre no estaba anclado al inicio,
asi que agarro un pedazo de una respuesta ("...cejas, aporta y estimula el
crecimiento") y lo guardo como nombre.
"""
import io
import re
import sys

BASE = "/root/universo/recepcionista/"


def leer(ruta):
    """Devuelve (texto_normalizado_a_LF, tenia_CRLF)."""
    t = io.open(ruta, "r", encoding="utf-8", newline="").read()
    crlf = "\r\n" in t
    return t.replace("\r\n", "\n"), crlf


def escribir(ruta, texto, crlf):
    if crlf:
        texto = texto.replace("\n", "\r\n")
    io.open(ruta, "w", encoding="utf-8", newline="").write(texto)


def aplicar(ruta, cambios, etiqueta):
    txt, crlf = leer(ruta)
    for i, (viejo, nuevo) in enumerate(cambios, 1):
        n = txt.count(viejo)
        if n != 1:
            print("ABORTO en %s cambio %d: %d coincidencia(s)" % (etiqueta, i, n))
            print("--- buscaba ---")
            print(viejo[:300])
            sys.exit(1)
        txt = txt.replace(viejo, nuevo)
    escribir(ruta, txt, crlf)
    print("%s: %d cambio(s) aplicado(s)" % (etiqueta, len(cambios)))


# ══════════════════════════════ 1) EL TOKEN ══════════════════════════════════
aplicar(BASE + "agenda_helper.py", [(
    'AGENDA_API = os.environ.get("AGENDA_API", "http://127.0.0.1:8001").rstrip("/")\n'
    'API_TOKEN = os.environ.get("API_TOKEN", "").strip()',
    'AGENDA_API = os.environ.get("AGENDA_API", "http://127.0.0.1:8001").rstrip("/")\n'
    '# OJO: este modulo se importa ANTES de que main.py llame a load_dotenv(),\n'
    '# asi que leer el token aqui lo dejaba vacio para siempre y la agenda\n'
    '# respondia 401 en cada llamada. Se lee en el momento de usarlo.\n'
    'API_TOKEN = os.environ.get("API_TOKEN", "").strip()\n'
    '\n'
    '\n'
    'def _token() -> str:\n'
    '    return (os.environ.get("API_TOKEN") or API_TOKEN or "").strip()\n'
), (
    '    h = {"accept": "application/json"}\n'
    '    if API_TOKEN:\n'
    '        h["X-API-Token"] = API_TOKEN\n'
    '    return h',
    '    h = {"accept": "application/json"}\n'
    '    tok = _token()\n'
    '    if tok:\n'
    '        h["X-API-Token"] = tok\n'
    '    return h'
)], "agenda_helper.py (token)")

# ══════════════════ 2) INSTRUCCIONES DE ESCALAMIENTO ═════════════════════════
aplicar(BASE + "herramientas.py", [(
    '## Cuándo NO sigues tú\n'
    '\n'
    'Pasa la conversación a un asesor —y déjalo ahí, no sigas intentando— cuando:\n'
    '\n'
    '- El cliente pida hablar con una persona.\n'
    '- Haya un PQRS, una queja o un reclamo.\n'
    '- La conversación se esté enredando y el cliente no esté entendiendo.\n'
    '- Pida un diagnóstico o una recomendación médica.\n'
    '- Haya un problema de pago.\n'
    '\n'
    'En esos casos avísale que un asesor de CJ Medical lo va a contactar, y no\n'
    'prometas tiempos que no dependen de ti.',
    '## Cuándo NO sigues tú\n'
    '\n'
    'Tú eres quien atiende: agendar, reprogramar, cancelar y responder dudas es\n'
    'tu trabajo. Solo pasas la conversación a un asesor —y lo dejas ahí— en\n'
    'estos tres casos:\n'
    '\n'
    '- El cliente pide expresamente hablar con una persona o un asesor.\n'
    '- El cliente está molesto, o pone una queja, un reclamo o una petición\n'
    '  (PQRS).\n'
    '- El cliente insiste en algo que no puedes resolver tú (por ejemplo un\n'
    '  problema de pago) y además se nota molesto por eso.\n'
    '\n'
    'En esos casos avísale que un asesor de CJ Medical lo va a contactar, y no\n'
    'prometas tiempos que no dependen de ti.\n'
    '\n'
    'NO pasas a un asesor por: una pregunta que puedes responder, una duda de\n'
    'precios, sedes u horarios, un enredo pasajero, o porque una herramienta te\n'
    'falló. Si una herramienta falla, discúlpate con naturalidad, vuelve a\n'
    'intentarlo y sigue ayudándole con su cita. Nunca lo mandes a un asesor por\n'
    'un problema técnico.'
), (
    '            "Pasa la conversación a una persona del equipo. Se usa cuando el "\n'
    '            "cliente lo pide, cuando hay una queja o un PQRS, cuando hay un "\n'
    '            "reclamo, cuando el cliente no está entendiendo y la cosa se está "\n'
    '            "enredando, cuando pide un diagnóstico médico, o cuando hay un "\n'
    '            "problema de pago. Después de llamarla, se le avisa al cliente que "\n'
    '            "un asesor lo va a contactar y NO se sigue intentando resolver."',
    '            "Pasa la conversación a una persona del equipo. SOLO se usa en "\n'
    '            "tres casos: (1) el cliente pide expresamente hablar con una "\n'
    '            "persona o un asesor; (2) el cliente está molesto o pone una "\n'
    '            "queja, un reclamo o una petición (PQRS); (3) el cliente insiste "\n'
    '            "en algo que no puedes resolver tú (por ejemplo un pago) y además "\n'
    '            "se nota molesto. NO la uses por dudas que puedas responder, ni "\n'
    '            "porque una herramienta falló. Después de llamarla, se le avisa al "\n'
    '            "cliente que un asesor lo va a contactar."'
), (
    '"enum": ["lo_pidio", "pqrs", "queja", "no_entiende",\n'
    '                                "medico", "pago", "otro"]',
    '"enum": ["lo_pidio", "pqrs", "queja", "molesto", "pago",\n'
    '                                "otro"]'
)], "herramientas.py (escalamiento)")

# ══════════════════ 3) PROMPT VIEJO EN main.py ══════════════════════════════
aplicar(BASE + "main.py", [(
    '# ESCALAMIENTO A ASESOR\n'
    '\n'
    'Pasa a humano cuando:\n'
    '- Cliente lo solicite\n'
    '- Cancelación definitiva\n'
    '- Problema con cita existente\n'
    '- Queja\n'
    '- Situación médica compleja\n'
    '- Cliente pida diagnóstico\n'
    '- Pregunta fuera de tu conocimiento\n'
    '- Problema de pago',
    '# ESCALAMIENTO A ASESOR\n'
    '\n'
    'Tú eres quien atiende. Solo pasas la conversación a una persona del equipo\n'
    'en estos casos, y en ningún otro:\n'
    '\n'
    '1. El cliente pide expresamente hablar con una persona o un asesor.\n'
    '2. El cliente está molesto, o pone una queja, un reclamo o una petición\n'
    '   (PQRS). Si es una queja, aplica el flujo de PQRS de más abajo.\n'
    '3. El cliente insiste en algo que no puedes resolver tú (por ejemplo un\n'
    '   problema de pago) y además se nota molesto por eso.\n'
    '\n'
    'Todo lo demás lo resuelves tú: agendar, reprogramar, cancelar, precios,\n'
    'sedes, horarios, dudas de servicios. Tu trabajo es que el cliente NO se\n'
    'quede sin su cita. No lo mandes a un asesor por una dificultad tuya ni por\n'
    'una pregunta que puedas responder.'
), (
    'Cada nueva solicitud de cita sigue el flujo normal: ciudad → sede → servicio → fecha → hora → datos → resumen → asesor.',
    'Cada nueva solicitud de cita sigue el flujo normal: ciudad → sede → servicio → fecha → hora → datos → resumen → confirmación, y la agendás tú.'
), (
    'Si pide cambiar cita: pregunta nueva fecha y hora, luego resumen → confirmación → asesor.',
    'Si pide cambiar cita: pregunta nueva fecha y hora, luego resumen → confirmación, y la mueves tú con la herramienta de reprogramar.'
), (
    'Si pide cancelar: pregunta si reprogramar o cancelar definitivamente.\n'
    '- Reprogramar: nueva fecha y hora → resumen → asesor.\n'
    '- Cancelar definitivamente: transferir a asesor.',
    'Si pide cancelar: pregunta si reprogramar o cancelar definitivamente.\n'
    '- Reprogramar: nueva fecha y hora → resumen → confirmación, y la mueves tú.\n'
    '- Cancelar definitivamente: pregúntale el motivo con naturalidad, cancélala\n'
    '  tú y dile que la hora quedó liberada. No insistas en que no cancele.'
), (
    'Si el cliente expresa una queja, reclamo, está inconforme o tiene un problema:',
    'Si el cliente expresa una queja, un reclamo o una petición (PQRS), o está\nclaramente molesto e inconforme:'
), (
    '3. Nunca confirmes una cita que no haya sido agendada por un asesor',
    '3. Tú agendás la cita con la herramienta de agendar. No esperes a que un asesor la agende.'
), (
    '14. Si no sabes algo, no lo inventes — escala a asesor\n'
    '15. Antes de entregar al asesor, muestra resumen completo y pide confirmación',
    '14. Si no sabes algo, no lo inventes: di lo que sí sabes y sigue con la cita. Solo pasas a un asesor en los casos de arriba.\n'
    '15. Antes de agendar, muestra el resumen completo y pide confirmación.'
)], "main.py (prompt)")

# ══════════════════════ 4) REGEX DEL NOMBRE ═════════════════════════════════
aplicar(BASE + "main.py", [(
    '    name_match = re.search(r"(?:Mucho\\s+gusto|Gracias|Listo|Perfecto|Excelente)[^,]*,\\s*([^.¡!:\\n]+)", reply, re.IGNORECASE)',
    '    # Anclado al inicio y exigiendo la coma pegada al saludo: antes cualquier\n'
    '    # "Perfecto, ..." de media respuesta se guardaba como nombre del cliente\n'
    '    # (quedó uno llamado "Aporta Y Estimula El Crecimiento").\n'
    '    name_match = re.match(\n'
    '        r"^\\s*(?:Mucho\\s+gusto|Gracias|Listo|Perfecto|Excelente)\\s*,\\s*"\n'
    '        r"([A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:\\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+){0,2})\\s*[.!,¡?\\n]",\n'
    '        reply, re.IGNORECASE)'
)], "main.py (regex nombre)")

print()
print("=== VERIFICACION DE SINTAXIS ===")
import py_compile
for f in ("agenda_helper.py", "herramientas.py", "main.py"):
    py_compile.compile(BASE + f, doraise=True)
    print("  OK", f)
