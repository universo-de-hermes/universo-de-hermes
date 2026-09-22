#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificacion final del reporte "Quien agenda" + chequeo de sintaxis del JS."""
import io
import json
import pathlib
import re
import subprocess
import urllib.request
from collections import Counter

import psycopg2

TOK = pathlib.Path("/root/universo/agenda/.api_token").read_text().strip()
ENV = "/root/universo/agenda/.api_env"
HTML = "/var/www/html/agenda.html"

req = urllib.request.Request(
    "http://127.0.0.1:8001/api/v2/citas?desde=2026-09-01&hasta=2026-09-30&limite=2000",
    headers={"accept": "application/json", "x-api-token": TOK})
citas = json.loads(urllib.request.urlopen(req, timeout=20).read().decode())

url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    if linea.strip().startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")
conn = psycopg2.connect(url)
cur = conn.cursor()
cur.execute("select id, nombre, canal from usuarios")
perfiles = {r[0]: {"nombre": r[1], "canal": r[2]} for r in cur.fetchall()}
conn.close()

por = {}
for c in citas:
    if c.get("tipo") == "bloqueo":
        continue
    k = c.get("asignada_por") or c.get("creado_por") or "—"
    u = por.setdefault(k, {"total": 0, "canal": Counter()})
    u["total"] += 1
    if c.get("canal"):
        u["canal"][c["canal"]] += 1

print("=== LO QUE MOSTRARA EL REPORTE ===")
print("%-22s %-16s %s" % ("Persona", "Canal", "Agendadas"))
print("-" * 50)
for k, u in sorted(por.items(), key=lambda x: -x[1]["total"]):
    reg = perfiles.get(k)
    if k.startswith(("u-", "u_")):
        persona = (reg or {}).get("nombre", "Usuario sin nombre")
    else:
        persona = "Sin registrar" if k == "—" else k
    canal_top = u["canal"].most_common(1)[0][0] if u["canal"] else None
    canal = (reg or {}).get("canal") or canal_top or "—"
    print("%-22s %-16s %d" % (persona, canal, u["total"]))

# ── sintaxis del JavaScript ─────────────────────────────────────────────────
html = io.open(HTML, encoding="utf-8").read()
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S | re.I)
print()
print("bloques <script> encontrados:", len(bloques))
js = "\n;\n".join(bloques)
ruta = "/tmp/agenda_check.js"
io.open(ruta, "w", encoding="utf-8").write(js)
try:
    out = subprocess.run(["node", "--check", ruta], capture_output=True, text=True)
    print("node --check ->", "SINTAXIS OK" if out.returncode == 0 else "ERROR")
    if out.returncode != 0:
        print(out.stderr[:1500])
except FileNotFoundError:
    print("node no esta instalado en el VPS; no se pudo validar la sintaxis")
