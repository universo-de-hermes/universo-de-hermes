#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guarda las credenciales de WhatsApp Cloud API en el .env.

El token se lee de /tmp/wa_token.txt (que se borra al terminar) para no
dejarlo escrito en ningun script que quede en la carpeta.
"""
import os
import re
import shutil

ENV = "/root/universo/recepcionista/.env"
FICHERO_TOKEN = "/tmp/wa_token.txt"

with open(FICHERO_TOKEN, encoding="utf-8") as f:
    token = f.read().strip()

if not token.startswith("EAA") or len(token) < 100:
    raise SystemExit("X el token no parece valido (empieza con %r, %d chars)"
                     % (token[:6], len(token)))

VALORES = {
    "WA_TOKEN": token,
    "WA_PHONE_ID": "1065788356623155",
    "WA_WABA_ID": "1127559659526096",
    "WA_VERIFY_TOKEN": "cj_medical_2026",
}

shutil.copy2(ENV, ENV + ".pre-token.bak")
with open(ENV, encoding="utf-8", newline="") as f:
    lineas = f.read().replace("\r\n", "\n").splitlines()

vistas = set()
salida = []
for l in lineas:
    m = re.match(r"^([A-Z_]+)=", l)
    if m and m.group(1) in VALORES:
        k = m.group(1)
        salida.append("%s=%s" % (k, VALORES[k]))
        vistas.add(k)
    else:
        salida.append(l)
for k, v in VALORES.items():
    if k not in vistas:
        salida.append("%s=%s" % (k, v))

with open(ENV, "w", encoding="utf-8", newline="") as f:
    f.write("\n".join(salida) + "\n")

os.chmod(ENV, 0o600)
os.remove(FICHERO_TOKEN)

print("  credenciales guardadas en el .env (permisos 600, respaldo hecho)")
print("  token: %s...%s  (%d caracteres)" % (token[:6], token[-4:], len(token)))
print("  phone id: 1065788356623155")
print("  waba id : 1127559659526096")
