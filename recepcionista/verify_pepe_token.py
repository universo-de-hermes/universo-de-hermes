#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba de fuego con el MISMO orden que main.py:

  1. se importa agenda_helper (antes de load_dotenv)  -> token vacio al importar
  2. load_dotenv()                                    -> main.py linea 40
  3. se llama la agenda                               -> ahora SI debe mandar token
"""
import asyncio
import sys

sys.path.insert(0, "/root/universo/recepcionista")

import agenda_helper as ag            # noqa: E402  (import ANTES de load_dotenv)

print("token al importar el modulo:", repr(ag.API_TOKEN))

from dotenv import load_dotenv        # noqa: E402
load_dotenv()                          # main.py hace esto despues del import

print("token despues de load_dotenv:", repr(ag.API_TOKEN))
cab = ag._cabeceras()
print("cabeceras:", {k: (v[:10] + "..." if k == "X-API-Token" else v)
                     for k, v in cab.items()})
print("manda el token:", "X-API-Token" in cab)

print()
print("=== GET /datos (lo que daba 401) ===")
d = asyncio.run(ag.datos(refrescar=True))
print("   estados:", len(d.get("estados", [])),
      "| sedes:", len(d.get("sedes", [])),
      "| servicios:", len(d.get("servicios", [])),
      "| especialistas:", len(d.get("especialistas", [])))

print()
print("=== HERRAMIENTA ver_horas_libres (la que fallo en la conversacion) ===")
import herramientas                   # noqa: E402
r = asyncio.run(herramientas.ejecutar("ver_horas_libres", {
    "servicio": "Terapia de Revitalización",
    "sede": "El Tesoro",
    "fecha": "2026-09-21"}))
print("   ok:", r.get("ok"))
print("   respuesta:", str(r)[:600])
