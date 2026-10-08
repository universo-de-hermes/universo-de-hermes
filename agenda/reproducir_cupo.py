#!/usr/bin/env python3
"""QUE mensaje sale en cada caso del cupo apartado. No crea citas reales."""
import io, json, re, urllib.request, urllib.error
from datetime import date, timedelta
import psycopg2

BASE = "http://127.0.0.1:8001/api/v2/autoservicio"
SID = "sede-cj-medical-el-tesoro"
APODO = "el-tesoro"
T = {"t": None}

def pedir(ep, body=None):
    url = BASE + ep
    if body is not None and T["t"] and "t" not in body:
        body = dict(body, t=T["t"])
    if body is None and T["t"]:
        url += ("&" if "?" in url else "?") + "t=" + T["t"]
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                 headers={"content-type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=20).read())
    except urllib.error.HTTPError as e:
        crudo = e.read().decode()
        return {"_http": e.code, "_cuerpo_crudo": crudo[:260]}

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("select count(*) from citas"); citas_antes = cur.fetchone()[0]

T["t"] = pedir("/abrir", {"sede": APODO, "correo": "jhotas96@gmail.com",
                          "clave": "TzEi4LntP6I8TC"}).get("token")
d = pedir("/datos?sede=" + APODO)
srv = f = hora = esp = None
for s in (d.get("servicios") or []):
    for k in (1, 2, 3, 4, 5):
        fx = (date.today() + timedelta(days=k)).isoformat()
        h = pedir("/horas", {"sede": APODO, "servicio": s.get("id"), "fecha": fx})
        if h.get("horas"):
            srv, f, hora = s.get("id"), fx, h["horas"][0]["hora"][:5]
            esp = h["horas"][0]["especialistas"][0]["id"]; break
    if srv: break
print("servicio %s | %s | %s | %s\n" % (srv, f, hora, esp))

def reservar():
    return pedir("/reservar", {"sede": APODO, "servicio": srv, "fecha": f,
                               "hora": hora, "especialista": esp})

def apartar_otro(ref):
    cur.execute("""select * from apartar_cupo(p_especialista=>%s, p_sede=>%s, p_fecha=>%s,
                     p_inicio=>%s, p_servicio=>%s, p_minutos=>%s, p_referencia=>%s, p_canal=>%s)""",
                (esp, SID, f, hora, srv, 2, ref, "Autoservicio"))
    return str(cur.fetchone()[0])

print("=== A) aparto la hora (normal) ===")
r1 = reservar(); R1 = r1.get("reserva")
print("   ->", json.dumps(r1, ensure_ascii=False)[:170])

print("\n=== B) toco LA MISMA hora otra vez (la reserva viva es MIA) ===")
print("   ->", json.dumps(reservar(), ensure_ascii=False)[:300])

print("\n=== C) se me VENCE la reserva y toco la misma hora ===")
cur.execute("update reservas set expira_en = now() - interval '1 minute' where id=%s", (R1,))
r3 = reservar(); print("   ->", json.dumps(r3, ensure_ascii=False)[:200])
R3 = r3.get("reserva")

print("\n=== E) OTRA tablet aparta la hora y yo intento reservarla ===")
cur.execute("delete from reservas")
apartar_otro("otra-tablet")
print("   ->", json.dumps(reservar(), ensure_ascii=False)[:300])

print("\n=== E2) y si intento CONFIRMAR una reserva ajena viva (ROLLBACK) ===")
cur.execute("delete from reservas\\n")
apartar_otro("otra-tablet")
try:
    cur.execute("begin")
    cur.execute("""select * from agendar_cita(p_cliente=>'cl_muacieiqlefqt', p_especialista=>%s,
                     p_sede=>%s, p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                     p_canal=>'Autoservicio', p_por=>'Autoservicio', p_reserva=>null)""",
                (esp, SID, f, hora, srv))
    print("   -> NO dio error (MALO)")
except Exception as e:
    print("   -> ERROR:", str(e).split("\\n")[0][:170])
finally:
    cur.execute("rollback"); cn.rollback()

print("\n=== D) se me VENCE la reserva e intento CONFIRMAR (ROLLBACK) ===")
cur.execute("delete from reservas")
rid = apartar_otro("mio")
cur.execute("update reservas set expira_en = now() - interval '1 minute' where id=%s", (rid,))
try:
    cur.execute("begin")
    cur.execute("""select * from agendar_cita(p_cliente=>'cl_muacieiqlefqt', p_especialista=>%s,
                     p_sede=>%s, p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                     p_canal=>'Autoservicio', p_por=>'Autoservicio', p_reserva=>%s)""",
                (esp, SID, f, hora, srv, rid))
    print("   -> NO dio error: se agenda igual (no culpa a nadie)")
except Exception as e:
    print("   -> ERROR:", str(e).split("\\n")[0][:170])
finally:
    cur.execute("rollback"); cn.rollback()

print("\n=== limpieza ===")
cur.execute("delete from reservas")
cur.execute("select count(*) from citas"); c = cur.fetchone()[0]
print("   citas: %d (antes %d) %s" % (c, citas_antes, "OK" if c == citas_antes else "!!! CAMBIO !!!"))
cur.execute("select count(*) from reservas"); print("   reservas:", cur.fetchone()[0])
cn.close()
