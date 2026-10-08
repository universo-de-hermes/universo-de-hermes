#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Habla con Pepe DE VERDAD: el modelo real, el prompt real, las
herramientas reales. Solo preguntas de lectura: no agenda nada.

  cd /root/universo/recepcionista && ./venv/bin/python verify_pepe_live.py
"""
import asyncio
import os
import sys

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import main as m  # noqa: E402

PREGUNTAS = [
    ("El Dr. Cueter", "¿El Dr. Cueter atiende el miércoles en Medellín? "
                      "¿A qué horas tiene cupo?"),
    ("La doctora Arias", "Quiero que me atienda la doctora Arias para "
                         "remoción de micropigmentación en Medellín. "
                         "¿Qué horas tiene el miércoles?"),
    ("Valentina + remoción", "¿Puedo hacerme la remoción de micropigmentación "
                             "con Valentina en El Tesoro?"),
]


async def main():
    fallas = []
    for titulo, pregunta in PREGUNTAS:
        print("\n" + "=" * 74)
        print("CLIENTE: %s" % pregunta)
        print("-" * 74)
        try:
            r = await m.ask_pepe(pregunta, history=[], telefono="3012466958",
                                 client_id=25)
        except Exception as e:
            print("  ERROR: %s" % e)
            fallas.append(titulo)
            continue
        print("PEPE: %s" % r)

        bajo = m.re.sub(r"\s+", " ", r.lower())
        if titulo == "El Dr. Cueter":
            # tiene que reconocerlo y hablar de su horario real
            ok = ("cueter" in bajo and
                  ("no tengo" not in bajo and "no está" not in bajo and
                   "no encuentro" not in bajo))
            detalle = "lo reconoce y da su horario real"
        elif titulo == "La doctora Arias":
            ok = ("arias" in bajo and "no tengo" not in bajo and
                  "no está" not in bajo)
            detalle = "reconoce a la doctora Arias"
        else:
            # Valentina NO hace remoción: debe decirlo y ofrecer a quien sí
            ok = (("no" in bajo and ("remoción" in bajo or "remocion" in bajo))
                  and ("cueter" in bajo or "arias" in bajo))
            detalle = "avisa que Valentina no hace remoción y ofrece a quien sí"
        print("  %s %s" % ("OK  " if ok else "REVISAR", detalle))
        if not ok:
            fallas.append(titulo)

    print("\n" + "=" * 74)
    print("RESUMEN: %d de %d conversaciones bien" % (len(PREGUNTAS) - len(fallas),
                                                     len(PREGUNTAS)))
    for f in fallas:
        print("  REVISAR: %s" % f)
    print("=" * 74)
    return 1 if fallas else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
