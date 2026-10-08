#!/usr/bin/env python3
"""[SOLO LECTURA] Donde vive el tiempo del cupo apartado y como estan
hoy los nombres y direcciones de las sedes en agenda, panel, CRM y base."""
import io, re, os, subprocess
import psycopg2

SEP = "=" * 72

print(SEP); print("1. DONDE VIVE EL TIEMPO DEL APARTADO (8 min)"); print(SEP)
patrones = ["expira_en", "minutos", "apartar_cupo", "interval", "8 minutes", "SOSTENER", "T_APART"]
for base, _, files in os.walk("/root/universo"):
    if "node_modules" in base or "/venv" in base or ".git" in base:
        continue
    for f in files:
        if not f.endswith((".py", ".html", ".sql", ".js")):
            continue
        p = os.path.join(base, f)
        try:
            t = io.open(p, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        hits = []
        for i, line in enumerate(t.split("\n"), 1):
            if re.search(r"expira_en|apartar_cupo|interval '[0-9]+ ?min|SOSTENER|T_APART", line):
                hits.append("      L%-5d %s" % (i, line.strip()[:150]))
        if hits:
            print("\n  %s" % p)
            print("\n".join(hits[:14]))

print()
print(SEP); print("2. LA BASE: tablas sedes y funciones de apartado"); print(SEP)
t = io.open("/root/universo/agenda/.api_env").read()
url = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1).strip().strip('"').strip("'")
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()

cur.execute("""select column_name from information_schema.columns
                where table_name='sedes' order by ordinal_position""")
print("  columnas de sedes:", [r[0] for r in cur.fetchall()])
cur.execute("select * from sedes")
cur.execute("""select column_name from information_schema.columns
                where table_name='sedes' order by ordinal_position""")
cols = [r[0] for r in cur.fetchall()]
cur.execute("select " + ", ".join(cols) + " from sedes")
print("  --- SEDES HOY ---")
for fila in cur.fetchall():
    print("   ", dict(zip(cols, fila)))

print()
print("  --- funciones que tocan reservas ---")
cur.execute("""select p.proname, pg_get_functiondef(p.oid)
                 from pg_proc p join pg_namespace n on n.oid=p.pronamespace
                where n.nspname='public'
                  and (p.proname ilike '%apartar%' or p.proname ilike '%soltar%'
                       or p.proname ilike '%reserva%')""")
for nom, defi in cur.fetchall():
    print("\n   >>> %s" % nom)
    for line in defi.split("\n"):
        if re.search(r"expira|interval|minut", line, re.I):
            print("        %s" % line.strip()[:150])

cur.execute("select column_name, data_type from information_schema.columns where table_name='reservas' order by ordinal_position")
print("\n  --- columnas de reservas ---")
print("   ", [r[0] for r in cur.fetchall()])
cn.close()

print()
print(SEP); print("3. LOS NOMBRES: como se llama cada sede en cada sistema"); print(SEP)
objetivo = "/root/universo /var/www/html"
salida = subprocess.run(["grep", "-rIn", "-E", "El Tesoro|TESORO|Centro Comercial|C\\.C\\.|Plaza Norte|Parque Comercial",
                         "--include=*.py", "--include=*.html", "--include=*.js", "--include=*.sql",
                         "/root/universo/agenda", "/var/www/html"],
                        capture_output=True, text=True)
lineas = [l for l in salida.stdout.split("\n") if l.strip()
          and "node_modules" not in l and "/venv/" not in l]
print("  total coincidencias:", len(lineas))
vistos = {}
for l in lineas:
    clave = re.sub(r"^[^:]+:[0-9]+:", "", l).strip()[:110]
    vistos.setdefault(clave, 0)
    vistos[clave] += 1
for k, v in sorted(vistos.items(), key=lambda x: -x[1])[:30]:
    print("   %3dx  %s" % (v, k))
