#!/usr/bin/env python3
# Prueba BIEN el candado de cruces: con una cita que SI ocupa cupo. ROLLBACK al final.
import re, io, datetime
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.autocommit = False
cur = cn.cursor()

print("=" * 74)
print("  LA REGLA: funcion citas_calcular_ocupa()")
print("=" * 74)
cur.execute("""select prosrc from pg_proc where proname='citas_calcular_ocupa'""")
r = cur.fetchone()
print(r[0].strip()[:900] if r else "NO EXISTE")

print("\n" + "=" * 74)
print("  ESTADOS: cual ocupa cupo")
print("=" * 74)
cur.execute("select id, nombre, tipo, activo from estados order by orden")
for e in cur.fetchall():
    print(f"   {e[0]:<20} {e[1]:<14} tipo={e[2]:<12} activo={e[3]}")

print("\n" + "=" * 74)
print("  PRUEBA REAL con estado que SI ocupa")
print("=" * 74)
cur.execute("""select id from estados where id='est-confirmado'""")
f = cur.fetchone()
if not f:
    print("   no hay estado confirmado"); raise SystemExit(1)
EST = f[0]
print(f"   usando estado: {EST}  (ocupa cupo)")

base = datetime.date(2026, 10, 20)
ESP = 'esp-jorge-ramiro-cueter-guzman-17'
SEDE = 'sede-cj-medical-el-tesoro'
SERV = 'srv-consulta-medica'
CLI = 'cl_muacieiqlefqt'

def meter(cid, h1, m1, h2, m2):
    cur.execute("""insert into citas (id, tipo, fecha, inicio, fin, especialista_id, sede_id,
                    servicio_id, cliente_id, estado_id, canal)
                   values (%s,'cita',%s,%s,%s,%s,%s,%s,%s,%s,'Prueba')""",
                (cid, base, datetime.time(h1, m1), datetime.time(h2, m2),
                 ESP, SEDE, SERV, CLI, EST))
    cur.execute("select ocupa_cupo from citas where id=%s", (cid,))
    return cur.fetchone()[0]

print("\n   a) cita 1:  10:00-10:30")
try:
    oc = meter('test-cruce-a', 10, 0, 10, 30); print(f"      -> ACEPTADA, ocupa_cupo={oc}")
except Exception as e:
    print(f"      -> RECHAZADA: {str(e)[:150]}"); cn.rollback(); raise SystemExit(1)

print("   b) cita 2 (MISMA especialista, 10:00-10:30 EXACTAMENTE igual):")
try:
    oc = meter('test-cruce-b', 10, 0, 10, 30); print(f"      -> *** ACEPTADA *** ocupa_cupo={oc}  <<<< PROBLEMA")
except Exception as e:
    print(f"      -> RECHAZADA ✅  {str(e)[:230]}")
cn.rollback()
print("      (revertido)")

print("   c) cita 3 (se cruza por 15 min: 10:15-10:45), despues de meter otra vez la 1:")
try:
    meter('test-cruce-c1', 10, 0, 10, 30)
    print("      cita 1 aceptada")
    meter('test-cruce-c2', 10, 15, 10, 45)
    print("      -> *** la cruzada ACEPTADA ***  <<<< PROBLEMA")
except Exception as e:
    print(f"      -> la cruzada RECHAZADA ✅  {str(e)[:230]}")
cn.rollback()

print("   d) control: MISMO horario pero con OTRA especialista (debe aceptar):")
try:
    cur.execute("select id from especialistas where activo and id<>%s limit 1", (ESP,))
    otra = cur.fetchone()[0]
    cur.execute("""insert into citas (id,tipo,fecha,inicio,fin,especialista_id,sede_id,servicio_id,cliente_id,estado_id,canal)
                   values ('t-d1','cita',%s,'10:00','10:30',%s,%s,%s,%s,%s,'Prueba')""",
                (base, otra, SEDE, SERV, CLI, EST))
    print("      -> ACEPTADA ✅ (correcto: dos especialistas pueden atender a la misma hora)")
except Exception as e:
    print(f"      -> RECHAZADA: {str(e)[:200]}")
cn.rollback()

print("\n   e) control: cita PEGADA sin cruzarse (10:30-11:00) con la misma especialista:")
try:
    meter('t-e1', 10, 0, 10, 30)
    meter('t-e2', 10, 30, 11, 0)
    print("      -> ACEPTADA ✅ (correcto: 10:30 empieza justo cuando termina la otra)")
except Exception as e:
    print(f"      -> RECHAZADA: {str(e)[:200]}")
cn.rollback()

cur.execute("select count(*) from citas")
print("\n   citas en la base ahora:", cur.fetchone()[0], "(nada quedo)")
cn.close()
