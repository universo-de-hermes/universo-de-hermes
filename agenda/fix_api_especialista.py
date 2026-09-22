#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agrega a la API el endpoint /agenda-especialista.

Responde tres cosas de una sola vez:
  - si la especialista trabaja ese día (y si no, no aparece en `franjas`)
  - su horario de ese día (desde, hasta, almuerzo y en qué sede)
  - sus horas libres reales, ya con la duración del servicio

El bot lo usa cuando el cliente pregunta por alguien puntual.
"""
import io
import sys

RUTA = "/root/universo/agenda/agenda_api.py"

t = io.open(RUTA, "r", encoding="utf-8", newline="").read()
crlf = "\r\n" in t
s = t.replace("\r\n", "\n")

ancla = '@r.get("/horarios-fecha")\n'
if s.count(ancla) != 1:
    print("ABORTO: no pude ubicar el ancla de /horarios-fecha (%d)" % s.count(ancla))
    sys.exit(1)

nuevo = '''@r.get("/agenda-especialista")
def agenda_especialista(especialista: str = Query(...),
                        fecha: date = Query(...),
                        sede: Optional[str] = Query(None),
                        servicio: Optional[str] = Query(None),
                        paso: int = Query(30)):
    """¿Esta especialista trabaja ese día y a qué horas tiene cupo?

    Se usa cuando el cliente pregunta por alguien puntual. Con `huecos` solo no
    se puede distinguir «no trabaja» de «trabaja pero está llena», por eso se
    devuelven las dos cosas: las franjas de trabajo y las horas libres.
    """
    fila = None
    with cursor() as cur:
        cur.execute("""select id, trim(nombres || ' ' || apellidos) as nombre
                         from especialistas where id=%s""", (especialista,))
        fila = cur.fetchone()
        if not fila:
            # tambien acepta el nombre: «Valentina», «Valentina Baquero»
            cur.execute("""select id, trim(nombres || ' ' || apellidos) as nombre
                             from especialistas
                            where activo
                              and (nombres || ' ' || apellidos) ilike %s
                            order by length(nombres || ' ' || apellidos)
                            limit 1""", ("%" + especialista + "%",))
            fila = cur.fetchone()
    if not fila:
        raise HTTPException(404, "ESPECIALISTA_NO_EXISTE: no encontré a esa especialista")
    eid = fila["id"]

    franjas = todos("""select f.especialista_id, f.sede_id, s.nombre as sede,
                              to_char(f.desde,'HH24:MI')     as desde,
                              to_char(f.hasta,'HH24:MI')     as hasta,
                              to_char(f.alm_desde,'HH24:MI') as alm_desde,
                              to_char(f.alm_hasta,'HH24:MI') as alm_hasta,
                              f.origen
                         from franjas_del_dia(%s, %s, %s, %s) f
                         join sedes s on s.id = f.sede_id
                        order by f.desde""",
                    (fecha, sede, eid, servicio))

    libres = todos("""select to_char(inicio,'HH24:MI') as inicio,
                             to_char(fin,'HH24:MI')    as fin,
                             sede_id
                        from huecos_del_dia(p_fecha=>%s, p_sede=>%s,
                             p_especialista=>%s, p_servicio=>%s, p_paso=>%s)""",
                   (fecha, sede, eid, servicio, paso))

    return {"especialista_id": eid, "especialista": fila["nombre"],
            "fecha": fecha, "trabaja": bool(franjas),
            "franjas": franjas, "libres": libres}


'''

s = s.replace(ancla, nuevo + ancla, 1)
if crlf:
    s = s.replace("\n", "\r\n")
io.open(RUTA, "w", encoding="utf-8", newline="").write(s)
print("endpoint /agenda-especialista agregado")

import py_compile
py_compile.compile(RUTA, doraise=True)
print("sintaxis OK")
