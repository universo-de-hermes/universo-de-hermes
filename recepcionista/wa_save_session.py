"""
Toma la sesión de WhatsApp de la pestaña que ya está abierta en Chrome
"""
import asyncio, logging, os, json, time
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("wa_save")

BASE = os.path.dirname(__file__)
SESSION_FILE = os.path.join(BASE, "wa_session.json")

async def main():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        contexts = browser.contexts
        logger.info(f"Contextos encontrados: {len(contexts)}")

        # Buscar el contexto que tenga WhatsApp
        for ctx in contexts:
            pages = ctx.pages
            for page in pages:
                title = await page.title()
                url = page.url
                logger.info(f"Pestaña: {title} | {url[:80]}")

                if "whatsapp" in url.lower() or "whatsapp" in title.lower():
                    logger.info(f"✅ Encontrada pestaña de WhatsApp!")
                    
                    # Verificar si está conectada (buscar chat list)
                    has_chats = await page.query_selector('div[data-testid="chat-list"], div[aria-label="Lista de chats"], div[role="textbox"][contenteditable="true"]')
                    
                    if has_chats:
                        logger.info("✅ Sesión activa detectada! Guardando...")
                        await ctx.storage_state(path=SESSION_FILE)
                        logger.info(f"💾 SESIÓN GUARDADA en {SESSION_FILE}")
                        
                        # Marcar como listo
                        with open(os.path.join(BASE, "wa_ready.txt"), "w") as f:
                            f.write("connected")
                        
                        logger.info("🎉 WhatsApp conectado permanentemente!")
                        return
                    else:
                        logger.warning("⚠️ WhatsApp abierto pero sin sesión activa")
                        logger.info("👉 Escanea el QR en la pestaña de Chrome que está abierta")

        # Si no encontró, tomar la sesión del primer contexto de todas formas
        if contexts and len(contexts) > 0:
            logger.info("Guardando sesión del contexto principal...")
            try:
                await contexts[0].storage_state(path=SESSION_FILE)
                logger.info(f"Sesión guardada de contexto principal")
            except:
                pass

        logger.info("No se encontró sesión activa de WhatsApp")

    input("\n🔴 Presiona Enter para cerrar...")

if __name__ == "__main__":
    asyncio.run(main())