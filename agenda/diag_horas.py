#!/usr/bin/env python3
# Diagnostico "no me da opciones de hora" — SOLO LECTURA. v2: argumentos por NOMBRE
import re, datetime
import psycopg2

txt = open('/root/universo/agenda/.api_env').read()
m = re.search(r'DATABASE_URL=["\']?([^"\'\n]+)', txt)
cn = psycopg2.connect(m.group(1))
cn.set_session(readonly=True, autocommit=True)
cur = cn.cursor()

cur.execute("select now(), current_date, (now() at time zone 'America/Bogota')")
ahora, cd, col = cur.fetchone()
print("ahora_UTC         =", ahora)
print("current_date(UTC) =", cd)
print("ahora_Colombia    =", col)
print("  -> desfase del reloj de la BD:", (ahora.replace(tzinfo=None) - col).total_seconds()/3600, "horas")
print()

cur.execute("select id, nombre, duracion from servicios where activo order by nombre")
servs = cur.fetchall()
hoy = datetime.date.today()

print("=== HUECOS POR DIA  (servicio por NOMBRE, sin filtro de sede) ===")
for s in servs:
    fila = []
    for d in range(0, 6):
        f = hoy + datetime.timedelta(days=d)
        cur.execute("""select inicio from huecos_del_dia(p_fecha => %s, p_servicio => %s)""", (f, s[0]))
        horas = sorted({str(r[0])[:5] for r in cur.fetchall()})
        fila.append((f, d, horas))
    tot = sum(len(h) for _, _, h in fila)
    marca = "  <<<< NO DA OPCIONES" if tot == 0 else ""
    print(f"\n  --- {s[1]} ({s[2]} min){marca}")
    for f, d, horas in fila:
        etq = "HOY" if d == 0 else ("manana" if d == 1 else f"+{d}")
        if horas:
            print(f"    {f} {etq:<7} {len(horas):>3} horas: {', '.join(horas[:8])}{' ...' if len(horas) > 8 else ''}")
        else:
            print(f"    {f} {etq:<7}   0 horas")

print()
print("=== HUECOS POR SEDE (Zona M, hoy y manana) ===")
for sede in ('sede-cj-medical-el-tesoro', 'sede-cj-medical-bogota', None):
    for d in (0, 1):
        f = hoy + datetime.timedelta(days=d)
        cur.execute("""select inicio, especialista_id from huecos_del_dia(
            p_fecha => %s, p_sede => %s, p_servicio => %s)""", (f, sede, 'srv-1-sesion-zona-m'))
        rows = cur.fetchall()
        esp = sorted({r[1] for r in rows})
        print(f"  {str(sede):<26} {f} ({'HOY' if d==0 else 'manana'}): {len(rows)} huecos · {len(esp)} especialistas")
cn.close()
