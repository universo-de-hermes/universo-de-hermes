#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Falta get_conversation en los imports del CRM (el webhook nuevo lo usa)."""
import os
import shutil

CS = "/root/universo/recepcionista/crm/server.py"
b = CS + ".pre-wa-import.bak"
if not os.path.exists(b):
    shutil.copy2(CS, b)

with open(CS, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

viejo = """    get_all_advisors, update_client_data, create_appointment, get_connection
)"""
nuevo = """    get_all_advisors, update_client_data, create_appointment, get_connection,
    get_conversation
)"""
if t.count(viejo) != 1:
    raise SystemExit("X ancla no encontrada (%d)" % t.count(viejo))
t = t.replace(viejo, nuevo)

if crlf:
    t = t.replace("\n", "\r\n")
with open(CS, "w", encoding="utf-8", newline="") as f:
    f.write(t)
print("  ok get_conversation agregado a los imports del CRM")
