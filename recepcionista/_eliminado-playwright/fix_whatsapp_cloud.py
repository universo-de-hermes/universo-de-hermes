#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monta el webhook de WhatsApp por la via oficial (Meta Cloud API).

Por que esta via y no las otras dos que ya hay en el CRM:
  - Twilio (/api/twilio/whatsapp) era SOLO sandbox de pruebas.
  - EvolutionAPI (/api/evolution/whatsapp) usa la sesion no oficial de
    WhatsApp Web: Meta puede banear el numero del negocio.
  - Meta Cloud API es la oficial, es gratis para las conversaciones que
    inicia el cliente (que es el caso: el cliente escribe primero) y no
    tiene riesgo de baneo.

Lo que agrega:
  GET  /api/whatsapp/cloud   -> verificacion del webhook (hub.challenge)
  POST /api/whatsapp/cloud   -> los mensajes entrantes
  GET  /api/whatsapp/estado  -> si quedo bien conectado (pide sesion)

Uso:  cd /root/universo/recepcionista && python3 fix_whatsapp_cloud.py
"""
import os
import shutil

BASE = "/root/universo/recepcionista"
CS = os.path.join(BASE, "crm", "server.py")
ENV = os.path.join(BASE, ".env")
CAMBIOS = []
CRLF = {}


def leer(p):
    with open(p, encoding="utf-8", newline="") as f:
        bruto = f.read()
    CRLF[p] = "\r\n" in bruto
    if CRLF[p]:
        print("  (aviso) %s usa saltos de linea CRLF" % os.path.basename(p))
    return bruto.replace("\r\n", "\n")


def escribir(p, t):
    if CRLF.get(p):
        t = t.replace("\n", "\r\n")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def cambiar(t, viejo, nuevo, etiqueta):
    n = t.count(viejo)
    if n != 1:
        raise SystemExit("  X ancla '%s' aparece %d veces" % (etiqueta, n))
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)
    return t.replace(viejo, nuevo)


print("\n== crm/server.py ==")
t = leer(CS)
b = CS + ".pre-whatsapp.bak"
if not os.path.exists(b):
    shutil.copy2(CS, b)
    print("  respaldo: %s" % os.path.basename(b))

# ── imports ──
t = cambiar(t, "import json\nimport os\nimport sys\nfrom datetime import datetime",
            "import asyncio\nimport hashlib\nimport hmac\nimport json\n"
            "import logging\nimport os\nimport re\nimport sys\nfrom datetime import datetime",
            "imports: asyncio, hashlib, hmac, logging, re")

t = cambiar(t, "from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, FileResponse",
            "import httpx\nfrom fastapi.responses import (HTMLResponse, RedirectResponse,\n"
            "                                JSONResponse, FileResponse, PlainTextResponse)",
            "imports: httpx y PlainTextResponse")

t = cambiar(t, """from crm.database import (
    init_db, get_all_clients, get_client_detail, get_or_create_client,
    save_message, update_client_status, verify_advisor,
    get_all_advisors, update_client_data, create_appointment
)""",
            """from crm.database import (
    init_db, get_all_clients, get_client_detail, get_or_create_client,
    save_message, update_client_status, verify_advisor,
    get_all_advisors, update_client_data, create_appointment, get_connection
)""",
            "imports: get_connection")

# ── el bloque de WhatsApp Cloud API ──
WA_BLOQUE = '''# ─── WhatsApp Cloud API (Meta oficial) ───
# El camino definitivo: gratis para las conversaciones que inicia el cliente
# (que es el caso: el cliente escribe primero) y sin riesgo de baneo.
# Twilio queda como sandbox y EvolutionAPI se puede apagar.
WA_TOKEN = os.getenv("WA_TOKEN", "").strip()
WA_PHONE_ID = os.getenv("WA_PHONE_ID", "").strip()
WA_WABA_ID = os.getenv("WA_WABA_ID", "").strip()
WA_VERIFY_TOKEN = os.getenv("WA_VERIFY_TOKEN", "cj_medical_2026").strip()
WA_APP_SECRET = os.getenv("WA_APP_SECRET", "").strip()
WA_API = os.getenv("WA_API", "https://graph.facebook.com/v21.0").rstrip("/")

wa_logger = logging.getLogger("whatsapp-cloud")

# Meta reintenta el webhook si tarda: se recuerdan los ids ya contestados
# para no responder dos veces el mismo mensaje.
_WA_VISTOS = set()


def _wa_firma_valida(crudo: bytes, cabecera: str, secreto: str) -> bool:
    """Meta firma cada webhook con el App Secret (HMAC SHA256)."""
    if not cabecera.startswith("sha256="):
        return False
    esperado = hmac.new(secreto.encode(), crudo, hashlib.sha256).hexdigest()
    return hmac.compare_digest(esperado, cabecera.split("=", 1)[1])


def _wa_telefono(numero: str) -> str:
    """Deja el numero como lo tiene la agenda: 573015001772 -> 3015001772."""
    n = re.sub(r"\\D", "", str(numero or ""))
    if len(n) == 12 and n.startswith("57"):
        return n[2:]
    return n


def _wa_texto(m: dict) -> str:
    """El texto del mensaje, sea escrito, boton o respuesta de lista."""
    tipo = m.get("type")
    if tipo == "text":
        return (m.get("text") or {}).get("body", "")
    if tipo == "button":
        return (m.get("button") or {}).get("text", "")
    if tipo == "interactive":
        i = m.get("interactive") or {}
        return ((i.get("button_reply") or {}).get("title")
                or (i.get("list_reply") or {}).get("title") or "")
    return ""


def _wa_cliente(wa_id: str, nombre: str) -> dict:
    """La ficha del cliente en el CRM para este numero de WhatsApp.

    Se reutiliza la que ya exista (por el numero internacional o por el
    celular local) para que WhatsApp y Telegram no creen dos tarjetas del
    mismo cliente.
    """
    local = _wa_telefono(wa_id)
    try:
        conn = get_connection()
        fila = conn.execute(
            "SELECT * FROM clients WHERE whatsapp_id = ? "
            "OR (COALESCE(phone, '') <> '' AND phone = ?) "
            "ORDER BY id LIMIT 1", (wa_id, local)).fetchone()
        conn.close()
        if fila:
            c = dict(fila)
            update_client_data(c["id"], whatsapp_id=wa_id, channel="whatsapp")
            c["channel"] = "whatsapp"
            return c
    except Exception as e:
        wa_logger.error(f"No pude buscar la ficha del cliente: {e}")
    # no existe: se crea con el numero de WhatsApp como llave
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO clients (whatsapp_id, name, phone, status, channel) "
                    "VALUES (?, ?, ?, 'nuevo', 'whatsapp')",
                    (wa_id, nombre or local, local or None))
        conn.commit()
        cid = cur.lastrowid
        conn.close()
        wa_logger.info(f"Ficha nueva de WhatsApp: {nombre or local} ({wa_id})")
        return {"id": cid, "whatsapp_id": wa_id, "name": nombre or local,
                "phone": local, "status": "nuevo", "channel": "whatsapp"}
    except Exception as e:
        wa_logger.error(f"No pude crear la ficha: {e}")
        return get_or_create_client(wa_id, name=nombre)


async def _wa_enviar(wa_id: str, texto: str) -> bool:
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


async def _wa_responder(wa_id: str, msg: dict, perfil: str) -> None:
    """El corazon: guarda el mensaje, se lo pasa a Pepe y contesta."""
    if not wa_id:
        return
    msg_id = msg.get("id") or ""
    texto = _wa_texto(msg).strip()
    if not texto:
        wa_logger.info(f"Mensaje sin texto ({msg.get('type')}): se ignora")
        return
    wa_logger.info(f"WhatsApp de {wa_id} ({perfil}): {texto[:70]}")
    await _wa_marcar_leido(msg_id)

    client = _wa_cliente(wa_id, perfil)
    save_message(client["id"], "client", texto, channel="whatsapp")
    if client.get("status") in ("nuevo",):
        update_client_status(client["id"], "en_conversacion", "Pepe Bot")

    pqrs_kw = ["queja", "reclamo", "me quejo", "pqrs", "inconforme",
               "cobro indebido", "mala atencion", "mal servicio"]
    if any(p in texto.lower() for p in pqrs_kw):
        update_client_status(client["id"], "pqrs", "Pepe Bot")

    history = get_conversation(client["id"])
    para_ia = [{"role": "user" if m["role"] == "client" else "assistant",
                "content": m["content"]} for m in history[-20:]]

    reply = None
    try:
        from main import ask_pepe
        reply = await ask_pepe(texto, para_ia,
                               telefono=_wa_telefono(wa_id) or wa_id,
                               client_id=client["id"])
    except Exception as e:
        wa_logger.error(f"Error de la IA: {e}")

    if not reply:
        reply = ("Hola, gracias por escribir a CJ Medical. \\U0001f44b\\n\\n"
                 "Somos un departamento medico especializado en el cuidado y "
                 "recuperacion de tus cejas.\\n\\n"
                 "\\u00bfDesde que ciudad nos contactas: Bogota o Medellin?")

    save_message(client["id"], "bot", reply, channel="whatsapp")
    await _wa_enviar(wa_id, reply)


async def _wa_procesar(datos: dict) -> None:
    """Recorre el lote que manda Meta y responde cada mensaje."""
    for entrada in (datos.get("entry") or []):
        for cambio in (entrada.get("changes") or []):
            valor = cambio.get("value") or {}
            perfil = (((valor.get("contacts") or [{}])[0]
                       ).get("profile") or {}).get("name") or ""
            for m in (valor.get("messages") or []):
                mid = m.get("id") or ""
                if mid and mid in _WA_VISTOS:
                    continue          # Meta reintento: ya se contesto
                if mid:
                    _WA_VISTOS.add(mid)
                    if len(_WA_VISTOS) > 500:
                        _WA_VISTOS.clear()
                try:
                    await _wa_responder(m.get("from") or "", m, perfil)
                except Exception as e:
                    wa_logger.error(f"Error procesando un mensaje: {e}")
            for s in (valor.get("statuses") or []):
                wa_logger.info(f"estado {s.get('status')} -> {s.get('recipient_id')}")


@app.get("/api/whatsapp/cloud")
async def whatsapp_cloud_verificar(request: Request):
    """Meta llama aqui UNA vez, al guardar el webhook, para verificarlo."""
    q = request.query_params
    if (q.get("hub.mode") == "subscribe"
            and q.get("hub.verify_token") == WA_VERIFY_TOKEN):
        wa_logger.info("Webhook de WhatsApp verificado por Meta")
        return PlainTextResponse(q.get("hub.challenge", ""))
    wa_logger.warning("Verify token no coincide")
    return PlainTextResponse("forbidden", status_code=403)


@app.post("/api/whatsapp/cloud")
async def whatsapp_cloud_webhook(request: Request):
    """Los mensajes entrantes de WhatsApp."""
    crudo = await request.body()
    if WA_APP_SECRET:
        if not _wa_firma_valida(crudo,
                                request.headers.get("x-hub-signature-256", ""),
                                WA_APP_SECRET):
            wa_logger.warning("Firma invalida: se ignora el webhook")
            return JSONResponse({"status": "forbidden"}, status_code=403)
    try:
        datos = json.loads(crudo or b"{}")
    except Exception:
        return JSONResponse({"status": "error"}, status_code=400)
    # Meta reintenta si se tarda: se contesta ya y Pepe piensa en el fondo
    asyncio.create_task(_wa_procesar(datos))
    return JSONResponse({"status": "ok"})


@app.get("/api/whatsapp/estado")
async def whatsapp_estado(request: Request):
    """Si WhatsApp quedo bien conectado. Pide sesion (expone el verify token)."""
    if not get_advisor(request):
        return JSONResponse({"error": "no autorizado"}, status_code=401)
    faltan = [k for k, v in (("WA_TOKEN", WA_TOKEN), ("WA_PHONE_ID", WA_PHONE_ID))
              if not v]
    d = {"configurado": not faltan, "faltan": faltan,
         "verify_token": WA_VERIFY_TOKEN, "firma_activa": bool(WA_APP_SECRET),
         "webhook": "https://crmcjm.universojota.tech/api/whatsapp/cloud"}
    if not faltan:
        try:
            async with httpx.AsyncClient(timeout=20) as c:
                r = await c.get(f"{WA_API}/{WA_PHONE_ID}",
                                params={"fields": "display_phone_number,"
                                                  "verified_name,quality_rating"},
                                headers={"Authorization": f"Bearer {WA_TOKEN}"})
            d["conexion"] = "ok" if r.status_code < 400 else "error"
            d["meta"] = (r.json() if r.status_code < 400
                         else {"error": r.text[:300]})
        except Exception as e:
            d["conexion"] = f"sin conexion: {e}"
    return d


'''

t = cambiar(t, '@app.get("/qr")\nasync def qr_page():',
            WA_BLOQUE + '@app.get("/qr")\nasync def qr_page():',
            "bloque WhatsApp Cloud API")

escribir(CS, t)

# ── .env: dejar los campos listos ──
print("\n== .env ==")
texto = leer(ENV)
agregar = []
for k, v, com in (("WA_TOKEN", "", "token PERMANENTE del usuario de sistema"),
                  ("WA_PHONE_ID", "", "Phone Number ID (el del numero nuevo)"),
                  ("WA_WABA_ID", "", "WhatsApp Business Account ID"),
                  ("WA_APP_SECRET", "", "App Secret (valida la firma de Meta)"),
                  ("WA_VERIFY_TOKEN", "cj_medical_2026", "palabra secreta del webhook")):
    if k + "=" not in texto:
        agregar.append("%s=%s  # %s" % (k, v, com))
if agregar:
    texto = texto.rstrip("\n") + "\n\n# ─── WhatsApp Cloud API (Meta) ───\n" + \
            "\n".join(agregar) + "\n"
    escribir(ENV, texto)
    print("  ok %d variables agregadas al .env (varias en blanco, faltan los datos)"
          % len(agregar))
else:
    print("  las variables ya estaban")

print("\n%d cambios aplicados." % len(CAMBIOS))
