#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pepe pasa a Mistral Medium 3.1: mejor que DeepSeek V4 Pro en lo medible.

Medido con el flujo real de Pepe (prompt real + 12 herramientas, 6 casos que
antes fallaban), dos corridas:

    mistral-medium-3.1   6/6 y 6/6   2.1 s promedio   <- el unico consistente
    claude-haiku-4.5     6/6 y 4/6   3.2 s
    deepseek-v4-pro      6/6 y 5/6  12.0 s
    gpt-4o-mini          5/6 y 6/6   1.7 s
    qwen3.8-flash        6/6        14.4 s
    gpt-4.1-mini         5/6         2.2 s

Con DeepSeek V4 Pro se pagaban 12 s por respuesta para acertar lo mismo.
RESPALDO sigue siendo gpt-4o-mini (barato y probado).
"""
import os
import shutil

MP = "/root/universo/recepcionista/main.py"
b = MP + ".pre-mistral.bak"
if not os.path.exists(b):
    shutil.copy2(MP, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(MP, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

VIEJO = '''# ── Selección de modelo ──
# PRIMARIO: DeepSeek V4 Pro por OpenRouter (1M de contexto y buen manejo de
# herramientas). Es más lento que gpt-4o-mini —unos 12 s por vuelta— pero se
# equivoca menos, que es de donde venían casi todos los enredos.
PRIMARY_MODEL = "deepseek/deepseek-v4-pro"
# RESPALDO: si DeepSeek falla o está saturado, Pepe sigue contestando con
# gpt-4o-mini en vez de quedarse mudo.
FALLBACK_MODEL = "openai/gpt-4o-mini"
'''

NUEVO = '''# ── Selección de modelo ──
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

if t.count(VIEJO) != 1:
    raise SystemExit("X ancla no encontrada (%d veces)" % t.count(VIEJO))
t = t.replace(VIEJO, NUEVO)

if crlf:
    t = t.replace("\n", "\r\n")
with open(MP, "w", encoding="utf-8", newline="") as f:
    f.write(t)

print("  ok PRIMARY_MODEL  = mistralai/mistral-medium-3.1")
print("  ok FALLBACK_MODEL = openai/gpt-4o-mini")
