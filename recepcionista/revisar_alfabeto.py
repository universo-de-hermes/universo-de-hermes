#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detecta si un modelo se equivoca de alfabeto.

Un modelo multilingue a veces mete una palabra en otro alfabeto en medio de
una respuesta en espanol: «solo la реалиzan los medicos». El cliente lo ve y
queda fatal. Esto lo mide con respuestas reales.

  cd /root/universo/recepcionista && ./venv/bin/python revisar_alfabeto.py [veces]
"""
import asyncio
import os
import re
import sys
import time

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import main as m  # noqa: E402

# cirilico, griego, hebreo, arabe, devanagari, CJK, hangul, tailandes
OTROS = re.compile(r"[\u0400-\u04FF\u0370-\u03FF\u0590-\u05FF\u0600-\u06FF"
                   r"\u0900-\u097F\u4E00-\u9FFF\u3040-\u30FF\uAC00-\uD7AF"
                   r"\u0E00-\u0E7F]")

MENSAJES = [
    "Hola, quiero agendar una cita",
    "¿Qué servicios tienen?",
    "¿Cuánto vale la depilación láser?",
    "¿Puedo hacerme la remoción de micropigmentación con Valentina en El Tesoro?",
    "¿Quién hace el botox en Medellín?",
    "¿El Dr. Cueter trabaja los sábados?",
    "Quiero cita para hidrafacial el sábado a las 10",
    "¿Tienen sede en Bogotá?",
    "Me duele la ceja después del procedimiento",
    "¿Cuántas sesiones de micropigmentación necesito?",
    "¿Atienden los domingos?",
    "Quiero cancelar mi cita del 26 de septiembre",
]


async def principal():
    veces = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    revisadas = 0
    sucias = []

    for vuelta in range(veces):
        if veces > 1:
            print("\n--- vuelta %d de %d ---" % (vuelta + 1, veces))
        for msg in MENSAJES:
            t0 = time.time()
            try:
                r = await m.ask_pepe(msg, history=[], telefono="3012466958",
                                     client_id=None)
            except Exception as e:
                r = "ERROR: %s" % e
            dt = time.time() - t0
            revisadas += 1
            malos = OTROS.findall(r or "")
            if malos:
                sucias.append((msg, r, malos))
            print("  %s %5.1fs  %s" % ("SUCIA" if malos else "ok   ", dt,
                                       msg[:52]))

    print("\n" + "=" * 72)
    print("RESULTADO: %d respuestas revisadas | %d con otro alfabeto"
          % (revisadas, len(sucias)))
    print("=" * 72)
    for msg, r, malos in sucias:
        print("\n  PREGUNTA:   %s" % msg)
        print("  CARACTERES: %s" % " ".join(sorted(set(malos))))
        i = OTROS.search(r).start()
        print("  RESPUESTA:  ...%s..." % r[max(0, i - 70):i + 70].replace("\n", " "))
    return len(sucias)


if __name__ == "__main__":
    sys.exit(0 if asyncio.run(principal()) == 0 else 1)
