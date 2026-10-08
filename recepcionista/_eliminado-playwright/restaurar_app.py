#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Restaura `app = FastAPI(...)` en crm/server.py.

Al quitar el bloque de Twilio se fue tambien esa linea, porque estaba pegada
debajo de las constantes de Twilio. Sin ella, el CRM no arranca:
    NameError: name 'app' is not defined
y todas las rutas responden 502.
"""
import shutil

CS = "/root/universo/recepcionista/crm/server.py"
b = CS + ".pre-restaurar-app.bak"
shutil.copy2(CS, b)
print("  respaldo: %s" % b.split("/")[-1])

with open(CS, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

if 'app = FastAPI(' in t:
    print("  (ya estaba: no hago nada)")
else:
    viejo = ('load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))\n'
             '\n'
             '# ─── HTML EMBEBIDO ───')
    nuevo = ('load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))\n'
             '\n'
             'app = FastAPI(title="CJ Medical CRM")\n'
             '\n'
             '# ─── HTML EMBEBIDO ───')
    if t.count(viejo) != 1:
        raise SystemExit("  X no encontre el ancla (%d)" % t.count(viejo))
    t = t.replace(viejo, nuevo)
    if crlf:
        t = t.replace("\n", "\r\n")
    with open(CS, "w", encoding="utf-8", newline="") as f:
        f.write(t)
    print("  ok `app = FastAPI(title=\"CJ Medical CRM\")` restaurado")
