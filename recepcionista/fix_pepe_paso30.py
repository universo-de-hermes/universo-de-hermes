#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La agenda agenda cada 30 minutos (en punto o y media). El bot pedia las
horas con paso=15, asi que ofrecia 09:45, 10:15... que no existen como cita.

Se cambia:
 1. agenda_helper: pide paso=30 y ademas filtra a :00 / :30 por seguridad
    (por si algun horario de especialista empieza a una hora rara).
 2. herramientas: el prompt y la descripcion de la herramienta dicen la regla.
"""
import io
import sys

BASE = "/root/universo/recepcionista/"


def leer(ruta):
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
    print("%s: %d cambio(s)" % (etiqueta, len(cambios)))


# ═════════════════ 1) agenda_helper: paso 30 + filtro ═══════════════════════
aplicar(BASE + "agenda_helper.py", [(
    '            "especialista": ep["id"], "paso": 15})',
    '            "especialista": ep["id"], "paso": PASO_MINUTOS})'
), (
    '            "especialista": ep["id"], "paso": 15, "limite": limite})',
    '            "especialista": ep["id"], "paso": PASO_MINUTOS,\n'
    '            "limite": limite})'
), (
    '    huecos = r["datos"] or []\n'
    '    # agrupadas por día, con la especialista, para que Pepe ofrezca sin marear',
    '    # La agenda agenda cada 30 minutos: las citas empiezan en punto o y\n'
    '    # media. La función de la base ya genera los candidatos cada\n'
    '    # PASO_MINUTOS desde el inicio del horario, pero se filtra igual por si\n'
    '    # algún horario de especialista empieza a una hora rara.\n'
    '    def _en_punto_o_media(hora) -> bool:\n'
    '        return str(hora or "").strip()[-2:] in ("00", "30")\n'
    '\n'
    '    huecos = [h for h in (r["datos"] or [])\n'
    '              if _en_punto_o_media(h.get("inicio"))]\n'
    '    # agrupadas por día, con la especialista, para que Pepe ofrezca sin marear'
), (
    'TIMEOUT = float(os.environ.get("AGENDA_TIMEOUT", "20"))',
    'TIMEOUT = float(os.environ.get("AGENDA_TIMEOUT", "20"))\n'
    '# Cada cuánto se puede agendar: la agenda trabaja cada 30 minutos\n'
    '# (9:00, 9:30, 10:00…), nunca en cuartos.\n'
    'PASO_MINUTOS = int(os.environ.get("AGENDA_PASO", "30"))'
)], "agenda_helper.py (paso 30)")

# ═════════════════ 2) herramientas: regla en el prompt ══════════════════════
aplicar(BASE + "herramientas.py", [(
    '3. OFRECE HORAS REALES. Nunca digas una hora que no venga de ver_horas_libres.\n'
    '   Ofrece dos o tres, no la lista entera: «tengo el martes a las 9:00 o a las\n'
    '   11:30, y el miércoles a las 3:00». Si ninguna le sirve, mira otros días.',
    '3. OFRECE HORAS REALES. Nunca digas una hora que no venga de ver_horas_libres.\n'
    '   La agenda agenda cada 30 minutos: las citas empiezan en punto o y media\n'
    '   (9:00, 9:30, 10:00, 10:30…), nunca en cuartos. La herramienta ya te\n'
    '   devuelve solo esas horas y ya tiene en cuenta lo que dura el servicio\n'
    '   (por ejemplo el Carbon Peel dura 1 hora), así que ofrécelas tal cual\n'
    '   vienen, sin inventar ni redondear. Ofrece dos o tres, no la lista\n'
    '   entera: «tengo el martes a las 9:00 o a las 11:30, y el miércoles a las\n'
    '   3:00». Si ninguna le sirve, mira otros días.'
), (
    '            "Las horas realmente disponibles. Ya descuenta el horario de cada "\n'
    '            "especialista, el almuerzo, las citas tomadas y los cupos apartados. "\n'
    '            "NUNCA ofrezcas una hora que no venga de aquí. Sin fecha, busca en "\n'
    '            "los próximos días."',
    '            "Las horas realmente disponibles. Ya descuenta el horario de cada "\n'
    '            "especialista, el almuerzo, las citas tomadas y los cupos apartados, "\n'
    '            "y ya respeta lo que dura el servicio. Devuelve las horas cada 30 "\n'
    '            "minutos (en punto o y media), que es como agenda CJ Medical. "\n'
    '            "NUNCA ofrezcas una hora que no venga de aquí. Sin fecha, busca en "\n'
    '            "los próximos días."'
)], "herramientas.py (regla 30 min)")

print()
import py_compile
for f in ("agenda_helper.py", "herramientas.py"):
    py_compile.compile(BASE + f, doraise=True)
    print("  sintaxis OK:", f)
