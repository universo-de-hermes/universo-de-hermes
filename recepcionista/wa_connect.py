"""
Conector WhatsApp - usa el Chrome real del usuario via remote debugging
Asume que Chrome ya está corriendo con --remote-debugging-port=9222
"""
import asyncio
import json
import logging
import os
import re
import time

from playwright.async_api import async_playwright

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("wa_connect")

BASE_DIR = os.path.dirname(__file__)
QR_FILE = os.path.join(BASE_DIR, "wa_qr.png")
SESSION_FILE = os.path.join(BASE_DIR, "wa_session.json")
READY_FILE = os.path.join(BASE_DIR, "wa_ready.txt")


async def connect_whatsapp():
    logger.info("=" * 60)
    logger.info("📱 Conectando WhatsApp via Chrome real...")
    logger.info("=" * 60)

    async with async_playwright() as p:
        # Conectar al Chrome que ya está corriendo (el de la terminal)
        try:
            browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
            logger.info("✅ Conectado a Chrome existente (127.0.0.1:9222)")
        except Exception as e:
            logger.error(f"❌ No se pudo conectar a Chrome: {e}")
            logger.error("Asegúrate de que Chrome esté abierto con --remote-debugging-port=9222")
            return

        # Crear un nuevo contexto (como una pestaña nueva aislada)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        # Cargar sesión guardada si existe
        if os.path.exists(SESSION_FILE):
            logger.info("📂 Cargando sesión guardada...")
            try:
                await context.storage_state(path=SESSION_FILE)
                logger.info("✅ Sesión cargada")
            except:
                pass

        page = await context.new_page()
        logger.info("🔷 Abriendo WhatsApp Web en una nueva pestaña...")

        await page.goto("https://web.whatsapp.com", wait_until="domcontentloaded")
        logger.info("⏳ Cargando WhatsApp Web...")

        # Esperar hasta 3 minutos para que se conecte o muestre QR
        start = time.time()
        max_wait = 180
        qr_count = 0
        connected = False

        while time.time() - start < max_wait:
            try:
                # Verificar múltiples formas de detectar conexión
                connected_detected = False

                # Buscar el panel de chats
                chat_selectors = [
                    'div[data-testid="chat-list"]',
                    'div[aria-label="Lista de chats"]',
                    'div[aria-label="Chat list"]',
                    'div[role="textbox"][contenteditable="true"]',
                    'div[data-testid="conversation-panel-header"]',
                    'footer div[contenteditable="true"]',
                ]
                for sel in chat_selectors:
                    el = await page.query_selector(sel)
                    if el:
                        connected_detected = True
                        break

                if connected_detected:
                    logger.info("✅ ¡SESION DE WHATSAPP ACTIVA!")
                    connected = True
                    break

                # Capturar QR si existe (para mostrarlo en la web)
                qr_elem = await page.query_selector("canvas") or await page.query_selector('div[data-ref]')
                if qr_elem:
                    try:
                        await qr_elem.screenshot(path=QR_FILE)
                        if qr_count % 5 == 0:
                            logger.info(f"📷 QR capturado ({os.path.getsize(QR_FILE)} bytes)")
                        qr_count += 1
                    except:
                        pass

            except Exception as e:
                logger.warning(f"Error: {e}")

            await asyncio.sleep(2)

        if connected:
            logger.info("🎉 WhatsApp conectado exitosamente!")
            # Guardar sesión
            try:
                await context.storage_state(path=SESSION_FILE)
                logger.info(f"💾 Sesión guardada en {SESSION_FILE}")
            except Exception as e:
                logger.warning(f"No se pudo guardar sesión: {e}")

            # Extraer número de teléfono
            try:
                # Click en los tres puntos del menú superior
                menu_btn = await page.query_selector('header span[data-testid="menu"], header div[role="button"]')
                if menu_btn:
                    await menu_btn.click()
                    await asyncio.sleep(1)
                    body_text = await page.text_content("body") or ""
                    phone_match = re.search(r'\+?\d{1,3}[\s\-]?\d{3}[\s\-]?\d{3}[\s\-]?\d{3,4}', body_text)
                    phone = phone_match.group(0).strip() if phone_match else "connected"
                    # Cerrar menú
                    await page.mouse.click(10, 10)
                else:
                    phone = "connected"
            except:
                phone = "connected"

            with open(READY_FILE, "w") as f:
                f.write(phone)
            logger.info(f"📱 Número: {phone}")
        else:
            logger.warning("⏰ Tiempo agotado - No se detectó conexión")
            with open(READY_FILE, "w") as f:
                f.write("timeout")

        # No cerramos el navegador porque es el Chrome del usuario
        # Solo cerramos la pestaña
        await page.close()
        await context.close()
        logger.info("👋 Conexión finalizada")


if __name__ == "__main__":
    asyncio.run(connect_whatsapp())