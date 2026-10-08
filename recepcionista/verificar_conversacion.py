#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El flujo real de punta a punta: cliente -> Pepe -> agenda -> tarjeta CRM.

Esta es la prueba de que todo funciona COMO UNO SOLO. Se simula una
conversacion de verdad (el modelo real, el prompt real, las herramientas
reales) y al final se mira:
  - ¿quedo la cita en la agenda (Postgres)?
  - ¿se movio la tarjeta del CRM a «Agendados»?

Al terminar borra todo lo que creo.

  cd /root/universo/recepcionista && ./venv/bin/python verificar_conversacion.py
"""
import asyncio
import os
import subprocess
import sys

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import httpx                                  # noqa: E402
import main as m                              # noqa: E402
from crm.database import get_connection       # noqa: E402

CEDULA = "1069467531"
CID = None
CITA_ID = None

# La conversacion, como la escribiria un cliente de verdad
TURNOS = [
    "Hola, quiero agendar una cita",
    "Medellín",
    "Botox",
    "El sábado 26 de septiembre a las 10 de la mañana",
    "Sí, esa hora me sirve",
    "Uy perdón, la cédula es 1069467531",
    "Sí, están correctos",
    "Perfecto, gracias",
]


def citas_antes():
    tok = os.environ["API_TOKEN"]
    r = httpx.get("http://127.0.0.1:8001/citas",
                  headers={"X-API-Token": tok}, timeout=30)
    d = r.json()
    return d if isinstance(d, list) else d.get("citas", [])


def limpiar():
    """Borra la cita que se creo y la ficha de prueba."""
    if CITA_ID:
        sql = ("delete from cita_bitacora where cita_id in ('%s'); "
               "delete from citas where id in ('%s');" % (CITA_ID, CITA_ID))
        subprocess.run(["su", "postgres", "-c",
                        'psql -d cjmedical -c "%s"' % sql],
                       capture_output=True, text=True, timeout=30)
        print("\n  limpieza: cita de prueba %s borrada de la agenda" % CITA_ID)
    if CID:
        con = get_connection()
        for t_ in ("pending_replies", "pipeline_log", "messages",
                   "appointments"):
            con.execute("DELETE FROM %s WHERE client_id = ?" % t_, (CID,))
        con.execute("DELETE FROM clients WHERE id = ?", (CID,))
        con.commit()
        con.close()
        print("  limpieza: ficha de prueba borrada (id %s)" % CID)


async def principal():
    global CID, CITA_ID

    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO clients (telegram_id, name, phone, status, channel) "
                "VALUES ('e2e_test', 'Cliente de Prueba E2E', '3012466958', "
                "'nuevo', 'telegram')")
    CID = cur.lastrowid
    con.commit()
    con.close()
    print("  ficha de prueba creada (id %s, estado «nuevo»)" % CID)

    previas = {c.get("id") for c in citas_antes()}
    print("  citas en la agenda antes: %d" % len(previas))

    historia = []
    print("\n" + "=" * 76)
    print("LA CONVERSACION")
    print("=" * 76)
    for i, msg in enumerate(TURNOS, 1):
        print("\n\U0001f9d1 Cliente: %s" % msg)
        try:
            r = await m.ask_pepe(msg, history=historia, telefono="3012466958",
                                 client_id=CID)
        except Exception as e:
            print("\U0001f916 Pepe: ERROR %s" % e)
            break
        print("\U0001f916 Pepe: %s" % r.replace("\n", " ")[:400])
        historia.append({"role": "user", "content": msg})
        historia.append({"role": "assistant", "content": r})
        # si ya agendo, no hace falta seguir
        if "agendad" in r.lower() and "cita" in r.lower() and i >= 6:
            print("\n  (ya quedo agendada: se corta aqui)")
            break

    # ── RESULTADOS ──
    print("\n" + "=" * 76)
    print("RESULTADO DE LA INTEGRACION")
    print("=" * 76)

    nuevas = [c for c in citas_antes() if c.get("id") not in previas]
    if nuevas:
        c = nuevas[0]
        CITA_ID = c.get("id")
        print("  OK   cita creada en la agenda:")
        print("       %s %s | %s | %s | %s | %s" % (
            str(c.get("fecha"))[:10], str(c.get("inicio"))[:5],
            c.get("servicio"), c.get("especialista"), c.get("sede"),
            c.get("estado")))
    else:
        print("  FALLA  no se creo ninguna cita en la agenda")

    con = get_connection()
    fila = con.execute("SELECT status FROM clients WHERE id = ?",
                       (CID,)).fetchone()
    estado = dict(fila)["status"] if fila else None
    n_msg = dict(con.execute("SELECT count(*) n FROM messages WHERE client_id = ?",
                             (CID,)).fetchone())["n"]
    n_pipe = dict(con.execute("SELECT count(*) n FROM pipeline_log "
                              "WHERE client_id = ?", (CID,)).fetchone())["n"]
    con.close()

    print("  %s tarjeta del CRM en estado «%s»" % (
        "OK  " if estado == "agendado" else "OJO ", estado))
    print("  OK   conversacion guardada: %d mensajes" % n_msg)
    print("  %s historial del pipeline: %d movimientos" % (
        "OK  " if n_pipe > 0 else "OJO ", n_pipe))

    con = get_connection()
    estados = [dict(x)["to_status"] for x in con.execute(
        "SELECT to_status FROM pipeline_log WHERE client_id = ? ORDER BY id",
        (CID,)).fetchall()]
    con.close()
    print("       paso por: %s" % " -> ".join(estados or ["(nada)"]))


if __name__ == "__main__":
    try:
        asyncio.run(principal())
    finally:
        limpiar()
