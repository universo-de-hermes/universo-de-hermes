#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Por que a veces Pepe contesta VACIO.

Con DeepSeek V4 Pro (modelo de razonamiento) la respuesta vuelve sin texto.
Aqui se ve el response crudo de la API: finish_reason, uso de tokens y si
trae campo de razonamiento.

  cd /root/universo/recepcionista && ./venv/bin/python diagnosticar_vacio.py
"""
import asyncio
import json
import os
import sys

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import httpx                        # noqa: E402
from dotenv import load_dotenv      # noqa: E402

load_dotenv(os.path.join(BASE, ".env"))
import main as m                    # noqa: E402
import herramientas as h            # noqa: E402

CLAVE = os.getenv("OPENROUTER_API_KEY")

# el turno exacto que salio vacio: el cliente acaba de confirmar el resumen
HISTORIA = [
    {"role": "user", "content": "Hola, quiero agendar una cita"},
    {"role": "assistant", "content": "¡Hola! ¿Desde qué ciudad nos estás contactando: Bogotá o Medellín?"},
    {"role": "user", "content": "Medellín"},
    {"role": "assistant", "content": "Perfecto. En Medellín estamos en el C.C. El Tesoro. ¿Qué servicio te gustaría agendar?"},
    {"role": "user", "content": "Botox"},
    {"role": "assistant", "content": "El Botox está disponible en El Tesoro con nuestros médicos. ¿Para qué fecha?"},
    {"role": "user", "content": "El sábado 26 de septiembre a las 10 de la mañana"},
    {"role": "assistant", "content": "La hora queda apartada. Para continuar necesito tu número de cédula."},
    {"role": "user", "content": "1069467531"},
    {"role": "assistant", "content": "Ya te tengo en el sistema. ¿Están correctos tus datos o quieres actualizar algo?"},
    {"role": "user", "content": "Sí, están correctos"},
    {"role": "assistant", "content": "Antes de agendar, confirma: Ciudad Medellín, Sede El Tesoro, Servicio Botox, Fecha 26 de septiembre, Hora 10:00. ¿Todos estos datos están correctos?"},
    {"role": "user", "content": "Perfecto, gracias"},
]

MENSAJES = [{"role": "system", "content": m.prompt_de_hoy()}] + HISTORIA

for max_tok in (1200, 4000):
    print("\n" + "=" * 74)
    print("PRUEBA con max_tokens=%d" % max_tok)
    print("=" * 74)
    r = httpx.post("https://openrouter.ai/api/v1/chat/completions",
                   headers={"Authorization": "Bearer " + CLAVE},
                   json={"model": m.PRIMARY_MODEL, "messages": MENSAJES,
                         "tools": h.HERRAMIENTAS, "tool_choice": "auto",
                         "max_tokens": max_tok, "temperature": 0.7},
                   timeout=240)
    if r.status_code != 200:
        print("  FALLA %s: %s" % (r.status_code, r.text[:300]))
        continue
    j = r.json()
    ch = j["choices"][0]
    msg = ch["message"]
    print("  finish_reason : %s" % ch.get("finish_reason"))
    print("  uso           : %s" % json.dumps(j.get("usage"), ensure_ascii=False))
    print("  content       : %r" % (msg.get("content") or "")[:200])
    print("  tool_calls    : %s" % [t["function"]["name"]
                                    for t in (msg.get("tool_calls") or [])])
    print("  campos extra  : %s" % [k for k in msg.keys()
                                    if k not in ("role", "content", "tool_calls")])
    for k in ("reasoning", "reasoning_content", "reasoning_details"):
        if msg.get(k):
            v = msg[k]
            print("  %s: %s" % (k, str(v)[:150]))
