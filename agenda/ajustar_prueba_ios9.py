#!/usr/bin/env python3
# Ajusta probar-ios9.js: el panel SALTA el paso de especialista cuando hay una sola.
import io, shutil, sys

R = '/root/universo/agenda/_paquete2/tools/probar-ios9.js'
s = io.open(R, encoding='utf-8').read()

VIEJO = "await p.locator('.opcion').first().click(); await p.waitForTimeout(2000);\n  t('llega al resumen'"
NUEVO = ("/* El panel NO pregunta cuando a esa hora hay una sola especialista:\n     pasa derecho al resumen. Asi que solo se toca la ficha si esa pantalla salio. */\n"
         "  if (/Escoja con quién/i.test(await texto())){\n"
         "    await p.locator('.opcion').first().click(); await p.waitForTimeout(2000);\n"
         "  }\n"
         "  t('llega al resumen'")

n = s.count(VIEJO)
print("coincidencias:", n)
if n != 1:
    print("ABORTO"); sys.exit(1)

shutil.copy(R, R + '.orig')
io.open(R, 'w', encoding='utf-8').write(s.replace(VIEJO, NUEVO, 1))
print("ajustado. respaldo:", R + '.orig')
print()
print("--- como quedo ---")
i = s.replace(VIEJO, NUEVO, 1).find('El panel NO pregunta')
print(s.replace(VIEJO, NUEVO, 1)[i - 80:i + 380])
