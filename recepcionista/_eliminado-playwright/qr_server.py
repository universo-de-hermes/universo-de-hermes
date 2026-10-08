"""
Servicio QR - Mantiene actualizado el código QR de WhatsApp Web
Ejecutar: python qr_server.py
"""
import asyncio
import logging
import os
import sys
import time
from pathlib import Path

from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("qr_server")

QR_FILE = os.path.join(os.path.dirname(__file__), "wa_qr.png")
SESSION_FILE = os.path.join(os.path.dirname(__file__), "wa_session.json")
READY_FILE = os.path.join(os.path.dirname(__file__), "wa_ready.txt")


async def qr_service():
    logger.info("=" * 60)
    logger.info("📱 QR SERVICE - MANTENIENDO QR ACTUALIZADO")
    logger.info("=" * 60)

    async with async_playwright() as p:
        # Usar Chrome del sistema si está disponible
        launch_args = {
            "headless": True,
            "args": ["--no-sandbox", "--disable-setuid-sandbox", "--disable-gpu", "--disable-software-rasterizer"]
        }
        # Intentar usar Chrome del sistema
        try:
            import shutil
            chrome_path = shutil.which("chrome") or shutil.which("google-chrome") or shutil.which("chromium")
            if not chrome_path:
                chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            if os.path.exists(chrome_path):
                launch_args["executable_path"] = chrome_path
                logger.info(f"Usando Chrome: {chrome_path}")
        except:
            pass

        # Si tenemos Chromium completo, usarlo (no headless-shell)
        import glob
        chromium_paths = sorted(glob.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome.exe")))
        if chromium_paths:
            launch_args["executable_path"] = chromium_paths[-1]
            logger.info(f"Usando Chromium: {chromium_paths[-1]}")
        browser = await p.chromium.launch(**launch_args)

        context_options = {"viewport": {"width": 1280, "height": 900}}
        if os.path.exists(SESSION_FILE):
            logger.info("Cargando sesión guardada...")
            context_options["storage_state"] = SESSION_FILE

        context = await browser.new_context(**context_options)
        page = await context.new_page()
        await page.goto("https://web.whatsapp.com", wait_until="domcontentloaded")

        logger.info("Cargando WhatsApp Web...")

        qr_count = 0
        session_found = False
        start_time = time.time()
        max_wait = 180  # 3 minutos máximo

        while time.time() - start_time < max_wait:
            try:
                title = await page.title()
                url = page.url

                # Verificar si ya está conectado
                connected = False
                # Método 1: buscar panel de chats por varios selectores
                chat_selectors = [
                    'div[data-testid="chat-list"]',
                    'div[aria-label="Lista de chats"]',
                    'div[aria-label="Chat list"]',
                    'div[data-testid="conversation-panel-messages"]',
                    'div[data-testid="conversation-panel-header"]',
                    'header[data-testid="conversation-header"]',
                    'div[data-testid="chat-footer"]',
                    'div[data-testid="main"] footer',
                    'div[role="textbox"][contenteditable="true"]',
                ]
                for selector in chat_selectors:
                    el = await page.query_selector(selector)
                    if el:
                        connected = True
                        break
                # Método 2: verificar si el título incluye "(" (número de mensajes)
                if not connected:
                    try:
                        title = await page.title()
                        if title and "(" in title and "WhatsApp" in title:
                            connected = True
                    except:
                        pass
                # Método 3: verificar si la URL cambió
                if not connected:
                    try:
                        cur_url = page.url
                        if cur_url and "/send?" not in cur_url:
                            pass
                    except:
                        pass

                if connected:
                    logger.info("SESION ACTIVA detectada!")
                    session_found = True
                    break

                # Capturar QR - puede ser canvas o SVG
                qr_elem = await page.query_selector("canvas") or await page.query_selector('svg[role="img"]') or await page.query_selector('div[data-ref]')
                if qr_elem:
                    tag = await qr_elem.get_attribute("tagName") or "canvas"
                    if tag.upper() == "CANVAS":
                        await qr_elem.screenshot(path=QR_FILE)
                    elif tag.upper() == "SVG":
                        # Para SVG tomar screenshot del contenedor padre
                        parent = await qr_elem.query_selector("xpath=..")
                        if parent:
                            await parent.screenshot(path=QR_FILE)
                        else:
                            await qr_elem.screenshot(path=QR_FILE)
                    else:
                        # div[data-ref] - intentar screenshot
                        await qr_elem.screenshot(path=QR_FILE)

                    if qr_count % 5 == 0:
                        logger.info(f"QR actualizado ({os.path.getsize(QR_FILE)} bytes)")
                    qr_count += 1
                else:
                    # Debug: ver qué hay en la página
                    if qr_count % 20 == 0:
                        title = await page.title()
                        body = await page.text_content("body") or ""
                        logger.info(f"Estado pagina: titulo={title}, url={page.url}")
                        logger.info(f"Body snippet: {body[:200]}")

                # Intentar detectar texto de "escanea" en la página
                body_text = await page.text_content("body") or ""

                # Si detecta "Escanera" o "para seguir usando" -> sesión puede estar cerrada
                if "vincular" in body_text.lower() or "víncula" in body_text.lower() or "link" in body_text.lower():
                    # Ya estamos en modo QR, seguir capturando
                    pass

                # Si detecta "sesión" + "cerrada" o "expiró" -> seguir capturando QR
                if "tu sesión" in body_text.lower() and ("cerrada" in body_text.lower() or "expiro" in body_text.lower()):
                    logger.info("⚠️ Sesión expirada - esperando nuevo QR")

                await asyncio.sleep(2)

            except Exception as e:
                logger.warning(f"Error: {e}")
                await asyncio.sleep(2)

        if session_found:
            logger.info("🎉 QR ESCANEADO - Sesión establecida!")
            await context.storage_state(path=SESSION_FILE)
            logger.info(f"💾 Sesión guardada en {SESSION_FILE}")

            # Extraer número
            try:
                # Click en el perfil
                profile_btn = await page.query_selector('header div[role="button"]')
                if profile_btn:
                    await profile_btn.click()
                    await asyncio.sleep(1)
                    body = await page.text_content("body") or ""
                    import re
                    phone_match = re.search(r'\+?\d{1,3}[\s\-]?\d{3}[\s\-]?\d{3}[\s\-]?\d{3,4}', body)
                    if phone_match:
                        phone = phone_match.group(0).strip()
                        with open(READY_FILE, "w") as f:
                            f.write(phone)
                        logger.info(f"📱 Número conectado: {phone}")
            except:
                pass

            with open(READY_FILE, "w") as f:
                f.write("connected")
        else:
            logger.warning("⏰ Tiempo agotado - QR no escaneado")
            with open(READY_FILE, "w") as f:
                f.write("timeout")

        await browser.close()
        logger.info("👋 QR Service finalizado")


if __name__ == "__main__":
    asyncio.run(qr_service())