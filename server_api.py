#!/usr/bin/env python3
"""
Command Center API Server — Metaverso
Lee el estado desde status/agent_status.json (donde Houdini y Pepe escriben)
y lo sirve al HTML 3D. También acepta POST para asignar/completar tareas.
"""
import json, os, math, time, threading, http.server, random, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
STATUS_FILE = os.path.join(ROOT, "status", "agent_status.json")
PORT = int(os.environ.get("PORT", 3000))

# ── Layout (mirrors the HTML) ──
L0 = -11.2
LB = 0
LAYOUT = {
    "houdini":    [0, L0, -9.3, 0],
    "gmail":      [-13, L0, -6.6, 0.35],
    "telegram":   [-9.4, L0, -2.2, -0.3],
    "tts":        [-13.4, L0, -1.2, 0.5],
    "whatsapp2":  [-8.6, L0, -6.9, -0.5],
    "sheets":     [13, L0, -6.6, -0.35],
    "drive":      [9.4, L0, -2.2, 0.3],
    "calendar":   [13.4, L0, -1.2, -0.5],
    "dashboard":  [9.6, L0, 7.4, 0.25],
    "design":     [13.4, L0, 8.2, -0.25],
    "recep":      [0, LB, -2.4, 0],
    "recep-cal":  [-6.6, LB, 3.2, 0.3],
    "wa-sender":  [6.6, LB, 3.2, -0.3],
    "handoff":    [-11, LB, -3.4, 0.8],
    "cm-cjcol":   [0, 11.2, -2.4, 0],  # L2 = 11.2
    "cm-content": [-6.6, 11.2, 3.2, 0.3],
    "cm-ig":      [6.6, 11.2, 3.2, -0.3],
    "cm-fb":      [10, 11.2, 3.2, -0.3],
    "cm-analytics": [-3.8, 11.2, -8.5, 0.2],
    "cm-shopify":  [-10.5, 11.2, -8.5, -0.3],
    "cm-metaads":  [10.5, 11.2, -8.5, 0.3],
}

TASK_OPTIONS = {
    "houdini": ["Planificar cadena de tareas", "Delegando a sub-agentes", "Comprobando estado de flota", "Procesando solicitud del jefe"],
    "gmail": ["Clasificando bandeja de entrada", "Enviando correo", "Revisando adjuntos", "Buscando correo de Carlos"],
    "telegram": ["Respondiendo alertas del canal", "Enviando notificación", "Programando recordatorio"],
    "tts": ["Sintetizando resumen diario", "Generando audio de respuesta", "Procesando comando de voz"],
    "whatsapp2": ["Integración pendiente"],
    "sheets": ["Actualizando registro operativo", "Normalizando rangos", "Generando hoja de membresías"],
    "drive": ["Versionando adjuntos nuevos", "Subiendo archivo a Drive", "Sincronizando carpeta"],
    "calendar": ["Reagendando cita de las 15:00", "Verificando disponibilidad", "Consultando espacios libres"],
    "dashboard": ["Recalculando latencia y coste", "Generando reporte", "Publicando tablero de métricas"],
    "design": ["Exportando pieza de campaña", "Maquetando plantilla", "Generando HTML corporativo"],
    "recep": ["Atendiendo chat entrante", "Capturando datos de cliente", "Calificando intención de consulta"],
    "recep-cal": ["Reservando turno del jueves", "Verificando agenda", "Buscando espacios disponibles"],
    "wa-sender": ["Enviando confirmaciones", "Programando plantilla", "Verificando estado de entrega"],
    "handoff": ["Escalando caso a persona", "Preparando contexto", "Transfiriendo sesión"],
    "cm-cjcol": ["Gestionando redes sociales", "Monitoreando menciones", "Respondiendo a clientes", "Analizando engagement"],
    "cm-content": ["Creando publicaciones", "Diseñando pieza visual", "Programando contenido", "Aprobando copy"],
    "cm-ig": ["Escuchando comentarios en IG", "Respondiendo en Instagram", "Detectando tendencias IG", "Reportando engagement IG"],
    "cm-fb": ["Escuchando comentarios en FB", "Respondiendo en Facebook", "Detectando tendencias FB", "Reportando engagement FB"],
    "cm-analytics": ["Calculando engagement", "Generando informe semanal", "Exportando KPI", "Analizando conversión"],
    "cm-shopify": ["Gestionando pedidos", "Actualizando inventario", "Revisando catálogo", "Generando reporte de ventas"],
    "cm-metaads": ["Optimizando campañas", "Ajustando presupuesto", "Analizando audiencias", "Generando reporte de pauta"],
}

