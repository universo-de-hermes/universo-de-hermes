#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica las capacidades nuevas de Pepe."""
import asyncio
import json
import sys

sys.path.insert(0, "/root/universo/recepcionista")
from dotenv import load_dotenv     # noqa: E402
load_dotenv()

import herramientas                # noqa: E402


def correr(herramienta, args):
    r = asyncio.run(herramientas.ejecutar(herramienta, args))
    print(json.dumps(r, ensure_ascii=False, indent=2)[:900])
    return r


print("=" * 66)
print("1) BUSCAR POR CÉDULA (la que existe: 1069467531)")
correr("buscar_cliente", {"documento": "1069467531"})

print("=" * 66)
print("2) BUSCAR POR CÉDULA QUE NO EXISTE (9999999999)")
correr("buscar_cliente", {"documento": "9999999999"})

print("=" * 66)
print("3) BUSCAR SIN DOCUMENTO (usa el teléfono del chat)")
correr("buscar_cliente", {"telefono": "3012466958"})

print("=" * 66)
print("4) ¿VALENTINA TRABAJA EL LUNES 21?")
correr("ver_agenda_especialista", {"especialista": "Valentina", "fecha": "2026-09-21"})

print("=" * 66)
print("5) ¿VALENTINA TRABAJA EL DOMINGO 20? (no debe trabajar)")
correr("ver_agenda_especialista", {"especialista": "Valentina", "fecha": "2026-09-20"})

print("=" * 66)
print("6) ¿CUÁNDO TRABAJA VALENTINA? (sin fecha, próximos días)")
correr("ver_agenda_especialista", {"especialista": "Valentina", "dias": 4})

print("=" * 66)
print("7) ESPECIALISTA QUE NO EXISTE")
correr("ver_agenda_especialista", {"especialista": "Pepito Pérez", "fecha": "2026-09-21"})
