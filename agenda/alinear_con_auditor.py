#!/usr/bin/env python3
# Vuelve a la forma "valor simple antes del moderno, MISMA propiedad"
# para que auditar-css.py quede limpio (23 con respaldo, 0 sin).
import io, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

VIEJO = "background-color:var(--acento);background-image:linear-gradient(180deg,"
NUEVO = "background:var(--acento);background:linear-gradient(180deg,"

n = h.count(VIEJO)
print("coincidencias:", n)
if n != 1:
    print("ABORTO"); sys.exit(1)

# el estado apagado debe seguir CLARO (no se toca) y el .toque tampoco
shutil.copy(RUTA, RUTA + '.pre-auditor.bak')
nuevo = h.replace(VIEJO, NUEVO, 1)
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)

print("APLICADO.  llaves balanceadas:", nuevo.count('{') == nuevo.count('}'),
      "| bytes:", len(nuevo.encode('utf-8')),
      "| md5", hashlib.md5(nuevo.encode()).hexdigest()[:12])
print("respaldo:", RUTA + ".pre-auditor.bak")
print()
print("sigue claro el apagado:", "btn.pri[disabled]{opacity:1;background:var(--ink-2)" in nuevo)
print("sigue claro el inicio: ", "#bienvenida .toque" in nuevo and "background:var(--acento)" in nuevo)
