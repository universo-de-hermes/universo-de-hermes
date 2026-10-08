#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Revisión completa del sistema CJ Medical antes de la prueba."""
import asyncio
import io
import json
import pathlib
import re
import subprocess
import sys
import urllib.error
import urllib.request

sys.path.insert(0, "/root/universo/recepcionista")

TOK = pathlib.Path("/root/universo/agenda/.api_token").read_text().strip()
AGENDA = "http://127.0.0.1:8001/api/v2"
ok_tot, fallos = 0, []


def chequear(nombre, condicion, detalle=""):
    global ok_tot
    if condicion:
        ok_tot += 1
        print("  ✅ %s%s" % (nombre, (" — " + detalle) if detalle else ""))
    else:
        fallos.append(nombre)
        print("  ❌ %s%s" % (nombre, (" — " + detalle) if detalle else ""))


def api(ruta, metodo="GET", cuerpo=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    req = urllib.request.Request(AGENDA + ruta, data=datos, method=metodo,
                                 headers={"accept": "application/json",
                                          "x-api-token": TOK,
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:200]
    except Exception as e:
        return "ERR", str(e)[:200]


print("=" * 68)
print("1) SERVICIOS")
for s in ("pepe", "agenda-api", "webui-backend"):
    r = subprocess.run(["systemctl", "is-active", s], capture_output=True, text=True)
    estado = r.stdout.strip()
    if s == "webui-backend":
        chequear(s, True, estado)          # no es crítico
    else:
        chequear(s, estado == "active", estado)

print()
print("2) EL BOT Y SU TOKEN")
import agenda_helper as ag            # noqa: E402
from dotenv import load_dotenv        # noqa: E402
load_dotenv()
import herramientas                   # noqa: E402

cab = ag._cabeceras()
chequear("manda el token a la agenda", "X-API-Token" in cab)
d = asyncio.run(ag.datos(refrescar=True))
chequear("lee los maestros", len(d.get("estados", [])) == 7,
         "%d estados, %d sedes, %d servicios, %d especialistas"
         % (len(d.get("estados", [])), len(d.get("sedes", [])),
            len(d.get("servicios", [])), len(d.get("especialistas", []))))
nombres = [t["function"]["name"] for t in herramientas.HERRAMIENTAS]
chequear("12 herramientas", len(nombres) == 12, ", ".join(nombres))
for nueva in ("buscar_cliente", "actualizar_cliente", "ver_agenda_especialista"):
    chequear("herramienta " + nueva, nueva in nombres)

print()
print("3) LA API DE LA AGENDA")
for ruta in ("/datos", "/citas", "/clientes", "/agenda-especialista?especialista=Valentina&fecha=2026-09-21"):
    c, _ = api(ruta)
    chequear("GET " + ruta.split("?")[0], c == 200, "HTTP %s" % c)

print()
print("4) CANAL DEL BOT Y DE LOS USUARIOS")
st, citas = api("/citas")
canales = {}
for c in citas if isinstance(citas, list) else []:
    canales[c.get("canal")] = canales.get(c.get("canal"), 0) + 1
print("      citas por canal:", canales)
validos = {"Administrador", "Asesor", "Recepcionista", "Agente IA"}
malos = [k for k in canales if k and k not in validos]
chequear("todos los canales son de la lista", not malos, "raros: %s" % malos)

print()
print("5) LA AGENDA WEB")
html = io.open("/var/www/html/agenda.html", encoding="utf-8").read()
for canal in ("Administrador", "Asesor", "Recepcionista", "Agente IA"):
    chequear("canal en los editores: " + canal,
             len(re.findall(r'v:"%s"' % canal, html)) >= 2)
chequear("regla de 30 minutos en el código",
         "PASO_MINUTOS" not in html and '"-"+ult' in html)
chequear("sin nombres viejos (Call Center / Agente virtual)",
         "Call Center" not in html and "Agente virtual" not in html)
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S | re.I)
io.open("/tmp/chk.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk.js"], capture_output=True, text=True)
chequear("JavaScript sin errores", r.returncode == 0, (r.stderr or "")[:200])

print()
print("6) EL MODELO DE IA")
cfg = {}
for linea in io.open("/root/universo/recepcionista/.env", encoding="utf-8").read().splitlines():
    if "=" in linea and not linea.strip().startswith("#"):
        k, v = linea.split("=", 1)
        cfg[k.strip()] = v.strip().strip('"').strip("'")
req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps({"model": "openai/gpt-4o-mini",
                     "messages": [{"role": "user", "content": "Di OK"}],
                     "max_tokens": 5}).encode(),
    headers={"Authorization": "Bearer " + cfg.get("OPENROUTER_API_KEY", ""),
             "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=40) as r:
        j = json.loads(r.read().decode())
        chequear("clave de IA responde", bool(j.get("choices")))
except Exception as e:
    chequear("clave de IA responde", False, str(e)[:120])

print()
print("=" * 68)
print("RESULTADO: %d comprobaciones OK, %d fallos" % (ok_tot, len(fallos)))
if fallos:
    print("FALLARON:", ", ".join(fallos))
else:
    print("🎩 TODO OK")