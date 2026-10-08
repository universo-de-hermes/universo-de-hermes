"""
Módulo WhatsApp para Pepe - Recepcionista CJ Medical
Usa Playwright para conectar vía WhatsApp Web (QR)
"""

import asyncio
import json
import os
import time
import re
import logging
from datetime import datetime
from pathlib import Path

from playwright.async_api import async_playwright, Page

logger = logging.getLogger(__name__)

# Estados del cliente
WAITING_QR = "waiting_qr"
CONNECTED = "connected"
DISCONNECTED = "disconnected"
ERROR = "error"

SESSION_FILE = os.path.join(os.path.dirname(__file__), "wa_session.json")
QR_FILE = os.path.join(os.path.dirname(__file__), "wa_qr.png")


class WhatsAppClient:
    def __init__(self, on_message_callback=None):
        self.status = DISCONNECTED
        self.page = None
        self.context = None
        self.browser = None
        self.playwright = None
        self.qr_data = None
        self._running = False
        self._on_message = on_message_callback  # async function(phone, text, timestamp)
        self._phone_number = None  # Número conectado

    async def start(self, headless=False, connect_to_existing_chrome=False):
        """Inicia Playwright y abre WhatsApp Web
        
        Args:
            headless: Si True, usa navegador headless
            connect_to_existing_chrome: Si True, se conecta al Chrome que ya está abierto en puerto 9222
        """
        logger.info("Iniciando cliente WhatsApp...")
        self._running = True
        self.playwright = await async_playwright().start()

        if connect_to_existing_chrome:
            logger.info("Conectando a Chrome existente (127.0.0.1:9222)...")
            try:
                self.browser = await self.playwright.chromium.connect_over_cdp("http://127.0.0.1:9222")
                logger.info("Conectado a Chrome existente!")
                
                # USAR el contexto existente del Chrome (ahi estan las cookies y localStorage reales)
                self.context = self.browser.contexts[0]
                logger.info(f"Usando contexto existente con {len(self.context.pages)} pestañas")
                
                # Buscar la pestaña de WhatsApp que ya esta abierta
                self.page = None
                for p in self.context.pages:
                    url = p.url
                    if "web.whatsapp.com" in url and "sw.js" not in url:
                        self.page = p
                        logger.info(f"Usando pestaña existente de WhatsApp")
                        break
                
                if not self.page:
                    self.page = await self.context.new_page()
                    await self.page.goto("https://web.whatsapp.com", wait_until="domcontentloaded")
                    logger.info("Nueva pestaña de WhatsApp creada")
                
                await asyncio.sleep(5)

                # Buscar si hay sesion activa
                # Metodo 1: buscar chat-list (tiene conversaciones)
                chat_el = await self.page.query_selector('div[data-testid="chat-list"]')
                # Metodo 2: buscar textbox (chat abierto)
                if not chat_el:
                    chat_el = await self.page.query_selector('div[role="textbox"][contenteditable="true"]')
                # Metodo 3: buscar panel-header
                if not chat_el:
                    chat_el = await self.page.query_selector('div[data-testid="conversation-panel-header"]')
                # Metodo 4: buscar barra lateral (sidebar/pane-side) - funciona incluso sin chats
                if not chat_el:
                    chat_el = await self.page.query_selector('div[data-testid="pane-side"], div#pane-side, div[data-testid="sidebar"]')
                # Metodo 5: verificar si el texto "Todos" y "No leidos" aparece (interfaz principal)
                if not chat_el:
                    try:
                        body_text = await self.page.text_content("body") or ""
                        if "Todos" in body_text and "No leídos" in body_text and "Favoritos" in body_text:
                            chat_el = True  # marcador de que hay sesion
                            logger.info("Sesion detectada por texto de interfaz")
                    except:
                        pass
                # Metodo 6: buscar el boton de "Nueva llamada" o "Enviar documento"
                if not chat_el:
                    try:
                        body_text = await self.page.text_content("body") or ""
                        if "Nueva llamada" in body_text and "Enviar documento" in body_text:
                            chat_el = True
                            logger.info("Sesion detectada por menu de acciones")
                    except:
                        pass

                if chat_el:
                    self.status = CONNECTED
                    logger.info("SESION ACTIVA detectada!")
                    await self._extract_phone()
                    asyncio.create_task(self._monitor_messages())
                    # Guardar sesion para proxima vez
                    try:
                        await self.context.storage_state(path=SESSION_FILE)
                        sz = os.path.getsize(SESSION_FILE)
                        logger.info(f"Sesion guardada ({sz} bytes)")
                    except:
                        pass
                else:
                    self.status = WAITING_QR
                    logger.info("QR visible en Chrome - escanea con el celular Tigo")
                    try:
                        canvas = await self.page.query_selector("canvas")
                        if canvas:
                            await canvas.screenshot(path=QR_FILE)
                            logger.info(f"QR capturado en {QR_FILE}")
                    except:
                        pass
                    # Loop detectando cuando escaneen
                    for i in range(120):  # 180 segundos
                        await asyncio.sleep(1.5)
                        try:
                            body = await self.page.text_content("body") or ""
                            # Si aparece la interfaz principal (sin QR)
                            if "Todos" in body and "No leídos" in body:
                                self.status = CONNECTED
                                logger.info("QR ESCANEADO! Sesion activa!")
                                await self._extract_phone()
                                asyncio.create_task(self._monitor_messages())
                                await self.context.storage_state(path=SESSION_FILE)
                                logger.info("Sesion guardada!")
                                break
                        except:
                            pass
                
                logger.info(f"Estado: {self.status}")
                return
            except Exception as e:
                logger.warning(f"No se pudo conectar a Chrome existente: {e}")
                logger.info("Fallback: lanzando navegador propio...")

        # Lanzar navegador propio (fallback)
        self.browser = await self.playwright.chromium.launch(
            headless=headless,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ]
        )

        context_options = {
            "viewport": {"width": 1280, "height": 720},
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

        # Cargar sesión guardada si existe
        if os.path.exists(SESSION_FILE):
            logger.info("Cargando sesión guardada...")
            context_options["storage_state"] = SESSION_FILE

        context = await self.browser.new_context(**context_options)
        self.page = await context.new_page()
        self.page.on("pageerror", lambda err: logger.error(f"Error en página: {err}"))

        await self.page.goto("https://web.whatsapp.com", wait_until="domcontentloaded")
        await asyncio.sleep(3)

        await self._check_session()
        if self.status == CONNECTED:
            asyncio.create_task(self._monitor_messages())
        logger.info(f"Estado: {self.status}")

    async def _check_session(self):
        """Verifica si ya hay sesión activa o espera QR"""
        max_wait = 60  # segundos esperando QR
        start = time.time()

        while time.time() - start < max_wait:
            try:
                title = await self.page.title()
                url = self.page.url

                # Si está en la página principal de WhatsApp con chats cargados
                if "WhatsApp" in title and url.startswith("https://web.whatsapp.com"):
                    # Verificar si hay sesión (buscando panel de chats)
                    sidebar = await self.page.query_selector('div[data-testid="chat-list"], div[aria-label="Lista de chats"], div[aria-label="Chat list"]')
                    if sidebar:
                        self.status = CONNECTED
                        logger.info("✅ Sesión de WhatsApp activa")

                        # Extraer número de teléfono del perfil
                        await self._extract_phone()
                        return

                # Buscar QR en la página
                qr_canvas = await self.page.query_selector('canvas')
                if qr_canvas:
                    self.status = WAITING_QR
                    qr_path = os.path.join(os.path.dirname(__file__), "wa_qr.png")
                    await qr_canvas.screenshot(path=qr_path)
                    logger.info(f"📷 QR capturado en {qr_path}")
                    print(f"\n{'='*60}")
                    print(f"📱 ESCANEA EL QR CON WHATSAPP")
                    print(f"📷 Abre: {qr_path}")
                    print(f"💡 O ve a WhatsApp Web en el navegador")
                    print(f"{'='*60}\n")

                # Si encuentra algo que no sea ni QR ni sesión, esperar
                await asyncio.sleep(2)

            except Exception as e:
                logger.warning(f"⏳ Esperando carga de WhatsApp... {e}")
                await asyncio.sleep(2)

        if self.status != CONNECTED:
            logger.warning("⚠️ No se pudo establecer sesión. Revisa el QR.")
            self.status = WAITING_QR

    async def _extract_phone(self):
        """Intenta extraer el número de teléfono conectado"""
        try:
            # Hacer clic en el perfil
            menu_btn = await self.page.query_selector('header div[role="button"], header span[data-testid="menu"]')
            if menu_btn:
                await menu_btn.click()
                await asyncio.sleep(1)

            # Buscar el número en el menú desplegado
            body = await self.page.text_content('body')
            # Patrón: +57 300 123 4567 o similar
            phone_match = re.search(r'\+?\d{1,3}[\s\-]?\d{3}[\s\-]?\d{3}[\s\-]?\d{4}', body or "")
            if phone_match:
                self._phone_number = phone_match.group(0).strip()
                logger.info(f"📱 Teléfono conectado: {self._phone_number}")

            # Cerrar haciendo clic fuera
            await self.page.mouse.click(10, 10)
            await asyncio.sleep(0.5)
        except Exception as e:
            logger.warning(f"No se pudo extraer teléfono: {e}")

    async def _monitor_messages(self):
        """Monitorea mensajes nuevos - leyendo el DOM real de WhatsApp Web"""
        logger.info("👂 Monitoreando chats de WhatsApp...")
        known_messages = set()
        await asyncio.sleep(6)

        while self._running and self.status == CONNECTED:
            try:
                # Leer TODOS los chats de la sidebar con sus últimos mensajes
                chats = await self.page.evaluate("""() => {
                    const results = [];
                    // El panel lateral de chats
                    const pane = document.querySelector('#pane-side');
                    if (!pane) return results;
                    
                    // Cada chat es un role=row dentro del pane-side
                    const rows = pane.querySelectorAll('div[role="row"]');
                    for (const row of rows) {
                        // El nombre está en el title del elemento
                        const titleEl = row.querySelector('[title]');
                        const name = titleEl ? titleEl.getAttribute('title') || titleEl.textContent : '';
                        if (!name || name.trim() === '') continue;
                        
                        // El último mensaje son los divs con dir="auto" (texto del mensaje)
                        const dirDivs = row.querySelectorAll('div[dir="auto"]');
                        let lastMsg = '';
                        for (const d of dirDivs) {
                            const txt = d.textContent || '';
                            if (txt.length > lastMsg.length) lastMsg = txt;
                        }
                        
                        results.push({
                            name: name.trim(),
                            lastMsg: lastMsg.trim()
                        });
                    }
                    return results;
                }""")

                if not chats or len(chats) == 0:
                    await asyncio.sleep(4)
                    continue

                for chat in chats:
                    name = chat.get('name', '') or ''
                    msg = chat.get('lastMsg', '') or ''
                    if not name or not msg:
                        continue

                    msg_key = f"{name}:{msg[:100]}"
                    if msg_key in known_messages:
                        continue

                    # Mensaje NUEVO detectado
                    known_messages.add(msg_key)
                    if len(known_messages) > 200:
                        known_messages.clear()

                    logger.info(f"📨 Nuevo mensaje de WhatsApp — {name}: {msg[:60]}...")

                    if self._on_message and msg.strip():
                        await self._on_message(name, msg.strip(), datetime.now().isoformat())

                await asyncio.sleep(4)

            except Exception as e:
                logger.warning(f"Error en monitoreo: {e}")
                await asyncio.sleep(6)

    async def _extract_contact_phone(self, contact_name):
        """Extrae el teléfono del contacto desde la cabecera del chat"""
        try:
            # Hacer clic en la cabecera para ver info
            header = await self.page.query_selector('header div[role="button"]')
            if header:
                await header.click()
                await asyncio.sleep(1)
                body = await self.page.text_content('body') or ""
                phone_match = re.search(r'\+?\d{10,15}', body)
                if phone_match:
                    return phone_match.group(0)
                # Cerrar
                await self.page.mouse.click(10, 10)
                await asyncio.sleep(0.5)
        except:
            pass
        return None

    async def send_message(self, phone: str, text: str):
        """Envía un mensaje WhatsApp a un número o contacto existente"""
        if self.status != CONNECTED:
            logger.warning("⚠️ WhatsApp no conectado. No se puede enviar mensaje.")
            return False

        try:
            # Determinar si es un número telefónico o un nombre de contacto
            digits_only = re.sub(r'[^\d]', '', phone)
            is_phone = len(digits_only) >= 8

            if is_phone:
                # ── Modo número: abrir chat por URL ──
                clean_phone = digits_only
                if clean_phone.startswith("0"):
                    clean_phone = "57" + clean_phone[1:]
                if not clean_phone.startswith("57"):
                    clean_phone = "57" + clean_phone

                await self.page.goto(f"https://web.whatsapp.com/send?phone={clean_phone}")
                await asyncio.sleep(3.5)

            else:
                # ── Modo nombre: buscar el chat en la sidebar y abrirlo ──
                contact_name = phone.strip()
                logger.info(f"🔍 Buscando chat por nombre: {contact_name}")

                found = await self.page.evaluate(f"""(name) => {{
                    // Buscar en la lista de chats
                    const items = document.querySelectorAll('div[role="row"], div[data-testid="cell-frame-container"]');
                    for (const item of items) {{
                        const titleEl = item.querySelector('[title], [data-testid="conversation-title"], div[aria-label]');
                        if (!titleEl) continue;
                        const t = (titleEl.getAttribute('title') || titleEl.textContent || titleEl.getAttribute('aria-label') || '').toLowerCase();
                        if (t.includes(name.toLowerCase())) {{
                            item.click();
                            return true;
                        }}
                    }}
                    return false;
                }}""", contact_name)

                if not found:
                    logger.warning(f"⚠️ No se encontró chat para: {contact_name}")
                    return False
                await asyncio.sleep(2)

            # Esperar a que cargue el cuadro de texto
            text_box = await self.page.wait_for_selector(
                'div[data-testid="conversation-compose-box-input"], div[contenteditable="true"][role="textbox"], footer div[contenteditable="true"]',
                timeout=15000
            )

            if not text_box:
                logger.warning(f"⚠️ No se pudo abrir chat con {phone}")
                return False

            # Escribir mensaje
            await text_box.click()
            await asyncio.sleep(0.5)

            # Dividir líneas (WhatsApp usa Shift+Enter para multilínea)
            lines = text.split("\n")
            for i, line in enumerate(lines):
                await text_box.type(line, delay=15)
                if i < len(lines) - 1:
                    await self.page.keyboard.press("Shift+Enter")
                    await asyncio.sleep(0.1)

            await asyncio.sleep(0.5)

            # Enviar (Enter)
            await self.page.keyboard.press("Enter")
            await asyncio.sleep(1.5)

            logger.info(f"✅ Mensaje enviado a {phone}: {text[:60]}...")
            return True

        except Exception as e:
            logger.error(f"❌ Error enviando mensaje a {phone}: {e}")
            return False

    async def save_session(self):
        """Guarda el estado de la sesión (storage state)"""
        if self.page and self.page.context:
            await self.page.context.storage_state(path=SESSION_FILE)
            logger.info("💾 Sesión guardada")

    async def wait_for_qr_scan(self, timeout=120):
        """Espera a que el usuario escanee el QR"""
        if self.status != WAITING_QR:
            return self.status == CONNECTED

        logger.info("⏳ Esperando escaneo QR...")
        start = time.time()

        while time.time() - start < timeout:
            try:
                title = await self.page.title()
                url = self.page.url

                if "WhatsApp" in title and url.startswith("https://web.whatsapp.com"):
                    sidebar = await self.page.query_selector(
                        'div[data-testid="chat-list"], div[aria-label="Lista de chats"]'
                    )
                    if sidebar:
                        self.status = CONNECTED
                        logger.info("✅ QR escaneado - Sesión activa")
                        await self.save_session()
                        await self._extract_phone()
                        asyncio.create_task(self._monitor_messages())
                        return True

                await asyncio.sleep(2)

            except Exception as e:
                logger.warning(f"⏳ Esperando QR: {e}")
                await asyncio.sleep(2)

        logger.warning("⚠️ Tiempo de espera para QR agotado")
        return False

    async def get_qr_image(self) -> str:
        """Retorna la ruta de la imagen QR"""
        if os.path.exists(QR_FILE):
            return QR_FILE
        return None

    async def disconnect(self):
        """Desconecta WhatsApp Web"""
        self._running = False
        self.status = DISCONNECTED
        if self.page:
            await self.save_session()
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        logger.info("🔌 WhatsApp desconectado")


async def qr_cli():
    """
    Función CLI para escanear QR por primera vez.
    Uso: python -c "from whatsapp_client import qr_cli; import asyncio; asyncio.run(qr_cli())"
    """
    logging.basicConfig(level=logging.INFO)

    def dummy_cb(phone, text, ts):
        print(f"📨 {phone}: {text}")

    client = WhatsAppClient(on_message_callback=dummy_cb)
    await client.start(headless=False)

    if client.status == WAITING_QR:
        print("\n" + "=" * 60)
        print("📱 ESCANEA EL QR CON WHATSAPP EN TU CELULAR")
        print("📷 Busca la imagen: wa_qr.png")
        print("⏳ O espera a que aparezca el navegador...")
        print("=" * 60 + "\n")
        await client.wait_for_qr_scan(timeout=180)

    if client.status == CONNECTED:
        print(f"\n✅ CONECTADO! Número: {client._phone_number}")
        print("💾 Sesión guardada. Ya puedes cerrar.")
        await client.save_session()
    else:
        print("\n❌ No se pudo conectar. Reintenta.")

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(qr_cli())