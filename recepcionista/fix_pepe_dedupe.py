#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Si dos especialistas estan libres a la misma hora, la lista la repetia
(«10:00, 10:00»). Se ofrece una sola vez, con el primer especialista libre."""
import io
import sys

RUTA = "/root/universo/recepcionista/agenda_helper.py"
t = io.open(RUTA, "r", encoding="utf-8", newline="").read()
crlf = "\r\n" in t
s = t.replace("\r\n", "\n")

viejo = """    por_dia = {}
    for hu in huecos:
        f = str(hu["fecha"])[:10]
        por_dia.setdefault(f, []).append({"""
nuevo = """    por_dia = {}
    vistas = set()
    for hu in huecos:
        f = str(hu["fecha"])[:10]
        # Dos especialistas libres a la misma hora: se ofrece una sola vez.
        clave = (f, str(hu["inicio"]))
        if clave in vistas:
            continue
        vistas.add(clave)
        por_dia.setdefault(f, []).append({"""

if s.count(viejo) != 1:
    print("ABORTO: %d coincidencias" % s.count(viejo))
    sys.exit(1)

s = s.replace(viejo, nuevo)
if crlf:
    s = s.replace("\n", "\r\n")
io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("dedupe por hora aplicado")

import py_compile
py_compile.compile(RUTA, doraise=True)
print("sintaxis OK")
