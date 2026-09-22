#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reproduce el fallo exacto y comprueba que ya no pasa.

Antes el modelo mandaba «Valentina Baquero» como especialista_id y la agenda
respondia 500. Ahora se manda el NOMBRE y el dispatcher lo resuelve.
"""
import asyncio
import sys

sys.path.insert(0, "/root/universo/recepcionista")
from dotenv import load_dotenv     # noqa: E402
load_dotenv()

import agenda_helper as ag         # noqa: E402
import herramientas                # noqa: E402


async def main():
    print("=== 1) RESOLVER CON NOMBRES (antes reventaba) ===")
    rc = await herramientas._resolver_cita({
        "especialista": "Valentina Baquero",
        "sede": "El Tesoro",
        "servicio": "Carbon Peel"})
    print("   ", rc)

    print()
    print("=== 2) RESOLVER EL CLIENTE POR CÉDULA ===")
    rcl = await herramientas._resolver_cliente(
        {"documento": "1069467531"}, {"telefono": ""})
    print("   ", rcl)

    print()
    print("=== 3) APARTAR UNA HORA (crea una reserva temporal) ===")
    if rc.get("ok") and rcl.get("ok"):
        r = await ag.apartar_cupo(
            especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],
            fecha="2026-09-22", hora="15:00",
            servicio_id=rc["servicio_id"], minutos=2,
            referencia="prueba-hermes")
        print("   apartar:", r)
        if r.get("ok") and r.get("reserva"):
            print("   soltando la reserva...")
            print("   soltar:", await ag.soltar_cupo(r["reserva"]))

    print()
    print("=== 4) QUE DEVUELVE SI FALTA LA ESPECIALISTA ===")
    print("   ", await herramientas._resolver_cita({
        "sede": "El Tesoro", "servicio": "Carbon Peel"}))

    print()
    print("=== 5) ESPECIALISTA QUE NO EXISTE ===")
    print("   ", await herramientas._resolver_cita({
        "especialista": "Pepito Pérez", "sede": "El Tesoro",
        "servicio": "Carbon Peel"}))


asyncio.run(main())