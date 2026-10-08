#!/usr/bin/env python3
"""Faltan 2 casos: confirmar con reserva ajena viva y confirmar con la mia vencida.
Todo con ROLLBACK: no se crea ninguna cita."""
import io, re
from datetime import date, timedelta
import psycopg2

SID = "sede-cj-medical-el-tesoro"
t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("select count(*) from citas"); antes = cur.fetchone()[0]

cur.execute("select count(*) from huecos_del_dia(p_fecha=>date '2026-10-05', p_sede=>%s,"
            " p_especialista=>null, p_servicio=>'srv-1-sesion-zona-l',"
            " p_duracion=>null, p_paso=>30)", (SID,))
print("huecos disponibles el 05-oct:", cur.fetchone()[0])

FECHA, HORA = "2026-10-05", "09:00"
cur.execute("select id from especialista_servicios es join especialistas e on e.id=es.especialista_id"
            " where es.servicio_id='srv-1-sesion-zona-l' limit 1")
ESP = cur.fetchone()[0]
print("especialista:", ESP)

def apartar(ref):
    cur.execute("select id from apartar_cupo(p_especialista=>%s, p_sede=>%s, p_fecha=>%s,"
                " p_inicio=>%s, p_servicio=>%s, p_minutos=>%s, p_referencia=>%s, p_canal=>%s)",
                (ESP, SID, FECHA, HORA, "srv-1-sesion-zona-l", 2, ref, "Autoservicio"))
    return str(cur.fetchone()[0])

def confirmar(rid):
    cur.execute("select id from agendar_cita(p_cliente=>'cl_muacieiqlefqt', p_especialista=>%s,"
                " p_sede=>%s, p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,"
                " p_canal=>'Autoservicio', p_por=>'Autoservicio', p_reserva=>%s)",
                (ESP, SID, FECHA, HORA, "srv-1-sesion-zona-l", rid))
    return str(cur.fetchone()[0])

cur.execute("delete from reservas")

print()
print("=== E2) OTRA tablet tiene la hora viva, y yo confirmo con reserva=null ===")
apartar("otra-tablet")
try:
    cur.execute("begin")
    print("   -> se agendo la cita:", confirmar(None), " <-- MALO (le quito el cupo al otro)")
except Exception as e:
    print("   -> RECHAZADO:", str(e).replace(chr(10), " ")[:150])
finally:
    cur.execute("rollback"); cn.rollback()

print()
print("=== E3) OTRA tablet tiene la hora viva, y yo confirmo con MI reserva (ajena) ===")
cur.execute("delete from reservas")
apartar("mio")
mia = apartar("otra")
try:
    cur.execute("begin")
    print("   -> se agendo:", confirmar(mia))
except Exception as e:
    print("   -> RECHAZADO:", str(e).replace(chr(10), " ")[:150])
finally:
    cur.execute("rollback"); cn.rollback()

print()
print("=== D) MI reserva SE VENCIO y yo confirmo ===")
cur.execute("delete from reservas")
rid = apartar("mio")
cur.execute("update reservas set expira_en = now() - interval '1 minute' where id=%s", (rid,))
try:
    cur.execute("begin")
    print("   -> se agendo la cita igual:", confirmar(rid), " <-- bien: no culpa a nadie")
except Exception as e:
    print("   -> RECHAZADO:", str(e).replace(chr(10), " ")[:150])
finally:
    cur.execute("rollback"); cn.rollback()

cur.execute("delete from reservas")
cur.execute("select count(*) from citas"); despues = cur.fetchone()[0]
print()
print("citas: %d (antes %d) %s" % (despues, antes, "OK" if despues == antes else "!!! CAMBIO !!!"))
cn.close()
