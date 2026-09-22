#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""1. Revisa que el .env se pueda cargar con systemd y se lo agrega al unit.
2. Restaura el nombre del cliente que el regex dano.
"""
import io
import re
import sqlite3
import sys

ENV = "/root/universo/recepcionista/.env"
UNIT = "/etc/systemd/system/pepe.service"
DB = "/root/universo/recepcionista/crm/cjmedical.db"

# ── 1) el .env es compatible con systemd? ───────────────────────────────────
malas = []
for i, linea in enumerate(io.open(ENV, encoding="utf-8").read().splitlines(), 1):
    s = linea.strip()
    if not s or s.startswith("#"):
        continue
    if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", s):
        malas.append((i, s[:80]))

if malas:
    print("El .env NO es seguro para systemd, no toco el unit:")
    for i, s in malas:
        print("   linea %d: %s" % (i, s))
    sys.exit(1)
print("El .env es compatible con systemd (todas las lineas son CLAVE=valor)")

unit = io.open(UNIT, encoding="utf-8", newline="").read()
crlf = "\r\n" in unit
u = unit.replace("\r\n", "\n")

if "EnvironmentFile" in u:
    print("El unit ya tiene EnvironmentFile; no lo toco")
else:
    viejo = "WorkingDirectory=/root/universo/recepcionista\n"
    nuevo = ("WorkingDirectory=/root/universo/recepcionista\n"
             "# Sin esto el proceso no veia el .env: la agenda respondia 401\n"
             "EnvironmentFile=/root/universo/recepcionista/.env\n")
    if u.count(viejo) != 1:
        print("ABORTO: no pude ubicar WorkingDirectory en el unit")
        sys.exit(1)
    u = u.replace(viejo, nuevo)
    if crlf:
        u = u.replace("\n", "\r\n")
    io.open(UNIT, "w", encoding="utf-8", newline="").write(u)
    print("pepe.service: EnvironmentFile agregado")

# ── 2) nombre del cliente ──────────────────────────────────────────────────
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("select id, name from clients where name like '%Aporta%'")
filas = cur.fetchall()
print()
print("clientes con el nombre danado:", filas)
for cid, nombre in filas:
    cur.execute("update clients set name=? where id=?", ("Juan José", cid))
    print("   cliente %s: '%s' -> 'Juan José'" % (cid, nombre))
con.commit()
cur.execute("select id, name, status from clients order by id desc limit 3")
print("clientes ahora:", cur.fetchall())
con.close()
print("LISTO")
