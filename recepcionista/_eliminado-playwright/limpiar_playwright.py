#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Elimina la via vieja de WhatsApp: Playwright / EvolutionAPI.

Ya no se usa. El camino oficial es la WhatsApp Cloud API de Meta, que entra
por el webhook del CRM (`/api/whatsapp/cloud`).

Que se quita:
  main.py        - el import de whatsapp_client, la global WHATSAPP_CLIENT,
                   la funcion handle_whatsapp_message (via Playwright) y el
                   arranque de WhatsApp que estaba comentado.
  crm/server.py  - el webhook /api/evolution/whatsapp y las pantallas de QR
                   (/qr, /wa_qr.png, /wa_qr_check), que eran para escanear el
                   QR de WhatsApp Web.

Los archivos no se borran de una: se MUEVEN a `_eliminado-playwright/`.
Si algo llegara a hacer falta, ahi estan.
"""
import os
import shutil

BASE = "/root/universo/recepcionista"
BASURA = os.path.join(BASE, "_eliminado-playwright")
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
    b = p + ".pre-limpieza-wa.bak"
    if not os.path.exists(b):
        shutil.copy2(p, b)
        print("  respaldo: %s" % os.path.basename(b))


def cambiar(t, viejo, nuevo, etiqueta):
    if t.count(viejo) != 1:
        raise SystemExit("  X '%s' aparece %d veces" % (etiqueta, t.count(viejo)))
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)
    return t.replace(viejo, nuevo)


def quitar(t, viejo, etiqueta):
    return cambiar(t, viejo, "", etiqueta)


def cortar(t, ini, fin, etiqueta):
    """Borra desde `ini` hasta justo antes de `fin`."""
    i = t.find(ini)
    j = t.find(fin, i + 1) if i >= 0 else -1
    if i < 0 or j < 0:
        raise SystemExit("  X no encontre las fronteras de %s" % etiqueta)
    n = t[i:j].count("\n")
    print("  ok %s (%d lineas fuera)" % (etiqueta, n))
    CAMBIOS.append(etiqueta)
    return t[:i] + t[j:]


# ══════════════════════════════════════════════════════════ main.py ══════
MP = os.path.join(BASE, "main.py")
print("\n== main.py ==")
t = leer(MP)
respaldar(MP)

t = quitar(t, "from whatsapp_client import WhatsAppClient\n",
           "import de whatsapp_client")

t = quitar(t, "WHATSAPP_CLIENT = None  # Se asigna en init si WhatsApp está disponible\n",
           "global WHATSAPP_CLIENT")

t = quitar(t, "    from crm.database import DB_PATH, get_connection\n    global WHATSAPP_CLIENT\n",
           "global dentro de send_pending_replies")

t = cortar(t, "# ── Manejar mensajes de WhatsApp ──", "# ── Manejar errores ──",
           "funcion handle_whatsapp_message (Playwright)")

t = cortar(t, "        # ── Iniciar WhatsApp ──",
           "        # ── Programar tarea periódica para enviar respuestas de asesores ──",
           "arranque de WhatsApp en cleanup_stale")

# dejar dicho por donde entra WhatsApp ahora
t = cambiar(t, "        # ── Programar tarea periódica para enviar respuestas de asesores ──",
            "        # WhatsApp NO se conecta desde el bot: entra por el webhook del CRM\n"
            "        # (/api/whatsapp/cloud, Cloud API de Meta). Aqui solo queda Telegram.\n\n"
            "        # ── Programar tarea periódica para enviar respuestas de asesores ──",
            "nota: WhatsApp entra por el webhook del CRM")

escribir(MP, t)


# ══════════════════════════════════════════════════ crm/server.py ═══════
CS = os.path.join(BASE, "crm", "server.py")
print("\n== crm/server.py ==")
t = leer(CS)
respaldar(CS)

t = cortar(t, "# ─── EvolutionAPI Webhook ───",
           "# ─── WhatsApp Cloud API (Meta oficial) ───",
           "webhook de EvolutionAPI")

t = cortar(t, '@app.get("/qr")', '@app.exception_handler(Exception)',
           "pantallas de QR (EvolutionAPI/Playwright)")

escribir(CS, t)


# ══════════════════════════════════════════════ archivos muertos ════════
print("\n== archivos que se mueven a _eliminado-playwright/ ==")
os.makedirs(BASURA, exist_ok=True)
for f in ("whatsapp_client.py", "wa_save_session.py", "qr-page.html",
          "wa_qr.png", "wa_ready.txt"):
    origen = os.path.join(BASE, f)
    if os.path.exists(origen):
        shutil.move(origen, os.path.join(BASURA, f))
        print("  movido: %s" % f)

req = os.path.join(BASE, "requirements.txt")
if os.path.exists(req):
    with open(req, encoding="utf-8") as f:
        r = f.read()
    if "playwright" in r.lower() and "ELIMINADO 2026-09-23" not in r:
        with open(req, "w", encoding="utf-8") as f:
            f.write("# playwright: ELIMINADO 2026-09-23. La via de WhatsApp Web por QR\n"
                    "# (Playwright/EvolutionAPI) se reemplazo por la Cloud API de Meta.\n" + r)
        print("  anotado en requirements.txt")

print("\n%d cambios aplicados." % len(CAMBIOS))
