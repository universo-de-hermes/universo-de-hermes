with open("/root/universo/agenda/agenda_api.py", "r") as f:
    c = f.read()

# Fix buscar_huecos - usar named parameters
old = '    cur.execute("SELECT * FROM buscar_huecos(%s,%s,%s,%s,%s)",\n                (req.desde or date.today(), req.dias, req.sede, req.servicio, req.limite))'
new = '    cur.execute("SELECT * FROM buscar_huecos(p_desde=>%s,p_dias=>%s,p_sede=>%s,p_servicio=>%s,p_limite=>%s,p_especialista=>NULL,p_duracion=>NULL,p_paso=>15)",\n                (req.desde or date.today(), req.dias, req.sede, req.servicio, req.limite))'
if old in c:
    c = c.replace(old, new)
    print("Fix 1 OK: buscar_huecos")
else:
    print("Fix 1 FAIL: buscar_huecos not found")

# Fix huecos_del_dia
old2 = '    cur.execute("SELECT * FROM huecos_del_dia(%s,%s,%s,%s,%s,%s)",\n                (req.fecha, req.sede, req.especialista, req.servicio, req.duracion, req.paso))'
new2 = '    cur.execute("SELECT * FROM huecos_del_dia(p_fecha=>%s,p_sede=>%s,p_servicio=>%s,p_paso=>%s,p_especialista=>%s,p_duracion=>%s)",\n                (req.fecha, req.sede, req.servicio, req.paso, req.especialista, req.duracion))'
if old2 in c:
    c = c.replace(old2, new2)
    print("Fix 2 OK: huecos_del_dia")
else:
    print("Fix 2 FAIL: huecos_del_dia not found")

with open("/root/universo/agenda/agenda_api.py", "w") as f:
    f.write(c)
print("Done")