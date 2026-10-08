#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Busca la mejor configuracion para DeepSeek V4 Pro.

Es un modelo de RAZONAMIENTO: "piensa" antes de contestar (459-916 tokens en
las pruebas). Dos problemas:
  1. Si el razonamiento se come el limite de tokens, la respuesta sale VACIA
     y el cliente recibe un mensaje en blanco.
  2. Tarda 12-20 s.

Aqui se prueban las opciones de razonamiento que acepta OpenRouter, a ver si
alguna lo hace mas rapido sin perder calidad.

  cd /root/universo/recepcionista && ./venv/bin/python probar_razonamiento.py
"""
import asyncio
import json
import os
import sys
import time

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import httpx                        # noqa: E402
from dotenv import load_dotenv      # noqa: E402

load_dotenv(os.path.join(BASE, ".env"))
import herramientas as h            # noqa: E402
import main as m                    # noqa: E402

CLAVE = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"

PREGUNTA = "¿Puedo hacerme la remoción de micropigmentación con Valentina en El Tesoro?"

CONFIGS = [
    ("como esta ahora", {"max_tokens": 1200}),
    ("solo subir el limite", {"max_tokens": 3000}),
    ("razonamiento apagado", {"max_tokens": 1200, "reasoning": {"enabled": False}}),
    ("razonamiento bajo", {"max_tokens": 1200, "reasoning": {"effort": "low"}}),
]


async def probar(nombre, extra):
    cuerpo = {"model": m.PRIMARY_MODEL,
              "messages": [{"role": "system", "content": m.prompt_de_hoy()},
                           {"role": "user", "content": PREGUNTA}],
              "tools": h.HERRAMIENTAS, "tool_choice": "auto",
              "temperature": 0.7}
    cuerpo.update(extra)
    t0 = time.time()
    r = httpx.post(URL, headers={"Authorization": "Bearer " + CLAVE},
                   json=cuerpo, timeout=240)
    dt = time.time() - t0
    if r.status_code != 200:
        print("\n  %-22s FALLA %s: %s" % (nombre, r.status_code, r.text[:160]))
        return
    j = r.json()
    ch = j["choices"][0]
    msg = ch["message"]
    uso = j.get("usage", {})
    raz = (uso.get("completion_tokens_details") or {}).get("reasoning_tokens", 0)
    texto = (msg.get("content") or "").strip()
    tools = [t["function"]["name"] for t in (msg.get("tool_calls") or [])]
    print("\n  %-22s %5.1fs | finish: %-11s | razonamiento: %-5s | salida: %s"
          % (nombre, dt, ch.get("finish_reason"), raz,
             ("%d chars" % len(texto)) if texto else "VACIA"))
    print("      herramientas: %s" % (tools or "ninguna"))
    if texto:
        print("      dijo: %s" % texto.replace("\n", " ")[:150])


async def principal():
    print("=" * 78)
    print("DEEPSEEK V4 PRO — opciones de razonamiento")
    print("=" * 78)
    for nombre, extra in CONFIGS:
        await probar(nombre, extra)


if __name__ == "__main__":
    asyncio.run(principal())
