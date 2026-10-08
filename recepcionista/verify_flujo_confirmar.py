#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba del flujo arreglado: confirmar sin cita_id + regla de días +
la tarjeta del CRM."""
import asyncio
import sys

sys.path.insert(0, "/root/universo/recepcionista")
from dotenv import load_dotenv     # noqa: E402
load_dotenv()

import herramientas                # noqa: E402
from crm.database import update_client_status, get_client_detail  # noqa: E402


def correr(h, args, ctx=None):
    return asyncio.run(herramientas.ejecutar(h, args, ctx))


print("=== 1) REGLA DE DÍAS (_dias_hasta) ===")
for f in ("2026-09-22", "2026-09-23", "2026-09-24", "2026-09-30", "malo"):
    print("   %s → %s días" % (f, herramientas._dias_hasta(f)))
print("   (hoy es 2026-09-22) → 0 y 1 = confirmada sola; 2+ = pendiente")

print()
print("=== 2) RESOLVER LA CITA CON SOLO LA CÉDULA ===")
r = asyncio.run(herramientas._resolver_cita_id(
    {"documento": "1069467531"}, {"telefono": ""}))
print("   ", r)

print()
print("=== 3) CONFIRMAR CON SOLO LA CÉDULA (esto fallaba) ===")
r = correr("confirmar_cita", {"documento": "1069467531"})
print("   ", r)

print()
print("=== 4) SIN CITA_ID INVENTADO ===")
r = correr("confirmar_cita", {"cita_id": "c_inventado_123"})
print("   ", r)

print()
print("=== 5) LA TARJETA DEL CRM ===")
c = get_client_detail(23)
print("   antes: ", c.get("name"), "|", c.get("status"))
update_client_status(23, "agendado", "Pepe Bot", "Cita agendada en la agenda")
c = get_client_detail(23)
print("   ahora: ", c.get("name"), "|", c.get("status"))
