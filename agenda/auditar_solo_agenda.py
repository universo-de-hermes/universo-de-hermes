#!/usr/bin/env python3
"""[SOLO LECTURA + genera 1 archivo] El stack del PROYECTO AGENDA, nada mas.
   Alcance: /root/universo/agenda/ + su frontend (/var/www/html/*.html)
   + su base (Postgres cjmedical) + su SQLite (autoservicio.db).
   NO entra: recepcionista (bot/CRM), web-ui, houdini."""
import io, os, re, subprocess

AG = "/root/universo/agenda"
def cab(t):
    print("\n" + "=" * 76); print(t); print("=" * 76)

MIO = re.compile(r"^(fix_|ver_|probar_|diag|investigar_|medir_|reproducir_|casos_|arreglar_|"
                 r"sinonimos_|un_solo_|unificar_|fijar_|abrir_|estado_|limpiar_|preparar_|"
                 r"ajustar_|correr_|datos_|auditar_|instalar_|formulario_|quitar_|alinear_|"
                 r"matriz_|foto-|control_|hallazgos_|filtro_|mensaje_|cuerpos_|compat_|auditar_)")

cab("1. EL CODIGO DEL PROYECTO (sin mis scripts de trabajo ni los .bak)")
py = sql = 0; lpy = lsql = 0
for f in sorted(os.listdir(AG)):
    p = os.path.join(AG, f)
    if not os.path.isfile(p) or ".bak" in f:
        continue
    if MIO.match(f) or f in ("agenda_helper.py",):
        continue
    if f.endswith(".py"):
        py += 1; lpy += sum(1 for _ in io.open(p, encoding="utf-8", errors="replace"))
        print("   %-34s %7d bytes" % (f, os.path.getsize(p)))
    elif f.endswith(".sql"):
        sql += 1; lsql += sum(1 for _ in io.open(p, encoding="utf-8", errors="replace"))
        print("   %-34s %7d bytes   (esquema)" % (f, os.path.getsize(p)))
print("   -> %d archivos .py (%d lineas) y %d .sql (%d lineas)" % (py, lpy, sql, lsql))

cab("2. LOS IMPORTS DEL BACKEND (aqui se ve el lenguaje y el framework)")
for p in (AG + "/agenda_api.py", AG + "/autoservicio.py"):
    print("\n--- %s ---" % p)
    for i, l in enumerate(io.open(p, encoding="utf-8", errors="replace").read().split("\n")[:60], 1):
        if re.match(r"\s*(import |from )", l):
            print("   L%-4d %s" % (i, l.strip()[:100]))

cab("3. COMO SE MONTA EL PANEL DENTRO DE LA AGENDA")
for p in (AG + "/agenda_api.py", AG + "/autoservicio.py"):
    t = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
    for i, l in enumerate(t, 1):
        if re.search(r"include_router|APIRouter\(|^app\s*=\s*FastAPI|^r\s*=\s*APIRouter", l):
            print("   %-22s L%-5d %s" % (os.path.basename(p), i, l.strip()[:95]))

cab("4. DEPENDENCIAS INSTALADAS (el venv de la agenda)")
r = subprocess.run([AG + "/venv/bin/pip", "list", "--format=freeze"], capture_output=True, text=True)
lineas = [l for l in r.stdout.split("\n") if l.strip()]
print("   %d paquetes instalados:" % len(lineas))
for l in lineas:
    print("     ", l)

cab("5. LA BASE: objetos que usa la agenda")
pyc = ("import psycopg2,io,re;t=io.open('%s/.api_env').read();"
       "u=re.search(r'DATABASE_URL=[\"\\']?([^\"\\'\\n]+)',t).group(1).strip().strip('\"').strip(\"'\");"
       "c=psycopg2.connect(u);q=c.cursor();"
       "q.execute(\"select table_type, count(*) from information_schema.tables where table_schema='public' group by 1\");"
       "print('   objetos:', q.fetchall());"
       "q.execute(\"select count(*) from pg_proc p join pg_namespace n on n.oid=p.pronamespace where n.nspname='public' and p.prokind='f'\");"
       "print('   funciones:', q.fetchone()[0]);"
       "q.execute(\"select table_name from information_schema.views where table_schema='public'\");"
       "print('   vistas:', [r[0] for r in q.fetchall()]);"
       "q.execute(\"select p.proname from pg_proc p join pg_namespace n on n.oid=p.pronamespace where n.nspname='public' and p.proname in ('huecos_del_dia','apartar_cupo','soltar_cupo','agendar_cita','franjas_del_dia','buscar_cliente','cambiar_estado')\");"
       "print('   funciones clave presentes:', sorted(r[0] for r in q.fetchall()))") % AG
r = subprocess.run([AG + "/venv/bin/python", "-c", pyc], capture_output=True, text=True)
print(r.stdout.strip() or r.stderr[-300:])

cab("6. SU SQLITE (el registro de tablets del panel)")
p = AG + "/autoservicio.db"
if os.path.exists(p):
    r = subprocess.run([AG + "/venv/bin/python", "-c",
        "import sqlite3;c=sqlite3.connect('%s');"
        "print('   tablas:', [r[0] for r in c.execute(\"select name from sqlite_master where type='table'\")]);"
        "print('   filas en tabletas:', c.execute('select count(*) from tabletas').fetchone()[0])" % p],
        capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr[-200:])

cab("7. SU FRONTEND Y COMO SE SIRVE")
for f in ("agenda.html", "autoservicio.html"):
    p = "/var/www/html/" + f
    t = io.open(p, encoding="utf-8", errors="replace").read()
    print("   %-20s %7d bytes | scripts propios: %d | externos: %d | css externo: %d | fetch(): %d"
          % (f, len(t.encode()), len(re.findall(r"<script(?![^>]*\bsrc=)", t, re.I)),
             len(re.findall(r"<script[^>]+src=", t, re.I)),
             len(re.findall(r"<link[^>]+stylesheet", t, re.I)),
             len(re.findall(r"fetch\(", t))))
print("\n   --- nginx del dominio de la agenda ---")
for l in io.open("/etc/nginx/sites-enabled/agenda", encoding="utf-8", errors="replace").read().split("\n"):
    if re.search(r"server_name|root |index |location|proxy_pass", l):
        print("     ", l.strip()[:100])
print("\n   --- el servicio (systemd) ---")
for l in io.open("/etc/systemd/system/agenda-api.service", encoding="utf-8", errors="replace").read().split("\n"):
    if re.search(r"ExecStart|WorkingDirectory|EnvironmentFile|User", l):
        print("     ", l.strip()[:110])
