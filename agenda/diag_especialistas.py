#!/usr/bin/env python3
# Quien hace "Terapias de Revitalizacion"? SOLO LECTURA.
import re, io
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

print("=== ESTADOS DE LAS ESPECIALISTAS ===")
cur.execute("select id, nombres, activo from especialistas order by nombres")
for r in cur.fetchall():
    print(f"   {'ACTIVA ' if r[2] else 'INACTIVA'} {r[0]:<34} {r[1]}")

print()
print("=== COLUMNAS de especialista_servicios ===")
cur.execute("""select column_name from information_schema.columns
               where table_name='especialista_servicios' order by ordinal_position""")
print("   ", [r[0] for r in cur.fetchall()])

SID = 'srv-terapias-de-revitalizacion'
print()
print(f"=== QUIEN TIENE ASIGNADO '{SID}' ===")
cur.execute("""select e.id, e.nombres from especialista_servicios s
               join especialistas e on e.id = s.especialista_id
               where s.servicio_id = %s and e.activo order by e.nombres""", (SID,))
asig = cur.fetchall()
for r in asig:
    print(f"   {r[0]:<34} {r[1]}")
print("   TOTAL:", len(asig))

print()
print("=== QUE SERVICIOS TIENE CADA ESPECIALISTA ACTIVA (conteo) ===")
cur.execute("""select e.nombres, count(s.servicio_id) from especialistas e
               left join especialista_servicios s on s.especialista_id = e.id
               where e.activo group by e.nombres order by 1""")
for r in cur.fetchall():
    print(f"   {r[0]:<36} {r[1]} servicios")

print()
print("=== QUE DEVUELVE huecos_del_dia PARA 'Terapias' (por especialista) ===")
for fecha in ('2026-10-02', '2026-10-03'):
    cur.execute("""select e.nombres, count(*), min(to_char(h.inicio,'HH24:MI'))
                   from huecos_del_dia(p_fecha=>%s, p_servicio=>%s) h
                   join especialistas e on e.id = h.especialista_id
                   group by e.nombres order by 1""", (fecha, SID))
    print(f"   --- {fecha} ---")
    for r in cur.fetchall():
        print(f"      {r[0]:<36} {r[1]:>3} huecos (desde {r[2]})")

print()
print("=== Y SIN FILTRO DE SEDE? (El Tesoro) ===")
for fecha in ('2026-10-02',):
    cur.execute("""select e.nombres, count(*) from huecos_del_dia(
                       p_fecha=>%s, p_sede=>%s, p_servicio=>%s) h
                   join especialistas e on e.id = h.especialista_id
                   group by e.nombres order by 1""", (fecha, 'sede-cj-medical-el-tesoro', SID))
    for r in cur.fetchall():
        print(f"      {r[0]:<36} {r[1]:>3} huecos")
cn.close()
