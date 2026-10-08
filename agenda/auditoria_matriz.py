#!/usr/bin/env python3
# AUDITORIA de la matriz. SOLO LECTURA.
import re, io, datetime
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

cur.execute("select * from sedes order by nombre")
COLS = [d.name for d in cur.description]
SEDES = cur.fetchall()
print("columnas de sedes:", COLS)
print("\n=== SEDES (como estan en la base) ===")
for f in SEDES:
    d = dict(zip(COLS, f))
    print(f"   [{d.get('id')}]")
    for k in ('nombre', 'ciudad', 'departamento', 'direccion', 'telefono'):
        if k in d:
            print(f"      {k}: {d[k]!r}")

SEDE_NOM = {dict(zip(COLS, f)).get('id'): dict(zip(COLS, f)).get('nombre') for f in SEDES}

cur.execute("select id, nombre, activo, duracion from servicios where activo order by nombre")
SERV = cur.fetchall()
cur.execute("select id, nombres, activo from especialistas order by nombres")
ESP = cur.fetchall()
cur.execute("select especialista_id, servicio_id from especialista_servicios")
PAIR = {(r[0], r[1]) for r in cur.fetchall()}
cur.execute("select especialista_id, sede_id from especialista_sedes")
ESPSEDE = {(r[0], r[1]) for r in cur.fetchall()}
cur.execute("select especialista_id, sede_id, count(*) from horarios group by 1,2")
HOR = {(r[0], r[1]): r[2] for r in cur.fetchall()}

act = {e[0]: e for e in ESP if e[2]}
print("\n" + "=" * 74)
print("  1. INCOHERENCIAS")
print("=" * 74)
prob = 0
for eid, e in act.items():
    sedes_e = [s for s in ESPSEDE if s[0] == eid]
    if not sedes_e:
        print(f"   !! {e[1]}: ACTIVA y sin ninguna sede asignada"); prob += 1
        continue
    for _, sede in sedes_e:
        if HOR.get((eid, sede), 0) == 0:
            print(f"   !! {e[1]}: esta en {SEDE_NOM.get(sede, sede)} pero SIN HORARIO ahi"); prob += 1
for (eid, sede) in HOR:
    if eid in act and (eid, sede) not in ESPSEDE:
        print(f"   !! {act[eid][1]}: tiene HORARIO en {SEDE_NOM.get(sede, sede)} pero no esta en especialista_sedes"); prob += 1
for sid, nom, _, _ in SERV:
    if not any((eid, sid) in PAIR for eid in act):
        print(f"   !! SERVICIO '{nom}': no lo hace ninguna activa"); prob += 1
print("   (nada mas)" if prob == 0 else f"   TOTAL: {prob}")

print("\n" + "=" * 74)
print("  2. QUE OFRECE EL PANEL EN CADA SEDE, Y SI TIENE HORA DE VERDAD")
print("=" * 74)
hoy = datetime.date.today()
for sede_id in SEDE_NOM:
    print(f"\n   --- {SEDE_NOM[sede_id]}  ({sede_id})")
    for sid, nom, activo, dur in SERV:
        quien = [e[1].split()[0] for e in act.values() if (e[0], sid) in PAIR and (e[0], sede_id) in ESPSEDE]
        if not quien:
            continue
        cur.execute("select count(*) from huecos_del_dia(p_fecha=>%s, p_sede=>%s, p_servicio=>%s)",
                    ((hoy + datetime.timedelta(days=3)).isoformat(), sede_id, sid))
        n = cur.fetchone()[0]
        alerta = "   <<<< SIN HORAS" if n == 0 else ""
        print(f"      {nom[:42]:<42} {dur:>3}min  {','.join(quien)[:22]:<22} huecos:{n:>3}{alerta}")

print("\n" + "=" * 74)
print("  3. SERVICIOS QUE EL PANEL OFRECE PERO NADIE PUEDE HACER EN ESA SEDE")
print("=" * 74)
for sede_id in SEDE_NOM:
    huerf = [nom for sid, nom, _, _ in SERV
             if not any((e[0], sid) in PAIR and (e[0], sede_id) in ESPSEDE for e in act.values())]
    print(f"   {SEDE_NOM[sede_id]}: {huerf if huerf else 'ninguno'}")
cn.close()