# ── Track previous state to detect changes (for flow tracking) ──
_prev_status = {}
_flow_history = []  # list of flow steps for the UI

def compute_home_away(aid):
    x, y, z, rot = LAYOUT[aid]
    home_x = x + math.sin(rot) * 1.5
    home_z = z + math.cos(rot) * 1.5
    away_x = x + math.sin(rot) * 3.2
    away_z = z + math.cos(rot) * 3.2
    return {"x": home_x, "z": home_z}, {"x": away_x, "z": away_z}

def load_status():
    """Load agent status from the shared JSON file."""
    try:
        with open(STATUS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# ── Grace period: keep agent "active" for 10s after status changes to idle ──
_last_active = {}  # aid -> timestamp when it was last seen as active
_ACTIVE_GRACE = 10  # seconds

def build_status_payload():
    """Build the payload the HTML expects. Includes walk_x/walk_z from the JSON."""
    global _last_active
    raw = load_status()
    out = {}
    now = time.time()
    for aid in LAYOUT:
        s = raw.get(aid, {})
        doing = s.get("doing", "")
        task = s.get("task", "")
        status = s.get("status", "idle")
        walk_x = s.get("walk_x")
        walk_z = s.get("walk_z")
        active = status in ("active", "working")
        
        # If currently active, record timestamp
        if active:
            _last_active[aid] = now
        else:
            # Grace period: still show as active if recently active
            if aid in _last_active and (now - _last_active[aid]) < _ACTIVE_GRACE:
                active = True

        entry = {
            "active": active,
            "doing": doing or task or "—",
            "task": task or "—",
        }
        if walk_x is not None and walk_z is not None:
            entry["walk_x"] = walk_x
            entry["walk_z"] = walk_z

        # Detect changes for flow tracking
        global _prev_status
        prev = _prev_status.get(aid, {})
        if active and prev.get("status") != "active":
            _flow_history.append({
                "agent": aid,
                "doing": doing,
                "time": time.time(),
                "type": "started"
            })
        if not active and prev.get("status") == "active":
            _flow_history.append({
                "agent": aid,
                "doing": "Completado",
                "time": time.time(),
                "type": "completed"
            })
        _prev_status[aid] = s
        out[aid] = entry

    # Clean old flow entries (>30s)
    now = time.time()
    _flow_history[:] = [f for f in _flow_history if now - f["time"] < 30]

    return out

def write_status(agent_id, **fields):
    """Write updated status back to the shared JSON file."""
    data = load_status()
    if agent_id not in data:
        data[agent_id] = {"name": agent_id.upper(), "color": "#888", "team": "?"}
    data[agent_id].update(fields)
    data[agent_id]["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    os.makedirs(os.path.dirname(STATUS_FILE), exist_ok=True)
    with open(STATUS_FILE, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# ── Flow endpoint data ──
def get_flow():
    """Return recent flow steps for the UI."""
    now = time.time()
    return [f for f in _flow_history if now - f["time"] < 30]

# ── HTTP handler ──
class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        try:
            super().__init__(*args, directory=ROOT, **kwargs)
        except Exception:
            pass

    def do_GET(self):
        try:
            if self.path == "/api/status":
                self.send_json(build_status_payload())
            elif self.path == "/api/flow":
                self.send_json(get_flow())
            else:
                super().do_GET()
        except Exception:
            pass

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8") if length else "{}"
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                data = {}

            if self.path == "/api/assign":
                aid = data.get("agent")
                task = data.get("task", "")
                if aid not in LAYOUT:
                    self.send_json({"error": f"unknown: {aid}"}, 404)
                    return
                home, _ = compute_home_away(aid)
                write_status(aid, doing=task or random.choice(TASK_OPTIONS.get(aid,["—"])),
                            task=task or "—", status="active",
                            walk_x=home["x"], walk_z=home["z"])
                self.send_json({"ok": True, "agent": aid})

            elif self.path == "/api/complete":
                aid = data.get("agent")
                if aid not in LAYOUT:
                    self.send_json({"error": f"unknown: {aid}"}, 404)
                    return
                write_status(aid, doing="En espera", task="—", status="idle",
                            walk_x=None, walk_z=None)
                self.send_json({"ok": True, "agent": aid})

            elif self.path == "/api/batch":
                agents_data = data.get("agents", {})
                results = {}
                for aid, task in agents_data.items():
                    if aid not in LAYOUT:
                        results[aid] = {"error": "unknown"}
                        continue
                    home, _ = compute_home_away(aid)
                    write_status(aid, doing=task or random.choice(TASK_OPTIONS.get(aid,["—"])),
                                task=task or "—", status="active",
                                walk_x=home["x"], walk_z=home["z"])
                    results[aid] = {"ok": True}
                self.send_json({"ok": True, "results": results})

            elif self.path == "/api/fire":
                """Hermes / Telegram endpoint: triggers a full workflow sequence."""
                user_text = data.get("text", "")
                # Detect agent targets from the text
                agent_map = {
                    "calendario":"calendar","agenda":"calendar","cita":"calendar","evento":"calendar","reunion":"calendar","citar":"calendar","programar":"calendar",
                    "correo":"gmail","email":"gmail","gmail":"gmail","mail":"gmail","enviar":"gmail","envía":"gmail","envio":"gmail",
                    "telegram":"telegram","whatsapp":"whatsapp2",
                    "sheets":"sheets","excel":"sheets","hoja":"sheets",
                    "drive":"drive","archivo":"drive","documento":"drive",
                    "diseño":"design","diseñ":"design","diseña":"design","disen":"design","html":"design","pagina":"design","pag":"design","landing":"design","web":"design","interfaz":"design","ui":"design",
                    "dashboar":"dashboard","panel":"dashboard","membres":"dashboard","grafico":"dashboard","report":"dashboard",
                }
                targets = []
                for word, aid in agent_map.items():
                    if word in user_text.lower():
                        targets.append(aid)
                if not targets:
                    targets = ["houdini"]
                # Dedupe preserving order
                seen = set()
                targets = [t for t in targets if not (t in seen or seen.add(t))]
                
                # Mark flow in shared state
                flow_steps = []
                prev_pos = None
                for i, aid in enumerate(targets):
                    home, _ = compute_home_away(aid)
                    flow_steps.append({"agent": aid, "home_x": home["x"], "home_z": home["z"]})
                    # First: Houdini walks/teleports to this agent
                    if i == 0 and aid != "houdini":
                        # Houdini goes to first agent
                        write_status("houdini", doing=f"🚶 Desplazándose a {aid}",
                                    task=f"Paso 1: {aid}", status="active",
                                    walk_x=home["x"], walk_z=home["z"])
                    write_status(aid, doing=f"Asignado por jefe: {user_text[:40]}",
                                task=user_text[:80], status="active",
                                walk_x=home["x"], walk_z=home["z"])
                    prev_pos = home
                write_status("flow", steps=flow_steps, active=True)
                self.send_json({"ok": True, "targets": targets, "steps": len(flow_steps)})

            else:
                self.send_json({"error": "unknown endpoint"}, 404)
        except Exception:
            pass

    def send_json(self, obj, code=200):
        try:
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(obj).encode("utf-8"))
        except Exception:
            pass

    def log_message(self, fmt, *args):
        pass

if __name__ == "__main__":
    http.server.HTTPServer.allow_reuse_address = True
    server_started = False
    while not server_started:
        try:
            srv = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
            server_started = True
        except OSError:
            print(f"❌ Puerto {PORT} ocupado, reintentando...", flush=True)
            time.sleep(2)
    
    print(f"🎩 Metaverso API → http://localhost:{PORT}", flush=True)
    print(f"   📡 Status: /api/status", flush=True)
    print(f"   🔥 Fire:   POST /api/fire", flush=True)
    print(f"   📋 Flow:   /api/flow", flush=True)
    print(f"   🏢 HTML:   /Command%20Center%20Oficina.html", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n🎩 Servidor detenido.", flush=True)
        srv.shutdown()