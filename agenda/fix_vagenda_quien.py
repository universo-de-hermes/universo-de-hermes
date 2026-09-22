#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v_agenda no exponia asignada_por ni creado_por, asi que la agenda web nunca
recibia quien agendo la cita y el reporte "Quien agenda" mostraba
"Sin registrar".

Reconstruye la vista desde su definicion real (pg_get_viewdef) y le agrega las
dos columnas AL FINAL del select, que es lo unico que admite
CREATE OR REPLACE VIEW. Nada mas se toca.
"""
import io
import re
import sys

import psycopg2

ENV = "/root/universo/agenda/.api_env"

url = None
for linea in io.open(ENV, encoding="utf-8").read().splitlines():
    linea = linea.strip()
    if linea.startswith("DATABASE_URL"):
        url = linea.split("=", 1)[1].strip().strip('"').strip("'")
if not url:
    print("ABORTO: no encontre DATABASE_URL en " + ENV)
    sys.exit(1)

conn = psycopg2.connect(url)
cur = conn.cursor()
# Sin esto pg_get_viewdef califica los nombres con el esquema y el texto cambia.
cur.execute("SET search_path TO public")

cur.execute("select pg_get_viewdef('v_agenda'::regclass, false)")
vieja = cur.fetchone()[0]

cur.execute("""select column_name from information_schema.columns
                where table_name='v_agenda' order by ordinal_position""")
antes = [r[0] for r in cur.fetchall()]
print("=== COLUMNAS ANTES ===")
print(", ".join(antes))

if "asignada_por" in antes and "creado_por" in antes:
    print("Ya estaba arreglada. No hago nada.")
    sys.exit(0)

io.open("/root/universo/agenda/v_agenda.pre-fix.sql", "w",
        encoding="utf-8").write(vieja)

m = re.search(r"\n\s*FROM\s+", vieja, re.I)
if not m:
    print("ABORTO: no encontre el FROM. Definicion:")
    print(repr(vieja[-400:]))
    sys.exit(1)

nueva = vieja[:m.start()] + ",\n   c.asignada_por, c.creado_por" + vieja[m.start():]

cur.execute("CREATE OR REPLACE VIEW v_agenda AS " + nueva)
conn.commit()

cur.execute("""select column_name from information_schema.columns
                where table_name='v_agenda' order by ordinal_position""")
despues = [r[0] for r in cur.fetchall()]
print()
print("=== COLUMNAS DESPUES ===")
print(", ".join(despues))
print("asignada_por:", "asignada_por" in despues,
      "| creado_por:", "creado_por" in despues)
conn.close()
print("VISTA ACTUALIZADA OK")
