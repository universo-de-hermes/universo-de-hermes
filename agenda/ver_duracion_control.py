#!/usr/bin/env python3
"""Donde dice que la Cita de control medico dura 20 minutos. [SOLO LECTURA]"""
import io, os, re
import psycopg2

t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

print("=== EN LA BASE ===")
cur.execute("""select id, nombre, duracion, activo from servicios
                where nombre ilike '%control%' or duracion not in (30, 60)""")
for f in cur.fetchall():
    print("   ", f)

print("\n=== cuantas citas usan ese servicio ===")
cur.execute("""select s.nombre, count(c.id) from servicios s
                 left join citas c on c.servicio_id = s.id
                where s.nombre ilike '%control%' group by s.nombre""")
print("   ", cur.fetchall())

print("\n=== donde mas aparece escrita la duracion (codigo) ===")
SALTAR = ("node_modules", "/venv/", "respaldos", "respaldo", ".bak", "site-packages",
          ".orig", "_eliminado", "__pycache__", "instalar_", "ver_", "probar_",
          "investigar_", "fix_", "mensaje_", "medir_", "reproducir_", "casos_",
          "arreglar_", "sinonimos_", "un_solo_", "unificar_", "fijar_", "abrir_",
          "estado_", "limpiar_", "preparar_", "ajustar_", "correr_")
for raiz in ("/root/universo/recepcionista", "/root/universo/agenda", "/var/www/html"):
    for base, dirs, files in os.walk(raiz):
        if any(s in base for s in SALTAR):
            continue
        for f in files:
            if not f.endswith((".py", ".html")):
                continue
            p = os.path.join(base, f)
            if any(s in p for s in SALTAR):
                continue
            try:
                txt = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
            except Exception:
                continue
            for i, l in enumerate(txt, 1):
                if re.search(r"control.{0,30}(20|veinte)|20 ?min.{0,20}control", l, re.I):
                    print("   %s:%d  %s" % (p.replace("/root/universo/", "").replace("/var/www/", ""), i, l.strip()[:150]))

print("\n=== como lo lista el prompt del bot ===")
for f in ("/root/universo/recepcionista/main.py", "/root/universo/recepcionista/herramientas.py"):
    txt = io.open(f, encoding="utf-8", errors="replace").read().split("\n")
    for i, l in enumerate(txt, 1):
        if re.search(r"[Cc]ontrol", l):
            print("   %s:%d  %s" % (f.split("/")[-1], i, l.strip()[:150]))
cn.close()
