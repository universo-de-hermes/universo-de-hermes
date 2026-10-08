#!/usr/bin/env python3
# Columnas reales de `reservas`, para no pegar un SELECT que reviente. SOLO LECTURA.
import re, io
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

cur.execute("""select column_name, data_type from information_schema.columns
               where table_name='reservas' order by ordinal_position""")
cols = cur.fetchall()
print("=== columnas de reservas ===")
for c, d in cols:
    print(f"   {c:<18} {d}")

nombres = {c for c, _ in cols}
print("\n=== lo que necesita el endpoint de Claude ===")
for nec in ('id', 'especialista_id', 'sede_id', 'fecha', 'inicio', 'fin', 'canal', 'expira_en'):
    print(f"   {nec:<18} {'SI ✅' if nec in nombres else '*** NO EXISTE ❌ ***'}")

print("\n=== reservas vivas ahora ===")
cur.execute("select count(*) from reservas")
print("   total:", cur.fetchone()[0])
cur.execute("select count(*) from reservas where expira_en > now()")
print("   vivas (expira_en > now()):", cur.fetchone()[0])
cur.execute("""select id, especialista_id, sede_id, fecha, inicio, fin, expira_en,
                      extract(epoch from (expira_en - now()))/60 as min
               from reservas order by fecha desc limit 3""")
for r in cur.fetchall():
    print("   ", r)
cn.close()
