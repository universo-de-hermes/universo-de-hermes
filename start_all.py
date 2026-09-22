#!/usr/bin/env python3
"""Startup script with retry for Universo de JuanJo"""
import os, sys, time, subprocess, signal

ROOT = r"C:\Users\USER\proyecto hermes"
SRV = os.path.join(ROOT, "server_api.py")
HOUDINI = os.path.join(ROOT, "houdini", "main.py")
PEPE = os.path.join(ROOT, "recepcionista", "main.py")
PORT = 3000

def kill_port():
    """Kill anything on our port."""
    try:
        result = subprocess.run(
            f'netstat -ano | findstr ":{PORT} " | findstr LISTENING',
            shell=True, capture_output=True, text=True, timeout=5
        )
        for line in result.stdout.strip().split('\n'):
            parts = line.strip().split()
            if len(parts) >= 5:
                pid = parts[-1]
                if pid.isdigit():
                    os.system(f'taskkill /F /PID {pid} >nul 2>&1')
                    print(f"  Killed PID {pid} on port {PORT}")
    except:
        pass

print("🎩 Iniciando Universo de JuanJo...")
kill_port()
time.sleep(1)

# Start server  
print(f"📡 Server API en puerto {PORT}...")
srv_proc = subprocess.Popen([sys.executable, SRV], cwd=ROOT)
time.sleep(2)

# Verify
import socket
try:
    s = socket.socket()
    s.settimeout(3)
    s.connect(('127.0.0.1', PORT))
    s.sendall(b'GET /api/status HTTP/1.0\r\nHost: localhost\r\nConnection: close\r\n\r\n')
    resp = b''
    while True:
        try:
            d = s.recv(65536)
            if not d: break
            resp += d
        except: break
    s.close()
    parts = resp.split(b'\r\n\r\n', 1)
    import json
    data = json.loads(parts[1]) if len(parts) > 1 else {}
    print(f"✅ Server OK - {len(data)} agentes")
except Exception as e:
    print(f"❌ Server falló: {e}")
    kill_port()
    time.sleep(1)
    srv_proc = subprocess.Popen([sys.executable, SRV], cwd=ROOT)
    time.sleep(3)
    print("  Reintentado...")

# Start Houdini
print("🎩 Iniciando Houdini (Telegram)...")
subprocess.Popen([sys.executable, HOUDINI], cwd=os.path.join(ROOT, "houdini"))

# Start Pepe
print("🤖 Iniciando Pepe CJ Medical...")
subprocess.Popen([sys.executable, PEPE], cwd=os.path.join(ROOT, "recepcionista"))

print()
print("="*50)
print("🎩 Universo de JuanJo INICIADO")
print(f"   API:   http://localhost:{PORT}/api/status")
print(f"   HTML:  http://localhost:{PORT}/Command%20Center%20Oficina.html")
print("="*50)