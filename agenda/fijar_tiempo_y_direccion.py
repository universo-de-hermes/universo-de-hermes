#!/usr/bin/env python3
"""1) El cupo apartado del panel: 8 minutos -> 2 minutos.
2) Direccion de la sede El Tesoro a la que el dueno confirmo (en el codigo y
   en la base, para que la vean agenda, panel y CRM).
NO toca el tiempo del bot Pepe (el negocia por WhatsApp y necesita mas aire).
"""
import io, os, re, shutil, subprocess, sys

PANEL = "/root/universo/agenda/autoservicio.py"

VIEJO_MIN = 'os.getenv("AUTOSERVICIO_MINUTOS", "8")'
NUEVO_MIN = 'os.getenv("AUTOSERVICIO_MINUTOS", "2")'

VIEJO_DIR = ('"sede-cj-medical-el-tesoro": "Cra 25A #1a sur-45, S\u00f3tano 4 Plaza Norte, "\n'
             '                                 "Local 6100, Medell\u00edn",')
NUEVO_DIR = ('"sede-cj-medical-el-tesoro": "Cra 25A #1a sur-45, LC 6100, "\n'
             '                                 "S\u00f3tano 4 por la plaza de cines, Torre Norte, Medell\u00edn",')

DIR_CONFIRMADA = "Cra 25A #1a sur-45, LC 6100, S\u00f3tano 4 por la plaza de cines, Torre Norte, Medell\u00edn"

# --- 0. el entorno del servicio no debe pisar el valor nuevo -----------------
print("=== 0. el servicio tiene AUTOSERVICIO_MINUTOS puesto? ===")
for f in ("/etc/systemd/system/agenda-api.service",
          "/root/universo/agenda/.api_env"):
    if os.path.exists(f):
        t = io.open(f, encoding="utf-8", errors="replace").read()
        hallado = [l.strip() for l in t.split("\n") if "MINUTOS" in l or "PASO" in l]
        print("   %s -> %s" % (f, hallado or "(nada)"))

# --- 1. el .py --------------------------------------------------------------
print("\n=== 1. cambiando el tiempo del apartado ===")
src = io.open(PANEL, encoding="utf-8").read()
for viejo, etq in ((VIEJO_MIN, "MIN_RESERVA 8->2"),):
    n = src.count(viejo)
    print("   %s: %d coincidencia(s)" % (etq, n))
    if n != 1:
        print("   ABORTO: no es exactamente 1"); sys.exit(1)
src = src.replace(VIEJO_MIN, NUEVO_MIN)

print("\n=== 2. la direccion confirmada del Tesoro ===")
n = src.count(VIEJO_DIR)
print("   bloque de direccion: %d coincidencia(s)" % n)
if n != 1:
    print("   ABORTO: no es exactamente 1"); sys.exit(1)
src = src.replace(VIEJO_DIR, NUEVO_DIR)

shutil.copy2(PANEL, PANEL + ".pre-tiempo-dir.bak")
io.open(PANEL, "w", encoding="utf-8", newline="").write(src)
print("   respaldo:", PANEL + ".pre-tiempo-dir.bak")

# --- 3. la base ------------------------------------------------------------
print("\n=== 3. la direccion en la base (la leen agenda, panel y CRM) ===")
sys.path.insert(0, "/root/universo/agenda")
import psycopg2
t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("select id, nombre, direccion from sedes order by id")
print("   ANTES:", cur.fetchall())
cur.execute("update sedes set direccion=%s where id='sede-cj-medical-el-tesoro'",
            (DIR_CONFIRMADA,))
print("   filas tocadas:", cur.rowcount)
cur.execute("select id, nombre, direccion from sedes order by id")
print("   DESPUES:", cur.fetchall())
cn.close()

# --- 4. verificacion -------------------------------------------------------
print("\n=== 4. verificacion ===")
r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-m", "py_compile", PANEL],
                   capture_output=True, text=True)
print("   sintaxis del .py:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-200:])
src = io.open(PANEL, encoding="utf-8").read()
print("   MIN_RESERVA ahora:", re.search(r'MIN_RESERVA = .*', src).group(0))
print("   palabras 'Plaza Norte' que quedan:", src.count("Plaza Norte"))
