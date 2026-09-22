with open("/root/universo/agenda/agenda_api.py", "r") as f:
    lines = f.readlines()

new_lines = []
in_datos = False
added = False
for i, line in enumerate(lines):
    stripped = line.lstrip()
    if stripped.startswith("def datos_v2"):
        in_datos = True
    if in_datos and stripped.startswith("especialistas[r"):
        indent = line[:len(line) - len(stripped)]
        new_lines.append(line)
        sp_id_var = stripped.split("[")[1].split("]")[0]
        new_lines.append(indent + '    cur_h = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)\n')
        new_lines.append(indent + '    cur_h.execute("SELECT dia, desde::text, hasta::text, alm_desde::text, alm_hasta::text, sede_id FROM horarios WHERE especialista_id=%s ORDER BY dia", (r["id"],))\n')
        new_lines.append(indent + '    hrs = []\n')
        new_lines.append(indent + '    for h in cur_h.fetchall():\n')
        new_lines.append(indent + '        hrs.append({"dia": h["dia"], "desde": str(h["desde"])[:5], "hasta": str(h["hasta"])[:5], "almDesde": str(h["alm_desde"])[:5] if h["alm_desde"] else None, "almHasta": str(h["alm_hasta"])[:5] if h["alm_hasta"] else None, "sedeId": h["sede_id"]})\n')
        new_lines.append(indent + '    cur_h.close()\n')
        new_lines.append(indent + '    especialistas[r["id"]]["horarios"] = hrs\n')
        added = True
        continue
    new_lines.append(line)

if added:
    with open("/root/universo/agenda/agenda_api.py", "w") as f:
        f.writelines(new_lines)
    print("OK: Horarios agregados correctamente")
else:
    print("FAIL: No se encontro el punto de insercion")