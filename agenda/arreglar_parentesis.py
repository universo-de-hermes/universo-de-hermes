#!/usr/bin/env python3
"""Arregla el parentesis de la barra de fechas: view.appendChild(h(...)) lleva
«)));» no «)),» (ese dejaba colgando el bloque de los KPIs)."""
import io, re, subprocess

AG = "/var/www/html/agenda.html"
raw = open(AG, "rb").read()

VIEJO = b'"Limpiar filtro")),\n  view.appendChild(h("div",{class:"kpis"},'
NUEVO = b'"Limpiar filtro")));\n  view.appendChild(h("div",{class:"kpis"},'

n = raw.count(VIEJO)
print("coincidencias:", n)
if n != 1:
    raise SystemExit("ABORTO")
open(AG, "wb").write(raw.replace(VIEJO, NUEVO))
print("arreglado. bytes:", len(raw))

h = io.open(AG, encoding="utf-8", errors="replace").read()
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", h, re.S | re.I)
io.open("/tmp/chk_rango2.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk_rango2.js"], capture_output=True, text=True)
print("JS de la agenda:", "OK" if r.returncode == 0 else "MAL\n" + r.stderr[-600:])
