#!/usr/bin/env python3
# Deja TODO a 30 minutos (:00 / :30): panel, agenda, API y base.
# Cada ancla debe calzar EXACTAMENTE 1 vez o aborta.
import io, os, re, shutil, sys
import psycopg2

OK = True


def parchear(ruta, pares):
    global OK
    print(f"\n--- {ruta}")
    if not os.path.exists(ruta):
        print("   NO EXISTE"); OK = False; return
    b = open(ruta, 'rb').read()
    for v, n in pares:
        c = b.count(v.encode())
        print(f"   {c} coincidencia(s): {v[:78]}")
        if c != 1:
            print("   >>> ABORTO: no calza exactamente 1"); OK = False; return
    shutil.copy(ruta, ruta + '.pre-paso30.bak')
    b2 = b
    for v, n in pares:
        b2 = b2.replace(v.encode(), n.encode(), 1)
    open(ruta, 'wb').write(b2)
    print(f"   OK {len(b)} -> {len(b2)} bytes  (respaldo .pre-paso30.bak)")


# 1. PANEL
parchear('/root/universo/agenda/autoservicio.py', [
    ('os.getenv("AUTOSERVICIO_PASO", "15")', 'os.getenv("AUTOSERVICIO_PASO", "30")'),
])

# 2. AGENDA (buscador de cupos del mostrador)
parchear('/var/www/html/agenda.html', [
    ('paso=opts.paso||15', 'paso=opts.paso||30'),
])

# 3. API (defaults)
parchear('/root/universo/agenda/agenda_api.py', [
    ('Optional[int] = None; paso: int = 15', 'Optional[int] = None; paso: int = 30'),
    ('paso: int = 15; limite: int = 40', 'paso: int = 30; limite: int = 40'),
])

# 4. BASE DE DATOS: p_paso DEFAULT 15 -> 30
print("\n--- BASE DE DATOS")
txt = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', txt).group(1))
cn.autocommit = False
cur = cn.cursor()
pat = re.compile(r'(p_paso\s+integer\s+DEFAULT\s+)15\b')
for fname in ('huecos_del_dia', 'buscar_huecos'):
    cur.execute("""select pg_get_functiondef(p.oid) from pg_proc p
                   join pg_namespace n on n.oid=p.pronamespace
                   where n.nspname='public' and p.proname=%s""", (fname,))
    f = cur.fetchone()
    if not f:
        print(f"   {fname}: NO EXISTE"); OK = False; continue
    src = f[0]
    if 'p_paso integer DEFAULT 30' in src:
        print(f"   {fname}: ya estaba en 30"); continue
    nuevo, n = pat.subn(r'\g<1>30', src)
    if n != 1:
        print(f"   {fname}: ABORTO, {n} coincidencias del DEFAULT 15"); OK = False; continue
    io.open(f'/root/universo/agenda/{fname}.pre-paso30.sql', 'w').write(src)
    cur.execute(nuevo)
    print(f"   {fname}: DEFAULT 15 -> 30  (respaldo {fname}.pre-paso30.sql)")

if not OK:
    print("\n*** ALGO FALLO: NO se confirma la base (rollback) ***")
    cn.rollback()
    sys.exit(1)
cn.commit()
print("   commit hecho")

# 5. VERIFICACION
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()
print("\n=== VERIFICACION ===")
for fname in ('huecos_del_dia', 'buscar_huecos'):
    cur.execute("""select pg_get_function_arguments(p.oid) from pg_proc p
                   join pg_namespace n on n.oid=p.pronamespace
                   where n.nspname='public' and p.proname=%s""", (fname,))
    m = re.search(r'p_paso[^,)]*', cur.fetchone()[0])
    print(f"  {fname:<16} {m.group(0)}")

print("\n  Horas que saldrian SIN decirle el paso (usa el default):")
for sid in ('srv-1-sesion-zona-m', 'srv-terapias-de-revitalizacion', 'srv-1-sesion-zona-l'):
    for f in ('2026-10-02', '2026-10-03'):
        cur.execute("select distinct to_char(inicio,'HH24:MI') from huecos_del_dia(p_fecha=>%s, p_servicio=>%s) order by 1", (f, sid))
        hs = [r[0] for r in cur.fetchall()]
        mal = [h for h in hs if h[3:] not in ('00', '30')]
        print(f"    {sid[:34]:<34} {f}: {len(hs):>2} horas  fuera de :00/:30 -> {mal if mal else 'NINGUNA ✅'}")
cn.close()
print("\n>>> LISTO" if OK else "\n>>> CON ERRORES")
