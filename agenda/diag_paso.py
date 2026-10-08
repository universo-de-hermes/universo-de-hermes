#!/usr/bin/env python3
# Radiografia del "paso" de las citas. SOLO LECTURA.
import re, io
import psycopg2

txt = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', txt).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

print("=== 1. VALOR POR DEFECTO DE p_paso EN LA BASE ===")
cur.execute("""select p.proname, pg_get_function_arguments(p.oid)
 from pg_proc p join pg_namespace n on n.oid=p.pronamespace
 where n.nspname='public' and p.proname in ('huecos_del_dia','buscar_huecos')""")
for nom, args in cur.fetchall():
    m = re.search(r'p_paso[^,)]*', args)
    print(f"  {nom:<16} -> {m.group(0) if m else '(sin p_paso)'}")

print()
print("=== 2. A QUE HORA EMPIEZAN LOS TURNOS (si no son :00, el paso 30 desalinea) ===")
cur.execute("""select distinct h.desde::text, h.hasta::text from horarios h order by 1""")
for d, hs in cur.fetchall():
    print(f"  desde {d}  hasta {hs}")
cur.execute("""select count(*) from horarios""")
print("  total franjas:", cur.fetchone()[0])
cur.execute("""select count(*) from horarios where date_part('minute', desde) % 30 <> 0""")
print("  franjas que NO arrancan en :00/:30:", cur.fetchone()[0])

print()
print("=== 3. QUE OFRECE HOY CON paso 15 vs paso 30 ===")
hoy = '2026-10-01'
for paso in (15, 30):
    cur.execute("""select distinct to_char(inicio,'HH24:MI') from huecos_del_dia(
        p_fecha=>%s, p_servicio=>%s, p_paso=>%s) order by 1""", (hoy, 'srv-1-sesion-zona-m', paso))
    hs = [r[0] for r in cur.fetchall()]
    print(f"  paso {paso}: {len(hs)} horas -> {hs}")
cn.close()
