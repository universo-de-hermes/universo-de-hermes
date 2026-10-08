#!/usr/bin/env python3
"""Verifica el arreglo del cupo: los 3 casos deben dar mensajes DISTINTOS."""
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
        return {"_http": e.code, **json.loads(e.read().decode())}

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("select count(*) from citas"); antes = cur.fetchone()[0]

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
print("servicio %s | %s | %s | %s" % (srv, f, hora, esp))

def reservar(mio=None):
    return pedir("/reservar", {"sede": APODO, "servicio": srv, "fecha": f,
                               "hora": hora, "especialista": esp, "mio": mio})

print()
print("=== A) aparto la hora ===")
r1 = reservar(); R1 = r1.get("reserva")
print("   ->", json.dumps(r1, ensure_ascii=False)[:200])
print("   segundos que le quedan:", r1.get("segundos"), "(debe ser ~120)")

print()
print("=== B) toco LA MISMA hora otra vez, mandando mi propia reserva ===")
rB = reservar(mio=R1)
print("   ->", json.dumps(rB, ensure_ascii=False)[:220])
ok = (rB.get("ok") and rB.get("reserva") == R1)
print("   RESULTADO:", "OK — reusa la suya, NO culpa a nadie" if ok
      else ">>> SIGUE MALO <<<")

print()
print("=== E) OTRA tablet aparta la hora y yo intento reservarla ===")
cur.execute("delete from reservas")
cur.execute("""select id from apartar_cupo(p_especialista=>%s, p_sede=>%s, p_fecha=>%s,
                 p_inicio=>%s, p_servicio=>%s, p_minutos=>%s, p_referencia=>%s, p_canal=>%s)""",
            (esp, SID, f, hora, srv, 2, "otra-tablet", "Autoservicio"))
rE = reservar()
print("   ->", json.dumps(rE, ensure_ascii=False)[:220])
print("   RESULTADO:", "OK — aqui SI es otra persona, el mensaje es correcto"
      if rE.get("error") == "CUPO_APARTADO" else ">>> revisar <<<")

print()
print("=== limpieza ===")
cur.execute("delete from reservas")
cur.execute("select count(*) from citas"); dsp = cur.fetchone()[0]
print("   citas: %d (antes %d) %s" % (dsp, antes, "OK" if dsp == antes else "!!! CAMBIO !!!"))
cur.execute("select count(*) from reservas"); print("   reservas:", cur.fetchone()[0])
cn.close()
