#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detalles finales de la limpieza de Playwright/EvolutionAPI."""
import os
import shutil

BASE = "/root/universo/recepcionista"
CS = os.path.join(BASE, "crm", "server.py")

with open(CS, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

viejo = "# Twilio queda como sandbox y EvolutionAPI se puede apagar."
nuevo = "# Twilio quedo como sandbox de pruebas; se puede eliminar tambien."
if t.count(viejo) == 1:
    t = t.replace(viejo, nuevo)
    if crlf:
        t = t.replace("\n", "\r\n")
    with open(CS, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("  ok comentario viejo de EvolutionAPI corregido")
else:
    print("  (el comentario ya no estaba)")

# el script de limpieza ya no hace falta en la carpeta del bot
for f in ("limpiar_playwright.py", "fix_wa_import.py", "fix_wa_v26.py",
          "fix_respuestas_asesor_wa.py", "fix_env_wa.py"):
    o = os.path.join(BASE, f)
    if os.path.exists(o):
        shutil.move(o, os.path.join(BASE, "_eliminado-playwright", f))
        print("  movido: %s" % f)
