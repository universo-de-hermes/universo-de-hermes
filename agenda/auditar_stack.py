#!/usr/bin/env python3
"""[SOLO LECTURA] Evidencia del stack: que lenguaje, frameworks y bases usa el sistema.
Imprime ARCHIVO + LINEA para que cada afirmacion quede respaldada."""
import io, os, re, subprocess

def cab(t):
    print("\n" + "=" * 78); print(t); print("=" * 78)

def leer(p, n=40):
    try:
        return io.open(p, encoding="utf-8", errors="replace").read().split("\n")[:n]
    except Exception as e:
        return ["(no se pudo leer: %s)" % e]

# ── 1. Que hay en cada carpeta ───────────────────────────────────────────
for d in ("/root/universo/agenda", "/root/universo/recepcionista",
          "/root/universo/recepcionista/crm", "/var/www/html"):
    cab("CARPETA " + d)
    try:
        for f in sorted(os.listdir(d))[:26]:
            p = os.path.join(d, f)
            if os.path.isfile(p):
                print("   %-46s %8d bytes" % (f, os.path.getsize(p)))
    except Exception as e:
        print("   ", e)

# ── 2. Los imports de los archivos de entrada (el lenguaje y el framework) ─
cab("IMPORTS DE LOS ARCHIVOS DE ENTRADA")
for p in ("/root/universo/agenda/agenda_api.py",
          "/root/universo/agenda/autoservicio.py",
          "/root/universo/recepcionista/main.py",
          "/root/universo/recepcionista/crm/server.py",
          "/root/universo/recepcionista/crm/database.py",
          "/root/universo/recepcionista/agenda_helper.py"):
    print("\n--- %s ---" % p)
    for i, l in enumerate(leer(p, 45), 1):
        if re.match(r"\s*(import |from |app\s*=\s*FastAPI|FastAPI\()", l):
            print("   L%-4d %s" % (i, l.strip()[:110]))

# ── 3. requirements / dependencias declaradas ─────────────────────────────
cab("DEPENDENCIAS DECLARADAS (requirements.txt / pyproject)")
hallado = False
for raiz in ("/root/universo", "/var/www/html"):
    for base, dirs, files in os.walk(raiz):
        if "/venv" in base or "site-packages" in base or "node_modules" in base:
            continue
        for f in files:
            if f in ("requirements.txt", "pyproject.toml", "Pipfile", "package.json"):
                p = os.path.join(base, f); hallado = True
                print("\n--- %s ---" % p)
                for l in leer(p, 30):
                    if l.strip():
                        print("   ", l.strip()[:110])
if not hallado:
    print("   (no hay requirements.txt)")

# ── 4. Versiones instaladas de verdad en cada entorno ────────────────────
cab("VERSIONES INSTALADAS (del venv, no de un archivo)")
for venv in ("/root/universo/agenda/venv/bin/pip",
             "/root/universo/recepcionista/venv/bin/pip"):
    if not os.path.exists(venv):
        print("   (no existe %s)" % venv); continue
    r = subprocess.run([venv, "list", "--format=freeze"], capture_output=True, text=True)
    quiero = ("fastapi", "uvicorn", "starlette", "pydantic", "psycopg2", "python-telegram-bot",
              "openai", "requests", "httpx", "python-dotenv", "apscheduler", "pillow",
              "playwright", "twilio", "sqlalchemy", "jinja2")
    print("\n--- %s ---" % venv.replace("/bin/pip", ""))
    for l in r.stdout.split("\n"):
        if l and l.split("==")[0].lower() in quiero:
            print("   ", l)

# ── 5. Bases de datos: con que se conectan y donde estan ─────────────────
cab("BASES DE DATOS")
print("--- Postgres (agenda) ---")
for l in leer("/root/universo/agenda/.api_env", 20):
    if "DATABASE_URL" in l:
        print("   %s  <- (valor oculto: solo digo que EXISTE)" % l.split("=")[0].strip())
