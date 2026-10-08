#!/usr/bin/env python3
"""SOLO el proyecto AGENDA:
   1) Le genera el requirements.txt que le falta (hoy las dependencias viven
      solo dentro del venv).
   2) Aparta la basura historica (los .bak y la version vieja del API) a una
      carpeta, sin borrar nada. Ademas los .bak del HTML estaban en la raiz
      web (/var/www/html) y se podian descargar por HTTP.
"""
import io, os, re, shutil, subprocess, glob

AG = "/root/universo/agenda"
RESP = AG + "/_respaldos"
WEB = "/var/www/html"

# ── 1. requirements.txt ──────────────────────────────────────────────────
print("=== 1. requirements.txt de la agenda ===")
r = subprocess.run([AG + "/venv/bin/pip", "list", "--format=freeze"], capture_output=True, text=True)
lineas = sorted(l.strip() for l in r.stdout.split("\n")
                if l.strip() and not l.lower().startswith("pip=="))
destino = AG + "/requirements.txt"
cabeza = ("# Proyecto AGENDA CJ Medical (agenda_api.py + autoservicio.py)\n"
          "# Generado del venv real el 2026-10-03: pip freeze.\n"
          "# Instalar con:  venv/bin/pip install -r requirements.txt\n"
          "# Framework: FastAPI + Uvicorn · Base: PostgreSQL (psycopg2-binary, SQL directo)\n")
io.open(destino, "w", encoding="utf-8", newline="\n").write(cabeza + "\n".join(lineas) + "\n")
print("   escrito %s (%d paquetes)" % (destino, len(lineas)))
for l in lineas:
    print("     ", l)

# comprobar leyendo el archivo DE VUELTA contra el venv
print("\n   verificacion (el archivo leido de vuelta contra el venv):")
leido = io.open(destino, encoding="utf-8").read().split("\n")
del_archivo = sorted(l.strip() for l in leido
                     if l.strip() and not l.startswith("#") and "==" in l)
instalados = {l.split("==")[0].lower() for l in lineas}
faltan = [l for l in del_archivo if l.split("==")[0].lower() not in instalados]
print("     paquetes en el archivo: %d (el venv tiene %d)" % (len(del_archivo), len(lineas)))
print("     paquetes del archivo que no esten en el venv:", faltan or "ninguno")
r2 = subprocess.run([AG + "/venv/bin/pip", "install", "--dry-run", "-q", "-r", destino],
                    capture_output=True, text=True)
print("     pip lo acepta:", "SI" if r2.returncode == 0 else "NO -> " + (r2.stderr or r2.stdout)[-300:])

# ── 2. apartar la basura historica ───────────────────────────────────────
print("\n=== 2. respaldos historicos -> %s ===" % RESP)
os.makedirs(RESP + "/html", exist_ok=True)

movidos = []
# 2a. .bak y la version vieja dentro del proyecto
for p in sorted(glob.glob(AG + "/*.bak")):
    movidos.append((p, RESP + "/" + os.path.basename(p)))
viejo = AG + "/agenda_api_v3.py"
if os.path.exists(viejo):
    movidos.append((viejo, RESP + "/agenda_api_v3.py"))
# 2b. .bak del HTML (estaban en la raiz web: descargables por HTTP)
for p in sorted(glob.glob(WEB + "/agenda*.bak") + glob.glob(WEB + "/autoservicio*.bak")):
    movidos.append((p, RESP + "/html/" + os.path.basename(p)))

for origen, destino_f in movidos:
    if os.path.exists(destino_f):
        destino_f = destino_f + ".2"
    shutil.move(origen, destino_f)
print("   movidos: %d archivos (nada borrado)" % len(movidos))
for o, d in movidos[:6]:
    print("     %s" % os.path.basename(o))
if len(movidos) > 6:
    print("     ... y %d mas" % (len(movidos) - 6))

# ── 3. verificar que NO se rompio nada ───────────────────────────────────
print("\n=== 3. verificacion (nada se puede haber roto) ===")
for f in ("agenda.html", "autoservicio.html"):
    p = WEB + "/" + f
    print("   %-20s existe: %s  %d bytes" % (f, os.path.exists(p), os.path.getsize(p) if os.path.exists(p) else 0))
print("   .bak que quedan en la web:", glob.glob(WEB + "/*.bak") or "ninguno")
for cmd in (["systemctl", "is-active", "agenda-api"],):
    print("   agenda-api:", subprocess.run(cmd, capture_output=True, text=True).stdout.strip())
for u in ("https://agenda.universojota.tech/agenda.html",
          "https://agenda.universojota.tech/autoservicio.html"):
    c = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code} %{size_download}",
                        u], capture_output=True, text=True).stdout
    print("   %-52s %s" % (u.replace("https://", ""), c))
# y que un .bak ya NO se pueda descargar
c = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                    "https://agenda.universojota.tech/agenda.html.pre-msg-apartado.bak"],
                   capture_output=True, text=True).stdout
print("   un .bak por HTTP (antes 200, ahora debe ser 404):", c)
