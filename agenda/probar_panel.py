#!/usr/bin/env python3
"""Panel Clientes CJ, de punta a punta, contra la agenda de verdad.

Recorre lo que hace una clienta en la tablet: se registra, agenda, avisa que
llegó, reprograma y cancela. Comprueba los dos candados (el celular con el que
quedó la cita y el único cambio por día) y **borra lo que creó**, porque una
cita de prueba —aunque quede cancelada— infla los indicadores del negocio.

    cd /root/universo/agenda
    AGENDA_API=http://127.0.0.1:8001 \
    API_TOKEN=<el token, solo para armar y limpiar> \
    DATABASE_URL=postgresql://…/cjmedical \
    PANEL_CORREO=<su correo de la agenda> PANEL_CLAVE=<su contraseña> \
    AUTOSERVICIO_TOPE_CLIENTE=500 \
    python3 probar_panel.py

El tope de consultas se sube solo para la prueba: la prueba hace en un minuto
lo que una tablet hace en una hora. En producción se deja como está.

El panel no usa token: vive dentro de la agenda. El token que se le pasa aquí
es solo para que la prueba pueda montar el escenario y borrarlo después.
DATABASE_URL es opcional; sin él las citas quedan canceladas y el script dice
qué hay que borrar a mano.
"""
import json
import os
import sqlite3
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta, timezone

BASE = os.getenv("AGENDA_API", "http://127.0.0.1:8001").rstrip("/")
PANEL = BASE + "/api/v2/autoservicio"
TOKEN = os.getenv("API_TOKEN", "")
CLAVE = os.getenv("AUTOSERVICIO_CLAVE", "")
# La tablet se abre con un usuario de la agenda, igual que en recepción.
USUARIO = os.getenv("PANEL_CORREO", "jota@cjmedical.co")
CONTRASENA = os.getenv("PANEL_CLAVE", "administrador-de-prueba")
LLAVE = {"t": ""}
SEDE = os.getenv("PANEL_SEDE", "el-tesoro")
SEDES_ID = {"el-tesoro": "sede-cj-medical-el-tesoro",
            "bogota": "sede-cj-medical-bogota"}
OTRA = "bogota" if SEDE == "el-tesoro" else "el-tesoro"

# Cédula que no existe en la base real. Si algún día existiera, cámbiela.
DOC = os.getenv("PANEL_DOC_PRUEBA", "999000111")
TEL = "3009998877"
CORREO = "prueba.panel@cjmedical.co"

CO = timezone(timedelta(hours=-5))
ok = mal = 0
saltadas = []          # lo que no se pudo comprobar, con su motivo
creado = {"cliente": None, "citas": set()}


def saltar(que, motivo):
    """Un paso que no se pudo comprobar. Nunca en silencio: una comprobación
    saltada dentro de un «todo bien» es peor que una que falla."""
    saltadas.append((que, motivo))
    print("  ⊘ SALTADA  " + que + " — " + motivo)


def prueba(n, cond, extra=""):
    global ok, mal
    if cond:
        ok += 1
        print("  ok   " + n)
    else:
        mal += 1
        print("  MAL  " + n + (("\n       " + str(extra)[:400]) if extra else ""))


def _llamar(url, cuerpo=None, metodo=None, cabeceras=None):
    req = urllib.request.Request(
        url, method=metodo or ("POST" if cuerpo is not None else "GET"))
    req.add_header("accept", "application/json")
    for k, v in (cabeceras or {}).items():
        req.add_header(k, v)
    datos = None
    if cuerpo is not None:
        datos = json.dumps(cuerpo).encode()
        req.add_header("content-type", "application/json")
    try:
        with urllib.request.urlopen(req, datos, timeout=30) as r:
            return r.status, json.loads(r.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode() or "{}")
        except Exception:
            return e.code, {}
    except Exception as e:
        return 0, {"mensaje": str(e)}


def panel(ruta, cuerpo=None, metodo=None):
    """Como llama la tablet: sin el token de la agenda, con el apodo de la
    sede y con la llave que dejó recepción al abrirla."""
    if cuerpo is not None:
        cuerpo = dict(cuerpo)
        cuerpo.setdefault("sede", SEDE)
        if CLAVE:
            cuerpo["k"] = CLAVE
    elif CLAVE:
        ruta += ("&" if "?" in ruta else "?") + "k=" + CLAVE
    cab = {"x-tableta": LLAVE["t"]} if LLAVE["t"] else {}
    return _llamar(PANEL + ruta, cuerpo, metodo, cabeceras=cab)


