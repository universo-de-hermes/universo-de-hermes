#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vuelve al token ANTERIOR, que si funcionaba.

El token nuevo que llego esta incompleto (283 caracteres contra 290 del
bueno): Meta responde 401 «The access token could not be decrypted». Un token
con caracteres de menos no sirve.

Y no hace falta un token nuevo: lo unico que impedia enviar era la lista de
destinatarios (error 131030), que ya se agrego. El token anterior sigue vivo.
Se recupera del respaldo que dejo `guardar_token_wa.py`.
"""
import os
import re
import shutil

BASE = "/root/universo/recepcionista"
ENV = os.path.join(BASE, ".env")
RESPALDO = ENV + ".pre-token.bak"

if not os.path.exists(RESPALDO):
    raise SystemExit("X no hay respaldo del .env")

with open(RESPALDO, encoding="utf-8", newline="") as f:
    viejo = f.read().replace("\r\n", "\n")

m = re.search(r"^WA_TOKEN=(.+)$", viejo, re.M)
if not m:
    raise SystemExit("X el respaldo no tiene WA_TOKEN")
token_bueno = m.group(1).strip()
if not token_bueno.startswith("EAA"):
    raise SystemExit("X el token del respaldo no parece valido")
print("  token del respaldo: %s...%s (%d caracteres)"
      % (token_bueno[:6], token_bueno[-4:], len(token_bueno)))

with open(ENV, encoding="utf-8", newline="") as f:
    actual = f.read().replace("\r\n", "\n")

nuevo = re.sub(r"^WA_TOKEN=.*$", "WA_TOKEN=" + token_bueno, actual, flags=re.M)
with open(ENV, "w", encoding="utf-8", newline="") as f:
    f.write(nuevo)
os.chmod(ENV, 0o600)
print("  ok token anterior restaurado en el .env")