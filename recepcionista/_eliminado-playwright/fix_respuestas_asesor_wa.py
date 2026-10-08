#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Las respuestas de un ASESOR desde el CRM nunca llegaban a WhatsApp.

Por qué:
  1. `send_pending_replies` (main.py) enviaba por WhatsApp usando
     `WHATSAPP_CLIENT`, que es el cliente viejo de Playwright/EvolutionAPI
     y está APAGADO (`WHATSAPP_CLIENT = None`). Así que esa rama nunca
     corría y la respuesta quedaba sin enviar, en silencio.
  2. La consulta ni siquiera traía `whatsapp_id`: solo `telegram_id` y
     `phone`, que no alcanzan para la Cloud API.
  3. El endpoint `/api/clients/{id}/reply` guardaba el mensaje con
     `channel="telegram"` fijo, aunque el cliente hubiera escrito por
     WhatsApp.

Arreglo: el envío real se centraliza en `whatsapp_cloud.py` y lo usan los
dos (el webhook del CRM y la tarea de respuestas pendientes del bot).
"""
import os
import shutil

BASE = "/root/universo/recepcionista"
CAMBIOS = []
CRLF = {}


def leer(p):
    with open(p, encoding="utf-8", newline="") as f:
        bruto = f.read()
    CRLF[p] = "\r\n" in bruto
    if CRLF[p]:
        print("  (aviso) %s usa CRLF" % os.path.basename(p))
    return bruto.replace("\r\n", "\n")


def escribir(p, t):
    if CRLF.get(p):
        t = t.replace("\n", "\r\n")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def respaldar(p):
    b = p + ".pre-asesor-wa.bak"
    if not os.path.exists(b):
        shutil.copy2(p, b)
        print("  respaldo: %s" % os.path.basename(b))


def cambiar(t, viejo, nuevo, etiqueta):
    n = t.count(viejo)
    if n != 1:
        raise SystemExit("  X ancla '%s' aparece %d veces" % (etiqueta, n))
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)
    return t.replace(viejo, nuevo)


# ══════════════════════════════════════════════════ crm/server.py ════════
CS = os.path.join(BASE, "crm", "server.py")
print("\n== crm/server.py ==")
t = leer(CS)
respaldar(CS)

VIEJO_ENVIAR = '''async def _wa_enviar(wa_id: str, texto: str) -> bool:
    """Manda el texto por la Cloud API. Devuelve si salio bien."""
    if not (WA_TOKEN and WA_PHONE_ID):
        wa_logger.error("WhatsApp sin configurar: faltan WA_TOKEN / WA_PHONE_ID")
        return False
    try:
        async with httpx.AsyncClient(timeout=30) as c:
            r = await c.post(
                f"{WA_API}/{WA_PHONE_ID}/messages",
                json={"messaging_product": "whatsapp",
                      "recipient_type": "individual", "to": wa_id,
                      "type": "text",
                      "text": {"preview_url": False, "body": texto}},
                headers={"Authorization": f"Bearer {WA_TOKEN}"})
        if r.status_code >= 400:
            # 131047 = fuera de la ventana de 24 h: ahi Meta solo acepta una
            # plantilla aprobada, no se puede improvisar el mensaje.
            wa_logger.error(f"WhatsApp no pudo enviar ({r.status_code}): {r.text[:300]}")
            return False
        wa_logger.info(f"WhatsApp enviado a {wa_id}")
        return True
    except Exception as e:
        wa_logger.error(f"WhatsApp error de red: {e}")
        return False


async def _wa_marcar_leido(msg_id: str) -> None:
    """Visto azul mientras Pepe piensa."""
    if not (WA_TOKEN and WA_PHONE_ID and msg_id):
        return
    try:
        async with httpx.AsyncClient(timeout=15) as c:
            await c.post(f"{WA_API}/{WA_PHONE_ID}/messages",
                         json={"messaging_product": "whatsapp", "status": "read",
                               "message_id": msg_id},
                         headers={"Authorization": f"Bearer {WA_TOKEN}"})
    except Exception:
        pass
'''

NUEVO_ENVIAR = '''async def _wa_enviar(wa_id: str, texto: str) -> bool:
    """Manda el texto por WhatsApp.

    El envío de verdad vive en `whatsapp_cloud.py`, porque también lo usa
    `main.py` para sacar las respuestas de los asesores desde el CRM.
    Así solo hay UN lugar donde se habla con la API de Meta.
    """
    from whatsapp_cloud import enviar_texto
    r = await enviar_texto(wa_id, texto)
    return bool(r.get("ok"))


async def _wa_marcar_leido(msg_id: str) -> None:
    """Visto azul mientras Pepe piensa."""
    from whatsapp_cloud import marcar_leido
    await marcar_leido(msg_id)
'''
t = cambiar(t, VIEJO_ENVIAR, NUEVO_ENVIAR, "_wa_enviar delega en whatsapp_cloud")

VIEJO_CANAL = '''    save_message(client_id, "advisor", content, channel="telegram")
'''
NUEVO_CANAL = '''    # El canal REAL del cliente: antes quedaba siempre en «telegram» aunque
    # el cliente hubiera escrito por WhatsApp, y quien miraba el CRM no sabía
    # por dónde contestarle.
    _con = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    _fila = _con.execute("SELECT channel FROM clients WHERE id = ?",
                         (client_id,)).fetchone()
    _con.close()
    _canal = (_fila["channel"] if _fila else None) or "telegram"
    save_message(client_id, "advisor", content, channel=_canal)
'''
t = cambiar(t, VIEJO_CANAL, NUEVO_CANAL, "respuesta de asesor guarda el canal real")

escribir(CS, t)


# ══════════════════════════════════════════════════════ main.py ═════════
MP = os.path.join(BASE, "main.py")
print("\n== main.py ==")
t = leer(MP)
respaldar(MP)

VIEJO_PEND = '''        cursor.execute("""
            SELECT pr.id, pr.client_id, pr.content, pr.advisor_name, c.telegram_id, c.phone
            FROM pending_replies pr
            JOIN clients c ON c.id = pr.client_id
            WHERE pr.sent = 0
            LIMIT 10
        """)
        pending = cursor.fetchall()
        for row in pending:
            reply_id, client_id, content, advisor_name, tg_id, phone = row
            try:
                msg = f"{advisor_name or 'Asesor'} de CJ Medical:\\n\\n{content}"
                sent = False

                # Intentar enviar por Telegram
                if tg_id:
                    try:
                        await app.bot.send_message(chat_id=int(tg_id), text=msg)
                        sent = True
                        logger.info(f"Respuesta enviada por Telegram a {tg_id}")
                    except Exception as e:
                        logger.warning(f"Telegram fallo para {tg_id}: {e}")

                # Si no tiene Telegram, intentar WhatsApp
                if not sent and phone and WHATSAPP_CLIENT is not None and WHATSAPP_CLIENT.status == "connected":
                    wa_phone = phone.strip()
                    if wa_phone.startswith("0"):
                        wa_phone = "57" + wa_phone[1:]
                    elif not wa_phone.startswith("57"):
                        wa_phone = "57" + wa_phone
                    await WHATSAPP_CLIENT.send_message(wa_phone, msg)
                    sent = True
                    logger.info(f"Respuesta enviada por WhatsApp a {wa_phone}")

                if sent:
                    conn.execute("UPDATE pending_replies SET sent = 1 WHERE id = ?", (reply_id,))
                    conn.commit()'''

NUEVO_PEND = '''        cursor.execute("""
            SELECT pr.id, pr.client_id, pr.content, pr.advisor_name,
                   c.telegram_id, c.phone, c.whatsapp_id, c.channel
            FROM pending_replies pr
            JOIN clients c ON c.id = pr.client_id
            WHERE pr.sent = 0
            LIMIT 10
        """)
        pending = cursor.fetchall()
        for row in pending:
            (reply_id, client_id, content, advisor_name,
             tg_id, phone, wa_id, canal) = row
            try:
                msg = f"{advisor_name or 'Asesor'} de CJ Medical:\\n\\n{content}"
                sent = False

                # WhatsApp PRIMERO si el cliente vino de ahí. Se manda por la
                # Cloud API de Meta (whatsapp_cloud.py). Antes esto dependía
                # del cliente viejo de Playwright/EvolutionAPI, que está
                # apagado: la respuesta del asesor NUNCA salía y nadie se
                # enteraba.
                if canal == "whatsapp" or (wa_id and not tg_id):
                    from whatsapp_cloud import enviar_texto
                    r = await enviar_texto(wa_id or phone, msg)
                    if r["ok"]:
                        sent = True
                        logger.info(f"Respuesta de asesor enviada por WhatsApp a {wa_id or phone}")
                    else:
                        logger.warning(f"WhatsApp no pudo con {wa_id or phone}: {r['detalle']}")

                # Telegram
                if not sent and tg_id:
                    try:
                        await app.bot.send_message(chat_id=int(tg_id), text=msg)
                        sent = True
                        logger.info(f"Respuesta enviada por Telegram a {tg_id}")
                    except Exception as e:
                        logger.warning(f"Telegram fallo para {tg_id}: {e}")

                # Último intento: WhatsApp por el celular guardado
                if not sent and phone and not tg_id:
                    from whatsapp_cloud import enviar_texto
                    r = await enviar_texto(phone, msg)
                    if r["ok"]:
                        sent = True
                        logger.info(f"Respuesta de asesor enviada por WhatsApp a {phone}")

                if sent:
                    conn.execute("UPDATE pending_replies SET sent = 1 WHERE id = ?", (reply_id,))
                    conn.commit()
                else:
                    logger.warning(f"No pude entregar la respuesta {reply_id} "
                                   f"(cliente {client_id}, canal {canal})")'''
t = cambiar(t, VIEJO_PEND, NUEVO_PEND, "respuestas de asesor salen por WhatsApp")

escribir(MP, t)

print("\n%d cambios aplicados." % len(CAMBIOS))
