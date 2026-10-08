#!/usr/bin/env python3
"""[SOLO LECTURA] El nombre unico, visto desde los tres sistemas."""
import io, json, urllib.request, re

TOK = io.open("/root/universo/agenda/.api_token").read().strip()

def traer(url, cab=None):
    req = urllib.request.Request(url, headers=cab or {})
    try:
        return urllib.request.urlopen(req, timeout=15).read().decode()
    except Exception as e:
        return "ERROR: %s" % e

print("=== 1. LA AGENDA (API) ===")
d = traer("http://127.0.0.1:8001/api/v2/sedes", {"x-api-token": TOK})
try:
    for s in json.loads(d):
        print("   %-28s | nombre: %-24s | dir: %s" % (s.get("id"), s.get("nombre"), (s.get("direccion") or "(vacia)")[:52]))
except Exception:
    print("   ", d[:300])

print("\n=== 2. EL PANEL (/salud) ===")
d = traer("http://127.0.0.1:8001/api/v2/autoservicio/salud")
try:
    j = json.loads(d)
    print("   direcciones:", json.dumps(j.get("direcciones"), ensure_ascii=False, indent=1))
except Exception:
    print("   ", d[:400])

print("\n=== 3. EL PANEL: que nombre le llega a la clienta ===")
d = traer("http://127.0.0.1:8001/api/v2/autoservicio/datos?sede=el-tesoro")
try:
    j = json.loads(d)
    print("   sede:", json.dumps(j.get("sede"), ensure_ascii=False))
except Exception:
    print("   (pide sesion, se prueba en la regresion):", d[:200])
d = traer("http://127.0.0.1:8001/api/v2/autoservicio/datos?sede=bogota")
try:
    j = json.loads(d)
    print("   sede:", json.dumps(j.get("sede"), ensure_ascii=False))
except Exception:
    pass

print("\n=== 4. PAGINAS EN VIVO ===")
for u in ("https://agenda.universojota.tech/agenda.html",
          "https://agenda.universojota.tech/autoservicio.html",
          "https://crmcjm.universojota.tech/"):
    r = traer(u)
    print("   %-52s %s" % (u.replace("https://", ""), "ERROR" if r.startswith("ERROR") else "%d bytes" % len(r)))

print("\n=== 5. EL CRM: de donde saca el nombre de la sede ===")
for f in ("/root/universo/recepcionista/crm/server.py",
          "/root/universo/recepcionista/crm/index.html"):
    try:
        t = io.open(f, encoding="utf-8", errors="replace").read().split("\n")
    except Exception:
        continue
    for i, l in enumerate(t, 1):
        if re.search(r"sedes|sede\b", l) and re.search(r"nombre|select|from sedes", l, re.I):
            print("   %s L%d: %s" % (f.split("/")[-1], i, l.strip()[:120]))
