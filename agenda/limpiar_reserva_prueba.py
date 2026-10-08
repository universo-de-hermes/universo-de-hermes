#!/usr/bin/env python3
"""Muestra la reserva de prueba y la borra. Solo toca la referencia de prueba."""
import io, re
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

print("=== reservas ANTES ===")
cur.execute("select id, referencia, sede_id, fecha, inicio, canal, expira_en from reservas")
for f in cur.fetchall():
    print("  ", f)

cur.execute("delete from reservas where referencia in ('999000777','3009998877','999000444')")
print("borradas:", cur.rowcount)

print("=== reservas DESPUES ===")
cur.execute("select count(*) from reservas"); print("   reservas:", cur.fetchone()[0])
cur.execute("select count(*) from citas"); print("   citas:", cur.fetchone()[0])
cur.execute("select count(*) from clientes"); print("   clientes:", cur.fetchone()[0])
cn.close()
