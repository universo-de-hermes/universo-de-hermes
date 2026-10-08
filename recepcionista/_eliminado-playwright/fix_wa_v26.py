#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sube la version de la API de WhatsApp de v21.0 a v26.0.

El panel de Meta recomienda v26.0 para la suscripcion del webhook, y v21.0
(octubre 2024) ya esta por cumplir los dos anos que Meta mantiene cada version.
Comprobado que v26.0 existe: sin token responde «access token required», no
«version does not exist».
"""
import os
import shutil

CS = "/root/universo/recepcionista/crm/server.py"
b = CS + ".pre-v26.bak"
if not os.path.exists(b):
    shutil.copy2(CS, b)

with open(CS, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

viejo = 'WA_API = os.getenv("WA_API", "https://graph.facebook.com/v21.0").rstrip("/")'
nuevo = 'WA_API = os.getenv("WA_API", "https://graph.facebook.com/v26.0").rstrip("/")'

if t.count(viejo) != 1:
    raise SystemExit("X ancla no encontrada (%d)" % t.count(viejo))
t = t.replace(viejo, nuevo)

if crlf:
    t = t.replace("\n", "\r\n")
with open(CS, "w", encoding="utf-8", newline="") as f:
    f.write(t)
print("  ok API de WhatsApp: v21.0 -> v26.0")
