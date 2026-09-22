#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El formulario de cliente mostraba un toast generico y se comia el error real
de la API. Ahora muestra el mensaje del servidor, que es el que permite
diagnosticar. Cambio solo de presentacion: no toca la logica de guardado."""
import io
import sys

RUTA = "/var/www/html/agenda.html"
s = io.open(RUTA, encoding="utf-8").read()

viejo = 'catch(e){ toast("No se pudo guardar el cliente.",true); }'
nuevo = ('catch(e){ toast("No se pudo guardar el cliente: "'
         '+(e&&e.message?e.message:"error desconocido"),true); }')

n = s.count(viejo)
if n != 1:
    print("ABORTO: %d coincidencias de la linea del catch" % n)
    sys.exit(1)

s = s.replace(viejo, nuevo)
io.open(RUTA, "w", encoding="utf-8").write(s)
print("PATCH HTML APLICADO OK")
