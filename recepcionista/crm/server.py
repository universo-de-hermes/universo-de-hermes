"""
CRM CJ Medical - Servidor Web (FastAPI)
Panel de asesores con pipeline, historial y respuestas
Sin Jinja2 - HTML embebido + API REST
"""
import json
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from fastapi import FastAPI, Request, HTTPException, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from crm.database import (
    init_db, get_all_clients, get_client_detail, get_or_create_client,
    save_message, update_client_status, verify_advisor,
    get_all_advisors, update_client_data, create_appointment
)

# Cargar .env
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

# ─── Twilio ───
from twilio.rest import Client as TwilioClient
from twilio.twiml.messaging_response import MessagingResponse

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER", "+14155238886")
twilio_client = None
if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    twilio_client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print("✅ Twilio cliente listo")

app = FastAPI(title="CJ Medical CRM")

# ─── HTML EMBEBIDO ───

LOGIN_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CJ Medical - CRM</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .login-card {
            background: white;
            border-radius: 20px;
            padding: 48px 40px;
            width: 400px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        .logo { text-align: center; margin-bottom: 24px; }
        .logo .icon { font-size: 48px; }
        .logo h2 { color: #1a1a2e; font-size: 20px; }
        .login-card h1 { color: #1a1a2e; font-size: 24px; margin-bottom: 4px; }
        .login-card .subtitle { color: #666; font-size: 14px; margin-bottom: 32px; }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; font-size: 13px; font-weight: 600; color: #333; margin-bottom: 6px; }
        .form-group input {
            width: 100%; padding: 12px 16px; border: 2px solid #e0e0e0;
            border-radius: 10px; font-size: 15px; transition: border-color 0.2s;
        }
        .form-group input:focus { outline: none; border-color: #667eea; }
        .btn {
            width: 100%; padding: 14px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; border: none; border-radius: 10px; font-size: 16px; font-weight: 600; cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .btn:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(102,126,234,0.4); }
        .error { background: #ffe0e0; color: #d32f2f; padding: 12px; border-radius: 10px; margin-bottom: 16px; font-size: 14px; text-align: center; }
        .hidden { display: none; }
    </style>
</head>
<body>
    <div class="login-card">
        <div class="logo"><div class="icon">🏥</div><h2>CJ Medical</h2></div>
        <h1>Panel de Asesores</h1>
        <p class="subtitle">Inicia sesión para gestionar las solicitudes</p>
        <div id="errorBox" class="error hidden"></div>
        <form id="loginForm" onsubmit="return doLogin(event)">
            <div class="form-group"><label>Usuario</label><input type="text" id="username" placeholder="admin" required></div>
            <div class="form-group"><label>Contraseña</label><input type="password" id="password" placeholder="••••••" required></div>
            <button type="submit" class="btn">Ingresar</button>
        </form>
    </div>
    <script>
        async function doLogin(e) {
            e.preventDefault();
            const fd = new URLSearchParams();
            fd.set('username', document.getElementById('username').value);
            fd.set('password', document.getElementById('password').value);
            const r = await fetch('/login', { method: 'POST', body: fd, redirect: 'manual' });
            if (r.status === 302) { window.location.href = '/dashboard'; return; }
            const html = await r.text();
            if (html.includes('error')) {
                document.getElementById('errorBox').textContent = 'Usuario o contraseña incorrectos';
                document.getElementById('errorBox').classList.remove('hidden');
            }
        }
    </script>
</body>
</html>
"""


def dashboard_html(advisor_name: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CJ Medical - CRM Dashboard</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
@font-face{{font-family:'Neue Montreal';src:url('/fonts/NeueMontreal-Light.otf') format('opentype');font-weight:300;font-style:normal;font-display:swap;}}
@font-face{{font-family:'Neue Montreal';src:url('/fonts/NeueMontreal-LightItalic.otf') format('opentype');font-weight:300;font-style:italic;font-display:swap;}}
@font-face{{font-family:'Neue Montreal';src:url('/fonts/NeueMontreal-Italic.otf') format('opentype');font-weight:400;font-style:italic;font-display:swap;}}
@font-face{{font-family:'Neue Montreal';src:url('/fonts/NeueMontreal-Medium.otf') format('opentype');font-weight:500;font-style:normal;font-display:swap;}}
:root{{--ink:#0f1a14;--ink-soft:#5b6b62;--line:#e7ece8;--bg:#f4f7f5;--surface:#ffffff;--brand:#1f8a5b;--brand-deep:#0f6e45;--accent:#0f1a14;}}
body{{font-family:'Neue Montreal','Segoe UI',system-ui,sans-serif;background:var(--bg);min-height:100vh;color:var(--ink);letter-spacing:-0.01em;-webkit-font-smoothing:antialiased;}}
@keyframes pp{{0%{{opacity:1}}50%{{opacity:0.4}}100%{{opacity:1}}}}
.navbar{{background:rgba(255,255,255,0.85);backdrop-filter:saturate(180%) blur(14px);border-bottom:1px solid var(--line);padding:0 32px;height:72px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:100;}}
.navbar-brand{{display:flex;align-items:center;gap:14px;font-size:19px;font-weight:500;color:var(--ink);letter-spacing:-0.02em;}}
.navbar-right{{display:flex;align-items:center;gap:18px;}}
.navbar-right span{{font-size:13px;color:var(--ink-soft);font-weight:300;}}
.navbar-right strong{{color:var(--ink);font-weight:500;}}
.btn-logout{{padding:9px 18px;background:transparent;border:1px solid var(--line);border-radius:99px;cursor:pointer;font-size:13px;color:var(--ink-soft);text-decoration:none;font-weight:400;transition:all .18s;}}
.btn-logout:hover{{background:#fdecec;color:#c0392b;border-color:#f3c9c9;}}
.stats-bar{{display:flex;gap:14px;padding:22px 32px 6px;background:transparent;overflow-x:auto;}}
.stat-item{{flex:1;min-width:120px;padding:18px 20px;border-radius:18px;text-align:left;font-size:12px;font-weight:400;color:var(--ink-soft);cursor:pointer;border:1px solid var(--line);background:var(--surface);transition:all .22s cubic-bezier(.2,.8,.2,1);position:relative;overflow:hidden;}}
.stat-item::after{{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:currentColor;opacity:.55;}}
.stat-item:hover{{transform:translateY(-3px);box-shadow:0 12px 28px rgba(15,26,20,0.08);border-color:transparent;}}
.stat-item .count{{font-size:32px;font-weight:500;display:block;margin-bottom:2px;color:var(--ink);letter-spacing:-0.03em;line-height:1;}}
.pipeline{{display:flex;gap:18px;padding:20px 32px 40px;overflow-x:auto;min-height:calc(100vh - 240px);align-items:flex-start;}}
.pipeline-column{{min-width:300px;max-width:340px;flex:1;background:transparent;border-radius:18px;padding:0;}}
.pipeline-column-header{{font-size:13px;font-weight:500;color:var(--ink);margin-bottom:14px;padding:12px 16px;background:var(--surface);border:1px solid var(--line);border-radius:14px;display:flex;justify-content:space-between;align-items:center;letter-spacing:-0.01em;box-shadow:0 2px 8px rgba(15,26,20,0.03);}}
.pipeline-column-header .badge{{background:var(--ink);color:#fff;padding:2px 11px;border-radius:99px;font-size:12px;font-weight:500;min-width:26px;text-align:center;}}
.client-card{{background:var(--surface);border-radius:16px;padding:16px;margin-bottom:12px;cursor:pointer;border:1px solid var(--line);box-shadow:0 1px 2px rgba(15,26,20,0.03);transition:all .22s cubic-bezier(.2,.8,.2,1);}}
.client-card:hover{{border-color:var(--brand);box-shadow:0 10px 26px rgba(31,138,91,0.14);transform:translateY(-3px);}}
.urgent{{border-color:#ff5252!important;box-shadow:0 0 0 1px #ff5252,0 8px 22px rgba(255,82,82,0.18)!important;}}
.client-card .name{{font-size:15px;font-weight:500;color:var(--ink);margin-bottom:4px;letter-spacing:-0.01em;}}
.client-card .meta{{font-size:11px;color:var(--ink-soft);font-weight:300;}}
.client-card .preview{{font-size:12px;color:var(--ink-soft);margin-top:10px;padding-top:10px;border-top:1px solid var(--line);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-weight:300;}}
.channel-badge{{display:inline-block;padding:3px 9px;border-radius:8px;font-size:10px;font-weight:500;margin-bottom:8px;}}
.channel-telegram{{background:#e8f3fb;color:#1f7ac0;}}
.empty-col{{border:1px dashed var(--line);border-radius:14px;padding:22px;text-align:center;font-size:12px;color:#a7b2ab;font-weight:300;}}
.toolbar{{display:flex;gap:12px;padding:6px 32px 4px;background:transparent;align-items:center;flex-wrap:wrap;}}
.tb-search{{flex:1;min-width:220px;padding:12px 18px;border:1px solid var(--line);border-radius:99px;font-size:14px;font-family:inherit;background:var(--surface);color:var(--ink);font-weight:300;transition:border-color .15s,box-shadow .15s;}}
.tb-search::placeholder{{color:#9aa8a0;}}
.tb-search:focus,.tb-date:focus{{outline:none;border-color:var(--brand);box-shadow:0 0 0 3px rgba(31,138,91,0.12);}}
.tb-date{{padding:11px 14px;border:1px solid var(--line);border-radius:12px;font-size:13px;font-family:inherit;background:var(--surface);color:var(--ink-soft);}}
.tb-excel{{padding:12px 22px;background:var(--ink);color:#fff;border:none;border-radius:99px;font-size:13px;font-weight:500;font-family:inherit;cursor:pointer;transition:transform .15s,box-shadow .15s,background .15s;}}
.tb-excel:hover{{background:var(--brand-deep);transform:translateY(-1px);box-shadow:0 8px 20px rgba(15,110,69,0.25);}}
.side-panel{{position:fixed;top:0;right:-600px;width:580px;height:100vh;background:white;box-shadow:-10px 0 40px rgba(0,0,0,0.15);transition:right 0.3s;z-index:200;display:flex;flex-direction:column;}}
.side-panel.open{{right:0;}}
.side-panel-header{{padding:20px 24px;border-bottom:1px solid #eee;display:flex;justify-content:space-between;align-items:flex-start;}}
.side-panel-header h2{{font-size:18px;color:#1a1a2e;}}
.side-panel-header .sub{{font-size:13px;color:#888;margin-top:4px;}}
.btn-close{{background:none;border:none;font-size:24px;cursor:pointer;color:#999;padding:4px;}}
.side-panel-body{{flex:1;overflow-y:auto;padding:20px 24px;}}
.msg{{padding:10px 14px;border-radius:12px;margin-bottom:8px;font-size:14px;line-height:1.5;}}
.msg.client{{background:#e8f0fe;color:#1a1a2e;}}
.msg.bot{{background:#f0f0f0;color:#333;}}
.msg.advisor{{background:#667eea;color:white;}}
.msg .time{{font-size:10px;color:#999;margin-top:4px;display:block;}}
.msg.advisor .time{{color:rgba(255,255,255,0.7);}}
.status-badge{{display:inline-block;padding:4px 12px;border-radius:20px;font-size:11px;font-weight:600;}}
.s-nuevo{{background:#e3f2fd;color:#1565c0;}}
.s-en_conversacion{{background:#fff3e0;color:#e65100;}}
.s-pendiente{{background:#fce4ec;color:#c62828;}}
.s-agendado{{background:#e8f5e9;color:#2e7d32;}}
.s-exitoso{{background:#e8f5e9;color:#1b5e20;}}
.s-no_interesado{{background:#fafafa;color:#888;}}
.btn-status{{padding:6px 14px;border:2px solid;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;background:white;margin:3px;}}
.btn-status:hover{{transform:translateY(-1px);}}
.quick-chips{{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px;}}
.chip{{padding:6px 12px;border:1px solid #d7d9dd;border-radius:16px;background:#f5f6f7;font-size:12px;color:#333;cursor:pointer;transition:all .12s;white-space:nowrap;user-select:none;}}
.chip:hover{{background:#667eea;color:#fff;border-color:#667eea;transform:translateY(-1px);}}
.composer{{background:#fff;border:1px solid #e4e6eb;border-radius:22px;padding:6px 6px 6px 16px;display:flex;align-items:flex-end;gap:8px;box-shadow:0 1px 4px rgba(0,0,0,0.06);transition:border-color .15s,box-shadow .15s;}}
.composer:focus-within{{border-color:#667eea;box-shadow:0 2px 12px rgba(102,126,234,0.18);}}
.composer textarea{{flex:1;border:none;outline:none;resize:none;font-size:14px;font-family:inherit;line-height:1.45;max-height:180px;min-height:24px;padding:8px 0;background:transparent;color:#1a1a2e;overflow-y:auto;}}
.composer textarea::placeholder{{color:#8a8d91;}}
.send-btn{{flex:none;width:40px;height:40px;border-radius:50%;border:none;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;font-size:17px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:transform .12s,box-shadow .12s,opacity .12s;}}
.send-btn:hover:not(:disabled){{transform:scale(1.08);box-shadow:0 4px 14px rgba(102,126,234,0.45);}}
.send-btn:disabled{{opacity:.4;cursor:default;}}
.composer-bar{{display:flex;align-items:center;justify-content:space-between;margin:6px 8px 0;}}
.composer-hint{{font-size:11px;color:#8a8d91;}}
.char-count{{font-size:11px;color:#8a8d91;}}
.char-count.warn{{color:#e65100;font-weight:600;}}
.tools-row{{margin-top:16px;display:flex;gap:8px;flex-wrap:wrap;}}
.btn-reply{{padding:10px 24px;background:linear-gradient(135deg,#667eea,#764ba2);color:white;border:none;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;transition:transform .12s,box-shadow .12s;}}
.btn-reply:hover{{transform:translateY(-2px);box-shadow:0 4px 15px rgba(102,126,234,0.4);}}
.msg{{white-space:pre-wrap;}}
.overlay{{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.3);display:none;z-index:150;}}
.overlay.show{{display:block;}}
.info-grid{{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0;padding:12px;background:#f8f9fa;border-radius:10px;font-size:13px;}}
.info-grid .lbl{{color:#888;}}
.info-grid .val{{color:#1a1a2e;font-weight:600;}}
.toast{{position:fixed;bottom:24px;right:24px;background:#2e7d32;color:white;padding:14px 24px;border-radius:12px;font-size:14px;box-shadow:0 4px 20px rgba(0,0,0,0.2);z-index:300;display:none;}}
.toast.show{{display:block;}}
@media(max-width:768px){{.pipeline{{flex-direction:column;}}.pipeline-column{{min-width:100%;}}.side-panel{{width:100%;right:-100%;}}}}
</style>
</head>
<body>
<nav class="navbar"><div class="navbar-brand"><img src="/logo.png" style="height:76px;margin-right:12px;vertical-align:middle;border-radius:8px;"> CJ Medical · CRM</div><div class="navbar-right"><span>👤 <strong>{advisor_name}</strong></span><a href="/logout" class="btn-logout">Salir</a></div></nav>
<div class="stats-bar" id="statsBar">
<div class="stat-item" style="color:#1f7ac0;" onclick="filter('leads_nuevos')"><span class="count" id="c-leads_nuevos">0</span>Leads Nuevos</div>
<div class="stat-item" style="color:#d98324;" onclick="filter('pendientes_agendar')"><span class="count" id="c-pendientes_agendar">0</span>Pendientes Agendar</div>
<div class="stat-item" style="color:#1f8a5b;" onclick="filter('agendados')"><span class="count" id="c-agendados">0</span>Agendados</div>
<div class="stat-item" style="color:#c0392b;" onclick="filter('pqrs')"><span class="count" id="c-pqrs">0</span>PQRS</div>
<div class="stat-item" style="color:#8a8d91;" onclick="filter('no_interesados')"><span class="count" id="c-no_interesados">0</span>No Interesados</div>
<div class="stat-item" style="color:#0f1a14;" onclick="filter('')"><span class="count" id="c-total">0</span>Todos</div>
</div>
<div class="toolbar">
<input id="searchInput" placeholder="Buscar cliente por nombre o teléfono" oninput="applyFilters()" class="tb-search">
<input id="dateFrom" type="date" onchange="applyFilters()" class="tb-date">
<input id="dateTo" type="date" onchange="applyFilters()" class="tb-date">
<button onclick="exportExcel()" class="tb-excel">Exportar Excel</button>
</div>
<div class="pipeline" id="pipeline"></div>
<div class="overlay" id="overlay" onclick="closePanel()"></div>
<div class="side-panel" id="panel">
<div class="side-panel-header"><div><h2 id="pName">Cliente</h2><div class="sub"><span id="pChannel" class="channel-badge">Telegram</span> <span id="pStatus" class="status-badge">Nuevo</span></div></div><button class="btn-close" onclick="closePanel()">✕</button></div>
<div class="side-panel-body">
<div class="info-grid" id="pInfo"></div>
<h4 style="color:#555;margin:16px 0 8px;font-size:13px;">💬 Conversación</h4>
<div id="pConversation"></div>
<h4 style="color:#555;margin:16px 0 8px;font-size:13px;">📋 Estado</h4>
<div id="pStatusActions"></div>
<h4 style="color:#555;margin:16px 0 8px;font-size:13px;">✏️ Responder</h4>
<div class="quick-chips" id="quickChips"></div>
<div class="composer">
<textarea id="replyInput" rows="1" placeholder="Escribe un mensaje..." oninput="growComposer(this)" onkeydown="composerKey(event)"></textarea>
<button class="send-btn" id="sendBtn" onclick="sendReply()" title="Enviar (Enter)" disabled>➤</button>
</div>
<div class="composer-bar"><span class="composer-hint">Enter para enviar · Shift+Enter para salto de línea</span><span class="char-count" id="charCount">0</span></div>
<div class="tools-row">
<button class="btn-reply" style="background:linear-gradient(135deg,#1565c0,#0d47a1);font-size:12px;padding:8px 16px;" onclick="loadTemplate()">📋 Plantilla confirmación</button>
<button class="btn-reply" style="background:linear-gradient(135deg,#d32f2f,#b71c1c);font-size:12px;padding:8px 16px;" onclick="clearConversation()">🗑️ Borrar conversación</button>
<button class="btn-reply" style="background:linear-gradient(135deg,#d32f2f,#b71c1c);font-size:12px;padding:8px 16px;" onclick="stopAI()">🚫 Detener IA</button><button class="btn-reply" style="background:linear-gradient(135deg,#333,#000);font-size:12px;padding:8px 16px;" onclick="deleteClient()">❌ Eliminar cliente</button>
</div>
<div id="pLog" style="margin-top:16px;padding:12px;background:#fafafa;border-radius:10px;"></div>
</div></div>
<div class="toast" id="toast"></div>
<script src="https://cdn.sheetjs.com/xlsx-0.20.2/package/dist/xlsx.full.min.js"></script>
<script>
let cid=null, flt='', allClients=[];
async function loadPipeline(){{let r=await fetch('/api/clients');allClients=await r.json();applyFilters();loadStats();}}
function applyFilters(){{const q=document.getElementById('searchInput').value.toLowerCase();const df=document.getElementById('dateFrom').value;const dt=document.getElementById('dateTo').value;let filtered=allClients;if(q)filtered=filtered.filter(c=>(c.name||'').toLowerCase().includes(q)||(c.phone||'').includes(q));if(df)filtered=filtered.filter(c=>!c.created_at||c.created_at.split(' ')[0]>=df);if(dt)filtered=filtered.filter(c=>!c.created_at||c.created_at.split(' ')[0]<=dt);if(flt){{const statusMap={{'leads_nuevos':['nuevo','en_conversacion'],'pendientes_agendar':['pendiente'],'agendados':['agendado','exitoso'],'pqrs':['pqrs'],'no_interesados':['no_interesado']}};const validStatuses=statusMap[flt]||[];filtered=filtered.filter(c=>validStatuses.includes(c.status))}}render(filtered);}}
function render(d){{const cols={{'leads_nuevos':[],'pendientes_agendar':[],'agendados':[],'pqrs':[],'no_interesados':[]}};const statusMap={{'nuevo':'leads_nuevos','en_conversacion':'leads_nuevos','pendiente':'pendientes_agendar','agendado':'agendados','exitoso':'agendados','pqrs':'pqrs','no_interesado':'no_interesados'}};d.forEach(c=>{{let mapped=statusMap[c.status||'nuevo']||'leads_nuevos';if(cols[mapped])cols[mapped].push(c)}});let html='';const labels={{'leads_nuevos':['Leads Nuevos','#1f7ac0'],'pendientes_agendar':['Pendientes por Agendar','#d98324'],'agendados':['Agendados','#1f8a5b'],'pqrs':['PQRS','#c0392b'],'no_interesados':['No Interesados','#8a8d91']}};for(let[k,v]of Object.entries(cols)){{let[l,fg]=labels[k];html+='<div class=pipeline-column><div class=pipeline-column-header><span style="display:flex;align-items:center;gap:8px;"><span style="width:9px;height:9px;border-radius:50%;background:'+fg+';display:inline-block;"></span>'+l+'</span> <span class=badge style="background:'+fg+';color:white;">'+v.length+'</span></div>'+(v.length?v.map(c=>card(c)).join(''):'<div class=empty-col>Sin registros</div>')+'</div>'}}document.getElementById('pipeline').innerHTML=html;}}
function card(c){{const n=c.name||'Sin nombre';const t=c.last_message?c.last_message.substring(0,60):'';const tm=c.updated_at?new Date(c.updated_at+'Z').toLocaleString('es-CO',{{hour:'2-digit',minute:'2-digit'}}):'';const urg=c.status==='pendiente'?'<span style=display:inline-block;background:#ff1744;color:white;font-size:10px;font-weight:700;padding:2px 8px;border-radius:10px;margin-left:6px;animation:pp 1.5s infinite;>🔔 Pendiente</span>':'';return'<div class='+(c.status==='pendiente'?'client-card urgent':'client-card')+' onclick="openClient('+c.id+')"><span class=channel-badge channel-telegram>📱 Telegram</span><div class=name>'+n+urg+'</div><div class=meta>🕐 '+tm+' · '+(c.message_count||0)+' msgs</div>'+(t?'<div class=preview>'+t+'</div>':'')+'</div>'}}
async function loadStats(){{let r=await fetch('/api/pipeline/stats');let d=await r.json();for(let[k,v]of Object.entries(d)){{let e=document.getElementById('c-'+k);if(e)e.textContent=v}}}}
function filter(s){{flt=s;applyFilters();}}
async function openClient(id){{cid=id;let r=await fetch('/api/clients/'+id);let c=await r.json();document.getElementById('pName').textContent=(c.name||'Cliente')+(c.ai_disabled?' 🔇':' ');document.getElementById('pChannel').textContent='📱 Telegram';let sb=document.getElementById('pStatus');sb.textContent=c.status||'nuevo';sb.className='status-badge s-'+(c.status||'nuevo');let info='';if(c.appointments&&c.appointments.length){{let a=c.appointments[0];info+='<div><span class=lbl>✨ Servicio:</span> <span class=val>'+(a.service||'—')+'</span></div><div><span class=lbl>📍 Sede:</span> <span class=val>'+(a.city||'')+' '+(a.location||'')+'</span></div><div><span class=lbl>📅 Fecha:</span> <span class=val>'+(a.date_requested||'—')+'</span></div><div><span class=lbl>🕐 Hora:</span> <span class=val>'+(a.time_requested||'—')+'</span></div>'}}
info+='<div><span class=lbl>📱 Celular:</span> <span class=val>'+(c.phone||'—')+'</span></div><div><span class=lbl>📧 Correo:</span> <span class=val>'+(c.email||'—')+'</span></div>';document.getElementById('pInfo').innerHTML=info;let conv=document.getElementById('pConversation');if(c.messages&&c.messages.length){{conv.innerHTML=c.messages.map(m=>{{let rc=m.role==='client'?'client':m.role==='advisor'?'advisor':'bot';let rl=m.role==='client'?'🧑 Cliente':m.role==='advisor'?'👤 Asesor':'🤖 Pepe';let tm=new Date(m.created_at+'Z').toLocaleTimeString('es-CO',{{hour:'2-digit',minute:'2-digit'}});return'<div class="msg '+rc+'"><strong>'+rl+'</strong><br>'+m.content+'<span class=time>'+tm+'</span></div>'}}).join('')}}else conv.innerHTML='<p style=color:#999>No hay mensajes aún.</p>';let sa=document.getElementById('pStatusActions');const ss=[{{k:'pendientes_agendar',l:'⏳ Pendiente Agendar',c:'#e65100'}},{{k:'agendados',l:'✅ Agendado',c:'#2e7d32'}},{{k:'pqrs',l:'🚨 PQRS',c:'#c62828'}},{{k:'no_interesados',l:'🚫 No Interesado',c:'#888'}}];sa.innerHTML=ss.map(s=>'<button class=btn-status style="border-color:'+s.c+';color:'+s.c+'" onclick="changeStatus('+id+',\\''+s.k+'\\')">'+s.l+'</button>').join('');let pl=document.getElementById('pLog');if(c.pipeline_log&&c.pipeline_log.length){{pl.innerHTML='<h4 style=color:#555;font-size:13px;>📋 Historial</h4>'+c.pipeline_log.map(l=>'<div style=font-size:12px;color:#888;padding:4px 0;border-bottom:1px solid #f0f0f0;>'+(l.created_at?new Date(l.created_at+'Z').toLocaleString('es-CO'):'')+' — <b>'+(l.from_status||'?')+'</b> → <b>'+l.to_status+'</b></div>').join('')}}else pl.innerHTML='';document.getElementById('panel').classList.add('open');document.getElementById('overlay').classList.add('show');renderChips();let ri=document.getElementById('replyInput');if(ri){{ri.value='';ri.style.height='auto';}}updateCharCount();}}
function closePanel(){{document.getElementById('panel').classList.remove('open');document.getElementById('overlay').classList.remove('show');cid=null;}}
async function changeStatus(id,s){{const statusMap={{'pendientes_agendar':'pendiente','agendados':'agendado','pqrs':'pqrs','no_interesados':'no_interesado'}};const dbStatus=statusMap[s]||s;let n=prompt('Nota opcional:');await fetch('/api/clients/'+id+'/status',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{status:dbStatus,note:n||''}})}});showToast('✅ Estado actualizado');if(cid===id)openClient(id);loadPipeline();}}
async function sendReply(){{let inp=document.getElementById('replyInput');let c=inp.value.trim();if(!c||!cid)return;let btn=document.getElementById('sendBtn');btn.disabled=true;await fetch('/api/clients/'+cid+'/reply',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{content:c}})}});inp.value='';inp.style.height='auto';updateCharCount();showToast('✅ Respuesta enviada al cliente');openClient(cid);loadPipeline();}}
function growComposer(el){{el.style.height='auto';el.style.height=Math.min(el.scrollHeight,180)+'px';updateCharCount();}}
function updateCharCount(){{let inp=document.getElementById('replyInput');let n=inp.value.length;let cc=document.getElementById('charCount');cc.textContent=n;cc.className='char-count'+(n>900?' warn':'');document.getElementById('sendBtn').disabled=inp.value.trim().length===0;}}
function composerKey(e){{if(e.key==='Enter'&&!e.shiftKey){{e.preventDefault();sendReply();}}}}
function insertChip(t){{let inp=document.getElementById('replyInput');let name=(document.getElementById('pName').textContent||'').trim().split(' ')[0]||'';t=t.replace('{{nombre}}',name);inp.value=inp.value?inp.value+(inp.value.endsWith('\\n')?'':'\\n')+t:t;growComposer(inp);inp.focus();}}
function renderChips(){{const chips=['Hola {{nombre}}, gracias por escribir a CJ Medical.','Con gusto verifico la disponibilidad y te confirmo en un momento.','Tu cita quedó confirmada. Te esperamos.','¿Deseas que te agende para otra fecha u hora?','Cualquier duda adicional, con gusto te ayudo.','Gracias por preferir a CJ Medical. Que tengas un excelente día.'];let el=document.getElementById('quickChips');if(el)el.innerHTML=chips.map(c=>'<span class=chip onclick="insertChip(this.dataset.t)" data-t="'+c.replace(/"/g,'&quot;')+'">'+c.replace('{{nombre}}','nombre').substring(0,32)+(c.length>32?'…':'')+'</span>').join('');}}
async function clearConversation(){{if(!cid||!confirm('¿Eliminar toda la conversación de este cliente?'))return;await fetch('/api/clients/'+cid+'/clear-conversation',{{method:'POST'}});showToast('🗑️ Conversación eliminada');openClient(cid);loadPipeline();}}
async function deleteClient(){{if(!cid||!confirm('¿Eliminar este cliente COMPLETAMENTE? Se borrarán todos sus datos.'))return;await fetch('/api/clients/'+cid+'/delete',{{method:'POST'}});showToast('❌ Cliente eliminado');closePanel();loadPipeline();}}
async function stopAI(){{if(!cid)return;await fetch('/api/clients/'+cid+'/toggle-ai',{{method:'POST'}});showToast('🚫 IA detenida para este cliente');openClient(cid);loadPipeline();}}
async function loadTemplate(){{if(!cid)return;let r=await fetch('/api/clients/'+cid);let c=await r.json();let a=c.appointments&&c.appointments[0]||{{}};
let nm=c.name||'';let sv=a.service||'';let cy=a.city||'';let lo=a.location||'';let dt=a.date_requested||'';let tm=a.time_requested||'';let pr=a.professional||'';
// Siempre intentar extraer del último resumen del bot (más completo y actualizado que los campos guardados)
if(c.messages){{for(let m of c.messages){{if(m.role==='bot'&&m.content.indexOf('📍')>=0){{let s=m.content;
let g=function(p){{let i=s.indexOf(p);if(i<0)return'';let v=s.substring(i+p.length).trim();let e=v.indexOf('\\n');if(e<0)e=v.indexOf('\\r');if(e<0)e=v.length;return v.substring(0,e).trim();}};
cy=cy||g('Ciudad:');let sedeRaw=g('Sede:');if(sedeRaw)lo=sedeRaw;sv=sv||g('Servicio:');dt=dt||g('Fecha:');tm=tm||g('Hora:');
let ng=g('Nombre:');if(ng&&ng.split(' ').length>=nm.split(' ').filter(x=>x).length)nm=ng;
let esp=g('Especialista:');if(esp)pr=esp;}}}}}}
// Si la sede extraída trae "Sede - Dirección" en un solo campo, quedarnos solo con el nombre de la sede
if(lo.indexOf(' - ')>=0)lo=lo.split(' - ')[0].trim();
let name=nm||'[Nombre]';let svc=sv||'[Servicio]';let city=cy||'[Ciudad]';let loc=lo||'[Sede]';let date=dt||'[Fecha]';let time=tm||'[Hora]';
let addr='';if(city==='Bogota'||city==='Bogotá'||loc==='Chico Norte')addr='Cra 11A #96-51 Edificio Oficity Local 102';else if(city==='Medellin'||city==='Medellín'||loc.indexOf('Tesoro')>=0)addr='Parque Comercial El Tesoro, Sótano 4 Plaza Norte, Cra 25A #1a sur - 45, Local 6100, Medellín';
// Auto-detectar especialista
if(!pr){{let s=svc.toLowerCase();let c=city||'';if(s.includes('terapia'))pr=c.includes('Medellin')||c.includes('Medellín')?'Valentina Baquero':'Diana Carolina Ruiz';else if(s.includes('masaje'))pr='Valentina Baquero';else if(s.includes('carbon'))pr=c.includes('Medellin')||c.includes('Medellín')?'Valentina Baquero':'Diana Carolina Ruiz';else if(s.includes('hidra'))pr=c.includes('Medellin')||c.includes('Medellín')?'Valentina Baquero':'Diana Carolina Ruiz';else if(s.includes('casmara'))pr='Valentina Baquero';else if(s.includes('peeling'))pr='Dra. Julieth Arias';else if(s.includes('depilacion')||s.includes('depilación'))pr=c.includes('Medellin')||c.includes('Medellín')?'Valentina Baquero':'Diana Carolina Ruiz';else if(s.includes('micropigment'))pr=c.includes('Bogota')||c.includes('Bogotá')?'Dr. Jorge Cueter':'Dra. Julieth Arias';else if(s.includes('valoracion')||s.includes('valoración'))pr='Dr. Jorge Cueter';else if(s.includes('botox'))pr='Dr. Jorge Cueter';else if(s.includes('radiofrecuencia'))pr='Dr. Jorge Cueter';else if(s.includes('exosomas'))pr='Dr. Jorge Cueter';}}
let prof=pr||'[Especialista]';
let tpl='Confirmación de cita CJ Medical\\n\\nNombre: '+name+'\\nServicio: '+svc+'\\nSede: '+(loc||'')+(addr?'\\nDirección: '+addr:'')+'\\nFecha: '+date+'\\nHora: '+time+(prof?'\\nEspecialista: '+prof:'')+'\\n\\n¿Deseas confirmar tu cita? 😊';let ri=document.getElementById('replyInput');ri.value=tpl;growComposer(ri);ri.focus();showToast('Plantilla cargada - puedes editarla');}}
function showToast(m){{let t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),3000);}}
function exportExcel(){{if(typeof XLSX==='undefined'){{showToast('⏳ Cargando librería...');setTimeout(exportExcel,500);return}}let data=allClients.map(c=>{{let s=c.appointments&&c.appointments[0]||{{}};return{{'Nombre':c.name||'','Teléfono':c.phone||'','Correo':c.email||'','Documento':c.document||'','Servicio':s.service||'','Ciudad':s.city||'','Sede':s.location||'','Especialista':s.professional||'','Fecha':s.date_requested||'','Hora':s.time_requested||'','Estado':c.status||'','Creado':c.created_at||''}}}});let ws=XLSX.utils.json_to_sheet(data);let wb=XLSX.utils.book_new();XLSX.utils.book_append_sheet(wb,ws,'Clientes');// Auto ajustar ancho de columnas
let cols=Object.keys(data[0]||{{}}).map(k=>({{wch:Math.max(k.length,20)}}));ws['!cols']=cols;XLSX.writeFile(wb,'CJMedical_Clientes_'+new Date().toISOString().slice(0,10)+'.xlsx');showToast('✅ Excel descargado');}}
setInterval(loadPipeline,10000);loadPipeline();
</script>
</body>
</html>"""


# ─── Autenticación ───

def get_advisor(request: Request):
    advisor_json = request.cookies.get("advisor")
    if not advisor_json:
        return None
    try:
        return json.loads(advisor_json)
    except:
        return None


# ─── Rutas ───

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    advisor = get_advisor(request)
    if advisor:
        return RedirectResponse("/dashboard")
    # Check error query param
    error = request.query_params.get("error", "")
    html = LOGIN_HTML
    if error:
        html = html.replace('class="hidden"', '', 1)
    return HTMLResponse(html)


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    advisor = verify_advisor(username, password)
    if not advisor:
        return RedirectResponse("/?error=1", status_code=302)
    response = RedirectResponse("/dashboard", status_code=302)
    response.set_cookie(key="advisor", value=json.dumps(advisor), httponly=True, max_age=86400 * 7)
    return response


@app.get("/logout")
async def logout():
    response = RedirectResponse("/", status_code=302)
    response.delete_cookie("advisor")
    return response


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    advisor = get_advisor(request)
    if not advisor:
        return RedirectResponse("/")
    return HTMLResponse(dashboard_html(advisor["name"]))


# ─── API ───

@app.get("/api/clients")
async def api_clients(status: str = None):
    # Mapear nombres de columnas a estados reales en DB
    status_map = {
        "leads_nuevos": ["nuevo", "en_conversacion"],
        "pendientes_agendar": ["pendiente"],
        "agendados": ["agendado", "exitoso"],
        "pqrs": ["pqrs"],
        "no_interesados": ["no_interesado"],
    }
    if status and status in status_map:
        all_clients = get_all_clients(None)
        filtered = [c for c in all_clients if c["status"] in status_map[status]]
        clients = filtered
    elif status:
        clients = get_all_clients(status)
    else:
        clients = get_all_clients(None)
    # Incluir primera cita de cada cliente para export
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    result = []
    for c in clients:
        client_dict = dict(c)
        cursor = conn.execute("SELECT * FROM appointments WHERE client_id = ? ORDER BY created_at DESC LIMIT 1", (c["id"],))
        row = cursor.fetchone()
        client_dict["appointments"] = [dict(row)] if row else []
        result.append(client_dict)
    conn.close()
    return JSONResponse(result)


@app.get("/api/clients/{client_id}")
async def api_client_detail(client_id: int):
    client = get_client_detail(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    # Convertir datetimes a string
    if client.get("messages"):
        for m in client["messages"]:
            if isinstance(m.get("created_at"), str):
                pass  # ya es string
    # Asegurar campo ai_disabled
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ai_disabled FROM clients WHERE id = ?", (client_id,))
    row = cursor.fetchone()
    client["ai_disabled"] = bool(row["ai_disabled"]) if row else False
    conn.close()
    return JSONResponse(client)


@app.post("/api/clients/{client_id}/status")
async def api_update_status(client_id: int, request: Request):
    data = await request.json()
    advisor = get_advisor(request)
    advisor_name = advisor["name"] if advisor else "Sistema"
    update_client_status(client_id, data.get("status"), advisor=advisor_name, note=data.get("note", ""))

    if data.get("status") == "agendado":
        client = get_client_detail(client_id)
        if client and client.get("appointments"):
            conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
            conn.execute("UPDATE appointments SET status = 'agendado' WHERE client_id = ? AND status = 'pendiente'", (client_id,))
            conn.commit()
            conn.close()

    return JSONResponse({"ok": True})


@app.post("/api/clients/{client_id}/clear-conversation")
async def api_clear_conversation(client_id: int):
    """Elimina los mensajes de un cliente (para pruebas)."""
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    conn.execute("DELETE FROM messages WHERE client_id = ?", (client_id,))
    conn.execute("DELETE FROM pending_replies WHERE client_id = ?", (client_id,))
    conn.commit()
    conn.close()
    return JSONResponse({"ok": True, "message": "Conversación eliminada"})

@app.post("/api/clients/{client_id}/toggle-ai")
async def api_toggle_ai(client_id: int):
    """Activa/desactiva la IA para un cliente sin cambiar su columna."""
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT ai_disabled FROM clients WHERE id = ?", (client_id,))
    row = cursor.fetchone()
    current = row["ai_disabled"] if row else 0
    new_val = 1 - current
    conn.execute("UPDATE clients SET ai_disabled = ? WHERE id = ?", (new_val, client_id))
    conn.commit()
    conn.close()
    status = "desactivada" if new_val else "activada"
    return JSONResponse({"ok": True, "ai_disabled": bool(new_val), "message": f"IA {status}"})

@app.post("/api/clients/{client_id}/delete")
async def api_delete_client(client_id: int):
    """Elimina un cliente completo con todos sus datos (para pruebas)."""
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    conn.execute("DELETE FROM pending_replies WHERE client_id = ?", (client_id,))
    conn.execute("DELETE FROM pipeline_log WHERE client_id = ?", (client_id,))
    conn.execute("DELETE FROM appointments WHERE client_id = ?", (client_id,))
    conn.execute("DELETE FROM messages WHERE client_id = ?", (client_id,))
    conn.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    conn.commit()
    conn.close()
    return JSONResponse({"ok": True})

@app.post("/api/clients/{client_id}/reply")
async def api_reply_client(client_id: int, request: Request):
    data = await request.json()
    content = data.get("content", "").strip()
    advisor = get_advisor(request)
    if not content:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")

    save_message(client_id, "advisor", content, channel="telegram")

    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    conn.execute(
        "INSERT INTO pending_replies (client_id, content, advisor_name) VALUES (?, ?, ?)",
        (client_id, content, advisor["name"] if advisor else "Asesor")
    )
    conn.commit()
    conn.close()

    return JSONResponse({"ok": True, "message": "Respuesta registrada"})


@app.get("/api/pipeline/stats")
async def pipeline_stats():
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status, COUNT(*) as count FROM clients GROUP BY status")
    rows = cursor.fetchall()
    raw = {row["status"]: row["count"] for row in rows}
    conn.close()

    # Mapear a 4 columnas: leads_nuevos, pendientes_agendar, agendados, no_interesados
    stats = {
        "leads_nuevos": raw.get("nuevo", 0) + raw.get("en_conversacion", 0),
        "pendientes_agendar": raw.get("pendiente", 0),
        "agendados": raw.get("agendado", 0) + raw.get("exitoso", 0),
        "pqrs": raw.get("pqrs", 0),
        "no_interesados": raw.get("no_interesado", 0),
        "total": sum(raw.values()),
    }
    return JSONResponse(stats)


@app.get("/fonts/{font_name}")
async def serve_font(font_name: str):
    if not font_name.endswith(".otf") or "/" in font_name or "\\" in font_name:
        return JSONResponse({"error": "invalid"}, status_code=400)
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", font_name)
    if os.path.exists(font_path):
        return FileResponse(font_path, media_type="font/otf")
    return JSONResponse({"error": "Fuente no encontrada"}, status_code=404)


@app.get("/logo.png")
async def logo():
    logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
    if os.path.exists(logo_path):
        file_size = os.path.getsize(logo_path)
        print(f"📸 Sirviendo logo: {logo_path} ({file_size} bytes)")
        return FileResponse(logo_path, media_type="image/png")
    print(f"❌ Logo no encontrado en: {logo_path}")
    return JSONResponse({"error": "Logo no encontrado"}, status_code=404)


# ─── Twilio Webhook ───
@app.post("/api/twilio/whatsapp")
async def twilio_whatsapp_webhook(request: Request):
    """Recibe mensajes entrantes de WhatsApp via Twilio y responde por TwiML"""
    import logging
    logger = logging.getLogger("twilio-webhook")
    
    form = await request.form()
    from_wa = form.get("From", "")  # Ej: "whatsapp:+573001234567"
    body = form.get("Body", "").strip()
    
    if not body or not from_wa:
        return HTMLResponse(content=str(MessagingResponse()), media_type="application/xml")
    
    # Extraer número (quitar prefijo "whatsapp:+")
    phone = from_wa.replace("whatsapp:", "").replace("+", "").strip()
    logger.info(f"📩 Twilio WhatsApp de {phone}: {body[:60]}")
    
    resp = MessagingResponse()
    
    try:
        # Obtener o crear cliente
        client = get_or_create_client(phone, name=phone)
        
        # Guardar mensaje del cliente
        save_message(client["id"], "client", body, channel="whatsapp")
        
        # Actualizar estado
        if client["status"] in ("nuevo",):
            update_client_status(client["id"], "en_conversacion", "Pepe Bot")
        
        # Detectar PQRS
        pqrs_kw = ["queja", "reclamo", "me quejo", "pqrs", "inconforme", "cobro indebido",
                "mala atencion", "mal servicio"]  # «problema» y «devolucion» salieron:
    # eran demasiado comunes y mandaban al cliente a PQRS sin retorno
        if any(p in body.lower() for p in pqrs_kw):
            update_client_status(client["id"], "pqrs", "Pepe Bot")
        
        # Obtener historial y respuesta de IA
        from crm.database import get_conversation
        history = get_conversation(client["id"])
        messages_for_ai = []
        for msg in history[-20:]:
            role = "user" if msg["role"] == "client" else "assistant"
            messages_for_ai.append({"role": role, "content": msg["content"]})
        
        # Llamar a la IA - SINCrono (no espera internet del server)
        reply = None
        # Importar solo el SYSTEM_PROMPT para respuesta manual
        try:
            from main import ask_pepe, SYSTEM_PROMPT
            reply = await ask_pepe(body, messages_for_ai,
                                   telefono=str(client.get("phone") or ""),
                                   client_id=client["id"])
        except Exception as e:
            logger.error(f"Error IA: {e}")
            reply = None
        
        if not reply:
            # Respuesta manual de bienvenida cuando la IA no está disponible
            reply = """Hola, gracias por escribir a CJ Medical. 👋

Somos un departamento médico especializado en el cuidado y recuperación de tus cejas.

¿Desde qué ciudad nos contactas: Bogotá o Medellín?"""
            logger.info("Usando respuesta manual (IA no disponible)")
        
        # Guardar respuesta del bot
        save_message(client["id"], "bot", reply, channel="whatsapp")
        
        # Responder via TwiML - Twilio entrega el mensaje automáticamente
        msg_resp = resp.message(body=reply)
        logger.info(f"✅ Respuesta enviada por TwiML a {phone}")
        
    except Exception as e:
        logger.error(f"Error procesando mensaje Twilio: {e}")
        resp.message(body="Gracias por contactar a CJ Medical. En breve un asesor te atenderá.")
    
    return HTMLResponse(content=str(resp), media_type="application/xml")


# ─── EvolutionAPI Webhook ───
EVOLUTION_API_KEY = "pepe_cj_medical_2026"
EVOLUTION_API_BASE = "http://host.docker.internal:8080"
EVOLUTION_INSTANCE = "pepe"

@app.post("/api/evolution/whatsapp")
async def evolution_whatsapp_webhook(request: Request):
    """Recibe mensajes entrantes de WhatsApp via EvolutionAPI y responde"""
    import logging, httpx
    logger = logging.getLogger("evolution-webhook")
    
    try:
        body_data = await request.json()
    except Exception:
        return JSONResponse({"status": "error", "message": "invalid json"}, status_code=400)
    
    logger.info(f"📩 EvolutionAPI event: {body_data.get('event')}")
    
    # Solo procesar MESSAGES_UPSERT que NO sean de salida
    if body_data.get("event") != "MESSAGES_UPSERT":
        return JSONResponse({"status": "ok"})
    
    data = body_data.get("data", {})
    key = data.get("key", {})
    
    # Ignorar mensajes enviados por nosotros mismos
    if key.get("fromMe", True):
        return JSONResponse({"status": "ok", "note": "skip own message"})
    
    # Extraer número de teléfono del remoteJid (formato: 573001234567@s.whatsapp.net)
    remote_jid = key.get("remoteJid", "")
    phone = remote_jid.split("@")[0].strip()
    if not phone:
        logger.warning("⚠️ No se pudo extraer teléfono del remoteJid")
        return JSONResponse({"status": "ok", "note": "no phone"})
    
    # Extraer texto del mensaje
    message = data.get("message", {})
    msg_text = (message.get("conversation", "") or 
                message.get("extendedTextMessage", {}).get("text", "") or
                "").strip()
    
    if not msg_text:
        return JSONResponse({"status": "ok", "note": "empty message"})
    
    push_name = data.get("pushName", phone)
    logger.info(f"📨 Evolution WhatsApp de {phone} ({push_name}): {msg_text[:60]}")
    
    try:
        # Obtener o crear cliente
        client = get_or_create_client(phone, name=push_name)
        
        # Guardar mensaje del cliente
        save_message(client["id"], "client", msg_text, channel="whatsapp")
        
        # Actualizar estado
        if client["status"] in ("nuevo",):
            update_client_status(client["id"], "en_conversacion", "Pepe Bot")
        
        # PQRS
        pqrs_kw = ["queja", "reclamo", "me quejo", "pqrs", "inconforme", "cobro indebido",
                "mala atencion", "mal servicio"]  # «problema» y «devolucion» salieron:
    # eran demasiado comunes y mandaban al cliente a PQRS sin retorno
        if any(p in msg_text.lower() for p in pqrs_kw):
            update_client_status(client["id"], "pqrs", "Pepe Bot")
        
        # Obtener historial
        from crm.database import get_conversation
        history = get_conversation(client["id"])
        messages_for_ai = []
        for msg in history[-20:]:
            role = "user" if msg["role"] == "client" else "assistant"
            messages_for_ai.append({"role": role, "content": msg["content"]})
        
        # Llamar a la IA
        reply = None
        try:
            from main import ask_pepe, SYSTEM_PROMPT
            reply = await ask_pepe(msg_text, messages_for_ai,
                                   telefono=phone, client_id=client["id"])
        except Exception as e:
            logger.error(f"Error IA: {e}")
            reply = None
        
        if not reply:
            reply = """Hola, gracias por escribir a CJ Medical. 👋

Somos un departamento médico especializado en el cuidado y recuperación de tus cejas.

¿Desde qué ciudad nos contactas: Bogotá o Medellín?"""
        
        # Guardar respuesta del bot
        save_message(client["id"], "bot", reply, channel="whatsapp")
        
        # Enviar respuesta por EvolutionAPI
        async with httpx.AsyncClient(timeout=15) as hclient:
            evo_resp = await hclient.post(
                f"{EVOLUTION_API_BASE}/message/sendText/{EVOLUTION_INSTANCE}",
                json={
                    "number": phone,
                    "text": reply,
                    "delay": 1000,
                },
                headers={
                    "apikey": EVOLUTION_API_KEY,
                    "Content-Type": "application/json"
                }
            )
            logger.info(f"✅ Respuesta enviada por EvolutionAPI a {phone} (status: {evo_resp.status_code})")
        
    except Exception as e:
        logger.error(f"Error procesando mensaje EvolutionAPI: {e}")
    
    return JSONResponse({"status": "ok"})


@app.get("/qr")
async def qr_page():
    qr_html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "qr-page.html")
    if os.path.exists(qr_html_path):
        with open(qr_html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(f.read())
    return HTMLResponse("<h2>QR no disponible</h2><p>Espera a que el bot genere el QR.</p>")


@app.get("/wa_qr.png")
async def wa_qr_image():
    qr_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wa_qr.png")
    if os.path.exists(qr_path):
        return FileResponse(qr_path, media_type="image/png")
    return JSONResponse({"error": "QR no generado aun"}, status_code=404)


@app.get("/wa_qr_check")
async def wa_qr_check():
    ready_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wa_ready.txt")
    if os.path.exists(ready_path):
        with open(ready_path) as f:
            status = f.read().strip()
        if status == "connected" or status.startswith("+"):
            return {"status": "connected", "phone": status if status.startswith("+") else ""}
        if status == "timeout":
            return {"status": "timeout"}
    return {"status": "waiting"}


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Evita que el CRM se caiga por errores no manejados."""
    print(f"Error no manejado: {exc}")
    return JSONResponse({"error": str(exc)}, status_code=500)

@app.on_event("startup")
async def startup():
    init_db()
    # Asegurar tabla pending_replies
    conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pending_replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            content TEXT NOT NULL,
            advisor_name TEXT,
            sent INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("✅ CRM CJ Medical listo en http://localhost:8000")
    print("   Usuario: admin / Contraseña: admin123")


if __name__ == "__main__":
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)