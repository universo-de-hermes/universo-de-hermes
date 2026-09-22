"""
Houdini Bridge Server — Wrapper HTTP para la web UI
Con memoria de conversación para que Houdini recuerde el contexto.
"""
import asyncio
import json
import logging
import sys
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format="[BRIDGE] %(message)s")
logger = logging.getLogger("houdini-bridge")

# ── Ruta Houdini ──
_BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_HOUDINI = os.path.join(_BASE, 'houdini')
if os.path.isdir(_HOUDINI):
    sys.path.insert(0, _HOUDINI)
    os.chdir(_HOUDINI)
    logger.info(f"📁 Houdini path: {_HOUDINI}")
else:
    logger.error(f"❌ No se encuentra Houdini en {_HOUDINI}")

# ── Estado global ──
houdini_orchestrator = None
houdini_dispatcher = None
loop = None

# ── Historial de conversación (session_id -> list of {role, content}) ──
MAX_HISTORY = 50
conversation_history: dict[str, list] = {}

# ── Perfil de usuario persistente (se guarda en disco) ──
USER_PROFILE_PATH = os.path.join(_HOUDINI, 'config', 'user_profile.json')

def load_user_profile() -> dict:
    try:
        with open(USER_PROFILE_PATH, 'r') as f:
            return json.load(f)
    except:
        return {"name": None, "telegram_chat_id": None, "preferences": {}}

def save_user_profile(profile: dict):
    os.makedirs(os.path.dirname(USER_PROFILE_PATH), exist_ok=True)
    with open(USER_PROFILE_PATH, 'w') as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

def extract_user_facts(messages: list) -> dict:
    """Extrae datos del usuario del historial de la conversación actual."""
    facts = {}
    import re
    for msg in messages:
        text = msg.get("content", "")
        tlower = text.lower()
        # Detectar chat_id: "mi chat id es 1205850636" o "id 1205850636"
        chat_id_match = re.search(r'(?:chat\s*id|mi\s*id|telegram\s*id)[^0-9]*(\d{6,})', text, re.IGNORECASE)
        if not chat_id_match:
            chat_id_match = re.search(r'(?:^|\s)(\d{9,})\s*$', text)  # número largo suelto
        if chat_id_match:
            facts["telegram_chat_id"] = chat_id_match.group(1)
        # Detectar nombre: "soy Juan Jose" / "me llamo Juan" / "mi nombre es Juan"
        name_match = re.search(r'(?:soy|me llamo|mi nombre es)\s+([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+)?)', tlower)
        if name_match and "name" not in facts:
            candidate = name_match.group(1).strip().title()
            if len(candidate) > 1 and len(candidate.split()) <= 2:
                facts["name"] = candidate
        # También detectar cuando Houdini dice "es [nombre]?" en el historial
        if not facts.get("name"):
            name_match2 = re.search(r'llama[s]?\s+(?:es\s+)?([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+)?)', tlower)
            if name_match2:
                candidate = name_match2.group(1).strip().title()
                if len(candidate) > 1 and len(candidate.split()) <= 2 and candidate not in ['Jefe', 'Usuario', 'Usted', 'Su', 'Mi']:
                    facts["name"] = candidate
    return facts

