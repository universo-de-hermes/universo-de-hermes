#!/usr/bin/env python3
# Instala la entrega 2: los 2 HTML de Claude + el endpoint /reservas que falta.
import io, re, os, shutil, hashlib, subprocess, sys

WEB = '/var/www/html/autoservicio.html'
AG = '/var/www/html/agenda.html'
PY = '/root/universo/agenda/agenda_api.py'
INC = '/root/universo/agenda/_paquete2/'

print("=" * 74)
print("  ANTES (produccion)")
print("=" * 74)
for f in (WEB, AG, PY):
    b = open(f, 'rb').read()
    print(f"  {len(b):>7} bytes  md5 {hashlib.md5(b).hexdigest()[:12]}  {f}")

# ── 1. respaldos ──
for f in (WEB, AG, PY):
    shutil.copy(f, f + '.pre-encargo2.bak')

# ── 2. los dos HTML de Claude ──
for destino, origen in ((WEB, INC + 'autoservicio.html'), (AG, INC + 'agenda.html')):
    b = open(origen, 'rb').read()
    open(destino, 'wb').write(b)
    print(f"\n  instalado {destino}  {len(b)} bytes  md5 {hashlib.md5(b).hexdigest()[:12]}")

# ── 3. el endpoint /reservas (lo mio: Claude nunca vio agenda_api.py) ──
p = io.open(PY, encoding='utf-8').read()
ANCLA = '@r.get("/clientes")'
if p.count(ANCLA) != 1:
    print(f"\n*** ABORTO: el ancla aparece {p.count(ANCLA)} veces"); sys.exit(1)
if '/reservas' in p:
    print("\n  (el endpoint ya estaba)")
else:
    ENDPOINT = '''# ──────────────────────────────────────────── cupos apartados (tablet) ────
@r.get("/reservas")
def reservas_del_dia(fecha: str, sede: Optional[str] = Query(None),
                     _=Depends(sesion)):
    """Cupos que alguien esta apartando AHORA desde la tablet.

    Solo los vivos: la misma condicion que usa huecos_del_dia para
    descontarlos (expira_en > now()). Si se devolvieran los vencidos, la
    recepcionista veria ocupado algo que ya esta libre.

    quedan_minutos lo calcula Postgres a proposito: expira_en es un timestamp
    SIN zona, y si la resta la hace el navegador la lee como hora local y, con
    el servidor en UTC y la tablet en Colombia, da cinco horas de mas.
    """
    return todos("""
        select r.id,
               r.especialista_id,
               r.sede_id,
               r.fecha,
               to_char(r.inicio,'HH24:MI') as inicio,
               to_char(r.fin,'HH24:MI')    as fin,
               r.canal,
               ceil(extract(epoch from (r.expira_en - now())) / 60)::int
                 as quedan_minutos
          from reservas r
         where r.fecha = %s
           and r.expira_en > now()
           and (%s is null or r.sede_id = %s)
         order by r.inicio, r.especialista_id
    """, (fecha, sede, sede))


'''
    p = p.replace(ANCLA, ENDPOINT + ANCLA, 1)
    io.open(PY, 'w', encoding='utf-8').write(p)
    print("\n  endpoint /reservas AÑADIDO")

# ── 4. verificaciones ──
print("\n" + "=" * 74)
print("  VERIFICACION")
print("=" * 74)
p2 = io.open(PY, encoding='utf-8').read()
print("  endpoint presente:", '/reservas' in p2)
print("  usa el router r:", '@r.get("/reservas")' in p2)
print("  usa el guardian sesion:", '_=Depends(sesion)' in p2)
try:
    compile(p2, PY, 'exec')
    print("  el .py compila: SI")
except SyntaxError as e:
    print(f"  el .py compila: NO -> {e}"); sys.exit(1)

for f in (WEB, AG):
    h = io.open(f, encoding='utf-8', errors='replace').read()
    bloques = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S | re.I)
    io.open('/tmp/chk.js', 'w', encoding='utf-8').write("\n;\n".join(bloques))
    r = subprocess.run(['node', '--check', '/tmp/chk.js'], capture_output=True, text=True)
    etq = f.split('/')[-1]
    print(f"  {etq}: node --check rc={r.returncode} | llaves {h.count('{')}/{h.count('}')} ok={h.count('{')==h.count('}')}")
    print(f"     bytes {len(h.encode('utf-8'))}  md5 {hashlib.md5(h.encode()).hexdigest()[:12]}")

print("\n  respaldos: *.pre-encargo2.bak")
