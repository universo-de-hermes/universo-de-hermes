#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quedaban dos menciones a los nombres viejos de canal en agenda.html."""
import io
import re
import subprocess
import sys

RUTA = "/var/www/html/agenda.html"
h = io.open(RUTA, "r", encoding="utf-8", newline="").read()
crlf = "\r\n" in h
s = h.replace("\r\n", "\n")

cambios = [
    ('c.canal==="Agente virtual"?h("span",{title:"Agendada por el agente virtual",',
     'c.canal==="Agente IA"?h("span",{title:"Agendada por el agente IA (Pepe)",'),
    ('"El canal queda guardado en cada cita que esta persona agende, para poder medir Call Center contra Recepción."',
     '"El canal queda guardado en cada cita que esta persona agende, para saber "\n'
     '        "quién la agendó: Administrador, Asesor, Recepcionista o el Agente IA (Pepe)."'),
]

for i, (viejo, nuevo) in enumerate(cambios, 1):
    n = s.count(viejo)
    print("cambio %d: %d coincidencia(s)" % (i, n))
    if n != 1:
        print("ABORTO")
        sys.exit(1)
    s = s.replace(viejo, nuevo)

if crlf:
    s = s.replace("\n", "\r\n")
io.open(RUTA, "w", encoding="utf-8", newline="").write(s)

# comprobar que no queden nombres viejos y que el JS siga bien
sobra = [m for m in ("Call Center", "Agente virtual") if m in s]
print("nombres viejos restantes:", sobra or "ninguno")
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", s, re.S | re.I)
io.open("/tmp/chk2.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk2.js"], capture_output=True, text=True)
print("JavaScript:", "OK" if r.returncode == 0 else r.stderr[:300])