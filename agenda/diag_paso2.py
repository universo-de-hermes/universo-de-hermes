#!/usr/bin/env python3
# Citas/grid: minutos de arranque. SOLO LECTURA.
import re, io
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

print("=== CITAS: en que minuto arrancan ===")
cur.execute("select to_char(inicio,'HH24:MI') from citas order by 1")
todos = [r[0] for r in cur.fetchall()]
cur.execute("select distinct to_char(inicio,'MI') from citas order by 1")
print("  minutos distintos usados:", [r[0] for r in cur.fetchall()])
print("  total citas:", len(todos))
print("  ejemplos:", todos[:12])
mal = [h for h in todos if h[3:] not in ('00', '30')]
print(f"  citas que NO arrancan en :00/:30: {len(mal)} {mal}")

print()
print("=== RESERVAS (cupos apartados) ===")
cur.execute("""select count(*), min(to_char(inicio,'HH24:MI')), max(to_char(inicio,'HH24:MI'))
               from reservas""")
print("  reservas:", cur.fetchone())

print()
print("=== HORARIOS: minutos de arranque de cada franja y del almuerzo ===")
cur.execute("""select distinct to_char(desde,'HH24:MI'), to_char(hasta,'HH24:MI'),
                      coalesce(to_char(alm_desde,'HH24:MI'),'-'),
                      coalesce(to_char(alm_hasta,'HH24:MI'),'-')
               from horarios order by 1,2""")
for r in cur.fetchall():
    print("   desde", r[0], "hasta", r[1], "| almuerzo", r[2], "-", r[3])

print()
print("=== SI EL PASO ES 30, QUE MINUTOS SALEN (todas las franjas) ===")
cur.execute("""select count(*) from horarios
               where (date_part('minute', desde)::int % 30) <> 0""")
print("  franjas que arrancan fuera de :00/:30:", cur.fetchone()[0])
cur.execute("""select count(*) from horarios
               where (date_part('minute', coalesce(alm_hasta, desde))::int % 30) <> 0""")
print("  franjas que RETOMAN fuera de :00/:30 (tras almuerzo):", cur.fetchone()[0])
cn.close()
