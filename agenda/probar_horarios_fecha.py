#!/usr/bin/env python3
"""Prueba de los endpoints nuevos: horarios por fecha y bloqueos en rango.

Los horarios por fecha son de administrador (configurar la agenda), así que
esta prueba entra con la sesión del admin. El bloqueo en rango sí es de
operador (la recepcionista bloquea su almuerzo o una cita médica).
"""
import json, urllib.request, urllib.error

BASE = "http://127.0.0.1:8001"
TOKEN = open("/root/universo/agenda/.api_token").read().strip()
ADMIN = {"correo": "jhotas96@gmail.com", "clave": "TzEi4LntP6I8TC"}
ESP = "esp-diana-carolina-ruiz-rojas"
SEDE = "sede-cj-medical-bogota"

ok = mal = 0
def prueba(n, c, extra=""):
    global ok, mal
    if c:
        ok += 1; print("  ok   " + n)
    else:
        mal += 1; print("  MAL  " + n + (("\n       " + str(extra)[:300]) if extra else ""))

COOKIE = {"v": ""}

def llamar(metodo, ruta, cuerpo=None, admin=False):
    url = BASE + ruta
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(url, data=datos, method=metodo)
    if admin and COOKIE["v"]:
        req.add_header("Cookie", COOKIE["v"])
    else:
        req.add_header("X-API-Token", TOKEN)
    if datos: req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode() or "{}")
        except Exception: return e.code, {}

def huecos(fecha, admin=False):
    s, d = llamar("POST", "/huecos/dia",
                  {"fecha": fecha, "sede": SEDE, "especialista": ESP}, admin=admin)
    if s != 200: return None
    return sorted(h["inicio"][:5] for h in d)

print("\n— entrada del administrador —")
s, d = llamar("POST", "/auth/login", ADMIN)
prueba(f"entra como admin ({s})", s == 200, d)
if s == 200:
    # sacar la cookie de la respuesta
    url = BASE + "/auth/login"
    req = urllib.request.Request(url, data=json.dumps(ADMIN).encode(), method="POST")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=20) as r:
        for h in r.headers.get_all("Set-Cookie") or []:
            if h.startswith("sesion="):
                COOKIE["v"] = h.split(";")[0]
    prueba("recibe la cookie de sesión", COOKIE["v"].startswith("sesion="), COOKIE["v"][:20])

print("\n— horarios por fecha puntual —")
base = huecos("2026-09-21", admin=True)
prueba(f"antes: el lunes 21 va de 09:00 a 18:30 ({len(base) if base else 0} huecos)",
       base and base[0] == "09:00" and base[-1] == "18:30", base[:3] if base else base)

s, d = llamar("POST", "/horarios-fecha", {
    "especialista": ESP, "sede": SEDE,
    "desde": "2026-09-21", "hasta": "2026-09-21",
    "inicio": "14:00", "fin": "18:00", "nota": "prueba automatica"}, admin=True)
prueba(f"crea el horario puntual ({s})", s == 200 and d.get("puestas") == 1, d)

punt = huecos("2026-09-21", admin=True)
prueba(f"y ahora manda el puntual: {len(punt) if punt else 0} huecos, de "
       f"{punt[0] if punt else '?'} a {punt[-1] if punt else '?'}",
       punt and punt[0] == "14:00" and punt[-1] == "17:30", punt[:3] if punt else punt)

martes = huecos("2026-09-22", admin=True)
prueba("el martes 22 sigue con el semanal (09:00-18:30)",
       martes and martes[0] == "09:00" and martes[-1] == "18:30", martes[:3] if martes else martes)

s, d = llamar("GET", "/horarios-fecha?especialista=" + ESP + "&desde=2026-09-01&hasta=2026-09-30", admin=True)
prueba(f"GET /horarios-fecha lo lista ({s}, {len(d) if isinstance(d, list) else '?'})",
       s == 200 and isinstance(d, list) and len(d) == 1 and d[0]["desde"] == "14:00", d)

