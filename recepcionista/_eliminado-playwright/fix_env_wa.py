#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arregla las variables de WhatsApp en el .env.

Trampa: en un .env, `WA_TOKEN=  # comentario` NO deja el valor vacio —
python-dotenv lee el comentario COMO VALOR. Entonces WA_APP_SECRET quedaba
con texto, la validacion de firma se activaba sola y Meta (o la prueba)
recibia 403 forbidden. Los comentarios van en su propia linea.
"""
import os
import re
import shutil

ENV = "/root/universo/recepcionista/.env"
b = ENV + ".pre-wa-env.bak"
if not os.path.exists(b):
    shutil.copy2(ENV, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(ENV, encoding="utf-8") as f:
    t = f.read()

NUEVO = """
# ─── WhatsApp Cloud API (Meta) ───
# Token PERMANENTE del usuario de sistema (no el de 24 h)
WA_TOKEN=
# Phone Number ID del numero nuevo
WA_PHONE_ID=
# WhatsApp Business Account ID (WABA)
WA_WABA_ID=
# App Secret de la app: valida la firma de los webhooks
WA_APP_SECRET=
# Palabra secreta que se pega en el panel de Meta
WA_VERIFY_TOKEN=cj_medical_2026
"""

# se quita el bloque viejo (las 5 variables y su encabezado) y se pone limpio
lineas = [l for l in t.splitlines()
          if not re.match(r"^WA_(TOKEN|PHONE_ID|WABA_ID|APP_SECRET|VERIFY_TOKEN)=", l)
          and l.strip() != "# ─── WhatsApp Cloud API (Meta) ───"]
t = "\n".join(lineas).rstrip("\n") + "\n" + NUEVO

with open(ENV, "w", encoding="utf-8") as f:
    f.write(t)

from dotenv import load_dotenv          # noqa: E402
load_dotenv(ENV, override=True)
print("\n  Como quedan leidas ahora:")
for k in ("WA_TOKEN", "WA_PHONE_ID", "WA_WABA_ID", "WA_APP_SECRET",
          "WA_VERIFY_TOKEN"):
    print("    %-18s = %r" % (k, os.getenv(k)))