r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-c",
                    "import psycopg2,io,re;t=io.open('/root/universo/agenda/.api_env').read();"
                    "u=re.search(r'DATABASE_URL=[\"\\']?([^\"\\'\\n]+)',t).group(1).strip().strip('\"').strip(\"'\");"
                    "c=psycopg2.connect(u);q=c.cursor();q.execute('select version()');"
                    "print('   ', q.fetchone()[0][:60]);q.execute('select count(*) from information_schema.tables where table_schema=%s',('public',));"
                    "print('    tablas en public:', q.fetchone()[0])"],
                   capture_output=True, text=True)
print(r.stdout.strip() or r.stderr[-200:])
print("--- SQLite (CRM y panel) ---")
for p in ("/root/universo/recepcionista/crm/cjmedical.db",
          "/root/universo/agenda/autoservicio.db"):
    if os.path.exists(p):
        r = subprocess.run(["/root/universo/recepcionista/venv/bin/python", "-c",
                            "import sqlite3,sys;c=sqlite3.connect(sys.argv[1]);"
                            "print('   %s -> %d tablas: %s' % (sys.argv[1], "
                            "len(c.execute(\"select name from sqlite_master where type='table'\").fetchall()), "
                            "[r[0] for r in c.execute(\"select name from sqlite_master where type='table'\").fetchall()][:8]))",
                            p], capture_output=True, text=True)
        print(r.stdout.strip() or r.stderr[-150:])
    else:
        print("   (no existe %s)" % p)

# ── 6. El frontend: framework o a mano? ──────────────────────────────────
cab("FRONTEND: framework o a mano?")
for p in ("/var/www/html/agenda.html", "/var/www/html/autoservicio.html"):
    t = io.open(p, encoding="utf-8", errors="replace").read()
    print("\n--- %s (%d bytes) ---" % (p, len(t.encode("utf-8"))))
    for etq, pat in (("React", r"react"), ("Vue", r"vue"), ("Angular", r"angular"),
                     ("jQuery", r"jquery"), ("Bootstrap", r"bootstrap"),
                     ("Tailwind", r"tailwind"), ("<script src=", r"<script[^>]+src="),
                     ("<link rel=stylesheet", r"<link[^>]+stylesheet"),
                     ("fetch(", r"fetch\("), ("createElement", r"document\.createElement")):
        print("   %-22s %d" % (etq, len(re.findall(pat, t, re.I))))
    print("   bloques <script> propios:", len(re.findall(r"<script(?![^>]*\bsrc=)", t, re.I)))

# ── 7. Infra: como se sirve y como corre ─────────────────────────────────
cab("CUANTO CODIGO HAY (sin venv, sin node_modules)")
from collections import Counter
L, F = Counter(), Counter()
for raiz in ("/root/universo", "/var/www/html"):
    for base, dirs, fs in os.walk(raiz):
        if any(s in base for s in ("/venv", "site-packages", "node_modules",
                                   "__pycache__", "_eliminado", "/respaldo")):
            continue
        for f in fs:
            ext = os.path.splitext(f)[1].lower()
            if ext in (".py", ".html", ".js", ".sql", ".json", ".sh", ".md", ".css"):
                p = os.path.join(base, f)
                try:
                    n = sum(1 for _ in io.open(p, encoding="utf-8", errors="replace"))
                except Exception:
                    continue
                L[ext] += n; F[ext] += 1
for ext, n in L.most_common():
    print("   %-8s %4d archivos  %7d lineas" % (ext, F[ext], n))

cab("INFRAESTRUCTURA")
for cmd in (["systemctl", "is-active", "agenda-api"], ["systemctl", "is-active", "pepe"],
            ["systemctl", "is-active", "crm"], ["systemctl", "is-active", "nginx"],
            ["python3", "--version"]):
    r = subprocess.run(cmd, capture_output=True, text=True)
    print("   %-28s %s" % (" ".join(cmd), (r.stdout or r.stderr).strip()[:60]))
print("\n--- el servicio de la agenda ---")
for l in leer("/etc/systemd/system/agenda-api.service", 14):
    if l.strip() and not l.strip().startswith("#"):
        print("   ", l.strip()[:110])
print("\n--- nginx: como sirve el HTML ---")
r = subprocess.run(["grep", "-rn", "-A3", "root /var/www/html", "/etc/nginx/sites-enabled/"],
                   capture_output=True, text=True)
print(r.stdout[:600] or r.stderr[:200])
