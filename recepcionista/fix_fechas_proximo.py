#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""«Próximo sábado» se iba para la otra semana.

Causa: el bloque de fechas etiquetaba el sábado que viene como «este sábado» y
el de la otra semana como «próximo sábado», y la regla decía «"próximo [día]" =
el [día] de la semana siguiente». El cliente dijo «próximo sábado» y Pepe, muy
obediente, se fue al 3 de octubre en vez del 26 de septiembre.

Arreglo: en Colombia «el próximo sábado» es EL QUE VIENE. Se renombran las
etiquetas y se reescribe la regla.
"""
import io
import sys

RUTA = "/root/universo/recepcionista/main.py"

t = io.open(RUTA, "r", encoding="utf-8", newline="").read()
crlf = "\r\n" in t
s = t.replace("\r\n", "\n")

cambios = [
    # ── etiquetas del mapa de fechas ──
    ('                etiqueta = "hoy" if i == 0 else f"este {nombre}"\n'
     '                lineas.append(f"- {etiqueta} = {fmt(prox[i])} ({nombre})")\n'
     '                break\n'
     '        for i in range(7, 14):\n'
     '            if nom(prox[i]) == nombre:\n'
     '                lineas.append(f"- próximo {nombre} = {fmt(prox[i])} ({nombre})")\n'
     '                break',
     '                # «el que viene» = el más cercano. En Colombia «el próximo\n'
     '                # sábado» es ESTE, no el de la otra semana.\n'
     '                etiqueta = ("hoy" if i == 0\n'
     '                            else f"el {nombre} que viene (el más cercano)")\n'
     '                lineas.append(f"- {etiqueta} = {fmt(prox[i])} ({nombre})")\n'
     '                break\n'
     '        for i in range(7, 14):\n'
     '            if nom(prox[i]) == nombre:\n'
     '                lineas.append(\n'
     '                    f"- el {nombre} siguiente (el de la otra semana) = "\n'
     '                    f"{fmt(prox[i])} ({nombre})")\n'
     '                break'),
    # ── la regla ──
    ('NO adivines fechas. Usa los datos de FECHAS_AYUDA.\n'
     '- Si el cliente dice "viernes" busca en la lista cuándo cae viernes\n'
     '- Si el cliente dice "mañana" es la fecha que dice la lista\n'
     '- "próximo [día]" = el [día] de la semana siguiente\n'
     '- Siempre usa las fechas exactas de la lista, no inventes',
     'NO adivines fechas. Usa los datos de FECHAS_AYUDA.\n'
     '- "hoy", "mañana" y "pasado mañana" son los de la lista.\n'
     '- Si el cliente nombra un día («el sábado», «este sábado», «el próximo\n'
     '  sábado», «el sábado que viene») usa SIEMPRE EL MÁS CERCANO de la lista.\n'
     '  En Colombia «el próximo sábado» es el que viene, NO el de la otra semana.\n'
     '- Solo saltas al de la otra semana si lo dice claro: «el otro sábado»,\n'
     '  «el sábado siguiente», «el sábado de la otra semana», «en dos sábados».\n'
     '- Si el día que dijo ya pasó esta semana, usa el de la semana que viene.\n'
     '- SIEMPRE repite la fecha con número y mes («el sábado 26 de septiembre»)\n'
     '  para que el cliente te corrija si entendiste mal. Si te corrige, usa la\n'
     '  fecha que él diga, sin discutir, y sigue con esa.')
]

for i, (viejo, nuevo) in enumerate(cambios, 1):
    n = s.count(viejo)
    print("cambio %d: %d coincidencia(s)" % (i, n))
    if n != 1:
        print("ABORTO")
        print(viejo[:300])
        sys.exit(1)
    s = s.replace(viejo, nuevo)

if crlf:
    s = s.replace("\n", "\r\n")
io.open(RUTA, "w", encoding="utf-8", newline="").write(s)

import py_compile
py_compile.compile(RUTA, doraise=True)
print("sintaxis OK")
print()
print("=== ASI QUEDA EL MAPA DE FECHAS ===")
import datetime
DIAS_ES = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
hoy = datetime.datetime.now()
prox = [(hoy + datetime.timedelta(days=i)) for i in range(14)]
nom = lambda d: DIAS_ES[d.weekday()]
fmt = lambda d: d.strftime("%d/%m/%Y")
lineas = [f"Hoy es {nom(hoy)} {fmt(hoy)}."]
lineas.append(f"- mañana = {fmt(prox[1])} ({nom(prox[1])})")
lineas.append(f"- pasado mañana = {fmt(prox[2])} ({nom(prox[2])})")
for nombre in DIAS_ES:
    for i in range(0, 7):
        if nom(prox[i]) == nombre:
            etiqueta = ("hoy" if i == 0 else f"el {nombre} que viene (el más cercano)")
            lineas.append(f"- {etiqueta} = {fmt(prox[i])} ({nombre})")
            break
    for i in range(7, 14):
        if nom(prox[i]) == nombre:
            lineas.append(f"- el {nombre} siguiente (el de la otra semana) = {fmt(prox[i])} ({nombre})")
            break
for l in lineas:
    print("  " + l)