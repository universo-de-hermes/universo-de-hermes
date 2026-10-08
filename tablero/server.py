import json, os
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import hashlib, hmac

DATA_DIR = '/root/universo/tablero/data'
USERS = {
    'admincj': {'password': 'cejas2026', 'role': 'admin'},
}
SECRET = 'universo_hermes_2026_tablero_secret_key'
EXCEL_PATH = os.path.join(DATA_DIR, 'datos.xlsx')

INJECT_SCRIPT = '''<script>
(function(){
var A=window.location.pathname.startsWith('/tablero')?'/tablero':'';
var t=localStorage.getItem('tablero_token');
if(!t||t==='null'){window.location.href=A+'/login';return}
document.addEventListener('DOMContentLoaded',function(){
var origCargar=window.cargar;
window.cargar=async function(files){
if(origCargar) await origCargar(files);
if(files&&files.length){var f=files[0];if(f.name.match(/\.(xlsx|xls)$/i)){fetch(A+'/api/upload',{method:'POST',headers:{'Authorization':'Bearer '+t},body:f}).catch(function(){})}}}
fetch(A+'/api/status',{headers:{'Authorization':'Bearer '+t}}).then(function(r){return r.json()}).then(function(d){
if(!d.ok){localStorage.removeItem('tablero_token');window.location.href=A+'/login'}
window.__tablero_role=d.role;
if(d.has_data){fetch(A+'/api/excel',{headers:{'Authorization':'Bearer '+t}}).then(function(r){if(!r.ok)throw'no data';return r.blob()}).then(function(b){var f=new File([b],'datos.xlsx',{type:'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'});if(typeof window.cargar!=='undefined'){window.cargar([f])}}).catch(function(){})}}).catch(function(){})});
})();
</script>'''

def make_token(username, role):
    payload = '%s:%s:%.1f' % (username, role, datetime.now().timestamp() + 86400)
    sig = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()[:16]
    return '%s:%s' % (payload, sig)

def verify_token(token):
    try:
        parts = token.split(':')
        if len(parts) != 4: return None
        username, role, exp, sig = parts
        payload = '%s:%s:%s' % (username, role, exp)
        expected = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest()[:16]
        if sig != expected: return None
        if float(exp) < datetime.now().timestamp(): return None
        return {'username': username, 'role': role}
    except:
        return None

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)
        
        if path == '/login':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            with open('/root/universo/tablero/login.html', 'rb') as f:
                self.wfile.write(f.read())
            return
        
        if path == '/':
            token = self.headers.get('Authorization', '').replace('Bearer ', '')
            if qs.get('token'): token = qs['token'][0]
            user = verify_token(token)
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            with open('/root/universo/tablero-agendamiento.html', 'rb') as f:
                html = f.read()
            html = html.replace(b'</head>', INJECT_SCRIPT.encode() + b'</head>')
            self.wfile.write(html)
            return
        
        if path == '/api/status':
            token = self.headers.get('Authorization', '').replace('Bearer ', '')
            user = verify_token(token)
            if not user:
                self.send_json({'ok': False, 'error': 'No autorizado'})
                return
            exists = os.path.exists(EXCEL_PATH)
            self.send_json({
                'ok': True, 'user': user['username'],
                'role': user['role'], 'has_data': exists
            })
            return
        
        if path == '/api/excel':
            token = self.headers.get('Authorization', '').replace('Bearer ', '')
            user = verify_token(token)
            if not user:
                self.send_json({'ok': False, 'error': 'No autorizado'})
                return
            if os.path.exists(EXCEL_PATH):
                self.send_response(200)
                self.send_header('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Disposition', 'inline; filename=datos.xlsx')
                self.end_headers()
                with open(EXCEL_PATH, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_json({'ok': False, 'error': 'No hay datos aun. Admin debe subir Excel.'})
            return
        
        self.send_json({'ok': False, 'error': 'Ruta no encontrada'})

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        
        if path == '/api/login':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length)) if length else {}
            user = body.get('user', '')
            pwd = body.get('password', '')
            if user in USERS and USERS[user]['password'] == pwd:
                token = make_token(user, USERS[user]['role'])
                self.send_json({'ok': True, 'token': token, 'role': USERS[user]['role']})
            else:
                self.send_json({'ok': False, 'error': 'Credenciales invalidas'})
            return
        
        if path == '/api/upload':
            token = self.headers.get('Authorization', '').replace('Bearer ', '')
            user = verify_token(token)
            if not user or user['role'] != 'admin':
                self.send_json({'ok': False, 'error': 'Solo admin puede subir'})
                return
            length = int(self.headers.get('Content-Length', 0))
            data = self.rfile.read(length)
            with open(EXCEL_PATH, 'wb') as f:
                f.write(data)
            self.send_json({'ok': True, 'message': 'Archivo subido correctamente'})
            return
        
        self.send_json({'ok': False, 'error': 'Ruta no encontrada'})

    def send_json(self, obj):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(obj).encode())

    def log_message(self, format, *args):
        pass

print('Tablero API corriendo en puerto 3010')
HTTPServer(('127.0.0.1', 3010), Handler).serve_forever()