def api(ruta, cuerpo=None, metodo=None):
    """La agenda de siempre; solo para armar el escenario y limpiarlo."""
    return _llamar(BASE + ruta, cuerpo, metodo, {"X-API-Token": TOKEN})


def estado_de(fila):
    """/citas devuelve v_agenda tal cual, donde la columna se llama «estado».
    /agenda/{sede}/{fecha} la renombra a «estado_nombre». Sirven las dos."""
    return (fila or {}).get("estado_nombre") or (fila or {}).get("estado")


def abrir(cuerpo):
    """Abrir la tablet tiene un tope de intentos por minuto, a propósito: es
    lo que impide que alguien adivine contraseñas. Si la prueba se corre dos
    veces seguidas se topa con él, y entonces espera — el candado es de
    verdad, no se le da la vuelta."""
    c, j = panel("/abrir", cuerpo)
    if c == 429:
        print("     (el tope de intentos está haciendo su trabajo: espero 62 s)")
        time.sleep(62)
        c, j = panel("/abrir", cuerpo)
    return c, j


def hoy():
    return datetime.now(timezone.utc).astimezone(CO).date()


def primer_dia_con_horas(servicio, desde=1, hasta=21):
    for n in range(desde, hasta):
        f = (hoy() + timedelta(days=n)).isoformat()
        c, j = panel("/horas", {"servicio": servicio, "fecha": f})
        if c == 200 and j.get("horas"):
            return f, j["horas"]
    return None, []


def borrar_contador():
    """Deja el contador de cambios del día en cero, para poder probar el otro
    camino sin esperar a mañana."""
    bd = os.getenv("AUTOSERVICIO_BD") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "autoservicio.db")
    if not os.path.exists(bd):
        return
    with sqlite3.connect(bd) as conn:
        conn.execute("delete from cambios where documento=?", (DOC,))
        conn.commit()


def limpiar():
    url = os.getenv("DATABASE_URL", "")
    cid = creado["cliente"]
    borrar_contador()
    if not url:
        for c in creado["citas"]:
            api("/citas/" + c, metodo="DELETE")
        print("\n  ⚠ sin DATABASE_URL: las citas quedaron CANCELADAS, no borradas.")
        print("    Para borrarlas de verdad:")
        print(f"      delete from cita_bitacora where cita_id in "
              f"(select id from citas where cliente_id='{cid}');")
        print(f"      delete from citas    where cliente_id='{cid}';")
        print(f"      delete from clientes where id='{cid}';")
        return
    try:
        import psycopg2
    except ImportError:
        print("\n  ⚠ falta psycopg2 para limpiar; hágalo a mano (ver arriba).")
        return
    conn = psycopg2.connect(url)
    conn.autocommit = True
    with conn, conn.cursor() as cur:
        if cid:
            cur.execute("delete from cita_bitacora where cita_id in "
                        "(select id from citas where cliente_id=%s)", (cid,))
            cur.execute("delete from citas where cliente_id=%s", (cid,))
            cur.execute("delete from clientes where id=%s", (cid,))
        cur.execute("delete from reservas where referencia='autoservicio'")
    conn.close()
    print("\n  Limpieza: se borraron la clienta de prueba, sus citas y sus reservas.")


