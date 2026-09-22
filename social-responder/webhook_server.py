#!/usr/bin/env python3
"""
Hermes Social Responder — Webhook Server
Recibe notificaciones de Meta (Instagram + Facebook Comments)
"""
import json, os, sys, logging
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 3005
LOG_FILE = "/root/universo/social-responder/webhook.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

class WebhookHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Meta envía GET para verificar el webhook (challenge)"""
        params = self._parse_query()
        mode = params.get("hub.mode", [""])[0]
        challenge = params.get("hub.challenge", [""])[0]
        token = params.get("hub.verify_token", [""])[0]
        
        # Token de verificación (lo configuraremos después en la app de Meta)
        VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "hermes_cm_2026")
        
        logging.info(f"GET /webhook/meta/ — mode={mode}, token={token}")
        
        if mode == "subscribe" and token == VERIFY_TOKEN:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(challenge.encode())
            logging.info("✅ Webhook verificado exitosamente!")
        else:
            self.send_response(403)
            self.end_headers()
            logging.warning("❌ Verificación fallida")
    
    def do_POST(self):
        """Meta envía POST con los eventos (comentarios, mensajes)"""
        content_len = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_len)
        
        try:
            data = json.loads(body)
            logging.info(f"📩 Evento recibido: {json.dumps(data, indent=2)[:500]}")
            
            # Aquí procesaremos los comentarios y enviaremos DMs
            self._process_event(data)
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        except Exception as e:
            logging.error(f"Error procesando evento: {e}")
            self.send_response(200)  # Siempre 200 para que Meta no reintente
            self.end_headers()
    
    def _process_event(self, data):
        """Procesa el evento de Meta"""
        # Entry es el contenedor principal
        entries = data.get("entry", [])
        for entry in entries:
            # Changes contiene los cambios (comentarios, etc)
            changes = entry.get("changes", [])
            for change in changes:
                field = change.get("field", "")
                value = change.get("value", {})
                logging.info(f"📌 Field: {field}, Value keys: {list(value.keys())}")
                
                if field == "comments":
                    comment_id = value.get("id", "")
                    text = value.get("text", "")
                    from_name = value.get("from", {}).get("name", "Desconocido")
                    logging.info(f"💬 Comentario de {from_name}: {text}")
                    
                    # TODO: Aquí irá el Keyword Engine + DM Template
                    # TODO: Decidir si responder público o enviar DM
    
    def _parse_query(self):
        from urllib.parse import urlparse, parse_qs
        return parse_qs(urlparse(self.path).query)
    
    def log_message(self, format, *args):
        # Silenciar logs HTTP estándar
        pass

def main():
    server = HTTPServer(("0.0.0.0", PORT), WebhookHandler)
    logging.info(f"🚀 Webhook server corriendo en puerto {PORT}")
    logging.info(f"📡 Endpoint: https://edificio.universojota.tech/webhook/meta/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        logging.info("🛑 Servidor detenido")

if __name__ == "__main__":
    main()
