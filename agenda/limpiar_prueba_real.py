#!/usr/bin/env python3
"""Borra la clienta de prueba y todo lo suyo. Uso: limpiar-prueba-real.py <documento>"""
import re, io, sys
import psycopg2
Q, A, N = chr(34), chr(39), chr(10)
t = io.open("/root/universo/agenda/.api_env").read()
m = re.search("DATABASE_URL=([^" + N + "]+)", t)
url = m.group(1).strip().strip(Q).strip(A)
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
doc = sys.argv[1] if len(sys.argv) > 1 else ""
cur.execute("select id from clientes where documento=%s", (doc,))
ids = [r[0] for r in cur.fetchall()]
for cid in ids:
    cur.execute("delete from reservas where referencia=%s", (doc,))
    cur.execute("select id from citas where cliente_id=%s", (cid,))
    for (cita,) in cur.fetchall():
        cur.execute("update citas set reprogramada_de=null, reprogramada_a=null where reprogramada_de=%s or reprogramada_a=%s", (cita, cita))
        cur.execute("delete from citas where id=%s", (cita,))
    cur.execute("delete from clientes where id=%s", (cid,))
print("limpiado " + doc + ": " + str(len(ids)) + " clienta(s)")
