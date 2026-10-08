#!/usr/bin/env python3
"""Que error le sale a recepcion cuando la tablet tiene la hora apartada.
1) La base: agendar_cita con una reserva viva de otro (en transaccion, ROLLBACK).
2) El mensaje que la agenda le muestra a recepcion (se evalua su propia funcion).
"""
import io, re, subprocess
import psycopg2

SID = "sede-cj-medical-el-tesoro"
SRV = "srv-1-sesion-zona-l"
FECHA, HORA = "2026-10-05", "09:00"

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

cur.execute("""select e.id, e.nombres, e.activo from especialistas e
                 join especialista_servicios es on es.especialista_id = e.id
                 join especialista_sedes esd on esd.especialista_id = e.id
                where es.servicio_id = %s and esd.sede_id = %s and e.activo
                limit 4""", (SRV, SID))
filas = cur.fetchall()
print("especialistas que hacen ese servicio en esa sede:")
for f in filas:
    print("   ", f)
ESP = filas[0][0] if filas else None
print("uso:", ESP)

cur.execute("delete from reservas")
cur.execute("""select id from apartar_cupo(p_especialista=>%s, p_sede=>%s, p_fecha=>%s,
                 p_inicio=>%s, p_servicio=>%s, p_minutos=>%s, p_referencia=>%s, p_canal=>%s)""",
            (ESP, SID, FECHA, HORA, SRV, 2, "autoservicio", "Autoservicio"))
print("\nla tablet aparto la hora (reserva viva)")

err = ""
try:
    cur.execute("begin")
    cur.execute("""select id from agendar_cita(p_cliente=>'cl_muacieiqlefqt', p_especialista=>%s,
                     p_sede=>%s, p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                     p_canal=>'Recepcionista', p_por=>'Recepcionista')""",
                (ESP, SID, FECHA, HORA, SRV))
    print("   -> RECEPCION PUDO AGENDAR (malo: habria que bloquearlo)")
except Exception as e:
    err = str(e).replace(chr(10), " ")
    print("   -> recepcion NO puede:", err[:150])
finally:
    cur.execute("rollback"); cn.rollback()

cur.execute("delete from reservas")
cur.execute("select count(*) from reservas"); print("   reservas limpias:", cur.fetchone()[0])
cn.close()

# ── el mensaje que la agenda le muestra a recepcion ───────────────────────
print("\n=== el mensaje que ve recepcion en pantalla ===")
js = """
const {chromium} = require('playwright');
const fs = require('fs');
(async () => {
  const b = await chromium.launch({executablePath:'/root/.cache/ms-playwright/chromium-1234/chrome-linux64/chrome'});
  const p = await b.newPage();
  await p.goto('file:///var/www/html/agenda.html');
  await p.waitForTimeout(500);
  const r = await p.evaluate(() => ({
    apartado: mensajeDeError({detail:%s}, '', 409),
    tomado:   mensajeDeError({detail:%s}, '', 409)
  }));
  console.log('   CUPO_APARTADO -> ' + JSON.stringify(r.apartado));
  console.log('   CUPO_TOMADO   -> ' + JSON.stringify(r.tomado));
  await b.close();
})();
""" % (repr(err[:120]), repr("CUPO_TOMADO: ya hay una cita en ese horario"))
io.open("/tmp/msg_agenda.js", "w").write(js)
r = subprocess.run(["node", "/tmp/msg_agenda.js"], capture_output=True, text=True,
                   cwd="/root/universo/agenda/_paquete2/tools")
print(r.stdout or r.stderr[-400:])
