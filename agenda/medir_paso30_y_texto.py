#!/usr/bin/env python3
"""[SOLO LECTURA]
1) Cuanto cuesta de verdad la regla :00/:30, medido en la base.
2) El texto EXACTO que ve la clienta cuando se le vence el cupo.
"""
import io, re
from datetime import date, timedelta
import psycopg2

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

# ── 1. servicios y su duracion ────────────────────────────────────────────
cur.execute("""select id, nombre, duracion, activo from servicios order by nombre""")
servicios = cur.fetchall()
print("=== SERVICIOS Y SU DURACION ===")
for s in servicios:
    print("   %-34s %s min   %s" % (s[1][:34], s[2], "" if s[3] else "(inactivo)"))

cur.execute("select id, nombre from sedes order by id")
sedes = cur.fetchall()

def cuenta(sede, srv, f, paso):
    cur.execute("""select count(*) from huecos_del_dia(
                     p_fecha=>%s, p_sede=>%s, p_especialista=>null,
                     p_servicio=>%s, p_duracion=>null, p_paso=>%s)""",
                (f, sede, srv, paso))
    return cur.fetchone()[0]

print()
print("=== HORAS OFRECIDAS POR DIA (todos los servicios juntos) ===")
dias = [date.today() + timedelta(days=i) for i in range(0, 7)]
for sid, snom in sedes:
    tot30 = tot15 = 0
    for f in dias:
        if f.weekday() == 6:      # domingo, cerrado
            continue
        for srv, _n, _d, act in servicios:
            if not act:
                continue
            tot30 += cuenta(sid, srv, f, 30)
            tot15 += cuenta(sid, srv, f, 15)
    print("   %-24s  con :00/:30 -> %5d horas | con :00/:15/:30/:45 -> %5d horas  (%d%% menos)"
          % (snom, tot30, tot15, round(100 - (tot30 * 100.0 / tot15 if tot15 else 0))))

print()
print("=== POR SERVICIO (un dia, El Tesoro) ===")
sid = "sede-cj-medical-el-tesoro"
f = date.today() + timedelta(days=1)
while f.weekday() == 6:
    f += timedelta(days=1)
print("   fecha de prueba:", f)
print("   %-34s %-10s %-10s %s" % ("servicio", ":00/:30", ":00/:15", "duracion"))
for srv, nom, dur, act in servicios:
    if not act:
        continue
    a, b = cuenta(sid, srv, f, 30), cuenta(sid, srv, f, 15)
    print("   %-34s %-10d %-10d %s min" % (nom[:34], a, b, dur))
cn.close()

# ── 2. el texto exacto del cupo vencido ───────────────────────────────────
print()
print("=== EL TEXTO QUE VE LA CLIENTA (cupo vencido / hora tomada) ===")
for f in ("/root/universo/agenda/autoservicio.py", "/var/www/html/autoservicio.html"):
    txt = io.open(f, encoding="utf-8", errors="replace").read().split("\n")
    print("--- %s ---" % f)
    for i, l in enumerate(txt, 1):
        if re.search(r"ocup|quit|alguien|venci|venc|expir|otra persona|se acab", l, re.I):
            print("   L%-5d %s" % (i, l.strip()[:170]))
