#!/usr/bin/env python3
"""Prueba EN VIVO: cuanto dura de verdad el cupo que aparta el panel.
Reserva una hora real, mide `expira_en - now()` en Postgres, y suelta."""
import io, json, re, urllib.request, urllib.error
from datetime import date, timedelta
import psycopg2

BASE = "http://127.0.0.1:8001/api/v2/autoservicio"
SEDE = "el-tesoro"

TOKEN = {"t": None}

def pedir(ep, body=None, metodo=None):
    url = BASE + ep
    if body is not None and TOKEN["t"] and "t" not in body:
        body = dict(body, t=TOKEN["t"])
    if body is None and TOKEN["t"]:
        url += ("&" if "?" in url else "?") + "t=" + TOKEN["t"]
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=metodo or ("POST" if data else "GET"),
                                 headers={"content-type": "application/json"})
    try:
        return json.loads(urllib.request.urlopen(req, timeout=20).read())
    except urllib.error.HTTPError as e:
        return {"_error_http": e.code, "_cuerpo": e.read().decode()[:300]}

print("=== abrir la tablet (recepcion entrega la tablet) ===")
ab = pedir("/abrir", {"sede": SEDE, "correo": "jhotas96@gmail.com", "clave": "TzEi4LntP6I8TC"})
print("   respuesta:", json.dumps(ab, ensure_ascii=False)[:300])
for k in ("t", "token", "abierta_hasta"):
    if isinstance(ab, dict) and ab.get(k):
        TOKEN["t"] = ab[k]
print("   token de la tablet:", TOKEN["t"])

print("\n=== servicios que ofrece el panel ===")
d = pedir("/datos?sede=" + SEDE)
servicios = []

def buscar(o, nivel=0):
    if isinstance(o, list):
        for x in o:
            buscar(x, nivel + 1)
    elif isinstance(o, dict):
        if "id" in o and ("nombre" in o or "servicio" in o) and isinstance(o.get("id"), str):
            servicios.append(o)
        for v in o.values():
            buscar(v, nivel + 1)

buscar(d)
print("   claves de /datos:", list(d)[:12] if isinstance(d, dict) else type(d))
servicio = None
for s in servicios:
    if str(s.get("id", "")).startswith("srv") or "serv" in str(s.get("id", "")).lower():
        servicio = s["id"]; break
if not servicio and servicios:
    servicio = servicios[0]["id"]
print("   servicio escogido:", servicio)

# fecha: manana, para que no choque con el corte de "lo que ya paso"
for delta in (1, 2, 3):
    f = (date.today() + timedelta(days=delta)).isoformat()
    h = pedir("/horas", {"sede": SEDE, "servicio": servicio, "fecha": f})
    print("   crudo /horas:", json.dumps(h, ensure_ascii=False)[:300])
    horas = []
    def sacar(o):
        if isinstance(o, list):
            for x in o: sacar(x)
        elif isinstance(o, dict):
            if "inicio" in o or "hora" in o: horas.append(o)
            for v in o.values(): sacar(v)
    sacar(h)
    if horas:
        hora = (horas[0].get("inicio") or horas[0].get("hora"))[:5]
        e = horas[0].get("especialistas") or [{}]
        esp = horas[0].get("especialista_id") or horas[0].get("especialista") or e[0].get("id")
        print("   fecha %s -> %d horas, tomo %s (%s)" % (f, len(horas), hora, esp))
        break
else:
    print("   NO hay horas; aborto"); raise SystemExit(1)

print("\n=== RESERVAR (lo que hace la clienta al tocar la hora) ===")
r = pedir("/reservar", {"sede": SEDE, "servicio": servicio, "fecha": f,
                        "hora": hora, "especialista": esp})
print("   respuesta:", json.dumps(r, ensure_ascii=False)[:250])

rid = (r or {}).get("reserva")
if not rid:
    print("   no se creo la reserva; aborto"); raise SystemExit(1)

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("""select extract(epoch from (expira_en - now()))/60.0,
                      extract(epoch from (expira_en - creado_en))/60.0
                 from reservas where id=%s""", (rid,))
q = cur.fetchone()
print("\n=== LA MEDICION ===")
print("   le quedan   : %.2f minutos" % q[0])
print("   dura en total: %.2f minutos   <-- esto es MIN_RESERVA" % q[1])

print("\n=== limpiar (soltar el cupo de prueba) ===")
cur.execute("delete from reservas where id=%s", (rid,))
print("   borrada:", cur.rowcount)
cur.execute("select count(*) from reservas"); print("   reservas ahora:", cur.fetchone()[0])
cur.execute("select extract(epoch from (expira_en - creado_en))/60.0 from reservas")
print("   duracion de las reservas que queden:", [round(x[0], 2) for x in cur.fetchall()])
cn.close()
