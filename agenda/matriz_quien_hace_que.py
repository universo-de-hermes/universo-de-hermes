#!/usr/bin/env python3
# MATRIZ: quien hace que y en que sede. SOLO LECTURA.
import re, io
import psycopg2

t = io.open('/root/universo/agenda/.api_env').read()
cn = psycopg2.connect(re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', t).group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

cur.execute("select id, nombre, activo, duracion from servicios order by activo desc, nombre")
servs = cur.fetchall()
cur.execute("""select e.id, e.nombres,
                      (select string_agg(sd.nombre, ', ') from especialista_sedes es
                        join sedes sd on sd.id = es.sede_id
                       where es.especialista_id = e.id) as sedes
               from especialistas e where e.activo order by e.nombres""")
esps = cur.fetchall()
cur.execute("select especialista_id, servicio_id from especialista_servicios")
pares = {(r[0], r[1]) for r in cur.fetchall()}

corto = {e[0]: e[1].split()[0].title() for e in esps}
ancho = max(len(s[1]) for s in servs) + 2

cab = "SERVICIO".ljust(ancho) + " | " + " | ".join(corto[e[0]].center(9) for e in esps)
print(cab)
print("-" * len(cab))
for sid, nom, activo, dur in servs:
    fila = (nom + ("" if activo else " (INACTIVO)")).ljust(ancho) + " | "
    fila += " | ".join(("   SI    " if (e[0], sid) in pares else "    -    ") for e in esps)
    print(fila)

print()
print("=== DETALLE POR ESPECIALISTA ===")
for eid, nom, sedes in esps:
    mias = [s[1] for s in servs if (eid, s[0]) in pares]
    print(f"\n  {nom}")
    print(f"     sedes: {sedes or '(ninguna)'}")
    print(f"     {len(mias)} servicios:")
    for m in mias:
        print(f"        - {m}")

print()
print("=== SERVICIOS ACTIVOS SIN NADIE ===")
huerfanos = [s[1] for s in servs if s[2] and not any((e[0], s[0]) in pares for e in esps)]
print("   ", huerfanos if huerfanos else "ninguno")
cn.close()
