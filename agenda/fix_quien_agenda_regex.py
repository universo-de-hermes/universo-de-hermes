#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El reporte "Quien agenda" reconocia los usuarios solo si su id empezaba con
"u_" (guion bajo). El administrador de la agenda tiene id "u-juan-jose-otero"
(guiones), asi que no lo resolvia. Ahora acepta las dos formas.
"""
import io
import re
import sys

RUTA = "/var/www/html/agenda.html"
s = io.open(RUTA, encoding="utf-8").read()

n = len(re.findall(r"/\^u_/", s))
print("ocurrencias de /^u_/ encontradas:", n)
if n == 0:
    print("ABORTO: no encontre nada que cambiar")
    sys.exit(1)

s2 = re.sub(r"/\^u_/", "/^u[-_]/", s)
io.open(RUTA, "w", encoding="utf-8").write(s2)

print("ocurrencias de /^u[-_]/ ahora:", len(re.findall(r"/\^u\[-_\]/", s2)))
print("PATCH HTML OK")