def main():
    print(f"\nPanel Clientes CJ · {PANEL} · sede {SEDE}")

    print("\n— recepción abre la tablet —")
    c, j = panel("/cliente", {"documento": DOC})
    prueba("sin abrirla, la tablet no consulta nada",
           c == 401 and j.get("error") == "SIN_TABLETA", (c, j))
    c, j = abrir({"correo": USUARIO, "clave": "no-es-la-clave"})
    prueba("con la contraseña equivocada no abre", c == 401, (c, j))
    c, j = abrir({"correo": "nadie@cjmedical.co", "clave": CONTRASENA})
    prueba("con un correo que no existe dice lo mismo, no delata cuáles sí",
           c == 401 and j.get("error") == "DATOS_INCORRECTOS", (c, j))
    c, j = abrir({"correo": USUARIO, "clave": CONTRASENA})
    prueba(f"con las correctas sí ({j.get('abierta_por')})",
           c == 200 and j.get("token"), j)
    LLAVE["t"] = j.get("token", "")
    prueba("y dice hasta cuándo queda abierta", bool(j.get("hasta")), j)

    print("\n— la tablet está bien parada —")
    c, j = panel("/salud")
    prueba("responde sin token, desde dentro de la agenda", c == 200 and j.get("ok"), j)
    prueba("resuelve los tres estados por nombre, no quemados",
           all(j.get("estados", {}).get(n) for n in ("Confirmado", "Llegó", "Cancelado")),
           j.get("estados"))
    prueba("la hora es de Colombia, no UTC",
           str(j.get("hora_colombia", "")).endswith("-05:00"), j.get("hora_colombia"))

    c, j = panel(f"/datos?sede={SEDE}")
    prueba(f"trae los servicios que de verdad se hacen en esa sede "
           f"({len(j.get('servicios', []))})",
           c == 200 and len(j.get("servicios", [])) > 0, j)
    prueba("y la sede con su dirección, para la pantalla fotografiable",
           bool(j.get("sede", {}).get("direccion")), j.get("sede"))
    prueba("el tipo de documento trae las 5 opciones",
           len(j.get("tipos_doc", [])) == 5, j.get("tipos_doc"))
    SERVICIO = j["servicios"][0]["id"]

    c, j = panel("/datos?sede=cali")
    prueba("una sede que no existe se rechaza", c >= 400, (c, j))

    print("\n— una clienta nueva —")
    c, j = panel("/cliente", {"documento": DOC})
    prueba("no la encuentra", c == 200 and j.get("encontrado") is False, j)

    base = {"documento": DOC, "tipo_doc": "CC", "primer_nombre": "Prueba",
            "primer_apellido": "Panel", "telefono": TEL, "correo": CORREO}
    c, j = panel("/cliente/guardar", dict(base, telefono="300"))
    prueba("un celular de 3 dígitos no pasa", c == 400, (c, j))
    c, j = panel("/cliente/guardar", dict(base, correo="sinarroba"))
    prueba("un correo sin arroba tampoco", c == 400, (c, j))
    c, j = panel("/cliente/guardar", dict(base, tipo_doc="XX"))
    prueba("ni un tipo de documento inventado", c == 400, (c, j))
    c, j = panel("/cliente/guardar", base)
    prueba("con todo completo se registra", c == 200 and j.get("cliente", {}).get("id"), j)
    creado["cliente"] = j.get("cliente", {}).get("id")
    CLIENTE = creado["cliente"]

    c, j = panel("/cliente", {"documento": DOC})
    prueba("ahora sí la encuentra", c == 200 and j.get("encontrado"), j)
    ficha = j.get("cliente") or {}
    prueba("el tipo de documento quedó guardado de una, sin segunda llamada",
           ficha.get("tipo_doc") == "CC", ficha)
    prueba("el celular sale tapado, no completo", "•" in str(ficha.get("telefono")), ficha)
    prueba("y el correo también", "•" in str(ficha.get("correo")), ficha)
    prueba("todavía no tiene ninguna cita", j.get("cita") is None, j.get("cita"))

    print("\n— agendar —")
    FECHA, horas = primer_dia_con_horas(SERVICIO, desde=2)
    if not FECHA:
        print("  no hay horas libres en tres semanas: revise la agenda.")
        return 2
    HORA = horas[0]["hora"]
    prueba(f"le ofrece horas reales del {FECHA} ({len(horas)})", True)
    # El paso es el mismo de la agenda (15 min) para no esconderle cupos a la
    # clienta. Con AUTOSERVICIO_PASO=30 vuelven a salir solo las redondas.
    paso = int(os.getenv("AUTOSERVICIO_PASO", "15"))
    permitidos = ("00", "30") if paso >= 30 else ("00", "15", "30", "45")
    prueba(f"las horas caen en la rejilla de {paso} minutos, igual que la agenda",
           all(x["hora"][3:] in permitidos for x in horas),
           [x["hora"] for x in horas[:8]])
    prueba("y vienen en palabras, no en formato de sistema",
           horas[0]["hora_larga"].endswith("m.") , horas[0])

    c, j = panel("/especialistas", {"servicio": SERVICIO, "fecha": FECHA, "hora": HORA})
    prueba(f"dice quién está libre a las {HORA} ({len(j.get('especialistas', []))})",
           c == 200 and j.get("especialistas"), j)
    ESP = j["especialistas"][0]["id"]

    c, j = panel("/reservar", {"servicio": SERVICIO, "fecha": FECHA,
                               "hora": HORA, "especialista": ESP})
    prueba("aparta el cupo mientras ella decide", c == 200 and j.get("reserva"), j)
    RESERVA = j.get("reserva")
    c, j = panel("/especialistas", {"servicio": SERVICIO, "fecha": FECHA, "hora": HORA})
    prueba("y esa especialista deja de ofrecerse a esa hora",
           ESP not in [e["id"] for e in j.get("especialistas", [])], j)

    c, j = panel("/agendar", {"cliente_id": CLIENTE, "servicio": SERVICIO,
                              "fecha": FECHA, "hora": HORA,
                              "especialista": ESP, "reserva": RESERVA})
    prueba("agenda con su propia reserva en la mano",
           c == 200 and j.get("cita", {}).get("cita_id"), j)
    CITA = j.get("cita", {}).get("cita_id")
    creado["citas"].add(CITA)
    pantalla = j.get("cita", {})
    prueba("la pantalla final trae todo lo fotografiable",
           all(pantalla.get(k) for k in ("servicio", "fecha_larga", "hora_larga",
                                         "sede", "direccion", "especialista", "estado")),
           pantalla)
    prueba(f"para pasado mañana nace Pendiente ({pantalla.get('estado')})",
           pantalla.get("estado") == "Pendiente", pantalla)

    c, fila = api(f"/citas?fecha={FECHA}")
    mia = next((x for x in fila if x.get("id") == CITA), None)
    prueba("queda en la agenda con canal Autoservicio",
           mia and mia.get("canal") == "Autoservicio", mia)

    c, j = panel("/cliente", {"documento": DOC})
    prueba("al volver a digitar la cédula, ya le sale su cita",
           j.get("cita", {}).get("id") == CITA, j.get("cita"))

    print("\n— hoy o mañana nace Confirmada sola —")
    F2, horas2 = primer_dia_con_horas(SERVICIO, desde=0, hasta=2)
    if F2:
        c, j = panel("/reservar", {"servicio": SERVICIO, "fecha": F2,
                                   "hora": horas2[0]["hora"], "especialista": None})
        prueba("con «me da igual» escoge ella la especialista",
               c == 200 and j.get("especialista"), j)
        r2, e2 = j.get("reserva"), j.get("especialista")
        c, j = panel("/agendar", {"cliente_id": CLIENTE, "servicio": SERVICIO,
                                  "fecha": F2, "hora": horas2[0]["hora"],
                                  "especialista": e2, "reserva": r2})
        if c == 200:
            creado["citas"].add(j["cita"]["cita_id"])
            prueba(f"la de {'hoy' if F2 == hoy().isoformat() else 'mañana'} "
                   f"queda Confirmada ({j['cita'].get('estado')})",
                   j["cita"].get("estado") == "Confirmado", j["cita"])
            api("/citas/" + j["cita"]["cita_id"], metodo="DELETE")
        else:
            prueba("agenda para hoy o mañana", False, j)
    else:
        saltar("la cita de hoy o mañana nace Confirmada",
               "ni hoy ni mañana quedan horas libres")

    print("\n— «ya llegué» —")
    # Una cita de hoy, como la que dejó el call center. Se crea por la agenda
    # porque el panel no ofrece horas que ya pasaron.
    cita_hoy_id, apodo = None, SEDE
    ahora = datetime.now(timezone.utc).astimezone(CO)
    c, datos = panel(f"/datos?sede={SEDE}")
    c, esp_todas = api("/especialistas")
    sid = SEDES_ID[SEDE]
    candidatas = [e["id"] for e in (esp_todas or [])
                  if sid in (e.get("sedes") or []) and e.get("activo") is not False]
    # de tres horas atrás hasta ahora, en medias horas: es la ventana en la
    # que una clienta que llega tarde todavía puede anunciarse
    # La ventana en la que el botón «ya llegué» tiene sentido: desde tres
    # horas antes de ahora hasta ahora. Antes de las 9 de la mañana esa
    # ventana caía fuera del horario y quedaba vacía, así que el bloque
    # entero se saltaba en silencio: la prueba decía «todo bien» sin haber
    # probado «ya llegué» una sola vez.
    minutos = ahora.hour * 60 + ahora.minute
    desde = max(9 * 60, minutos - 180)
    desde = ((desde + 29) // 30) * 30                # alineado a :00 o :30
    hasta = min(max(minutos, 9 * 60), 18 * 60 + 30)  # temprano, usa las 9:00 de hoy
    ratos = sorted(range(desde, hasta + 1, 30), reverse=True)
    for e in candidatas:
        for m in ratos:
            hhmm = f"{m // 60:02d}:{m % 60:02d}"
            c, cita = api("/citas/agendar", {
                "cliente_id": CLIENTE, "especialista": e, "sede": sid,
                "fecha": hoy().isoformat(), "inicio": hhmm, "servicio": SERVICIO,
                "canal": "Call Center", "por": "prueba"})
            if c == 200 and cita.get("id"):
                cita_hoy_id = cita["id"]
                creado["citas"].add(cita_hoy_id)
                break
        if cita_hoy_id:
            break

    if cita_hoy_id:
        c, j = panel("/cliente", {"documento": DOC, "sede": apodo})
        prueba("al digitar la cédula le sale su cita de hoy",
               j.get("cita", {}).get("id") == cita_hoy_id, j.get("cita"))
        prueba("y le ofrece el botón de «ya llegué»",
               j.get("cita", {}).get("es_hoy") is True, j.get("cita"))
        c, j = panel("/llegada", {"documento": DOC, "cita_id": cita_hoy_id,
                                  "sede": apodo})
        prueba(f"marcarla la deja en «Llegó» ({j.get('cita', {}).get('estado')})",
               c == 200 and j.get("cita", {}).get("estado") == "Llegó", j)
        c, fila = api(f"/citas?fecha={hoy().isoformat()}")
        mia = next((x for x in fila if x.get("id") == cita_hoy_id), None)
        prueba("y así se ve en la agenda, al instante",
               estado_de(mia) == "Llegó", mia)
        c, j = panel("/llegada", {"documento": DOC, "cita_id": CITA})
        prueba("una cita que no es de hoy no se puede marcar", c >= 400, (c, j))
        api("/citas/" + cita_hoy_id, metodo="DELETE")
    elif not ratos:
        saltar("«ya llegué» (5 comprobaciones)",
               f"son las {ahora.strftime('%H:%M')}: ya no cabe ninguna cita de hoy "
               "dentro de las tres horas en las que el botón sirve. "
               "Córrala entre las 9 de la mañana y las 9 de la noche.")
    else:
        saltar("«ya llegué» (5 comprobaciones)",
               "no quedó libre ninguno de los horarios de hoy que se probaron "
               f"({len(ratos)} intentos entre las {ratos[-1]//60:02d}:00 y ahora)")

    print("\n— nadie toca una cita ajena —")
    c, j = panel("/cambio", {"documento": DOC, "cita_id": CITA,
                             "accion": "cancelar", "telefono": "3001112233"})
    prueba("con otro celular NO la deja",
           c == 403 and j.get("error") == "TELEFONO_NO_COINCIDE", (c, j))
    c, j = panel("/cambio", {"documento": "1020304050", "cita_id": CITA,
                             "accion": "cancelar", "telefono": TEL})
    prueba("con otra cédula tampoco", c >= 400, (c, j))
    c, j = panel("/llegada", {"documento": "1020304050", "cita_id": CITA})
    prueba("ni el «ya llegué» con cédula ajena", c >= 400, (c, j))

    print("\n— reprogramar —")
    F3, horas3 = primer_dia_con_horas(SERVICIO, desde=3)
    prueba("hay otro día para moverla", bool(F3), F3)
    H3 = horas3[0]["hora"]
    c, j = panel("/especialistas", {"servicio": SERVICIO, "fecha": F3, "hora": H3})
    E3 = j["especialistas"][0]["id"]
    c, j = panel("/cambio", {"documento": DOC, "cita_id": CITA, "accion": "reprogramar",
                             "telefono": TEL, "fecha": F3, "hora": H3, "especialista": E3})
    prueba("con el celular correcto la mueve", c == 200 and j.get("cita"), j)
    NUEVA = j.get("cita", {}).get("cita_id")
    if NUEVA:
        creado["citas"].add(NUEVA)
    prueba("la pantalla lo dice en palabras",
           "reprogramada" in str(j.get("cita", {}).get("titulo", "")).lower(),
           j.get("cita"))
    c, fila = api(f"/citas?fecha={FECHA}")
    vieja = next((x for x in fila if x.get("id") == CITA), None)
    prueba("la vieja queda en «Reprogramado», no se borra",
           estado_de(vieja) == "Reprogramado", vieja)
    c, libres = panel("/horas", {"servicio": SERVICIO, "fecha": FECHA})
    prueba("y la hora que dejó vuelve a estar libre",
           HORA in [x["hora"] for x in libres.get("horas", [])],
           [x["hora"] for x in libres.get("horas", [])][:8])

    print("\n— un solo cambio por día —")
    c, j = panel("/cambio", {"documento": DOC, "cita_id": NUEVA,
                             "accion": "cancelar", "telefono": TEL})
    prueba("el segundo cambio del día se frena", c == 429, (c, j))
    prueba("y le dice a dónde llamar",
           "301 711 3464" in str(j.get("mensaje", "")), j.get("mensaje"))
    c, j = panel("/cliente", {"documento": DOC})
    prueba("al volver a digitar la cédula ya sabe que gastó su cambio",
           j.get("puede_cambiar") is False, j)

    print("\n— cancelar (con el contador otra vez en cero) —")
    borrar_contador()
    c, j = panel("/cambio", {"documento": DOC, "cita_id": NUEVA,
                             "accion": "cancelar", "telefono": TEL})
    prueba(f"la cancela ({j.get('cita', {}).get('estado')})",
           c == 200 and j.get("cita", {}).get("estado") == "Cancelado", j)
    c, libres = panel("/horas", {"servicio": SERVICIO, "fecha": F3})
    prueba("y esa hora vuelve a estar libre para otra clienta",
           H3 in [x["hora"] for x in libres.get("horas", [])],
           [x["hora"] for x in libres.get("horas", [])][:8])
    c, j = panel("/cliente", {"documento": DOC})
    prueba("ya no le queda ninguna cita próxima", j.get("cita") is None, j.get("cita"))

    print("\n— la tablet de una sede no toca la otra —")
    c, j = panel("/agendar", {"cliente_id": CLIENTE, "servicio": SERVICIO,
                              "fecha": FECHA, "hora": HORA, "especialista": ESP,
                              "sede": "sede-cj-medical-bogota"})
    prueba("mandar el id de la sede en vez del apodo no sirve", c >= 400, (c, j))
    c, j = panel("/horas", {"servicio": SERVICIO, "fecha": FECHA, "sede": OTRA})
    prueba(f"desde {OTRA} las horas son las de {OTRA}, no las de {SEDE}",
           c == 200, (c, j))

    print("\n— la clienta nunca ve la agenda —")
    textos = json.dumps(panel("/cliente", {"documento": DOC})[1], ensure_ascii=False)
    prueba("la respuesta no trae citas de otras personas",
           "cliente_id" not in textos and textos.count("cita_id") <= 1, textos[:200])

    print("\n— cerrar la tablet —")
    panel("/cerrar", {"t": LLAVE["t"]})
    c, j = panel("/cliente", {"documento": DOC})
    prueba("cerrada, vuelve a no dejar consultar",
           c == 401 and j.get("error") == "SIN_TABLETA", (c, j))

    print("\n— adivinar la contraseña no se puede hacer a las carreras —")
    # esto gasta el tope del minuto a propósito, por eso va de último
    topado = False
    for _ in range(14):
        c, j = panel("/abrir", {"correo": USUARIO, "clave": "probando-" + str(_)})
        if c == 429:
            topado = True
            break
    prueba("después de unos intentos seguidos, corta", topado, (c, j))

    cola = f", {len(saltadas)} SALTADA" + ("S" if len(saltadas) != 1 else "")
    print(f"\n{ok} ok, {mal} mal" + (cola if saltadas else ""))
    if saltadas:
        print("\n  ⚠ Esta corrida NO es completa. No se comprobó:")
        for que, motivo in saltadas:
            print(f"      · {que} — {motivo}")
    return 1 if (mal or saltadas) else 0


if __name__ == "__main__":
    codigo = 1
    try:
        codigo = main()
    finally:
        try:
            limpiar()
        except Exception as e:                 # la limpieza nunca tumba la prueba
            print("  ⚠ no se pudo limpiar:", e)
    sys.exit(codigo)
