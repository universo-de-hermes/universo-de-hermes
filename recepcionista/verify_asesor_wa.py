#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba que una respuesta de ASESOR desde el CRM sale por WhatsApp.

Antes se quedaba en silencio: la rama de WhatsApp dependía del cliente viejo
de Playwright/EvolutionAPI, que está apagado.

  cd /root/universo/recepcionista && ./venv/bin/python verify_asesor_wa.py
"""
import asyncio
import os
import sys

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import main as m                                  # noqa: E402
from crm.database import get_connection           # noqa: E402

WA = "573015001772"
CID = None


class _Bot:
    async def send_message(self, chat_id=None, text=None):
        print("      (Telegram llamado con %s)" % chat_id)
        raise RuntimeError("no hay Telegram en este cliente")


class _App:
    bot = _Bot()


def limpiar():
    if not CID:
        return
    con = get_connection()
    con.execute("DELETE FROM pending_replies WHERE client_id = ?", (CID,))
    con.execute("DELETE FROM messages WHERE client_id = ?", (CID,))
    con.execute("DELETE FROM clients WHERE id = ?", (CID,))
    con.commit()
    con.close()
    print("  limpieza: ficha de prueba borrada")


async def principal():
    global CID
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO clients (whatsapp_id, name, phone, status, channel) "
                "VALUES (?, ?, ?, 'en_conversacion', 'whatsapp')",
                (WA, "Prueba Asesor", "3015001772"))
    CID = cur.lastrowid
    cur.execute("INSERT INTO pending_replies (client_id, content, advisor_name) "
                "VALUES (?, ?, ?)",
                (CID, "Hola, le escribe Ana de CJ Medical. ¿En qué le ayudo?",
                 "Ana"))
    con.commit()
    con.close()
    print("  ficha de prueba creada (id %s, canal whatsapp, celular 3015001772)" % CID)

    print("\n  --- corriendo la tarea de respuestas pendientes ---")
    await m.send_pending_replies(_App())

    con = get_connection()
    fila = con.execute("SELECT sent FROM pending_replies WHERE client_id = ?",
                       (CID,)).fetchone()
    enviado = dict(fila)["sent"] if fila else None
    con.close()

    print("\n" + "=" * 72)
    if enviado == 1:
        print("RESULTADO: la respuesta salio (WhatsApp configurado)")
    else:
        print("RESULTADO: NO salio todavia (enviado=%s)" % enviado)
        print("  -> Revisa el log: si dice «WhatsApp sin configurar: faltan")
        print("     WA_TOKEN, WA_PHONE_ID» es que el camino YA es el correcto")
        print("     y solo faltan las credenciales. Antes del arreglo no decia")
        print("     NADA: se quedaba muda.")
    print("=" * 72)


if __name__ == "__main__":
    try:
        asyncio.run(principal())
    finally:
        limpiar()
