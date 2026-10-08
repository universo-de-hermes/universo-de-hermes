#!/usr/bin/env python3
# ¿La base misma impide cruzar citas? Prueba real con ROLLBACK. SOLO LECTURA (nada queda).
import re, io
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.autocommit = False
cur = cn.cursor()

print("=" * 74)
print("  1. CANDADOS EN LA TABLA `citas` (triggers y restricciones)")
print("=" * 74)
cur.execute("""select tgname, pg_get_triggerdef(oid) from pg_trigger
               where tgrelid = 'citas'::regclass and not tgisinternal""")
trigs = cur.fetchall()
if not trigs:
    print("   !! NO hay triggers propios en citas")
for nombre, defi in trigs:
    print(f"   TRIGGER {nombre}:")
    print("      " + re.sub(r'\s+', ' ', defi)[:300])

cur.execute("""select conname, contype, pg_get_constraintdef(oid) from pg_constraint
               where conrelid = 'citas'::regclass order by contype""")
print("\n   RESTRICCIONES:")
for nombre, tipo, defi in cur.fetchall():
    etq = {'p': 'PRIMARY KEY', 'f': 'FOREIGN KEY', 'c': 'CHECK', 'u': 'UNIQUE', 'x': 'EXCLUDE'}.get(tipo, tipo)
    print(f"     [{etq}] {nombre}: {re.sub(r'[[:space:]]+', ' ', defi)[:200]}")

print("\n   (la agenda dice: «es la misma regla que aplica el trigger de la base»)")
cur.execute("select pg_get_viewdef('v_solapes'::regclass)")
print("\n   v_solapes (la vista de solapes):")
print("      " + re.sub(r'\s+', ' ', cur.fetchone()[0])[:400])

print("\n" + "=" * 74)
print("  2. PRUEBA REAL: intento meter una cita CRUZADA")
print("=" * 74)
cur.execute("select column_name, is_nullable from information_schema.columns where table_name='citas' order by ordinal_position")
cols = cur.fetchall()
print("   columnas de citas:", [c[0] for c in cols])
cur.execute("""select column_name, is_nullable, column_default from information_schema.columns
               where table_name='citas' and is_nullable='NO' order by ordinal_position""")
oblig = cur.fetchall()
print("   obligatorias:", [(c[0], c[2]) for c in oblig])

# tomar una cita real como molde
cur.execute("select * from citas limit 1")
fila = cur.fetchone()
nombres = [d.name for d in cur.description]
molde = dict(zip(nombres, fila)) if fila else {}
print("\n   molde (una cita real):", {k: molde.get(k) for k in ('id','fecha','inicio','fin','especialista_id','sede_id','servicio_id','cliente_id','estado_id','canal')})

if molde:
    import datetime
    base_fecha = molde['fecha'] + datetime.timedelta(days=21)
    def armar(ini_h, ini_m, fin_h, fin_m, cid):
        d = dict(molde)
        d['id'] = cid
        d['fecha'] = base_fecha
        d['inicio'] = datetime.time(ini_h, ini_m)
        d['fin'] = datetime.time(fin_h, fin_m)
        return d
    c1 = armar(10, 0, 10, 30, 'test-cruce-1')
    c2 = armar(10, 15, 10, 45, 'test-cruce-2')   # se cruza con la 1

    def meter(c):
        usados = [k for k in c if c[k] is not None]
        sql = "insert into citas (" + ",".join(usados) + ") values (" + ",".join(["%s"] * len(usados)) + ")"
        cur.execute(sql, [c[k] for k in usados])

    print(f"\n   a) meto la 1a cita: {base_fecha} 10:00-10:30 ...")
    try:
        meter(c1); print("      -> ACEPTADA (no hay candado para esto)")
    except Exception as e:
        print(f"      -> RECHAZADA: {str(e)[:160]}")
        cn.rollback()

    print(f"   b) meto la 2a cita CRUZADA: {base_fecha} 10:15-10:45 ...")
    try:
        meter(c2)
        print("      -> *** ACEPTADA ***  <<<< LA BASE NO FRENA EL CRUCE")
    except Exception as e:
        print(f"      -> RECHAZADA ✅: {str(e)[:220]}  <<<< ESTE es el candado")

cn.rollback()
print("\n   (transaccion revertida: no quedo nada en la base)")
cur.execute("select count(*) from citas")
print("   citas en la base ahora:", cur.fetchone()[0])
cn.close()
