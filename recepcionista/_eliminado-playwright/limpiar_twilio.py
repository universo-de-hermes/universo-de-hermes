#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Elimina Twilio: era solo el sandbox de pruebas.

El camino de WhatsApp quedo siendo uno solo: la Cloud API de Meta
(`/api/whatsapp/cloud`). Twilio ademas ya no hacia falta para nada:
- su webhook `/api/twilio/whatsapp` respondia por TwiML (solo sandbox);
- sus credenciales seguian guardadas en el `.env` sin usarse.

Se quitan: los imports y constantes, el webhook, las variables del `.env` y
el paquete `twilio` del venv.
"""
import os
import shutil
import subprocess

BASE = "/root/universo/recepcionista"
BASURA = os.path.join(BASE, "_eliminado-playwright")
CS = os.path.join(BASE, "crm", "server.py")
ENV = os.path.join(BASE, ".env")
CAMBIOS = []
CRLF = {}


def leer(p):
    with open(p, encoding="utf-8", newline="") as f:
        bruto = f.read()
    CRLF[p] = "\r\n" in bruto
    if CRLF[p]:
        print("  (aviso) %s usa CRLF" % os.path.basename(p))
    return bruto.replace("\r\n", "\n")


def escribir(p, t):
    if CRLF.get(p):
        t = t.replace("\n", "\r\n")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def cambiar(t, viejo, nuevo, etiqueta):
    if t.count(viejo) != 1:
        raise SystemExit("  X '%s' aparece %d veces" % (etiqueta, t.count(viejo)))
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)
    return t.replace(viejo, nuevo)


def cortar(t, ini, fin, etiqueta):
    i = t.find(ini)
    j = t.find(fin, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        raise SystemExit("  X no encontre las fronteras de %s" % etiqueta)
    print("  ok %s (%d lineas fuera)" % (etiqueta, t[i:j].count("\n")))
    CAMBIOS.append(etiqueta)
    return t[:i] + t[j:]


print("\n== crm/server.py ==")
b = CS + ".pre-sin-twilio.bak"
if not os.path.exists(b):
    shutil.copy2(CS, b)
    print("  respaldo: %s" % os.path.basename(b))

t = leer(CS)

# 1. imports, constantes y cliente de Twilio
t = cortar(t, "# ─── Twilio ───", "# ─── HTML EMBEBIDO ───",
           "imports y constantes de Twilio")

# 2. el webhook
t = cortar(t, "# ─── Twilio Webhook ───", "# ─── WhatsApp Cloud API (Meta oficial) ───",
           "webhook /api/twilio/whatsapp")

# 3. dejar claro que el camino es uno solo
t = cambiar(t,
            "# Twilio quedo como sandbox de pruebas; se puede eliminar tambien.",
            "# Twilio y EvolutionAPI se eliminaron el 2026-09-23: este es el\n"
            "# UNICO camino de WhatsApp.",
            "comentario: unico camino de WhatsApp")

escribir(CS, t)

# ── .env ──
print("\n== .env ==")
b = ENV + ".pre-sin-twilio.bak"
if not os.path.exists(b):
    shutil.copy2(ENV, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(ENV, encoding="utf-8", newline="") as f:
    e = f.read()
claves = ("TWILIO_ACCOUNT_SID=", "TWILIO_AUTH_TOKEN=", "TWILIO_WHATSAPP_NUMBER=")
lineas = [l for l in e.splitlines()
          if not any(l.strip().startswith(k) for k in claves)]
if len(lineas) != len(e.splitlines()):
    e2 = "\n".join(lineas).rstrip("\n") + "\n"
    e2 = e2.replace("# ─── Twilio ───\n", "").replace("# ─── Twilio ───\r\n", "")
    # si quedo el encabezado solo, se limpia
    e2 = "\n".join(l for l in e2.splitlines()
                   if l.strip() not in ("# ─── Twilio ───",))
    e2 = e2.rstrip("\n") + "\n"
    with open(ENV, "w", encoding="utf-8", newline="") as f:
        f.write(e2)
    print("  ok 3 variables de Twilio fuera del .env")
    CAMBIOS.append("variables TWILIO del .env")
else:
    print("  (no habia variables de Twilio)")

# ── scripts ya ejecutados ──
print("\n== scripts de un solo uso ==")
os.makedirs(BASURA, exist_ok=True)
for f in ("fix_whatsapp_cloud.py", "limpiar_playwright2.py"):
    o = os.path.join(BASE, f)
    if os.path.exists(o):
        shutil.move(o, os.path.join(BASURA, f))
        print("  movido: %s" % f)

# ── paquete twilio del venv ──
print("\n== paquete twilio del venv ==")
try:
    p = subprocess.run([os.path.join(BASE, "venv", "bin", "pip"),
                        "uninstall", "-y", "twilio"],
                       capture_output=True, text=True, timeout=180)
    if "Successfully uninstalled" in p.stdout:
        print("  ok paquete twilio desinstalado")
        CAMBIOS.append("paquete twilio")
    else:
        print("  (aviso) %s" % (p.stdout or p.stderr)[-200:])
except Exception as ex:
    print("  (aviso) no pude desinstalar: %s" % ex)

print("\n%d cambios aplicados." % len(CAMBIOS))
