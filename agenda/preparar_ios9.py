#!/usr/bin/env python3
# 1) Deja el limpiador que su arnes espera (/home/claude/limpiar-prueba.py),
#    como PUENTE al python del venv (el sistema no tiene psycopg2).
# 2) Limpia la basura que quedo: la clienta 999000444 y sus citas.
import io, os, re, subprocess
import psycopg2

REAL = '/root/universo/agenda/limpiar_prueba_real.py'
PUENTE = '/home/claude/limpiar-prueba.py'

REAL_PY = '''#!/usr/bin/env python3
"""Borra la clienta de prueba y todo lo suyo. Uso: limpiar-prueba-real.py <documento>"""
import re, io, sys
import psycopg2
Q, A, N = chr(34), chr(39), chr(10)
t = io.open("/root/universo/agenda/.api_env").read()
m = re.search("DATABASE_URL=([^" + N + "]+)", t)
url = m.group(1).strip().strip(Q).strip(A)
cn = psycopg2.connect(url); cn.autocommit = True
cur = cn.cursor()
doc = sys.argv[1] if len(sys.argv) > 1 else ""
cur.execute("select id from clientes where documento=%s", (doc,))
ids = [r[0] for r in cur.fetchall()]
for cid in ids:
    cur.execute("delete from reservas where referencia=%s", (doc,))
    cur.execute("select id from citas where cliente_id=%s", (cid,))
    for (cita,) in cur.fetchall():
        cur.execute("update citas set reprogramada_de=null, reprogramada_a=null where reprogramada_de=%s or reprogramada_a=%s", (cita, cita))
        cur.execute("delete from citas where id=%s", (cita,))
    cur.execute("delete from clientes where id=%s", (cid,))
print("limpiado " + doc + ": " + str(len(ids)) + " clienta(s)")
'''

PUENTE_PY = '''#!/usr/bin/env python3
"""Puente: el python del sistema no tiene psycopg2; el del venv si."""
import subprocess, sys
subprocess.run(["/root/universo/agenda/venv/bin/python",
                "/root/universo/agenda/limpiar_prueba_real.py"] + sys.argv[1:])
'''

io.open(REAL, 'w').write(REAL_PY)
os.chmod(REAL, 0o755)
os.makedirs('/home/claude', exist_ok=True)
io.open(PUENTE, 'w').write(PUENTE_PY)
os.chmod(PUENTE, 0o755)
print("creados:", REAL, "y", PUENTE)

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.autocommit = True
cur = cn.cursor()

def foto(etq):
    cur.execute("select count(*) from citas"); c = cur.fetchone()[0]
    cur.execute("select count(*) from reservas"); r = cur.fetchone()[0]
    cur.execute("select count(*) from clientes"); cl = cur.fetchone()[0]
    cur.execute("select documento, primer_nombre from clientes order by documento")
    print(f"   {etq}: citas={c} reservas={r} clientes={cl} -> {cur.fetchall()}")

print("\n=== ANTES ==="); foto("antes")
print("\n=== limpiando 999000444 con SU ruta exacta (python3 sistema) ===")
r = subprocess.run(['python3', PUENTE, '999000444'], capture_output=True, text=True)
print("   stdout:", (r.stdout or '').strip()[:160])
print("   stderr:", (r.stderr or '').strip()[:160])
print("\n=== DESPUES ==="); foto("despues")
cn.close()
