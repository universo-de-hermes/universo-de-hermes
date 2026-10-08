#!/usr/bin/env python3
"""Hace un agendamiento POR EL CAMINO DE PEPE (agenda_helper, canal 'Agente IA')
para comprobar en el indicador. Cliente de prueba: Juan Jose Otero."""
import asyncio, io, os, sys

# ── el entorno de Pepe (su .env) ─────────────────────────────────────────
for linea in io.open("/root/universo/recepcionista/.env", encoding="utf-8"):
    linea = linea.strip()
    if not linea or linea.startswith("#") or "=" not in linea:
        continue
    k, v = linea.split("=", 1)
    os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
sys.path.insert(0, "/root/universo/recepcionista")
import agenda_helper as ag          # noqa: E402

DOC = "1069467531"                  # cliente de prueba (Juan Jose Otero)
TELEFONO = "3012466958"
CIUDAD = "Medellín"
SERVICIOS = ["Consulta médica", "1 sesión zona M", "Terapias de Revitalización",
             "Toxina - Botox", "1 sesión zona L"]


async def main():
    print("=== 1. el cliente ===")
    r = await ag.buscar_cliente(documento=DOC)
    print("   ", r.get("ok"), [(c["id"], c.get("nombre") or c.get("primer_nombre"))
                              for c in (r.get("clientes") or [])][:3])
    if not r.get("ok") or not r.get("clientes"):
        print("   NO lo encontre:", r.get("mensaje")); return
    cid = r["clientes"][0]["id"]

    print("\n=== 2. horas libres (por nombre, como Pepe) ===")
    elegido = None
    for srv in SERVICIOS:
        h = await ag.horas_libres(srv, CIUDAD, dias=10)
        if not h.get("ok"):
            print("   %-28s -> %s" % (srv, h.get("mensaje") or h.get("error")))
            continue
        dias = h.get("dias") or []
        if not dias:
            print("   %-28s -> sin horas" % srv); continue
        d0 = dias[0]
        print("   %-28s -> %s (%s min) | primer día %s con %d hora(s)"
              % (srv, h.get("servicio"), h.get("duracion"), d0["fecha"], len(d0["horas"])))
        elegido = (h, d0)
        break
    if not elegido:
        print("   NO hay horas en ningun servicio (eso explicaria el problema)"); return
    h, d0 = elegido
    hora = d0["horas"][0]
    print("   ESCOJO: %s | %s | %s | %s" % (h["servicio"], d0["fecha"], hora["hora"], hora["especialista"]))

    print("\n=== 3. apartar el cupo (Pepe aparta 5 min) ===")
    r = await ag.apartar_cupo(hora["especialista_id"], h["sede_id"], d0["fecha"],
                              hora["hora"], h["servicio_id"], referencia=TELEFONO)
    print("   ", r)
    reserva = r.get("reserva")

    print("\n=== 4. AGENDAR (canal 'Agente IA', por 'Pepe') ===")
    r = await ag.agendar(cid, hora["especialista_id"], h["sede_id"], d0["fecha"],
                         hora["hora"], h["servicio_id"], reserva=reserva,
                         referencia=TELEFONO, notas="Prueba de Pepe (Hermes)")
    print("   ", r)
    if r.get("ok"):
        c = r.get("cita") or {}
        print("\n   ✅ AGENDADA: %s %s %s | canal %s | %s"
              % (c.get("fecha"), c.get("hora"), c.get("servicio"),
                 c.get("canal"), c.get("especialista")))
    else:
        print("\n   ❌ NO se pudo agendar:", r.get("mensaje") or r.get("error"))

asyncio.run(main())
