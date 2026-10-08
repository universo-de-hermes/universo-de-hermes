#!/usr/bin/env python3
"""Le enseña al bot los sinónimos del nombre nuevo, y quita 'C.C.' del prompt.

Sin esto, decirle al modelo «Parque Comercial El Tesoro» romperia el agendado:
resolver_sede no lo reconoceria y el bot contestaria "no tengo una sede que se
llame asi".
"""
import io, re, shutil, subprocess, unicodedata
import psycopg2

H = "/root/universo/recepcionista/agenda_helper.py"
M = "/root/universo/recepcionista/main.py"

# ── 1. los sinonimos ──────────────────────────────────────────────────────
VIEJO = '"medellin": "tesoro", "el tesoro": "tesoro", "tesoro": "tesoro",'
NUEVO = ('"medellin": "tesoro", "el tesoro": "tesoro", "tesoro": "tesoro",\n'
         '    # El nombre completo de la sede y el sitio (el modelo puede repetirlos).\n'
         '    "parque comercial el tesoro": "tesoro", "parque comercial": "tesoro",\n'
         '    "c.c. el tesoro": "tesoro", "cc el tesoro": "tesoro",\n'
         '    "centro comercial el tesoro": "tesoro",\n'
         '    "cj medical - el tesoro": "tesoro", "cj medical el tesoro": "tesoro",\n'
         '    "cjmedical el tesoro": "tesoro",\n'
         '    "cj medical - bogota": "bogota", "cj medical bogota": "bogota",\n'
         '    "cjmedical bogota": "bogota", "oficity": "bogota",')

print("=== 1. sinonimos de sede ===")
raw = open(H, "rb").read()
nl = b"\r\n" if b"\r\n" in raw else b"\n"
vb = VIEJO.encode("utf-8")
n = raw.count(vb)
print("   linea de sinonimos encontrada: %d vez/veces" % n)
if n != 1:
    print("   ABORTO"); raise SystemExit(1)
shutil.copy2(H, H + ".pre-sinonimos.bak")
open(H, "wb").write(raw.replace(vb, NUEVO.replace("\n", nl.decode()).encode("utf-8")))
print("   aplicado (fin de linea preservado: %r)" % nl)

# ── 2. 'C.C. El Tesoro' fuera del prompt ──────────────────────────────────
print("\n=== 2. el prompt: 'C.C.' -> 'Parque Comercial' ===")
raw = open(M, "rb").read()
vb = b"C.C. El Tesoro"
print("   coincidencias:", raw.count(vb))
if raw.count(vb):
    shutil.copy2(M, M + ".pre-cc.bak")
    open(M, "wb").write(raw.replace(vb, b"Parque Comercial El Tesoro"))
    print("   reemplazadas todas")

# ── 3. verificacion: el resolutor REAL del bot ────────────────────────────
print("\n=== 3. prueba del resolutor del bot (replica exacta) ===")
src = io.open(H, encoding="utf-8").read()

def _normal(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode()
    return " ".join(s.lower().split())

m = re.search(r"SINONIMOS_SEDE = \{(.*?)\}", src, re.S)
sinonimos = dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', m.group(1)))
print("   sinonimos cargados:", len(sinonimos))
print("   claves nuevas:", [k for k in sinonimos if "parque" in k or "cc" in k or "cj medical" in k])

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
cur.execute("select id, nombre, ciudad from sedes")
sedes = cur.fetchall()
cn.close()

def resuelve(texto):
    consulta = sinonimos.get(_normal(texto), _normal(texto))
    for sid, nom, ciu in sedes:
        pajar = _normal(sid + " " + nom + " " + (ciu or ""))
        if sid == texto or (consulta and consulta in pajar):
            return nom
    return None

for p in ["El Tesoro", "Medellín", "C.C. El Tesoro", "Parque Comercial El Tesoro",
          "Centro Comercial El Tesoro", "CJ Medical - El Tesoro", "CJ MEDICAL EL TESORO",
          "Chico Norte", "Bogotá", "CJ Medical - Bogotá", "Oficity", "sede-cj-medical-el-tesoro"]:
    r = resuelve(p)
    print("   %-30s -> %s" % (p, r or ">>> NO RESUELVE <<<"))

print("\n=== 4. compilan ===")
for f in (H, M):
    r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-m", "py_compile", f],
                       capture_output=True, text=True)
    print("   %-16s %s" % (f.split("/")[-1], "OK" if r.returncode == 0 else "MAL " + r.stderr[-250:]))
