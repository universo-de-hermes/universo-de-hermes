#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tercer bug del canal: la API devuelve el usuario con la columna `id`, pero la
pagina lo busca por `userId`, que no existe. Por eso `aplicarRol()` nunca
encontraba a la persona y dejaba el canal por defecto: TODA cita salia como
"Recepcionista", sin importar el canal del perfil.

Se arreglan tres cosas:
 1. aplicarRol(): acepta userId o id  -> el canal de la persona se aplica y las
    citas nuevas quedan bien marcadas.
 2. aliasDe(): igual, y usa el nombre como respaldo.
 3. Reporte "Quien agenda": encuentra el perfil y muestra el canal del PERFIL
    (que es el canal de la persona); el desglose por cita ya lo muestra el
    panel "Canal que asigna".
Ademas corrige la cita que quedo mal marcada por este bug.
"""
import io
import sys

import psycopg2

HTML = "/var/www/html/agenda.html"
ENV = "/root/universo/agenda/.api_env"

s = io.open(HTML, encoding="utf-8").read()

cambios = [
    # 1) aplicarRol: aceptar userId o id
    ("  const u=S.usuarios.find(x=>x.userId&&x.userId===S.uid&&x.activo!==false);",
     "  /* La API manda `id`; la pagina busca `userId`. Hay que aceptar los dos o\n"
     "     nunca encuentra a la persona y deja el canal por defecto. */\n"
     "  const u=S.usuarios.find(x=>(x.userId||x.id)===S.uid&&x.activo!==false);"),
    # 2) aliasDe
    ('const aliasDe=id=>{const u=S.usuarios.find(x=>x.userId===id);return u?u.alias:"";};',
     'const aliasDe=id=>{const u=S.usuarios.find(x=>(x.userId||x.id)===id);\n'
     '  return u?(u.alias||u.nombre||""):"";};'),
    # 3a) el perfil de la persona en el reporte
    ("      const reg=S.usuarios.find(x=>x.userId===k);",
     "      const reg=S.usuarios.find(x=>(x.userId||x.id)===k);"),
    # 3b) canal del perfil primero (el de la cita queda de respaldo)
    ('        canalTop||(reg&&reg.canal)||"—",',
     '        (reg&&reg.canal)||canalTop||"—",'),
    # 3c) el nombre tambien como respaldo
    ("          /^u[-_]/.test(k)?nombrePersona(k,reg&&reg.alias):(k===\"—\"?\"Sin registrar\":k)),",
     "          /^u[-_]/.test(k)?nombrePersona(k,reg&&(reg.alias||reg.nombre)):(k===\"—\"?\"Sin registrar\":k)),"),
]

for i, (viejo, nuevo) in enumerate(cambios, 1):
    n = s.count(viejo)
    print("cambio %d: %d coincidencia(s)" % (i, n))
    if n != 1:
        print("ABORTO en el cambio %d" % i)
        sys.exit(1)
    s = s.replace(viejo, nuevo)

io.open(HTML, "w", encoding="utf-8").write(s)
print("HTML actualizado")

# ── corregir la cita que quedo mal marcada ───────────────────────────────────
url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    if linea.strip().startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")
conn = psycopg2.connect(url)
conn.autocommit = True
cur = conn.cursor()
cur.execute("""update citas set canal='Administrador'
                where asignada_por='u-juan-jose-otero'
                  and canal is distinct from 'Administrador'""")
print("citas corregidas:", cur.rowcount)
cur.execute("select coalesce(canal,'(NULL)'), count(*) from citas group by 1")
print("canales en citas:", cur.fetchall())
conn.close()
print("LISTO")
