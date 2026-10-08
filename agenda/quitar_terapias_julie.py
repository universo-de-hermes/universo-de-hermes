#!/usr/bin/env python3
# Quita la fila MAL puesta: Julie no hace 'Terapias de Revitalizacion'.
# Reversible: guarda la fila en un archivo antes de borrarla.
import re, io, json
import psycopg2

SERVICIO = 'srv-terapias-de-revitalizacion'
JULIE = 'esp-julie-viviana-arias-hernandez-20'

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.autocommit = False
cur = cn.cursor()

print("=== ANTES ===")
cur.execute("""select e.id, e.nombres from especialista_servicios s
               join especialistas e on e.id=s.especialista_id
               where s.servicio_id=%s order by e.nombres""", (SERVICIO,))
antes = cur.fetchall()
for r in antes:
    print("   ", r[0], "|", r[1])
print("   total:", len(antes))

cur.execute("""select 1 from especialista_servicios
               where especialista_id=%s and servicio_id=%s""", (JULIE, SERVICIO))
existe = cur.fetchall()
if len(existe) != 1:
    print(f"\n*** ABORTO: esperaba 1 fila de Julie y encontre {len(existe)}. No se toco nada.")
    cn.rollback()
    raise SystemExit(1)

# respaldo de la fila
io.open('/root/universo/agenda/esp-serv-BORRADA-Terapias-Julie.json', 'w').write(
    json.dumps([{"especialista_id": JULIE, "servicio_id": SERVICIO}], indent=1))
print("\n   respaldo de la fila: esp-serv-BORRADA-Terapias-Julie.json")

cur.execute("""delete from especialista_servicios
               where especialista_id=%s and servicio_id=%s""", (JULIE, SERVICIO))
print(f"   filas borradas: {cur.rowcount}")
cn.commit()
print("   commit hecho")

cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()
print("\n=== DESPUES ===")
cur.execute("""select e.id, e.nombres from especialista_servicios s
               join especialistas e on e.id=s.especialista_id
               where s.servicio_id=%s order by e.nombres""", (SERVICIO,))
for r in cur.fetchall():
    print("   ", r[0], "|", r[1])

print("\n=== Y que ofrece el sistema ahora para 'Terapias' ===")
import datetime
for fecha in ('2026-10-02', '2026-10-03'):
    cur.execute("""select e.nombres, count(*) from huecos_del_dia(
                       p_fecha=>%s, p_servicio=>%s) h
                   join especialistas e on e.id=h.especialista_id
                   group by e.nombres order by 1""", (fecha, SERVICIO))
    print(f"   --- {fecha} ---")
    for r in cur.fetchall():
        print(f"      {r[0]}  ->  {r[1]} huecos")

print("\n=== Total de asignaciones (antes eran 43) ===")
cur.execute("select count(*) from especialista_servicios")
print("   ", cur.fetchone()[0])
cn.close()
