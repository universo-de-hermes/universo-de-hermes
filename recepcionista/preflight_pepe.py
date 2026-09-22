#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pre-vuelo antes de la prueba del flujo completo:
 1. La clave de IA responde de verdad (POST real, no solo GET /models).
 2. La Agenda API responde con el token que usa el bot.
 3. Hay citas y estados como para probar.
"""
import io
import json
import urllib.error
import urllib.request

ENV = "/root/universo/recepcionista/.env"

cfg = {}
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    linea = linea.strip()
    if "=" in linea and not linea.startswith("#"):
        k, v = linea.split("=", 1)
        cfg[k.strip()] = v.strip().strip('"').strip("'")

ok_key = cfg.get("OPENROUTER_API_KEY", "")
ant_key = cfg.get("ANTHROPIC_API_KEY", "")
agenda = cfg.get("AGENDA_API", "").rstrip("/")
tok = cfg.get("API_TOKEN", "")

print("AGENDA_API:", agenda)
print("API_TOKEN presente:", bool(tok), "| largo:", len(tok))
print("OPENROUTER_API_KEY presente:", bool(ok_key), "| empieza:", ok_key[:8])
print("ANTHROPIC_API_KEY presente:", bool(ant_key), "| empieza:", ant_key[:8])
print()

# ── 1) prueba REAL del modelo ────────────────────────────────────────────────
print("=== 1) PRUEBA REAL DEL MODELO (OpenRouter) ===")
cuerpo = {
    "model": "openai/gpt-4o-mini",
    "messages": [{"role": "user", "content": "Responde solo: OK"}],
    "max_tokens": 10,
}
req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps(cuerpo).encode(),
    headers={"Authorization": "Bearer " + ok_key,
             "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, timeout=45) as r:
        d = json.loads(r.read().decode())
        print("  200 OK ->", d["choices"][0]["message"]["content"].strip()[:60])
except urllib.error.HTTPError as e:
    print("  ERROR", e.code, "->", e.read().decode()[:300])
except Exception as e:
    print("  ERROR ->", str(e)[:300])

# ── 2) prueba de la Agenda API con el token del bot ──────────────────────────
print()
print("=== 2) AGENDA API (con el token del bot) ===")
for ruta in ("/datos", "/citas"):
    req = urllib.request.Request(agenda + ruta,
                                 headers={"accept": "application/json",
                                          "x-api-token": tok})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.loads(r.read().decode())
            if ruta == "/datos":
                print("  /datos -> 200 | estados:", len(d.get("estados", [])),
                      "| sedes:", len(d.get("sedes", [])),
                      "| especialistas:", len(d.get("especialistas", [])))
            else:
                print("  /citas -> 200 | citas:", len(d))
    except urllib.error.HTTPError as e:
        print("  %s -> ERROR %s %s" % (ruta, e.code, e.read().decode()[:200]))
    except Exception as e:
        print("  %s -> ERROR %s" % (ruta, str(e)[:200]))

# ── 3) estados disponibles ──────────────────────────────────────────────────
print()
print("=== 3) ESTADOS ===")
req = urllib.request.Request(agenda + "/datos",
                             headers={"accept": "application/json",
                                      "x-api-token": tok})
try:
    d = json.loads(urllib.request.urlopen(req, timeout=20).read().decode())
    for e in d.get("estados", []):
        if e.get("activo", True):
            print("  ", e.get("id"), "|", e.get("nombre"), "| tipo:", e.get("tipo"))
except Exception as e:
    print("  ERROR", str(e)[:200])
