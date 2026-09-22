#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba de fuego: el bot ya puede leer la agenda?

Se importa agenda_helper IGUAL que lo hace main.py y se llaman las mismas
cosas que fallaban con 401.
"""
import asyncio
import io
import json
import sys

sys.path.insert(0, "/root/universo/recepcionista")
import agenda_helper as ag          # noqa: E402
import herramientas                 # noqa: E402

print("=== CABECERAS QUE MANDA EL BOT ===")
cab = ag._cabeceras()
print("  ", {k: (v[:12] + "..." if k == "X-API-Token" else v) for k, v in cab.items()})
print("   token presente:", "X-API-Token" in cab)

print()
print("=== GET /datos (lo que daba 401) ===")
r = asyncio.run(ag.datos())
print("   ok:", r.get("ok"))
if r.get("ok"):
    d = r.get("datos") or {}
    print("   estados:", len(d.get("estados", [])),
          "| sedes:", len(d.get("sedes", [])),
          "| servicios:", len(d.get("servicios", [])),
          "| especialistas:", len(d.get("especialistas", [])))
else:
    print("   ERROR:", r)

print()
print("=== ESQUEMA DE ver_horas_libres ===")
for t in herramientas.HERRAMIENTAS:
    if t["function"]["name"] == "ver_horas_libres":
        print(json.dumps(t["function"]["parameters"], ensure_ascii=False, indent=2))
