#!/usr/bin/env python3
"""[SOLO LECTURA] Que textos de sede resuelven HOY, con el nombre nuevo."""
import io, re, unicodedata
import psycopg2

def _normal(s):
    s = unicodedata.normalize("NFKD", str(s or "").lower())
    return "".join(c for c in s if not unicodedata.combining(c)).strip()

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

cur.execute("select id, nombre, ciudad from sedes order by id")
sedes = cur.fetchall()
print("=== las sedes como estan ahora ===")
for s in sedes:
    print("   ", s)

SINONIMOS = {"bogota": "bogota", "chico": "bogota", "chico norte": "bogota",
             "medellin": "tesoro", "el tesoro": "tesoro", "tesoro": "tesoro"}

def resuelve_como_el_bot(texto):
    consulta = _normal(texto)
    consulta = SINONIMOS.get(consulta, consulta)
    for sid, nom, ciu in sedes:
        pajar = _normal(sid + " " + nom + " " + (ciu or ""))
        if sid == texto or (consulta and consulta in pajar):
            return nom
    return None

def resuelve_en_la_base(texto):
    cur.execute("""select count(*) from huecos_del_dia(
                     p_fecha=>date '2026-10-05', p_sede=>%s,
                     p_especialista=>null, p_servicio=>'srv-1-sesion-zona-l',
                     p_duracion=>null, p_paso=>30)""", (texto,))
    return cur.fetchone()[0]

PRUEBAS = ["El Tesoro", "Tesoro", "Medellín", "sede-cj-medical-el-tesoro",
           "CJ Medical - El Tesoro", "CJ MEDICAL EL TESORO",
           "C.C. El Tesoro", "Centro Comercial El Tesoro",
           "Parque Comercial El Tesoro", "Parque Comercial",
           "Chico Norte", "Bogotá", "CJ Medical - Bogotá"]

print()
print("%-30s | %-28s | huecos (lun 05-oct)" % ("texto que manda el bot", "lo resuelve a"))
print("-" * 92)
for p in PRUEBAS:
    d = resuelve_como_el_bot(p)
    try:
        h = resuelve_en_la_base(p)
    except Exception as e:
        cn.rollback()
        h = "ERROR %s" % str(e)[:40]
    print("%-30s | %-28s | %s" % (p, d or ">>> NO <<<", h))
cn.close()
