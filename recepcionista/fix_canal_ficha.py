#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La ficha del CRM decia SIEMPRE «📱 Telegram».

En el JavaScript del panel habia una linea con el canal quemado:

    document.getElementById('pChannel').textContent='📱 Telegram';

Asi que un cliente que escribio por WhatsApp aparecia como Telegram. Con
WhatsApp entrando de verdad, eso confunde al asesor (no sabe por donde
contestarle). Ahora usa el canal real del cliente.

OJO: ese HTML vive dentro de un f-string, asi que las llaves van dobles
({{ }}). El reemplazo NO puede llevar llaves sueltas.
"""
import os
import shutil

CS = "/root/universo/recepcionista/crm/server.py"
b = CS + ".pre-canal-badge.bak"
if not os.path.exists(b):
    shutil.copy2(CS, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(CS, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

VIEJO = "document.getElementById('pChannel').textContent='📱 Telegram';"

NUEVO = ("let ch=c.channel||'telegram';"
         "let chName=ch==='whatsapp'?'WhatsApp':(ch==='telegram'?'Telegram':ch);"
         "let chIcon=ch==='whatsapp'?'\U0001f4ac':'\U0001f4f1';"
         "document.getElementById('pChannel').textContent=chIcon+' '+chName;")

if VIEJO not in t:
    raise SystemExit("  X no encontre la linea del canal quemado")
if t.count(VIEJO) != 1:
    raise SystemExit("  X aparece %d veces" % t.count(VIEJO))

t = t.replace(VIEJO, NUEVO)

if crlf:
    t = t.replace("\n", "\r\n")
with open(CS, "w", encoding="utf-8", newline="") as f:
    f.write(t)

print("  ok el canal de la ficha ahora es el real (WhatsApp / Telegram)")
