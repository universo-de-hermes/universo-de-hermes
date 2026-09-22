"""
Extrae localStorage de WhatsApp de la pestaña abierta en Chrome
"""
import asyncio, logging, os, json
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("wa_force")

BASE = os.path.dirname(__file__)
SESSION_FILE = os.path.join(BASE, "wa_session.json")

async def main():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")

        for ctx in browser.contexts:
            for page in ctx.pages:
                title = await page.title()
                url = page.url
                if "whatsapp" in url.lower():
                    logger.info(f"🎯 WhatsApp tab: {title}")

                    # Mostrar algo del DOM para debug
                    body = await page.text_content("body") or ""
                    has_qr = "escanea" in body.lower() or "scan" in body.lower()
                    logger.info(f"¿Muestra QR?: {'SI' if has_qr else 'NO'}")

                    # Inyectar JS para forzar guardado
                    ls = await page.evaluate("""() => {
                        try {
                            const keys = Object.keys(localStorage);
                            return { count: keys.length, keys: keys.slice(0,20) };
                        } catch(e) { return { error: e.message }; }
                    }""")
                    logger.info(f"localStorage: {json.dumps(ls, indent=2)}")

                    # Forzar guardado del storage state COMPLETO
                    await ctx.storage_state(path=SESSION_FILE)
                    size = os.path.getsize(SESSION_FILE) if os.path.exists(SESSION_FILE) else 0
                    logger.info(f"Sesión guardada: {size} bytes")

                    # Verificar si realmente hay chat list
                    chat = await page.query_selector('div[data-testid="chat-list"]')
                    logger.info(f"¿Chat list visible?: {'SI' if chat else 'NO'}")

                    if chat:
                        with open(os.path.join(BASE, "wa_ready.txt"), "w") as f:
                            f.write("connected")
                        logger.info("✅ LISTO! WhatsApp conectado!")
                    else:
                        logger.info("⚠️ No detecta chat list - pero igual guardó sesión")
                    return

        logger.info("No se encontró pestaña de WhatsApp")

if __name__ == "__main__":
    asyncio.run(main())