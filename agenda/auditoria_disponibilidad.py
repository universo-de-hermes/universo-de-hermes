#!/usr/bin/env python3
# Disponibilidad REAL en 14 dias por sede+servicio. SOLO LECTURA.
import re, io, datetime
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

cur.execute("select id, nombre from sedes order by nombre")
SEDES = cur.fetchall()
cur.execute("select id, nombre, duracion from servicios where activo order by nombre")
SERV = cur.fetchall()
cur.execute("select especialista_id, servicio_id from especialista_servicios")
PAIR = {(r[0], r[1]) for r in cur.fetchall()}
cur.execute("select especialista_id, sede_id from especialista_sedes")
ESPSEDE = {(r[0], r[1]) for r in cur.fetchall()}
cur.execute("select id, nombres from especialistas where activo order by nombres")
ACT = {r[0]: r[1].split()[0] for r in cur.fetchall()}

hoy = datetime.date.today()
INI, FIN = hoy.isoformat(), (hoy + datetime.timedelta(days=13)).isoformat()
print(f"Ventana: {INI} .. {FIN}\n")

for sede_id, sede in SEDES:
    print("=" * 74)
    print(f"  {sede}")
    print("=" * 74)
    sin = []
    for sid, nom, dur in SERV:
        quien = [ACT[e] for e in ACT if (e, sid) in PAIR and (e, sede_id) in ESPSEDE]
        total = 0
        por_dia = []
        for d in range(14):
            f = (hoy + datetime.timedelta(days=d)).isoformat()
            cur.execute("select count(*) from huecos_del_dia(p_fecha=>%s, p_sede=>%s, p_servicio=>%s)",
                        (f, sede_id, sid))
            n = cur.fetchone()[0]
            total += n
            if n:
                por_dia.append(f"{f[5:]}:{n}")
        if not quien:
            print(f"   !! {nom[:40]:<40} NADIE LO HACE EN ESTA SEDE  <<<< el panel NO deberia ofrecerlo")
            sin.append(nom)
        elif total == 0:
            print(f"   !! {nom[:40]:<40} {','.join(quien):<18} 0 huecos en 14 dias <<<< OFRECE PERO NO HAY")
            sin.append(nom)
        else:
            print(f"    {nom[:40]:<40} {','.join(quien):<18} {total:>4} huecos  ({' '.join(por_dia[:5])}...)")
    print(f"   -> problematicos en {sede}: {sin if sin else 'ninguno'}\n")
cn.close()
