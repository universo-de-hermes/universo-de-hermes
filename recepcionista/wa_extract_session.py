"""
Extrae SESION REAL de WhatsApp usando CDP directo
"""
import asyncio, logging, os, json, time
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("wa_cdp")

BASE = os.path.dirname(__file__)
SESSION_FILE = os.path.join(BASE, "wa_session.json")
READY_FILE = os.path.join(BASE, "wa_ready.txt")

async def main():
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        
        # Obtener todas las páginas reales del navegador usando CDP
        cdp_session = await browser.new_browser_cdp_session()
        targets = await cdp_session.send("Target.getTargets")
        
        whatsapp_target = None
        for t in targets.get("targetInfos", []):
            url = t.get("url", "")
            if "web.whatsapp.com" in url:
                whatsapp_target = t
                logger.info(f"🎯 WhatsApp target encontrado: {t['targetId']} | {url[:80]}")
                break
        
        if not whatsapp_target:
            logger.warning("No hay pestaña de WhatsApp abierta")
            # Buscar pestañas con título WhatsApp
            for t in targets.get("targetInfos", []):
                title = t.get("title", "")
                if "whatsapp" in title.lower():
                    whatsapp_target = t
                    logger.info(f"🎯 WhatsApp por título: {t['targetId']}")
                    break
        
        if whatsapp_target:
            tid = whatsapp_target["targetId"]
            
            # Buscar la página en los contexts existentes
            page_obj = None
            for ctx in browser.contexts:
                for p in ctx.pages:
                    url = p.url
                    if "web.whatsapp.com" in url:
                        page_obj = p
                        break
                if page_obj:
                    break
            
            if not page_obj:
                logger.warning("No se encontró page object de WhatsApp, creando conexión CDP directa")
                # Usar CDP session desde el primer contexto
                page_cdp = browser.contexts[0].cdp_session if browser.contexts else None
            else:
                page_cdp = page_obj.context.cdp_session
            
            # Extraer localStorage
            ls_data = await page_cdp.send("Runtime.evaluate", {
                "expression": "JSON.stringify(window.localStorage)",
                "returnByValue": True
            })
            
            if ls_data.get("result", {}).get("type") == "string":
                ls = json.loads(ls_data["result"]["value"])
                logger.info(f"localStorage: {len(ls)} items")
                for k in list(ls.keys())[:10]:
                    v = ls[k][:40]
                    logger.info(f"  {k} = {v}...")
                
                # Verificar si hay WABA tokens (sesión activa)
                wa_keys = [k for k in ls.keys() if "WABrowserId" in k or "WAToken" in k or "wa_" in k]
                if wa_keys:
                    logger.info(f"✅ SESION REAL ENCONTRADA! {len(wa_keys)} claves de WhatsApp")
                    
                    # Extraer cookies
                    cookies_data = await page_cdp.send("Network.getAllCookies")
                    cookies = cookies_data.get("cookies", [])
                    wa_cookies = [c for c in cookies if "whatsapp" in c.get("domain","") or "facebook" in c.get("domain","")]
                    logger.info(f"Cookies WhatsApp: {len(wa_cookies)}")
                    
                    # Guardar storage state manualmente
                    storage_state = {
                        "cookies": [{"name": c["name"], "value": c["value"], "domain": c["domain"], 
                                      "path": c.get("path","/"), "expires": c.get("expires",-1),
                                      "httpOnly": c.get("httpOnly",False), "secure": c.get("secure",False),
                                      "sameSite": c.get("sameSite","Lax")} for c in cookies if "whatsapp" in c.get("domain","") or "facebook" in c.get("domain","")],
                        "origins": [{"origin": "https://web.whatsapp.com", "localStorage": [{"name": k, "value": v} for k,v in ls.items()]}]
                    }
                    
                    with open(SESSION_FILE, "w") as f:
                        json.dump(storage_state, f)
                    
                    sz = os.path.getsize(SESSION_FILE)
                    logger.info(f"💾 SESION GUARDADA: {sz} bytes")
                    
                    with open(READY_FILE, "w") as f:
                        f.write("connected")
                    
                    logger.info("🎉¡WHATSAPP CONECTADO PERMANENTEMENTE!")
                else:
                    logger.warning("⚠️ No hay claves de WhatsApp en localStorage - necesita escanear QR")
            else:
                logger.warning("No se pudo leer localStorage")
        else:
            logger.warning("No se encontró pestaña de WhatsApp")

if __name__ == "__main__":
    asyncio.run(main())