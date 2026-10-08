#!/usr/bin/env python3
# Aplica el arreglo de hora Colombia SOLO en el filtro de huecos_del_dia.
# NO toca r.expira_en > now() (las reservas SI guardan UTC).
import re, sys, datetime
import psycopg2

ENV = '/root/universo/agenda/.api_env'
txt = open(ENV).read()
m = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', txt)
cn = psycopg2.connect(m.group(1))
cn.autocommit = False
cur = cn.cursor()

cur.execute("""select pg_get_functiondef(p.oid) from pg_proc p
 join pg_namespace n on n.oid=p.pronamespace
 where n.nspname='public' and p.proname='huecos_del_dia'""")
fila = cur.fetchone()
if not fila:
    print("ABORTO: no existe huecos_del_dia"); sys.exit(1)
src = fila[0]

if 'America/Bogota' in src:
    print("YA ESTA APLICADO (la funcion ya menciona America/Bogota). Nada que hacer.")
    sys.exit(0)

A1 = "p_fecha = current_date"
A2 = "(p_fecha + c.ini) < now() + (coalesce(p_margen,15) || ' minutes')::interval"
B1 = "p_fecha = (now() at time zone 'America/Bogota')::date"
B2 = "(p_fecha + c.ini) < (now() at time zone 'America/Bogota') + (coalesce(p_margen,15) || ' minutes')::interval"

print("=== ANCLAS ===")
ok = True
for a in (A1, A2):
    n = src.count(a)
    print(f"  {n} x  {a[:60]}")
    if n != 1:
        ok = False
if not ok:
    print("ABORTO: las anclas no calzan exactamente 1 vez. No se toco nada.")
    sys.exit(1)

print("\n=== QUE OTROS now() QUEDAN (deben quedarse) ===")
for i, ln in enumerate(src.splitlines(), 1):
    if 'now()' in ln:
        print(f"  {i:>4}| {ln.strip()}")

open('/root/universo/agenda/huecos_del_dia.pre-fix-tz.sql', 'w').write(src)
nuevo = src.replace(A1, B1).replace(A2, B2)
open('/root/universo/agenda/huecos_del_dia.post-fix-tz.sql', 'w').write(nuevo)

print("\n=== DIFERENCIAS ===")
import difflib
for ln in difflib.unified_diff(src.splitlines(), nuevo.splitlines(), lineterm='', n=1):
    if ln.startswith(('---', '+++', '@@')):
        continue
    print("  " + ln)

cur.execute(nuevo)
cn.commit()
print("\n>>> APLICADO Y CONFIRMADO (commit hecho)")

# --- VERIFICACION INMEDIATA ---
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()
cur.execute("select now(), (now() at time zone 'America/Bogota')")
u, c = cur.fetchone()
print(f"\n=== VERIFICACION   UTC={u:%H:%M}  Colombia={c:%H:%M} ===")
hoy = datetime.date.today()
for nombre, sid in (('Zona M', 'srv-1-sesion-zona-m'), ('Terapias', 'srv-terapias-de-revitalizacion')):
    for d in range(0, 5):
        f = hoy + datetime.timedelta(days=d)
        cur.execute("select inicio from huecos_del_dia(p_fecha=>%s, p_servicio=>%s)", (f, sid))
        hs = sorted({str(r[0])[:5] for r in cur.fetchall()})
        etq = 'HOY' if d == 0 else ('manana' if d == 1 else f'+{d}')
        print(f"  {nombre:<10} {f} {etq:<7} {len(hs):>3} horas {hs[:4]}")

print("\n=== CONTROL: un cupo ya pasado NO debe salir ===")
cur.execute("""select count(*) from huecos_del_dia(p_fecha=>%s, p_servicio=>%s)
               where inicio < (now() at time zone 'America/Bogota')::time""", (hoy, 'srv-1-sesion-zona-m'))
print("  huecos de HOY ya pasados (debe ser 0):", cur.fetchone()[0])
cn.close()
