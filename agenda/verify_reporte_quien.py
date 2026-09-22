#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproduce en Python la misma cuenta que hace el reporte "Quien agenda"
(citas del mes -> agrupadas por asignada_por/creado_por -> nombre + canal) para
comprobar que ya no sale "Sin registrar"."""
import io
import json
import pathlib
import urllib.request
from collections import Counter

import psycopg2

TOK = pathlib.Path("/root/universo/agenda/.api_token").read_text().strip()
ENV = "/root/universo/agenda/.api_env"

req = urllib.request.Request("http://127.0.0.1:8001/api/v2/citas",
                             headers={"accept": "application/json",
                                      "x-api-token": TOK})
citas = json.loads(urllib.request.urlopen(req, timeout=20).read().decode())

mes = "2026-09"
del_mes = [c for c in citas if str(c.get("fecha", "")).startswith(mes)]
print("citas del mes %s: %d" % (mes, len(del_mes)))

url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    if linea.strip().startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")
conn = psycopg2.connect(url)
cur = conn.cursor()
cur.execute("select id, nombre, canal from usuarios")
nombres = {r[0]: (r[1], r[2]) for r in cur.fetchall()}
conn.close()

por_usuario = {}
for c in del_mes:
    k = c.get("asignada_por") or c.get("creado_por") or "—"
    u = por_usuario.setdefault(k, {"total": 0, "at": 0, "canal": Counter()})
    u["total"] += 1
    if c.get("canal"):
        u["canal"][c["canal"]] += 1

print()
print("=== LO QUE VA A MOSTRAR EL REPORTE ===")
print("%-22s %-16s %s" % ("Persona", "Canal", "Agendadas"))
print("-" * 52)
for k, u in sorted(por_usuario.items(), key=lambda x: -x[1]["total"]):
    es_usuario = k.startswith("u-") or k.startswith("u_")
    if es_usuario:
        persona = nombres.get(k, ("Usuario sin nombre", ""))[0]
    else:
        persona = "Sin registrar" if k == "—" else k
    canal = u["canal"].most_common(1)[0][0] if u["canal"] else "—"
    print("%-22s %-16s %d" % (persona, canal, u["total"]))
