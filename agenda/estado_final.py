#!/usr/bin/env python3
# Estado final de la base. SOLO LECTURA.
import re, io
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()
for q in ('citas', 'clientes', 'reservas'):
    cur.execute('select count(*) from ' + q)
    print(f"   {q:<10} {cur.fetchone()[0]}")
cur.execute("select documento, primer_nombre, primer_apellido from clientes order by documento")
print("   clientes:", cur.fetchall())
cur.execute("select coalesce(canal,'-'), count(*) from citas group by 1 order by 2 desc")
print("   citas por canal:", cur.fetchall())
cn.close()
