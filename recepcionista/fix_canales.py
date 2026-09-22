#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Canales unificados: Administrador · Asesor · Recepcionista · Agente IA.

Antes eran «Recepcionista · Call Center · Agente virtual · Administrador» y el
bot marcaba sus citas como «WhatsApp», así que no se podía medir cuánto agenda
Pepe. Se unifican los nombres en la agenda web, en el bot y en los datos ya
cargados.
"""
import io
import sys

import psycopg2

BASE = "/root/universo/recepcionista/"
HTML = "/var/www/html/agenda.html"
ENV = "/root/universo/agenda/.api_env"

# ── 1) el bot marca sus citas como «Agente IA» ──────────────────────────────
t = io.open(BASE + "agenda_helper.py", "r", encoding="utf-8", newline="").read()
crlf = "\r\n" in t
s = t.replace("\r\n", "\n")

viejo = '                  canal: str = "WhatsApp", por: str = "pepe") -> dict:'
nuevo = '                  canal: str = "Agente IA", por: str = "Pepe") -> dict:'
if s.count(viejo) != 1:
    print("ABORTO: %d coincidencias del canal del bot" % s.count(viejo))
    sys.exit(1)
s = s.replace(viejo, nuevo)
if crlf:
    s = s.replace("\n", "\r\n")
io.open(BASE + "agenda_helper.py", "w", encoding="utf-8", newline="").write(s)
print("agenda_helper.py: el bot ahora marca «Agente IA» y firma «Pepe»")

# ── 2) los dos editores de personas en la agenda web ────────────────────────
h = io.open(HTML, "r", encoding="utf-8", newline="").read()
hcrlf = "\r\n" in h
hs = h.replace("\r\n", "\n")

viejo_a = """      h("div", null, campo("Canal", sel([
          {v:"Recepcionista", t:"Recepcionista"},
          {v:"Call Center",   t:"Call Center"},
          {v:"Agente virtual", t:"Agente virtual (bot)"},
          {v:"Administrador", t:"Administrador"}],
        x.canal, {onchange:function(e){ x.canal = e.target.value; }}))),"""
nuevo_a = """      h("div", null, campo("Canal", sel([
          {v:"Administrador", t:"Administrador"},
          {v:"Asesor",        t:"Asesor"},
          {v:"Recepcionista", t:"Recepcionista"},
          {v:"Agente IA",     t:"Agente IA (Pepe)"}],
        x.canal, {onchange:function(e){ x.canal = e.target.value; }}))),"""

viejo_b = """      campo("Canal",sel([{v:"Recepcionista",t:"Recepcionista"},{v:"Call Center",t:"Call Center"},
        {v:"Agente virtual",t:"Agente virtual (bot)"},{v:"Administrador",t:"Administrador"}],x.canal,"""
nuevo_b = """      campo("Canal",sel([{v:"Administrador",t:"Administrador"},{v:"Asesor",t:"Asesor"},
        {v:"Recepcionista",t:"Recepcionista"},{v:"Agente IA",t:"Agente IA (Pepe)"}],x.canal,"""

viejo_c = 'panel("Canal que asigna","Call Center contra recepción",'
nuevo_c = 'panel("Canal que asigna","Quién agendó cada cita",'

for etiqueta, v in (("editor A", viejo_a), ("editor B", viejo_b), ("subtítulo", viejo_c)):
    n = hs.count(v)
    print("  %s: %d coincidencia(s)" % (etiqueta, n))
    if n != 1:
        print("ABORTO: no pude ubicar el %s" % etiqueta)
        sys.exit(1)

hs = hs.replace(viejo_a, nuevo_a).replace(viejo_b, nuevo_b).replace(viejo_c, nuevo_c)
if hcrlf:
    hs = hs.replace("\n", "\r\n")
io.open(HTML, "w", encoding="utf-8", newline="").write(hs)
print("agenda.html: los dos editores ya ofrecen los 4 canales")

# ── 3) migrar los datos ya cargados ─────────────────────────────────────────
url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    if linea.strip().startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")
conn = psycopg2.connect(url)
conn.autocommit = True
cur = conn.cursor()

print()
print("=== ANTES ===")
cur.execute("select canal, count(*) from citas group by canal")
print("  citas:", cur.fetchall())
cur.execute("select canal, nombre from usuarios")
print("  usuarios:", cur.fetchall())

cur.execute("""update citas set canal='Agente IA'
                where canal in ('WhatsApp', 'Agente virtual')""")
print("citas -> Agente IA:", cur.rowcount)
cur.execute("update citas set canal='Asesor' where canal='Call Center'")
print("citas -> Asesor:", cur.rowcount)
cur.execute("""update usuarios set canal='Agente IA'
                where canal in ('WhatsApp', 'Agente virtual')""")
print("usuarios -> Agente IA:", cur.rowcount)
cur.execute("update usuarios set canal='Asesor' where canal='Call Center'")
print("usuarios -> Asesor:", cur.rowcount)

print()
print("=== DESPUES ===")
cur.execute("select canal, count(*) from citas group by canal")
print("  citas:", cur.fetchall())
cur.execute("select canal, nombre from usuarios")
print("  usuarios:", cur.fetchall())
conn.close()

import py_compile
py_compile.compile(BASE + "agenda_helper.py", doraise=True)
print()
print("sintaxis OK: agenda_helper.py")