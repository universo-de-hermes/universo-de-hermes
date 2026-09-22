"""
WhatsApp QR - Modo visible
Abre Chromium en una ventana que puedes ver y escanear QR
"""
import asyncio, logging, os, re, time
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("wa_visible")

BASE = os.path.dirname(__file__)
QR_FILE = os.path.join(BASE, "wa_qr.png")
SESSION_FILE = os.path.join(BASE, "wa_session.json")
READY_FILE = os.path.join(BASE, "wa_ready.txt")

async def main():
    from playwright.async_api import async_playwright
    import glob
    logger.info("=" * 60)
    logger.info("🔷 Abriendo WhatsApp Web visible...")
    logger.info("📱 Escanea el QR con tu celular Tigo")
    logger.info("=" * 60)

    async with async_playwright() as p:
        # Usar Chromium completo (no headless-shell)
        chromium_paths = sorted(glob.glob(os.path.expanduser("~/AppData/Local/ms-playwright/chromium-*/chrome.exe")))
        if not chromium_paths:
            # Buscar Chrome del sistema
            chromium_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        else:
            chromium_path = chromium_paths[-1]

        logger.info(f"Usando: {chromium_path}")

        browser = await p.chromium.launch(
            headless=False,
            executable_path=chromium_path,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )

        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            no_viewport=True
        )

        # Cargar sesión si existe
        if os.path.exists(SESSION_FILE):
            try:
                await context.storage_state(path=SESSION_FILE)
                logger.info("Sesión guardada cargada")
            except:
                pass

        page = await context.new_page()
        await page.goto("https://web.whatsapp.com", wait_until="domcontentloaded")
        logger.info("⏳ WhatsApp Web cargando...")

        # Esperar hasta 3 minutos
        start = time.time()
        max_wait = 180
        qr_count = 0
        connected = False

        while time.time() - start < max_wait:
            try:
                # Detectar si está conectado
                connected = False
                selectors = [
                    'div[data-testid="chat-list"]', 'div[aria-label="Lista de chats"]',
                    'div[aria-label="Chat list"]', 'div[role="textbox"][contenteditable="true"]',
                    'div[data-testid="conversation-panel-header"]',
                ]
                for sel in selectors:
                    if await page.query_selector(sel):
                        connected = True
                        break

                if connected:
                    logger.info("✅ WHATSAPP CONECTADO!")
                    break

                # Capturar QR para la web
                canvas = await page.query_selector("canvas")
                if canvas:
                    await canvas.screenshot(path=QR_FILE)
                    if qr_count % 5 == 0:
                        logger.info(f"QR ({os.path.getsize(QR_FILE)} bytes)")
                    qr_count += 1

            except:
                pass
            await asyncio.sleep(2)

        if connected:
            await context.storage_state(path=SESSION_FILE)
            logger.info(f"Sesión guardada en {SESSION_FILE}")

            # Extraer número
            try:
                menu = await page.query_selector('header span[data-testid="menu"], header div[role="button"]')
                if menu:
                    await menu.click()
                    await asyncio.sleep(1)
                    body = await page.text_content("body") or ""
                    m = re.search(r'\+?\d{1,3}[\s\-]?\d{3}[\s\-]?\d{3}[\s\-]?\d{3,4}', body)
                    phone = m.group(0).strip() if m else "connected"
                    await page.mouse.click(10, 10)
                else:
                    phone = "connected"
            except:
                phone = "connected"

            with open(READY_FILE, "w") as f:
                f.write(phone)
            logger.info(f"✅ Listo! Número: {phone}")
        else:
            with open(READY_FILE, "w") as f:
                f.write("timeout")
            logger.warning("No se detectó conexión")

        input("\n🔴 Presiona Enter para cerrar...")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())