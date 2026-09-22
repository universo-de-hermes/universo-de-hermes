#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arregla la causa raiz de que "Quien agenda" diga "Sin registrar".

Cadena del problema:
 1. La pagina pedia las citas del mes con  hasta = mes + "-31".
    Septiembre (y abril, junio, noviembre) no tienen 31 dias, asi que la API
    respondia: date/time field value out of range "2026-09-31".
 2. El adaptador de la pagina se traga ese error en silencio y devuelve las
    citas que ya tenia en cache del dia (store.citas).
 3. Esas citas vienen del endpoint del dia (agenda_dia), que devolvia una lista
    de columnas SIN asignada_por ni creado_por. Resultado: el reporte no sabia
    quien agendo -> "Sin registrar".

Arreglo:
 A. agenda_dia tambien devuelve asignada_por y creado_por.
 B. La pagina calcula el ultimo dia real del mes en vez de asumir 31.
"""
import io
import sys

API = "/root/universo/agenda/agenda_api.py"
HTML = "/var/www/html/agenda.html"

# ── A) API: el endpoint del dia tambien manda quien agendo ───────────────────
api = io.open(API, encoding="utf-8").read()
viejo_a = """                    estado_id, estado as estado_nombre, estado_tipo,
                    color as estado_color
               from v_agenda where fecha=%s\"\"\""""
nuevo_a = """                    estado_id, estado as estado_nombre, estado_tipo,
                    color as estado_color, asignada_por, creado_por
               from v_agenda where fecha=%s\"\"\""""
n = api.count(viejo_a)
print("A) agenda_dia -> %d coincidencia(s)" % n)
if n != 1:
    print("ABORTO: no pude ubicar el select de agenda_dia")
    sys.exit(1)
io.open(API, "w", encoding="utf-8").write(api.replace(viejo_a, nuevo_a))
print("   API: agenda_dia ahora devuelve asignada_por y creado_por")

# ── B) HTML: ultimo dia real del mes ─────────────────────────────────────────
html = io.open(HTML, encoding="utf-8").read()
viejo_b = ('    const snap=await S.db.collection("citas").where("fecha",">=",mes+"-01")'
           '.where("fecha","<=",mes+"-31").limit(400).get();')
nuevo_b = ('    /* Ojo: no todos los meses tienen 31 dias. Pidiendo "-31" en\n'
           '       septiembre la API devolvia error y el reporte caia al cache del\n'
           '       dia, que no sabe quien agendo la cita. */\n'
           '    const ult=String(new Date(+mes.slice(0,4),+mes.slice(5,7),0).getDate()).padStart(2,"0");\n'
           '    const snap=await S.db.collection("citas").where("fecha",">=",mes+"-01")'
           '.where("fecha","<=",mes+"-"+ult).limit(400).get();')
n = html.count(viejo_b)
print("B) cargarMes -> %d coincidencia(s)" % n)
if n != 1:
    print("ABORTO: no pude ubicar la linea de cargarMes")
    sys.exit(1)
io.open(HTML, "w", encoding="utf-8").write(html.replace(viejo_b, nuevo_b))
print("   HTML: el mes se pide hasta su ultimo dia real")
print("LISTO")
