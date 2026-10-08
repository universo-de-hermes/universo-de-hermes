#!/usr/bin/env python3
"""Que el panel y la agenda digan lo mismo sobre QUIÉN hace QUÉ.

Esto es lo que se le descuadró a Jota: agendó desde la tablet y le salió una
especialista que no realiza ese servicio. Aquí se comprueban las tres cosas
que lo garantizan:

  1. Al asignarle servicios a una especialista, la tablet deja de ofrecerla
     para los que no hace — y sigue ofreciéndola para los que sí.
  2. Aunque alguien mande la petición a mano saltándose la pantalla, el
     servidor no deja agendarla para algo que no realiza.
  3. Reprogramar cambiando el servicio guarda el servicio NUEVO, con su
     duración, y «ya llegué» deja la cita en «Llegó» de verdad en la base.

Se corre igual que probar_panel.py y **deja la base como estaba**: lo que
asigna para probar, lo quita al final.

    API_TOKEN=… DATABASE_URL=… python3 probar_cuadre.py
"""
import os
import sys
from datetime import date, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import probar_panel as P          # se reaprovecha todo el andamiaje

DB = os.getenv("DATABASE_URL", "")


def bd(sql, args=(), traer=False):
    import psycopg2
    cn = psycopg2.connect(DB); cn.autocommit = True
    try:
        with cn.cursor() as cur:
            cur.execute(sql, args)
            return cur.fetchall() if traer else None
    finally:
        cn.close()


def esp_en(horas, hora=None):
    """Las especialistas que /horas ya trae para esa hora (o para todas)."""
    ids = set()
    for h in horas:
        if hora is None or h["hora"] == hora:
            ids |= {e["id"] for e in h.get("especialistas", [])}
    return ids