async def init_houdini():
    """Inicializa todos los componentes de Houdini (una sola vez)."""
    global houdini_orchestrator, houdini_dispatcher, loop
    
    # Cargar .env desde el directorio de Houdini
    from dotenv import load_dotenv
    env_path = os.path.join(_HOUDINI, '.env')
    if os.path.exists(env_path):
        load_dotenv(env_path, override=True)
        logger.info(f"📄 .env cargado desde {env_path}")
    else:
        logger.warning(f"⚠️ .env no encontrado en {env_path}")
    
    # Recargar settings (limpia caché)
    from config.settings import reload_settings
    settings = reload_settings()
    logger.info(f"⚙️ Modelo: {settings.openrouter_model}")

    from config.settings import get_settings
    from core.orchestrator import HoudiniOrchestrator
    from core.dispatcher import ToolDispatcher
    from schemas.tools import ToolCategory
    from services.oauth import GoogleOAuth
    from agents.gmail_agent import GmailAgent
    from agents.calendar_agent import CalendarAgent
    from agents.sheets_agent import SheetsAgent
    from agents.drive_agent import DriveAgent
    from agents.tts_agent import TTSAgent
    from agents.telegram_agent import TelegramAgent
    from agents.design_agent import DesignAgent
    from agents.dashboard_agent import DashboardAgent
    from agents.spotify_agent import SpotifyAgent

    settings = get_settings()
    logger.info("🎩 Inicializando Houdini Bridge...")

    dispatcher = ToolDispatcher()

    # TTS
    tts = TTSAgent(voice=settings.tts_voice, rate=settings.tts_rate, volume=settings.tts_volume)
    dispatcher.register_agent(ToolCategory.TTS, tts)

    # Google OAuth
    oauth = GoogleOAuth()
    google_creds = oauth.get_credentials()
    if google_creds:
        dispatcher.register_agent(ToolCategory.GMAIL, GmailAgent(credentials=google_creds))
        dispatcher.register_agent(ToolCategory.CALENDAR, CalendarAgent(credentials=google_creds))
        dispatcher.register_agent(ToolCategory.SHEETS, SheetsAgent(credentials=google_creds))
        dispatcher.register_agent(ToolCategory.DRIVE, DriveAgent(credentials=google_creds))
        logger.info("✅ Google autenticado")
    else:
        logger.warning("⚠️ Google NO autenticado — servicios limitados")

    # Telegram
    try:
        from core.memory import MemoryStore
        mem = MemoryStore()
        mem.init_db()
        telegram = TelegramAgent(bot_token=settings.telegram_bot_token, memory=mem)
        dispatcher.register_agent(ToolCategory.TELEGRAM, telegram)
    except Exception as e:
        logger.warning(f"⚠️ Telegram desactivado: {e}")

    # Design / Dashboard
    dispatcher.register_agent(ToolCategory.DESIGN, DesignAgent())
    dispatcher.register_agent(ToolCategory.DASHBOARD, DashboardAgent())
    
    # Spotify
    try:
        spotify = SpotifyAgent()
        dispatcher.register_agent(ToolCategory.SPOTIFY, spotify)
        logger.info("✅ Spotify registrado")
    except Exception as e:
        logger.warning(f"⚠️ Spotify no disponible: {e}")

    # Orquestador
    orchestrator = HoudiniOrchestrator()
    orchestrator.set_tool_executor(dispatcher)

    houdini_orchestrator = orchestrator
    houdini_dispatcher = dispatcher
    logger.info("✅ Houdini Bridge listo")