print("\n— bloqueo en varios días (permiso de operador) —")
s, d = llamar("POST", "/citas/bloqueo-rango", {
    "especialista": ESP, "sede": SEDE,
    "desde": "2026-09-21", "hasta": "2026-09-30",
    "inicio": "10:00", "fin": "12:00",
    "motivo": "Cita medica", "dias": [1, 3]})
prueba(f"bloquea lunes y miércoles del rango ({s}, bloqueados={d.get('bloqueados')})",
       s == 200 and d.get("bloqueados") == 4, d)

mie = huecos("2026-09-23", admin=True)
prueba("el miércoles 23 ya no hay 10:00", mie is not None and "10:00" not in mie, mie[:4] if mie else mie)
prueba("pero sí hay 09:00", mie is not None and "09:00" in mie, mie[:4] if mie else mie)

mar = huecos("2026-09-22", admin=True)
prueba("el martes 22 NO quedó bloqueado", mar is not None and "10:00" in mar, mar[:4] if mar else mar)

s, d = llamar("GET", "/citas/bloqueos?desde=2026-09-01&hasta=2026-09-30&especialista=" + ESP)
prueba(f"GET /citas/bloqueos los lista ({s}, {len(d) if isinstance(d, list) else '?'})",
       s == 200 and isinstance(d, list) and len(d) == 4, d)

print("\n— errores claros, no 500 —")
s, d = llamar("POST", "/horarios-fecha", {
    "especialista": ESP, "sede": SEDE,
    "desde": "2026-09-25", "hasta": "2026-09-20",
    "inicio": "09:00", "fin": "12:00"}, admin=True)
prueba(f"fecha final antes de la inicial -> {s} (400)", s == 400, d)

s, d = llamar("POST", "/horarios-fecha", {
    "especialista": ESP, "sede": SEDE,
    "desde": "2026-09-25", "hasta": "2026-09-25",
    "inicio": "18:00", "fin": "09:00"}, admin=True)
prueba(f"hora de fin antes de la inicial -> {s} (400)", s == 400, d)

s, d = llamar("POST", "/citas/bloqueo-rango", {
    "especialista": "esp-no-existe", "sede": SEDE,
    "desde": "2026-09-25", "hasta": "2026-09-25",
    "inicio": "09:00", "fin": "10:00"})
prueba(f"especialista inventada -> {s} (400)", s == 400, d)

print("\n— el operador NO puede tocar horarios (es de admin) —")
s, d = llamar("POST", "/horarios-fecha", {
    "especialista": ESP, "sede": SEDE, "desde": "2026-09-21",
    "inicio": "14:00", "fin": "18:00"})
prueba(f"token de Hermes -> {s} (403)", s == 403, d)

print("\n— limpieza —")
s, d = llamar("DELETE", "/horarios-fecha?especialista=" + ESP +
              "&desde=2026-09-01&hasta=2026-09-30", admin=True)
prueba(f"borra los horarios puntuales ({d.get('borradas')})",
       s == 200 and d.get("borradas") == 1, d)

s, d = llamar("GET", "/citas/bloqueos?desde=2026-09-01&hasta=2026-09-30&especialista=" + ESP)
for b in (d if isinstance(d, list) else []):
    llamar("DELETE", "/citas/" + b["id"], admin=True)

fin = huecos("2026-09-21", admin=True)
prueba("el lunes 21 volvió al semanal (09:00-18:30)",
       fin and fin[0] == "09:00" and fin[-1] == "18:30", fin[:3] if fin else fin)

s, d = llamar("GET", "/citas/bloqueos?desde=2026-09-01&hasta=2026-09-30&especialista=" + ESP)
prueba(f"quedan 0 bloqueos ({len(d) if isinstance(d, list) else '?'})",
       isinstance(d, list) and len(d) == 0, d)

print(f"\n{ok} ok, {mal} mal")
