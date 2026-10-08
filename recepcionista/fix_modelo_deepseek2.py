#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pepe vuelve a DeepSeek V4 Pro (OpenRouter). Decision del usuario.

De paso se deja anotado lo que se midio, para no repetir la prueba:
  mistral-medium-3.1  6/6 y 6/6   2.1 s   -- pero metio una palabra en cirilico
  deepseek-v4-pro     6/6 y 5/6  12.0 s   -- respuestas limpias, es el elegido
  claude-haiku-4.5    6/6 y 4/6   3.2 s
  gpt-4o-mini         5/6 y 6/6   1.7 s   (queda de respaldo)
"""
import os
import shutil

MP = "/root/universo/recepcionista/main.py"
b = MP + ".pre-deepseek2.bak"
if not os.path.exists(b):
    shutil.copy2(MP, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(MP, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

VIEJO = '''# ── Selección de modelo ──
# PRIMARIO: Mistral Medium 3.1. Se eligió midiendo con el flujo real (prompt
# real + las 12 herramientas, 6 casos que antes fallaban), dos corridas:
#   mistral-medium-3.1  6/6 y 6/6   2.1 s  <- el único consistente
#   claude-haiku-4.5    6/6 y 4/6   3.2 s
#   deepseek-v4-pro     6/6 y 5/6  12.0 s  <- se pagaban 12 s por lo mismo
#   gpt-4o-mini         5/6 y 6/6   1.7 s
# Para re-medir: ./venv/bin/python comparar_modelos.py
PRIMARY_MODEL = "mistralai/mistral-medium-3.1"
# RESPALDO: si Mistral falla o está saturado, Pepe sigue contestando con
# gpt-4o-mini en vez de quedarse mudo.
FALLBACK_MODEL = "openai/gpt-4o-mini"
'''

NUEVO = '''# ── Selección de modelo ──
# PRIMARIO: DeepSeek V4 Pro por OpenRouter (1M de contexto). Elegido por el
# jefe. Mide ~12 s por respuesta (es de razonamiento), más lento que
# gpt-4o-mini, pero sus respuestas salen limpias y bien redactadas.
#
# Medido con el flujo real (prompt real + 12 herramientas, 6 casos, 2 corridas)
# para no repetir la prueba — ./venv/bin/python comparar_modelos.py:
#   deepseek-v4-pro     6/6 y 5/6  12.0 s   <- el elegido
#   mistral-medium-3.1  6/6 y 6/6   2.1 s   <- rápido, pero metió una palabra
#                                              en cirílico («реалиzan»)
#   claude-haiku-4.5    6/6 y 4/6   3.2 s
#   gpt-4o-mini         5/6 y 6/6   1.7 s   <- respaldo
PRIMARY_MODEL = "deepseek/deepseek-v4-pro"
# RESPALDO: si DeepSeek falla o está saturado, Pepe sigue contestando con
# gpt-4o-mini en vez de quedarse mudo.
FALLBACK_MODEL = "openai/gpt-4o-mini"
'''

if t.count(VIEJO) != 1:
    raise SystemExit("X ancla no encontrada (%d veces)" % t.count(VIEJO))
t = t.replace(VIEJO, NUEVO)

if crlf:
    t = t.replace("\n", "\r\n")
with open(MP, "w", encoding="utf-8", newline="") as f:
    f.write(t)

print("  ok PRIMARY_MODEL  = deepseek/deepseek-v4-pro")
print("  ok FALLBACK_MODEL = openai/gpt-4o-mini")
