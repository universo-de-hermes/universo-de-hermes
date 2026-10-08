#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pepe pasa a trabajar con DeepSeek V4 Pro (OpenRouter).

  PRIMARIO:  deepseek/deepseek-v4-pro   (1M contexto, buen uso de herramientas)
  RESPALDO:  openai/gpt-4o-mini         (si DeepSeek falla, Pepe no se queda mudo)

De paso se arreglan los comentarios, que decian "DeepSeek V4 Flash - primario"
y "Cliente OpenRouter (fallback)" cuando el principal era gpt-4o-mini.
"""
import os
import shutil

MP = "/root/universo/recepcionista/main.py"
b = MP + ".pre-modelo.bak"
if not os.path.exists(b):
    shutil.copy2(MP, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(MP, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")

VIEJO = '''# ── Cliente OpenRouter (fallback) ──
ai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://cjmedical.com",
        "X-Title": "CJ Medical - Recepcionista Pepe",
    },
)

# ── Cliente OpenRouter (DeepSeek V4 Flash - primario) ──
# Anthropic deshabilitado por falta de créditos
anthropic_client = None

# ── Selección de modelo ──
PRIMARY_MODEL = "gpt-4o-mini"
FALLBACK_MODEL = "openai/gpt-4o-mini"
'''

NUEVO = '''# ── Cliente OpenRouter (el único proveedor que se usa) ──
ai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://cjmedical.com",
        "X-Title": "CJ Medical - Recepcionista Pepe",
    },
)

# Anthropic quedó deshabilitado (sin créditos) y ya nadie lo usa.
anthropic_client = None

# ── Selección de modelo ──
# PRIMARIO: DeepSeek V4 Pro por OpenRouter (1M de contexto y buen manejo de
# herramientas). Es más lento que gpt-4o-mini —unos 12 s por vuelta— pero se
# equivoca menos, que es de donde venían casi todos los enredos.
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
print("  ok comentarios corregidos")
