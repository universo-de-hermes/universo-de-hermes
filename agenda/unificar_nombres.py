#!/usr/bin/env python3
"""Un solo nombre para cada sede, igual en agenda, panel y CRM.
   CJ Medical - El Tesoro   /   CJ Medical - Bogotá
"""
import io, json, os, re, shutil, subprocess
import psycopg2

NUEVO = {
    "sede-cj-medical-el-tesoro": "CJ Medical - El Tesoro",
    "sede-cj-medical-bogota":    "CJ Medical - Bogot\u00e1",
}
DIR_BOGOTA = "Cra 11A #96-51, Edificio Oficity, Local 102, Chic\u00f3 Norte, Bogot\u00e1"

# ── 1. la base: el nombre que leen los tres ────────────────────────────────
t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("select id, nombre, direccion, bodega from sedes order by id")
print("=== ANTES ===")
for f in cur.fetchall():
    print("   ", f)
for sid, nom in NUEVO.items():
    cur.execute("update sedes set nombre=%s where id=%s", (nom, sid))
    print("   %s -> %s (%d fila)" % (sid, nom, cur.rowcount))
cur.execute("update sedes set direccion=%s where id='sede-cj-medical-bogota' and (direccion is null or direccion='')",
            (DIR_BOGOTA,))
print("   direccion de Bogota cargada:", cur.rowcount, "fila")
cur.execute("select id, nombre, direccion, bodega from sedes order by id")
print("=== DESPUES ===")
for f in cur.fetchall():
    print("   ", f)
cn.close()

# ── 2. agenda.html: el unico texto a mano ──────────────────────────────────
AG = "/var/www/html/agenda.html"
VIEJO = "Citas de CJ Medical Bogot\u00e1 y CJ Medical El Tesoro tra\u00eddas del informe ADC-08."
NUEVOTXT = "Citas de CJ Medical - Bogot\u00e1 y CJ Medical - El Tesoro tra\u00eddas del informe ADC-08."
print("\n=== agenda.html: texto del informe ===")
b = open(AG, "rb").read()
vb = VIEJO.encode("utf-8")
n = b.count(vb)
print("   coincidencias:", n)
if n == 1:
    shutil.copy2(AG, AG + ".pre-nombre-sede.bak")
    open(AG, "wb").write(b.replace(vb, NUEVOTXT.encode("utf-8")))
    print("   cambiado. respaldo:", AG + ".pre-nombre-sede.bak")
else:
    print("   no toco nada (no es exactamente 1)")

# ── 3. verificacion ────────────────────────────────────────────────────────
print("\n=== VERIFICACION ===")
AGP = "/root/universo/agenda/agenda_api.py"
print("   agenda_api.py compila:",
      "OK" if subprocess.run(["/root/universo/agenda/venv/bin/python", "-m", "py_compile", AGP],
                             capture_output=True).returncode == 0 else "MAL")
h = io.open(AG, encoding="utf-8", errors="replace").read()
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", h, re.S | re.I)
io.open("/tmp/chk.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk.js"], capture_output=True, text=True)
print("   JS de la agenda:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-300:])
print("   el texto viejo debe dar 0:", h.count("y CJ Medical El Tesoro"))
