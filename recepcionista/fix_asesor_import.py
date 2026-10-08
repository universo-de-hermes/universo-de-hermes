#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Las respuestas de ASESOR no salian por DOS razones.

1. Al limpiar Playwright/EvolutionAPI se borro una linea de mas:
   `from crm.database import DB_PATH, get_connection` estaba pegada al
   `global WHATSAPP_CLIENT` que si habia que quitar. Sin ese import, la tarea
   reventaba cada 10 segundos con
       Error en pending_replies: name 'get_connection' is not defined
   asi que NINGUNA respuesta de asesor se enviaba nunca.

2. El proceso del bot tenia el `WA_TOKEN` VIEJO (o vacio): arranco el
   2026-09-25, antes de que se guardaran las credenciales. `load_dotenv()` no
   pisa lo que ya esta en el entorno, asi que hay que REINICIAR el bot para
   que systemd lea el .env actualizado.
"""
import os
import re
import shutil

MP = "/root/universo/recepcionista/main.py"
b = MP + ".pre-import-fix.bak"
if not os.path.exists(b):
    shutil.copy2(MP, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(MP, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

# que le falta get_connection a la tarea?
m = re.search(r"async def send_pending_replies\(app: Application\):.*?try:\n(\s+)conn = get_connection\(\)",
              t, re.S)
if not m:
    raise SystemExit("  X no encontre el cuerpo de send_pending_replies")
bloque = m.group(0)
if "from crm.database import get_connection" in bloque:
    print("  (el import ya estaba)")
else:
    viejo = "    import sqlite3\n    try:\n        conn = get_connection()"
    nuevo = ("    import sqlite3\n"
             "    # `get_connection` se fue con el `global WHATSAPP_CLIENT` que si\n"
             "    # habia que borrar al quitar Playwright. Sin este import la tarea\n"
             "    # reventaba cada 10 s («name 'get_connection' is not defined») y\n"
             "    # NINGUNA respuesta de asesor se enviaba.\n"
             "    from crm.database import get_connection\n"
             "    try:\n        conn = get_connection()")
    if t.count(viejo) != 1:
        raise SystemExit("  X ancla no encontrada (%d)" % t.count(viejo))
    t = t.replace(viejo, nuevo)
    print("  ok `from crm.database import get_connection` restaurado")

    if crlf:
        t = t.replace("\n", "\r\n")
    with open(MP, "w", encoding="utf-8", newline="") as f:
        f.write(t)