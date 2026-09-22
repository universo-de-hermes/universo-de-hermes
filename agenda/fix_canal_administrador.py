#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agrega "Administrador" como cuarto canal y corrige la cita ya marcada.

Por que: el canal de cada cita se copia del canal del perfil de la persona.
El perfil del administrador dice "Administrador", pero ese valor no existia en
ninguna de las dos listas de canales de la agenda. Al abrir "Editar persona" el
desplegable no lo encontraba y lo habria cambiado a "Recepcionista" sin avisar.

Se agregan las cuatro opciones en los DOS editores (el de 885 y el de 3718)
para que ninguno pueda resetear un canal existente.
"""
import io
import sys

import psycopg2

RUTA = "/var/www/html/agenda.html"
ENV = "/root/universo/agenda/.api_env"

s = io.open(RUTA, encoding="utf-8").read()

# ── editor A (lista de personas, el de 2 opciones) ───────────────────────────
viejo_a = """      h("div", null, campo("Canal", sel([
          {v:"Recepcionista", t:"Recepcionista"},
          {v:"Call Center",   t:"Call Center"}],
        x.canal, {onchange:function(e){ x.canal = e.target.value; }}))),"""
nuevo_a = """      h("div", null, campo("Canal", sel([
          {v:"Recepcionista", t:"Recepcionista"},
          {v:"Call Center",   t:"Call Center"},
          {v:"Agente virtual", t:"Agente virtual (bot)"},
          {v:"Administrador", t:"Administrador"}],
        x.canal, {onchange:function(e){ x.canal = e.target.value; }}))),"""

# ── editor B (el de la ficha completa) ───────────────────────────────────────
viejo_b = """      campo("Canal",sel([{v:"Recepcionista",t:"Recepcionista"},{v:"Call Center",t:"Call Center"},
        {v:"Agente virtual",t:"Agente virtual (bot)"}],x.canal,"""
nuevo_b = """      campo("Canal",sel([{v:"Recepcionista",t:"Recepcionista"},{v:"Call Center",t:"Call Center"},
        {v:"Agente virtual",t:"Agente virtual (bot)"},{v:"Administrador",t:"Administrador"}],x.canal,"""

for nombre, viejo in (("editor A", viejo_a), ("editor B", viejo_b)):
    n = s.count(viejo)
    print("%s: %d coincidencia(s)" % (nombre, n))
    if n != 1:
        print("ABORTO: no pude ubicar el %s" % nombre)
        sys.exit(1)

s = s.replace(viejo_a, nuevo_a).replace(viejo_b, nuevo_b)
io.open(RUTA, "w", encoding="utf-8").write(s)
print("HTML: los dos editores ahora ofrecen Administrador")
print("HTML: ocurrencias de Administrador =",
      s.count('{v:"Administrador"'))

# ── corregir la cita mal marcada ─────────────────────────────────────────────
url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    if linea.strip().startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")

conn = psycopg2.connect(url)
conn.autocommit = True
cur = conn.cursor()

cur.execute("""select count(*) from citas
                where asignada_por='u-juan-jose-otero' and canal='Recepcionista'""")
print()
print("citas por corregir:", cur.fetchone()[0])

cur.execute("""update citas set canal='Administrador'
                where asignada_por='u-juan-jose-otero'
                  and canal is distinct from 'Administrador'""")
print("citas corregidas:", cur.rowcount)

cur.execute("select coalesce(canal,'(NULL)'), count(*) from citas group by 1")
print("estado final de citas:", cur.fetchall())

cur.execute("select id, nombre, canal from usuarios")
print("usuarios:", cur.fetchall())
conn.close()
print("LISTO")
