#!/usr/bin/env python3
"""La Cita de control medico pasa de 20 a 30 minutos (decision del dueno).
Con eso la regla :00/:30 deja de costar cupos."""
import io, re, subprocess
from datetime import date, timedelta
import psycopg2

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

cur.execute("select id, nombre, duracion from servicios order by duracion, nombre")
print("=== ANTES ===")
for f in cur.fetchall():
    print("   %-44s %s min" % (f[1][:44], f[2]))

cur.execute("update servicios set duracion=30 where id='srv-cita-de-control-medico' and duracion=20")
print("\nfilas cambiadas:", cur.rowcount)

cur.execute("select id, nombre, duracion from servicios order by duracion, nombre")
print("\n=== DESPUES ===")
durs = {}
for f in cur.fetchall():
    print("   %-44s %s min" % (f[1][:44], f[2]))
    durs[f[2]] = durs.get(f[2], 0) + 1
print("\nduraciones que quedan:", durs, "<- solo 30 y 60 = la regla no cuesta nada")

# ── comprobar que ya no se pierden horas ─────────────────────────────────
print("\n=== horas ofrecidas de la Cita de control (El Tesoro) ===")
SID = "sede-cj-medical-el-tesoro"
for f in (date.today() + timedelta(days=1), date.today() + timedelta(days=3)):
    if f.weekday() == 6:
        continue
    a = b = 0
    cur.execute("""select count(*) from huecos_del_dia(p_fecha=>%s, p_sede=>%s,
                     p_especialista=>null, p_servicio=>'srv-cita-de-control-medico',
                     p_duracion=>null, p_paso=>%s)""", (f, SID, 30))
    a = cur.fetchone()[0]
    cur.execute("""select count(*) from huecos_del_dia(p_fecha=>%s, p_sede=>%s,
                     p_especialista=>null, p_servicio=>'srv-cita-de-control-medico',
                     p_duracion=>null, p_paso=>%s)""", (f, SID, 15))
    b = cur.fetchone()[0]
    print("   %s  con :00/:30 -> %3d   con :15 -> %3d   %s"
          % (f, a, b, "sin perdida" if a == b else "OJO: %d menos" % (b - a)))

print("\n=== la API lo ve? ===")
r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-c",
                    "import json,urllib.request;"
                    "d=json.load(urllib.request.urlopen('http://127.0.0.1:8001/api/v2/servicios'));"
                    "print([ (s['nombre'], s['duracion']) for s in d if 'control' in s['nombre'].lower() ])"],
                   capture_output=True, text=True)
print("   ", r.stdout.strip() or r.stderr[-200:])
cn.close()
