#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba un modelo de OpenRouter ANTES de ponerselo a Pepe.

Lo critico no es que converse: es que sepa llamar herramientas y que lo
haga rapido. Un modelo que no soporta function calling deja a Pepe mudo.

  cd /root/universo/recepcionista && ./venv/bin/python probar_modelo.py [modelo]
"""
import json
import os
import sys
import time

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import httpx                       # noqa: E402
from dotenv import load_dotenv     # noqa: E402

load_dotenv(os.path.join(BASE, ".env"))
import herramientas as h           # noqa: E402

CLAVE = os.getenv("OPENROUTER_API_KEY")
URL = "https://openrouter.ai/api/v1/chat/completions"
MODELOS = sys.argv[1:] or ["deepseek/deepseek-v4-pro"]

SYS = ("Eres Pepe, el recepcionista de CJ Medical (clinica de cejas). "
       "Atiendes por chat y agendas citas. Usa las herramientas cuando el "
       "cliente pida algo que las necesite.")


def llamar(modelo, mensajes, con_tools=True, max_tokens=700):
    cuerpo = {"model": modelo, "messages": mensajes,
              "max_tokens": max_tokens, "temperature": 0.7}
    if con_tools:
        cuerpo["tools"] = h.HERRAMIENTAS
        cuerpo["tool_choice"] = "auto"
    t0 = time.time()
    r = httpx.post(URL, headers={"Authorization": "Bearer " + CLAVE},
                   json=cuerpo, timeout=240)
    dt = time.time() - t0
    if r.status_code != 200:
        try:
            msg = (r.json().get("error") or {}).get("message", r.text[:200])
        except Exception:
            msg = r.text[:200]
        return None, dt, "%s %s" % (r.status_code, msg)
    return r.json()["choices"][0]["message"], dt, None


for modelo in MODELOS:
    print("\n" + "=" * 74)
    print("MODELO: %s" % modelo)
    print("=" * 74)

    # 1. conversacion simple
    m, dt, err = llamar(modelo, [{"role": "user",
                                  "content": "Responde solo: listo"}],
                        con_tools=False, max_tokens=20)
    if err:
        print("  1. conversacion      FALLA: %s" % err)
        continue
    print("  1. conversacion      OK (%.1fs) -> %r" % (dt, (m.get("content") or "")[:45]))

    # 2. funcion de herramienta: lo que de verdad importa
    m, dt, err = llamar(modelo, [
        {"role": "system", "content": SYS},
        {"role": "user", "content": "Hola, quiero agendar una cita de botox "
                                    "en Medellin para el sabado"}])
    if err:
        print("  2. herramientas      FALLA: %s" % err)
        continue
    tc = m.get("tool_calls") or []
    if tc:
        nombres = [t["function"]["name"] for t in tc]
        args = tc[0]["function"].get("arguments", "")
        print("  2. herramientas      OK (%.1fs) -> llamo: %s" % (dt, nombres))
        print("       argumentos: %s" % str(args)[:110])
    else:
        print("  2. herramientas      NO LLAMO NINGUNA (%.1fs)" % dt)
        print("       dijo: %r" % (m.get("content") or "")[:130])

    # 3. seguir la instruccion de usar la herramienta correcta
    m, dt, err = llamar(modelo, [
        {"role": "system", "content": SYS},
        {"role": "user", "content": "Necesito saber si el Dr. Cueter atiende "
                                    "el sabado en Medellin"}])
    if err:
        print("  3. herramienta exacta FALLA: %s" % err)
        continue
    tc = m.get("tool_calls") or []
    nombres = [t["function"]["name"] for t in tc]
    bien = "ver_agenda_especialista" in nombres
    print("  3. herramienta exacta %s (%.1fs) -> %s"
          % ("OK" if bien else "DUDOSO", dt, nombres or "ninguna"))
