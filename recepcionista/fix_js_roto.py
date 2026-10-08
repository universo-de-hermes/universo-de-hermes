#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repara la línea que quedo mal: en JavaScript dos textos seguidos no se
concatenan solos, hace falta el +."""
import io
import re
import subprocess
import sys

RUTA = "/var/www/html/agenda.html"
h = io.open(RUTA, "r", encoding="utf-8", newline="").read()
crlf = "\r\n" in h
s = h.replace("\r\n", "\n")

viejo = ('"El canal queda guardado en cada cita que esta persona agende, para saber "\n'
         '        "quién la agendó: Administrador, Asesor, Recepcionista o el Agente IA (Pepe)."')
nuevo = ('"El canal queda guardado en cada cita que esta persona agende, para saber "\n'
         '        + "quién la agendó: Administrador, Asesor, Recepcionista o el Agente IA (Pepe)."')

if s.count(viejo) != 1:
    print("ABORTO: %d coincidencias" % s.count(viejo))
    sys.exit(1)
s = s.replace(viejo, nuevo)

if crlf:
    s = s.replace("\n", "\r\n")
io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("reparado")

bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", s, re.S | re.I)
io.open("/tmp/chk3.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk3.js"], capture_output=True, text=True)
print("JavaScript:", "SINTAXIS OK" if r.returncode == 0 else "SIGUE MAL:\n" + r.stderr[:400])
print("nombres viejos:", [m for m in ("Call Center", "Agente virtual") if m in s] or "ninguno")

# y que la pagina siga sirviendose
c = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                    "https://agenda.universojota.tech/agenda.html"],
                   capture_output=True, text=True)
print("agenda web:", c.stdout)