class BridgeHandler(BaseHTTPRequestHandler):

    def _set_cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._set_cors()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/health':
            self.send_response(200)
            self._set_cors()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            ok = houdini_orchestrator is not None
            self.wfile.write(json.dumps({"status": "ok" if ok else "starting", "orchestrator": ok}).encode())
        else:
            self._send_json(404, {"error": "not found"})

    def do_POST(self):
        parsed = urlparse(self.path)
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length else b'{}'

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._send_json(400, {"error": "invalid JSON"})
            return
        except UnicodeDecodeError:
            # Intentar con latin-1 (Windows/Mac)
            try:
                data = json.loads(body.decode('latin-1'))
            except:
                self._send_json(400, {"error": "invalid encoding"})
                return

        if parsed.path == '/chat':
            self._handle_chat(data)
        elif parsed.path == '/reset':
            self._handle_reset(data)
        elif parsed.path == '/profile':
            self._handle_profile(data)
        elif parsed.path == '/profile/save':
            self._handle_profile_save(data)
        elif parsed.path == '/profile/delete':
            self._handle_profile_delete(data)
        else:
            self._send_json(404, {"error": "not found"})

    def _send_json(self, status, data):
        self.send_response(status)
        self._set_cors()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

    def _handle_reset(self, data):
        """Resetea la conversación de una sesión."""
        session_id = data.get('session_id', 'default')
        if session_id in conversation_history:
            del conversation_history[session_id]
        self._send_json(200, {"ok": True, "message": f"Conversación {session_id} reiniciada"})

    def _handle_chat(self, data):
        """Chat con memoria persistente del usuario."""
        if not houdini_orchestrator:
            self._send_json(503, {"error": "Houdini aún no está listo"})
            return

        message = data.get('message', '')
        if not message:
            self._send_json(400, {"error": "message required"})
            return

        session_id = data.get('session_id', 'default')

        try:
            # Obtener o inicializar historial
            is_new_session = session_id not in conversation_history
            if is_new_session:
                conversation_history[session_id] = []

            history = conversation_history[session_id]

            # ── Inyectar perfil del usuario al inicio de la conversación ──
            context = []
            if is_new_session:
                profile = load_user_profile()
                profile_parts = []
                if profile.get("name"):
                    profile_parts.append(f"El usuario se llama {profile['name']}")
                if profile.get("telegram_chat_id"):
                    profile_parts.append(f"Su Chat ID de Telegram es {profile['telegram_chat_id']}")
                if profile.get("preferences"):
                    prefs = profile["preferences"]
                    if prefs.get("email"):
                        profile_parts.append(f"Su correo es {prefs['email']}")
                if profile_parts:
                    context.append({
                        "role": "user",
                        "content": "[DATOS DEL USUARIO] " + ". ".join(profile_parts) + ". Usa esta información sin preguntar de nuevo."
                    })
                    context.append({
                        "role": "assistant",
                        "content": "Entendido. Tengo los datos del usuario guardados."
                    })

            # Agregar historial de conversación
            for entry in history:
                context.append({"role": entry["role"], "content": entry["content"]})

            # Enviar a Houdini con contexto
            future = asyncio.run_coroutine_threadsafe(
                houdini_orchestrator.orchestrate(message, session_id=session_id, context=context),
                loop
            )
            result = future.result(timeout=120)

            # Guardar en historial
            history.append({"role": "user", "content": message})
            history.append({"role": "assistant", "content": result.text})

            # Podar si excede el límite
            while len(history) > MAX_HISTORY * 2:
                history.pop(0)
                history.pop(0)

            # ── Extraer datos nuevos para preguntar al usuario ──
            all_messages = history + [{"role": "user", "content": message}]
            new_facts = extract_user_facts(all_messages)
            pending_save = {}
            if new_facts:
                profile = load_user_profile()
                for key, value in new_facts.items():
                    if profile.get(key) != value:
                        pending_save[key] = value

            self._send_json(200, {
                "ok": True,
                "text": result.text,
                "tool_calls": result.tool_calls_made,
                "error": result.error,
                "pending_save": pending_save if pending_save else None,
            })
        except Exception as e:
            logger.error(f"Error: {e}")
            self._send_json(500, {"error": str(e)})

    def _handle_profile(self, data):
        """Devuelve el perfil del usuario."""
        profile = load_user_profile()
        self._send_json(200, {"ok": True, "profile": profile})

    def _handle_profile_save(self, data):
        """Guarda datos específicos en el perfil (solo si el usuario confirma)."""
        profile = load_user_profile()
        to_save = data.get("data", {})
        changed = []
        for key, value in to_save.items():
            if key in ["name", "telegram_chat_id"] and value:
                profile[key] = value
                changed.append(key)
        if changed:
            save_user_profile(profile)
            logger.info(f"💾 Usuario confirmó guardar: {', '.join(changed)}")
            self._send_json(200, {"ok": True, "saved": changed, "profile": profile})
        else:
            self._send_json(200, {"ok": True, "saved": [], "profile": profile})

    def _handle_profile_delete(self, data):
        """Elimina datos del perfil."""
        profile = load_user_profile()
        keys = data.get("keys", [])
        for key in keys:
            profile.pop(key, None)
        save_user_profile(profile)
        logger.info(f"🗑️ Datos eliminados: {', '.join(keys)}")
        self._send_json(200, {"ok": True, "profile": profile})


def run_server():
    global loop

    # Inicializar Houdini
    init_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(init_loop)
    init_loop.run_until_complete(init_houdini())
    init_loop.close()

    # Event loop en background thread
    loop = asyncio.new_event_loop()

    def _run_loop():
        asyncio.set_event_loop(loop)
        loop.run_forever()

    t = threading.Thread(target=_run_loop, daemon=True)
    t.start()

    import time
    while not loop.is_running():
        time.sleep(0.05)

    port = 9876
    server = HTTPServer(('127.0.0.1', port), BridgeHandler)
    logger.info(f"🌉 Houdini Bridge en http://127.0.0.1:{port}")
    logger.info(f"   Health: GET  http://127.0.0.1:{port}/health")
    logger.info(f"   Chat:   POST http://127.0.0.1:{port}/chat")
    logger.info(f"   Reset:  POST http://127.0.0.1:{port}/reset")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Deteniendo bridge...")
        loop.call_soon_threadsafe(loop.stop)
        server.shutdown()


if __name__ == '__main__':
    run_server()