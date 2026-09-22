#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica que las horas ofrecidas sean solo en punto o y media."""
import asyncio
import sys

sys.path.insert(0, "/root/universo/recepcionista")
from dotenv import load_dotenv     # noqa: E402
load_dotenv()

import herramientas                # noqa: E402

casos = [
    ("Carbon peel", "El Tesoro"),                 # 60 min
    ("Terapias de Revitalización", "El Tesoro"),  # 45 min
    ("Depilación láser zona M", "El Tesoro"),     # 30 min
]

for servicio, sede in casos:
    r = asyncio.run(herramientas.ejecutar("ver_horas_libres", {
        "servicio": servicio, "sede": sede, "dias": 2}))
    print("=" * 62)
    print("SERVICIO:", servicio, "| SEDE:", sede)
    if not r.get("ok"):
        print("   ERROR:", r)
        continue
    print("   resuelto como:", r.get("servicio"), "| duración:", r.get("duracion"), "min")
    malas = 0
    for dia in r.get("dias", []):
        horas = [h["hora"] for h in dia["horas"]]
        fuera = [h for h in horas if h[-2:] not in ("00", "30")]
        malas += len(fuera)
        print("   %s (%s): %s" % (dia["fecha"], len(horas), ", ".join(horas) if horas else "sin cupo"))
        if fuera:
            print("      >>> FUERA DE LA REGLA:", fuera)
    print("   horas que no son :00/:30 ->", malas)