def main():
    if not DB:
        print("Hace falta DATABASE_URL: esta prueba mira la base directamente.")
        return 2
    c, j = P.abrir({"correo": P.USUARIO, "clave": P.CONTRASENA})
    P.LLAVE["t"] = j.get("token", "")
    P.prueba("recepción abre la tablet", bool(P.LLAVE["t"]), j)
    if not P.LLAVE["t"]:
        return 1
    sid = P.SEDES_ID[P.SEDE]

    c, datos = P.panel(f"/datos?sede={P.SEDE}")
    servicios = datos.get("servicios") or []
    P.prueba("la tablet trae servicios", len(servicios) >= 2, datos)
    if len(servicios) < 2:
        return 1

    # ── 1. asignarle servicios a una especialista la limita de verdad ──────
    print("\n— lo que hace cada especialista —")
    esps = bd("""select e.id, e.nombres||' '||e.apellidos
                   from especialistas e
                   join especialista_sedes s on s.especialista_id=e.id
                  where e.activo and s.sede_id=%s order by 2""", (sid,), True)
    P.prueba("la sede tiene especialistas activas", len(esps) >= 2, esps)
    if len(esps) < 2:
        return 1

    sin_asignar = bd("select count(*) from especialista_servicios", (), True)[0][0]
    if sin_asignar == 0:
        print("  ⓘ  hoy la tabla especialista_servicios está VACÍA: por la regla\n"
              "     de la agenda, eso significa que todas hacen todo. Es\n"
              "     exactamente lo que se ve como «descuadre» en la tablet.")

    elegida, nombre_elegida = esps[0][0], esps[0][1]
    hace, no_hace = servicios[0], servicios[1]
    fecha = None
    for d in range(1, 21):
        f = (P.date.today() + timedelta(days=d)).isoformat()
        c, j = P.panel("/horas", {"servicio": hace["id"], "fecha": f})
        if j.get("horas"):
            fecha = f
            break
    if not fecha:
        P.saltar("cuadre de servicios", "no hay ningún día con horas libres")
        return 1

    # Foto de lo que esta especialista YA tenía, para devolverlo tal cual.
    antes = {r[0] for r in bd("select servicio_id from especialista_servicios "
                              "where especialista_id=%s", (elegida,), True)}
    print(f"  ⓘ  {nombre_elegida} ya tenía {len(antes)} servicios asignados "
          f"(se devuelven al terminar)")
    try:
        bd("insert into especialista_servicios(especialista_id, servicio_id) "
           "values (%s,%s) on conflict do nothing", (elegida, hace["id"]))

        # la que SÍ lo hace sigue apareciendo
        c, j = P.panel("/horas", {"servicio": hace["id"], "fecha": fecha})
        P.prueba(f"«{nombre_elegida}» sigue saliendo para «{hace['nombre']}»",
                 elegida in esp_en(j.get("horas") or []), j.get("horas", [])[:2])

        # y para el que NO le asignamos, ya no
        c, j2 = P.panel("/horas", {"servicio": no_hace["id"], "fecha": fecha})
        P.prueba(f"y ya NO sale para «{no_hace['nombre']}», que no realiza",
                 elegida not in esp_en(j2.get("horas") or []))

        # la misma respuesta que usa la pantalla de escoger especialista
        hh = (j.get("horas") or [{}])[0].get("hora")
        if hh:
            c, e2 = P.panel("/especialistas", {"servicio": hace["id"],
                                               "fecha": fecha, "hora": hh})
            P.prueba("y la pantalla de «con quién» dice lo mismo",
                     elegida in {x["id"] for x in (e2.get("especialistas") or [])}, e2)

        # ── 2. el candado del servidor ────────────────────────────────────
        print("\n— el candado, por si alguien se salta la pantalla —")
        c, j = P.panel("/horas", {"servicio": no_hace["id"], "fecha": fecha})
        hora = ((j.get("horas") or [{}])[0] or {}).get("hora")
        if not hora:
            P.saltar("el candado del servidor", "no quedaron horas para probarlo")
        else:
            c, j = P.panel("/reservar", {"servicio": no_hace["id"], "fecha": fecha,
                                         "hora": hora, "especialista": elegida})
            P.prueba("mandar a mano una especialista que no lo hace: no pasa",
                     j.get("ok") is False and j.get("error") == "NO_LO_REALIZA", j)
            c, j = P.panel("/reservar", {"servicio": "servicio-inventado",
                                         "fecha": fecha, "hora": hora})
            P.prueba("y un servicio inventado tampoco",
                     j.get("ok") is False and j.get("error") == "SERVICIO", j)
    finally:
        # Devolver EXACTAMENTE lo que tenía. Antes se borraba todo lo suyo:
        # si la especialista elegida ya tenía servicios, la prueba se los
        # llevaba por delante y la dejaba "haciendo todos" (la regla de la
        # agenda para una especialista sin nada marcado). Una prueba no puede
        # dañar la base que está midiendo.
        bd("delete from especialista_servicios where especialista_id=%s", (elegida,))
        for sv in sorted(antes):
            bd("insert into especialista_servicios(especialista_id, servicio_id) "
               "values (%s,%s) on conflict do nothing", (elegida, sv))
        ahora = {r[0] for r in bd("select servicio_id from especialista_servicios "
                                  "where especialista_id=%s", (elegida,), True)}
        print(f"  ⓘ  {nombre_elegida}: volvió a sus {len(ahora)} servicios — "
              f"{'igual que antes OK' if ahora == antes else '*** NO COINCIDE ***'}")

    # ── 3. reprogramar cambiando el servicio, y «ya llegué» ───────────────
    print("\n— reprogramar cambiando el servicio —")
    c, j = P.panel("/cliente/guardar", {
        "documento": P.DOC, "tipo_doc": "CC", "primer_nombre": "Prueba",
        "primer_apellido": "Cuadre", "telefono": P.TEL, "correo": P.CORREO})
    cliente = (j.get("cliente") or {}).get("id")
    P.prueba("la clienta de prueba queda registrada", bool(cliente), j)
    if not cliente:
        return 1
    P.creado["cliente"] = cliente

    c, j = P.panel("/horas", {"servicio": hace["id"], "fecha": fecha})
    hora = ((j.get("horas") or [{}])[0] or {}).get("hora")
    c, r = P.panel("/reservar", {"servicio": hace["id"], "fecha": fecha, "hora": hora})
    c, j = P.panel("/agendar", {"cliente_id": cliente, "servicio": hace["id"],
                                "fecha": fecha, "hora": hora,
                                "especialista": r.get("especialista"),
                                "reserva": r.get("reserva")})
    cita = (j.get("cita") or {}).get("cita_id")
    P.prueba("agenda la primera cita", bool(cita), j)
    P.creado["citas"].add(cita)

    # se mueve a otro día Y a otro servicio
    fecha2 = None
    for d in range(1, 21):
        f = (P.date.today() + timedelta(days=d)).isoformat()
        if f == fecha:
            continue
        c, j = P.panel("/horas", {"servicio": no_hace["id"], "fecha": f})
        if j.get("horas"):
            fecha2, hora2 = f, j["horas"][0]["hora"]
            break
    if not fecha2:
        P.saltar("reprogramar con otro servicio", "no hay otro día con horas")
    else:
        c, r2 = P.panel("/reservar", {"servicio": no_hace["id"], "fecha": fecha2,
                                      "hora": hora2})
        c, j = P.panel("/cambio", {"documento": P.DOC, "cita_id": cita,
                                   "accion": "reprogramar", "telefono": P.TEL,
                                   "fecha": fecha2, "hora": hora2,
                                   "especialista": r2.get("especialista"),
                                   "servicio": no_hace["id"],
                                   "reserva": r2.get("reserva")})
        nueva = (j.get("cita") or {})
        P.prueba("la mueve y la pantalla muestra el servicio NUEVO",
                 nueva.get("servicio", "").lower() == no_hace["nombre"].lower(),
                 nueva)
        nid = nueva.get("cita_id")
        P.creado["citas"].add(nid)
        fila = bd("""select s.nombre, c.fin - c.inicio
                       from citas c join servicios s on s.id=c.servicio_id
                      where c.id=%s""", (nid,), True)
        P.prueba("y en la agenda queda guardado ese servicio, no el viejo",
                 fila and fila[0][0].lower() == no_hace["nombre"].lower(), fila)
        dur = bd("select duracion from servicios where id=%s", (no_hace["id"],), True)
        P.prueba("con la duración del servicio nuevo",
                 fila and int(fila[0][1].total_seconds() // 60) == dur[0][0],
                 (fila, dur))

    # ── «ya llegué» deja la cita en Llegó ─────────────────────────────────
    print("\n— «ya llegué» contra la base —")
    hoy = P.date.today().isoformat()
    c, j = P.panel("/horas", {"servicio": hace["id"], "fecha": hoy})
    hoy_hora = ((j.get("horas") or [{}])[0] or {}).get("hora")
    if not hoy_hora:
        P.saltar("«ya llegué»", "hoy ya no quedan horas libres")
    else:
        c, r = P.panel("/reservar", {"servicio": hace["id"], "fecha": hoy,
                                     "hora": hoy_hora})
        c, j = P.panel("/agendar", {"cliente_id": cliente, "servicio": hace["id"],
                                    "fecha": hoy, "hora": hoy_hora,
                                    "especialista": r.get("especialista"),
                                    "reserva": r.get("reserva")})
        choy = (j.get("cita") or {}).get("cita_id")
        P.creado["citas"].add(choy)
        c, j = P.panel("/llegada", {"documento": P.DOC, "cita_id": choy})
        P.prueba("la tablet dice que quedó anunciada",
                 j.get("ok") and "anunciada" in (j.get("cita") or {}).get("titulo", "").lower(),
                 j.get("cita"))
        est = bd("""select e.nombre from citas c join estados e on e.id=c.estado_id
                     where c.id=%s""", (choy,), True)
        P.prueba("y en la agenda el estado es «Llegó», no otra cosa",
                 bool(est) and est[0][0].lower().startswith("lleg"), est)

    P.limpiar()
    print(f"\n{P.ok} ok, {P.mal} mal")
    return 1 if (P.mal or P.saltadas) else 0


if __name__ == "__main__":
    sys.exit(main())
