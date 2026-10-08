#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
`reasoning` tiene que ir por `extra_body`.

Error que salio:
    Completions.create() got an unexpected keyword argument 'reasoning'

El SDK de OpenAI (que usamos apuntando a OpenRouter) solo acepta sus propios
argumentos. Los parametros del proveedor van dentro de `extra_body`. Como se
pasaba directo, la llamada al modelo PRINCIPAL reventaba en cada turno y todo
se iba por el respaldo (gpt-4o-mini) sin que se notara.

De paso se limpian las reservas que dejaron las pruebas anteriores: una hora
apartada por una corrida previa hacia fallar la siguiente con CUPO_APARTADO.
"""
import os
import shutil
import subprocess

MP = "/root/universo/recepcionista/main.py"
b = MP + ".pre-extra-body.bak"
if not os.path.exists(b):
    shutil.copy2(MP, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(MP, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

VIEJO = '''            extra = {"reasoning": REASONING} if REASONING else {}
            resp = ai_client.chat.completions.create(
                model=PRIMARY_MODEL, messages=messages,
                tools=HERRAMIENTAS, tool_choice="auto",
                max_tokens=3000, temperature=0.7, **extra)'''

NUEVO = '''            # `reasoning` NO va como argumento normal: el SDK de OpenAI no lo
            # conoce y lanza «unexpected keyword argument». Los parametros
            # propios de OpenRouter se mandan por `extra_body`. Si se pasa
            # directo, TODAS las llamadas al modelo principal fallan y el bot
            # se va en silencio por el respaldo.
            extra = ({"extra_body": {"reasoning": REASONING}}
                     if REASONING else {})
            resp = ai_client.chat.completions.create(
                model=PRIMARY_MODEL, messages=messages,
                tools=HERRAMIENTAS, tool_choice="auto",
                max_tokens=3000, temperature=0.7, **extra)'''

if t.count(VIEJO) != 1:
    raise SystemExit("  X ancla no encontrada (%d)" % t.count(VIEJO))
t = t.replace(VIEJO, NUEVO)
print("  ok `reasoning` va por extra_body")

if crlf:
    t = t.replace("\n", "\r\n")
with open(MP, "w", encoding="utf-8", newline="") as f:
    f.write(t)

# limpiar reservas que dejaron las pruebas
p = subprocess.run(["su", "postgres", "-c",
                    'psql -d cjmedical -c "select count(*) as reservas_vivas '
                    'from reservas; delete from reservas;"'],
                   capture_output=True, text=True, timeout=30)
print("  reservas de prueba limpiadas:")
for linea in (p.stdout or "").strip().splitlines():
    print("    %s" % linea)
