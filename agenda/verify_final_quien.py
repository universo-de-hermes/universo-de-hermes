#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificacion final: el endpoint del dia y la cuenta del reporte."""
import io
import json
import pathlib
import urllib.request
from collections import Counter

import psycopg2

TOK = pathlib.Path("/root/universo/agenda/.api_token").read_text().strip()
ENV = "/root/universo/agenda/.api_env"
BASE = "http://127.0.0.1:8001/api/v2"


def get(path):
    req = urllib.request.Request(BASE + path,
                                 headers={"accept": "application/json",
                                          "x-api-token": TOK})
    return json.loads(urllib.request.urlopen(req, timeout=20).read().decode())


print("=== 1) endpoint del DIA (agenda_dia) ===")
dia = get("/agenda/todas/2026-09-21")
print("citas del dia:", len(dia))
for c in dia:
    print("   asignada_por:", repr(c.get("asignada_por")),
          "| creado_por:", repr(c.get("creado_por")),
          "| canal:", repr(c.get("canal")))

print()
print("=== 2) rango del MES corregido (hasta=2026-09-30) ===")
mes_citas = get("/citas?desde=2026-09-01&hasta=2026-09-30&limite=2000")
print("citas del mes:", len(mes_citas))

print()
print("=== 3) LA CUENTA QUE HACE EL REPORTE ===")
url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    if linea.strip().startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")
conn = psycopg2.connect(url)
cur = conn.cursor()
cur.execute("select id, nombre from usuarios")
nombres = {r[0]: r[1] for r in cur.fetchall()}
conn.close()

por = {}
for c in mes_citas:
    if c.get("tipo") == "bloqueo":
        continue
    k = c.get("asignada_por") or c.get("creado_por") or "—"
    u = por.setdefault(k, {"total": 0, "canal": Counter()})
    u["total"] += 1
    if c.get("canal"):
        u["canal"][c["canal"]] += 1

print("%-22s %-16s %s" % ("Persona", "Canal", "Agendadas"))
print("-" * 50)
for k, u in sorted(por.items(), key=lambda x: -x[1]["total"]):
    if k.startswith(("u-", "u_")):
        persona = nombres.get(k, "Usuario sin nombre")
    else:
        persona = "Sin registrar" if k == "—" else k
    canal = u["canal"].most_common(1)[0][0] if u["canal"] else "—"
    print("%-22s %-16s %d" % (persona, canal, u["total"]))
