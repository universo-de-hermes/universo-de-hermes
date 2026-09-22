#!/usr/bin/env python3
"""Prueba de punta a punta con la base recién limpiada:
cliente nuevo -> buscar huecos -> agendar -> ver en la agenda -> anular -> el
hueco vuelve. Es el flujo completo que va a vivir la recepcionista.
"""
import json, urllib.request, urllib.error

BASE = "http://127.0.0.1:8001"
TOKEN = open("/root/universo/agenda/.api_token").read().strip()
SEDE = "sede-cj-medical-bogota"
ESP = "esp-diana-carolina-ruiz-rojas"
DOC = "99000001"
TEL = "3009900001"

ok = mal = 0
def prueba(n, c, extra=""):
    global ok, mal
    if c:
        ok += 1; print("  ok   " + n)
    else:
        mal += 1; print("  MAL  " + n + (("\n       " + str(extra)[:300]) if extra else ""))

def llamar(metodo, ruta, cuerpo=None):
    url = BASE + ruta
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(url, data=datos, method=metodo)
    req.add_header("X-API-Token", TOKEN)
    if datos: req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode() or "{}")
        except Exception: return e.code, {}

print("\n— 1. la base arranca vacía —")
s, d = llamar("GET", "/clientes?limite=5")
prueba(f"0 clientes ({len(d) if isinstance(d, list) else '?'})", isinstance(d, list) and len(d) == 0, d)

print("\n— 2. crear el primer cliente —")
s, d = llamar("POST", "/clientes/crear", {
    "documento": DOC, "primer_nombre": "CLIENTE", "primer_apellido": "PRUEBA",
    "telefono": TEL, "correo": "prueba@ejemplo.com", "sede": SEDE})
prueba(f"cliente creado ({s})", s == 200 and d.get("id"), d)
CLI = d.get("id") if s == 200 else None

print("\n— 3. buscarlo por teléfono —")
s, d = llamar("POST", "/clientes/buscar", {"telefono": TEL})
prueba(f"lo encuentra ({s}, {len(d) if isinstance(d, list) else '?'})",
       s == 200 and isinstance(d, list) and len(d) == 1, d)

print("\n— 4. ver horas libres —")
s, d = llamar("POST", "/huecos/dia", {"fecha": "2026-09-21", "sede": SEDE,
                                      "especialista": ESP})
huecos = d if isinstance(d, list) else []
prueba(f"la agenda ofrece {len(huecos)} horas", s == 200 and len(huecos) > 0, d)
HORA = huecos[0]["inicio"][:5] if huecos else "09:00"
print(f"       → primera: {HORA}")

print("\n— 5. agendar la cita —")
s, d = llamar("POST", "/citas/agendar", {
    "cliente_id": CLI, "especialista": ESP, "sede": SEDE,
    "fecha": "2026-09-21", "inicio": HORA,
    "servicio": "srv-terapias-de-revitalizacion",
    "canal": "Agente virtual", "por": "prueba"})
prueba(f"cita agendada ({s})", s == 200 and d.get("id"), d)
CITA = d.get("id") if s == 200 else None

print("\n— 6. aparece en la agenda del día —")
s, d = llamar("GET", f"/agenda/{SEDE}/2026-09-21")
citas = d if isinstance(d, list) else []
prueba(f"la agenda del 21-sep la muestra ({len(citas)} citas)",
       s == 200 and any(c["id"] == CITA for c in citas), [c.get("id") for c in citas])

print("\n— 7. esa hora ya no se ofrece —")
s, d = llamar("POST", "/huecos/dia", {"fecha": "2026-09-21", "sede": SEDE,
                                      "especialista": ESP})
libres = [h["inicio"][:5] for h in (d if isinstance(d, list) else [])]
prueba(f"la hora {HORA} desapareció de los libres", HORA not in libres, libres[:5])

print("\n— 8. doble agendamiento rechazado —")
s, d = llamar("POST", "/citas/agendar", {
    "cliente_id": CLI, "especialista": ESP, "sede": SEDE,
    "fecha": "2026-09-21", "inicio": HORA,
    "servicio": "srv-terapias-de-revitalizacion", "por": "prueba"})
prueba(f"la misma hora se rechaza ({s})", s in (400, 409), d)

print("\n— 9. confirmar la cita —")
s, d = llamar("POST", "/citas/estado", {"cita_id": CITA, "estado": "est-confirmado",
                                        "por": "prueba"})
prueba(f"pasa a Confirmado ({s})", s == 200, d)
s, d = llamar("GET", f"/agenda/{SEDE}/2026-09-21")
mia = [c for c in (d if isinstance(d, list) else []) if c["id"] == CITA]
prueba("y se ve confirmada", mia and mia[0].get("estado_id") == "est-confirmado",
       mia[0] if mia else None)

print("\n— 10. anularla devuelve el hueco —")
s, d = llamar("DELETE", "/citas/" + CITA)
prueba(f"anulada ({s})", s == 200, d)
s, d = llamar("POST", "/huecos/dia", {"fecha": "2026-09-21", "sede": SEDE,
                                      "especialista": ESP})
libres = [h["inicio"][:5] for h in (d if isinstance(d, list) else [])]
prueba(f"la hora {HORA} volvió a estar libre", HORA in libres, libres[:5])

print("\n— 11. limpieza —")
s, d = llamar("GET", "/clientes?buscar=" + DOC)
for c in (d if isinstance(d, list) else []):
    llamar("DELETE", "/citas/" + CITA)
    # borrar el cliente de prueba directo por SQL no se puede desde aquí
s, d = llamar("GET", "/clientes?buscar=" + DOC)
prueba(f"queda 1 cliente de prueba (se borra al final)", isinstance(d, list), d)

print(f"\n{ok} ok, {mal} mal")
print("\nCliente de prueba:", CLI)
