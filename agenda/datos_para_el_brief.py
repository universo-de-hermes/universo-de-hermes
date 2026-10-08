#!/usr/bin/env python3
"""[SOLO LECTURA] Los datos reales del sistema, para el brief de la presentacion."""
import io, os, re
import psycopg2

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

def uno(sql, *a):
    cur.execute(sql, a); return cur.fetchone()

print("=== TAMANOS DEL SISTEMA ===")
for etq, sql in (
    ("citas (todas)", "select count(*) from citas"),
    ("citas de octubre", "select count(*) from citas where fecha >= '2026-10-01'"),
    ("clientes", "select count(*) from clientes"),
    ("sedes activas", "select count(*) from sedes where activo"),
    ("especialistas activos", "select count(*) from especialistas where activo"),
    ("servicios activos", "select count(*) from servicios where activo"),
    ("estados de cita", "select count(*) from estados"),
):
    print("   %-24s %s" % (etq, uno(sql)[0]))

print("\n=== POR CANAL ===")
cur.execute("select canal, count(*) from citas group by canal order by 2 desc")
for f in cur.fetchall(): print("   %-16s %d" % f)

print("\n=== SEDES ===")
cur.execute("select nombre, ciudad, direccion, hora_inicio, hora_fin, capacidad_dia from sedes where activo order by nombre")
for f in cur.fetchall():
    print("   %s\n      %s | %s-%s | %s citas/dia\n      %s" % f)

print("\n=== ESPECIALISTAS Y SU SEDE ===")
cur.execute("""select e.nombres, e.apellidos, s.nombre, count(es.servicio_id)
                 from especialistas e
                 left join especialista_sedes esd on esd.especialista_id = e.id
                 left join sedes s on s.id = esd.sede_id
                 left join especialista_servicios es on es.especialista_id = e.id
                where e.activo group by 1,2,3 order by 3,1""")
for f in cur.fetchall(): print("   %-26s %-16s %-26s %s servicios" % f)

print("\n=== SERVICIOS (orden del panel = los mas pedidos primero) ===")
cur.execute("""select s.nombre, s.duracion, count(c.id) as pedidos
                 from servicios s left join citas c on c.servicio_id = s.id
                where s.activo group by s.id, s.nombre, s.duracion
                order by count(c.id) desc, s.nombre""")
for f in cur.fetchall(): print("   %-42s %2d min  %d citas" % f)

print("\n=== ESTADOS ===")
cur.execute("select nombre, tipo, color from estados order by nombre")
for f in cur.fetchall(): print("   %-16s %-12s %s" % f)

print("\n=== RUTAS DEL PANEL DE CLIENTES ===")
src = io.open("/root/universo/agenda/autoservicio.py", encoding="utf-8", errors="replace").read()
for m in re.finditer(r'@router\.(get|post)\("([^"]+)"\)', src):
    print("   %-5s %s" % (m.group(1).upper(), m.group(2)))
cn.close()
