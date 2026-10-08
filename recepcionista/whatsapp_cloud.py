"""
Envío de mensajes por la WhatsApp Cloud API (Meta oficial).

Vive en su propio módulo porque lo usan DOS lugares:

  - `crm/server.py`: para contestarle al cliente cuando escribe;
  - `main.py` (tarea `send_pending_replies`): para que un asesor humano
    pueda responderle a mano desde el panel del CRM.

OJO: la configuración se lee EN EL MOMENTO DE USARLA, nunca al importar.
Ya nos pasó: `agenda_helper` leía el token al importarse, el bot arrancaba
antes de cargar el `.env`, el token quedaba vacío para siempre y la agenda
respondía 401 en cada llamada.
"""
import logging
import os

import httpx

log = logging.getLogger("whatsapp-cloud")

TIEMPO_LIMITE = 30


def _token() -> str:
    return (os.environ.get("WA_TOKEN") or "").strip()


def _phone_id() -> str:
    return (os.environ.get("WA_PHONE_ID") or "").strip()


def _api() -> str:
    return (os.environ.get("WA_API")
            or "https://graph.facebook.com/v26.0").rstrip("/")


def configurado() -> bool:
    """¿Están los datos para poder enviar?"""
    return bool(_token() and _phone_id())


def faltantes() -> list:
    return [k for k, v in (("WA_TOKEN", _token()),
                           ("WA_PHONE_ID", _phone_id())) if not v]


def a_internacional(numero: str) -> str:
    """Deja el número como lo pide Meta: `3015001772` -> `573015001772`.

    La agenda guarda el celular local (10 dígitos, sin indicativo) y Meta
    necesita el indicativo del país. Si ya viene con 57, se respeta.
    """
    n = "".join(c for c in str(numero or "") if c.isdigit())
    if not n:
        return ""
    if n.startswith("57") and len(n) >= 12:
        return n
    if len(n) == 10 and n.startswith("3"):
        return "57" + n
    return n


async def enviar_texto(numero: str, texto: str) -> dict:
    """Manda un texto por WhatsApp.

    Devuelve {'ok', 'error', 'detalle'}. No lanza excepciones: quien llama
    tiene que poder decidir qué hacer si WhatsApp no está disponible.
    """
    if not configurado():
        log.error("WhatsApp sin configurar: faltan %s", ", ".join(faltantes()))
        return {"ok": False, "error": "SIN_CONFIGURAR",
                "detalle": ", ".join(faltantes())}

    destino = a_internacional(numero)
    if not destino:
        return {"ok": False, "error": "SIN_NUMERO",
                "detalle": "El cliente no tiene celular guardado."}

    try:
        async with httpx.AsyncClient(timeout=TIEMPO_LIMITE) as c:
            r = await c.post(
                "%s/%s/messages" % (_api(), _phone_id()),
                json={"messaging_product": "whatsapp",
                      "recipient_type": "individual", "to": destino,
                      "type": "text",
                      "text": {"preview_url": False, "body": texto}},
                headers={"Authorization": "Bearer " + _token()})
    except Exception as e:
        log.error("WhatsApp error de red: %s", e)
        return {"ok": False, "error": "RED", "detalle": str(e)[:200]}

    if r.status_code >= 400:
        # El 131047 es el importante: el cliente no escribe desde hace más de
        # 24 h, así que Meta solo acepta una PLANTILLA aprobada. No se puede
        # improvisar el texto en ese caso.
        log.error("WhatsApp no pudo enviar a %s (%s): %s",
                  destino, r.status_code, r.text[:300])
        return {"ok": False, "error": "RECHAZADO",
                "detalle": r.text[:300], "codigo": r.status_code}

    log.info("WhatsApp enviado a %s", destino)
    return {"ok": True, "error": None, "detalle": ""}


async def marcar_leido(msg_id: str) -> None:
    """Pone el visto azul mientras Pepe piensa. Es cortesía, no es crítico."""
    if not (configurado() and msg_id):
        return
    try:
        async with httpx.AsyncClient(timeout=15) as c:
            await c.post("%s/%s/messages" % (_api(), _phone_id()),
                         json={"messaging_product": "whatsapp",
                               "status": "read", "message_id": msg_id},
                         headers={"Authorization": "Bearer " + _token()})
    except Exception:
        pass
