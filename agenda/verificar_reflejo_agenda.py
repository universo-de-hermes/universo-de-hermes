#!/usr/bin/env python3
# ¿Se refleja en la agenda todo lo que hace la clienta en el panel? SOLO LECTURA.
import io, re
import psycopg2

PANEL = '/root/universo/agenda/autoservicio.py'
AGENDA = '/var/www/html/agenda.html'

p = io.open(PANEL, encoding='utf-8').read()
a = io.open(AGENDA, encoding='utf-8', errors='replace').read()

print("=" * 74)
print("  1. A QUE ESCRIBE EL PANEL (por cada endpoint)")
print("=" * 74)
for m in re.finditer(r'@router\.(post|get)\("(/autoservicio/[a-z/_]+)"\)', p):
    metodo, ruta = m.group(1), m.group(2)
    cuerpo = p[m.end():m.end() + 2600]
    fin = len(cuerpo)
    for marca in ('\n@router', '\ndef '):
        k = cuerpo.find(marca)
        if k > 0:
            fin = min(fin, k)
    cuerpo = cuerpo[:fin]
    escribe = set()
    for pat, que in ((r'\bagendar\b', 'FUNCION agendar'), (r'cambiar_estado', 'cambiar_estado'),
                     (r'apartar_cupo', 'apartar_cupo (cupo apartado)'), (r'soltar_cupo', 'soltar_cupo'),
                     (r'insert into clientes', 'INSERT clientes'), (r'insert into citas', 'INSERT citas'),
                     (r'update clientes', 'UPDATE clientes'), (r'update citas', 'UPDATE citas'),
                     (r'update reservas', 'UPDATE reservas')):
        if re.search(pat, cuerpo, re.I):
            escribe.add(que)
    print(f"  {metodo.upper():<5} {ruta:<34} -> {', '.join(sorted(escribe)) if escribe else '(solo lee)'}")

print()
print("=" * 74)
print("  2. QUE LEE LA AGENDA (las piezas clave)")
print("=" * 74)
for que, pat in (("v_agenda", r'v_agenda'), ("tabla citas", r'\bcitas\b'),
                 ("tabla clientes", r'\bclientes\b'), ("tabla reservas (cupos apartados)", r'\breservas\b'),
                 ("v_solapes", r'v_solapes'), ("reporte Quien agenda", r'Qui[eé]n agenda'),
                 ("canal de la cita (asignada_por/creado_por)", r'asignada_por|creado_por')):
    print(f"  {'SI' if re.search(pat, a) else 'NO':<4} {que}")

print()
print("=" * 74)
print("  3. EN LA BASE: lo que la clienta creo desde el panel")
print("=" * 74)
t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

print("  citas por canal (lo que ve el reporte «Quien agenda»):")
cur.execute("select coalesce(canal,'(sin canal)'), count(*) from citas group by 1 order by 2 desc")
for r in cur.fetchall():
    print(f"     {r[0]:<18} {r[1]}")

print("\n  ¿v_agenda (lo que pinta la agenda) devuelve las del panel?")
cur.execute("""select canal, count(*) from v_agenda where canal = 'Autoservicio' group by 1""")
filas = cur.fetchall()
print("     Autoservicio en v_agenda:", filas if filas else "0 (no hay citas de panel ahora)")

print("\n  estados que puede dejar el panel:")
cur.execute("""select e.nombre, count(*) from v_agenda v join estados e on e.id=v.estado_id
               where v.canal='Autoservicio' group by 1""")
print("    ", cur.fetchall() or "0")

print("\n  columnas de v_agenda relevantes (que SI puede ver recepcion):")
cur.execute("select column_name from information_schema.columns where table_name='v_agenda' order by ordinal_position")
cols = [r[0] for r in cur.fetchall()]
print("    ", [c for c in cols if c in ('id','fecha','inicio','fin','cliente','cliente_id','servicio','especialista','sede','estado','estado_tipo','canal','asignada_por','creado_por','documento','telefono','correo')])

print("\n   ¿la agenda muestra los CUPOS APARTADOS (reservas)?")
cur.execute("select count(*) from reservas")
print("     reservas ahora:", cur.fetchone()[0])
cur.execute("select count(*) from v_solapes")
print("     filas en v_solapes:", cur.fetchone()[0])
cn.close()
