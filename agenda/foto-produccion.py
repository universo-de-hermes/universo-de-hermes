#!/usr/bin/env python3
"""Una foto de la agenda de producción, para que yo deje de adivinar.

POR QUÉ EXISTE
Mi copia de la base no es la suya. Hoy eso costó dos veces: una prueba mía
pasaba en verde aquí y en producción le habría borrado asignaciones de verdad,
y no pude responder lo de la duración de un servicio porque en mi copia sí
cuadra. Esta foto cierra esa brecha.

QUÉ SE LLEVA
La forma de la agenda y sus datos de configuración: tablas y columnas,
servicios con sus duraciones, quién realiza qué, sedes, horarios, estados,
versión de Postgres y zona horaria, y conteos agregados.

QUÉ NO SE LLEVA — NUNCA
Ni un dato de una clienta. Ni nombres, ni cédulas, ni teléfonos, ni correos,
ni notas de citas, ni el contenido de ninguna cita concreta. Solo conteos.
Tampoco contraseñas ni tokens: de las variables de entorno solo se dice si
están puestas, jamás lo que valen. Y no escribe nada en la base: todas las
consultas son de lectura.

CÓMO SE USA
    DATABASE_URL=postgresql://…/cjmedical python3 foto-produccion.py

Deja dos archivos al lado:
    foto-produccion.json   — para mí
    foto-produccion.txt    — para que usted lo lea ANTES de mandarlo

Léalo. Si algo no le gusta, no lo mande.

    --sin-nombres   cambia los nombres de las especialistas por «Especialista 1»,
                    «Especialista 2»… El cuadre se sigue entendiendo igual.
"""
import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import date, datetime

DB = os.getenv("DATABASE_URL", "")
SALIDA = os.path.dirname(os.path.abspath(__file__))

# Las variables del panel de las que se informa. De las que llevan secreto se
# dice "puesta" o "sin poner", nunca el valor.
SECRETAS = {"AUTOSERVICIO_CLAVE", "API_TOKEN", "DATABASE_URL", "PANEL_CLAVE",
            "COOKIE_SECRETO", "SECRET_KEY"}
VARIABLES = ["AUTOSERVICIO_CLAVE", "AUTOSERVICIO_ABIERTO", "AUTOSERVICIO_DIAS",
             "AUTOSERVICIO_PASO", "AUTOSERVICIO_MINUTOS", "AUTOSERVICIO_TOPE",
             "AUTOSERVICIO_TOPE_CLIENTE", "AUTOSERVICIO_DATOS_COMPLETOS",
             "AUTOSERVICIO_BD", "API_TOKEN", "DATABASE_URL", "ORIGENES", "TZ"]


def conectar():
    if not DB:
        sys.exit("Falta DATABASE_URL.\n"
                 "  DATABASE_URL=postgresql://usuario@localhost/cjmedical "
                 "python3 foto-produccion.py")
    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        sys.exit("Falta psycopg2:  pip3 install psycopg2-binary")
    cn = psycopg2.connect(DB)
    cn.set_session(readonly=True, autocommit=True)   # de lectura, y punto
    return cn


def q(cn, sql, args=()):
    import psycopg2.extras
    with cn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(sql, args)
        return [dict(r) for r in cur.fetchall()]


def limpio(v):
    """Para que el JSON no lleve tipos raros de Postgres."""
    if isinstance(v, (date, datetime)):
        return v.isoformat()
    if hasattr(v, "total_seconds"):
        return int(v.total_seconds() // 60)
    if isinstance(v, (list, tuple)):
        return [limpio(x) for x in v]
    if isinstance(v, dict):
        return {k: limpio(x) for k, x in v.items()}
    return v


def tomar(cn, sin_nombres):
    f = {"tomada": datetime.now().isoformat(timespec="seconds"),
         "aviso": "Sin datos de clientas. Solo configuración y conteos."}

    # ── el motor ──────────────────────────────────────────────────────────
    f["postgres"] = {
        "version": q(cn, "select version() as v")[0]["v"].split(",")[0],
        "zona_de_la_base": q(cn, "show timezone")[0]["TimeZone"],
        "ahora_sin_zona": str(q(cn, "select now()::timestamp as t")[0]["t"]),
        "hoy_en_colombia": str(q(cn, "select (now() at time zone 'America/Bogota')::date as d")[0]["d"]),
    }

    # ── el esquema: tablas y columnas, sin una sola fila ───────────────────
    cols = q(cn, """select table_name, column_name, data_type, is_nullable
                      from information_schema.columns
                     where table_schema='public'
                     order by table_name, ordinal_position""")
    tablas = {}
    for c in cols:
        tablas.setdefault(c["table_name"], []).append(
            f"{c['column_name']} {c['data_type']}" + ("" if c["is_nullable"] == "YES" else " NOT NULL"))
    f["tablas"] = tablas

    f["conteos"] = {}
    for t in sorted(tablas):
        try:
            f["conteos"][t] = q(cn, f'select count(*) as n from "{t}"')[0]["n"]
        except Exception as e:
            f["conteos"][t] = "no se pudo contar: " + str(e)[:60]

    # ── la función de disponibilidad, que es el corazón ───────────────────
    fn = q(cn, """select p.proname, pg_get_functiondef(p.oid) as cuerpo
                    from pg_proc p join pg_namespace n on n.oid=p.pronamespace
                   where n.nspname='public' and p.proname in
                     ('huecos_del_dia','agendar_cita','apartar_cupo',
                      'reprogramar_cita','cambiar_estado','crear_cliente')""")
    f["funciones"] = sorted({x["proname"] for x in fn})
    huecos = next((x["cuerpo"] for x in fn if x["proname"] == "huecos_del_dia"), "")
    f["huecos_del_dia"] = {
        "existe": bool(huecos),
        # El arreglo de la hora de Colombia: si NO está, la agenda esconde
        # cupos de día y ofrece horas viejas de noche.
        "tiene_el_arreglo_de_hora_colombia":
            bool(re.search(r"at\s+time\s+zone\s+'America/Bogota'", huecos or "")),
        # Postgres reescribe la firma a su manera ("p_paso integer DEFAULT 15"),
        # así que el patrón no puede pegarse a cómo se escribió el SQL.
        "paso_por_defecto":
            (re.search(r"p_paso\s+\w+\s+DEFAULT\s+(\d+)", huecos or "", re.I)
             or [None, "?"])[1],
        "margen_por_defecto":
            (re.search(r"p_margen\s+\w+\s+DEFAULT\s+(\d+)", huecos or "", re.I)
             or [None, "?"])[1],
        "filtra_por_especialista_servicios":
            "especialista_servicios" in (huecos or ""),
    }

    # ── servicios: lo que la tablet muestra y lo que reparte el día ───────
    servs = q(cn, """select id, nombre, duracion, activo,
                            coalesce(codigo,'') as codigo
                       from servicios order by nombre""")
    f["servicios"] = [{k: limpio(v) for k, v in s.items()} for s in servs]

    # nombres repetidos (sin tildes ni mayúsculas) con duraciones distintas
    def plano(t):
        import unicodedata
        t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode()
        return " ".join(t.lower().split())
    grupos = {}
    for s in servs:
        if s["activo"]:
            grupos.setdefault(plano(s["nombre"]), []).append(s)
    f["servicios_repetidos"] = [
        {"nombre": g[0]["nombre"], "veces": len(g),
         "duraciones": sorted({x["duracion"] for x in g}),
         "ids": [x["id"] for x in g]}
        for g in grupos.values() if len(g) > 1]

    # lo que dice el maestro contra lo que duran las citas de verdad
    reales = q(cn, """select s.id, s.nombre, s.duracion,
                             (extract(epoch from (c.fin - c.inicio))/60)::int as minutos,
                             count(*) as n
                        from servicios s
                        join citas c on c.servicio_id = s.id and c.fin > c.inicio
                       group by 1,2,3,4""")
    por_serv = {}
    for r in reales:
        por_serv.setdefault((r["id"], r["nombre"], r["duracion"]), Counter())[r["minutos"]] += r["n"]
    f["duracion_maestro_vs_citas"] = []
    for (sid, nombre, dur), cuenta in sorted(por_serv.items(), key=lambda k: k[0][1]):
        manda, veces = cuenta.most_common(1)[0]
        f["duracion_maestro_vs_citas"].append({
            "servicio": nombre, "id": sid, "maestro": dur,
            "lo_que_mas_dura": manda, "citas_asi": veces,
            "total_citas": sum(cuenta.values()),
            "reparto": dict(cuenta.most_common(5)),
            "cuadra": manda == dur})

    # ── especialistas, sedes, horarios ────────────────────────────────────
    esps = q(cn, """select e.id, trim(e.nombres||' '||e.apellidos) as nombre, e.activo
                      from especialistas e order by 2""")
    if sin_nombres:
        for i, e in enumerate(esps, 1):
            e["nombre"] = f"Especialista {i}"
    nombre_de = {e["id"]: e["nombre"] for e in esps}

    pares = q(cn, "select especialista_id, servicio_id from especialista_servicios")
    por_esp = {}
    for p in pares:
        por_esp.setdefault(p["especialista_id"], []).append(p["servicio_id"])
    nom_serv = {s["id"]: s["nombre"] for s in servs}
    f["quien_hace_que"] = [
        {"especialista": e["nombre"], "activa": e["activo"],
         "servicios": sorted(nom_serv.get(x, x) for x in por_esp.get(e["id"], [])),
         "sin_marcar_nada": not por_esp.get(e["id"])}
        for e in esps]
    f["regla"] = ("Una especialista sin ningún servicio marcado realiza TODOS. "
                  "Si la tabla está vacía, la agenda dice que todas hacen todo.")

    f["sedes"] = [{k: limpio(v) for k, v in s.items()} for s in
                  q(cn, """select id, nombre, coalesce(ciudad,'') as ciudad,
                                  coalesce(direccion,'') as direccion,
                                  (coalesce(direccion,'')='') as sin_direccion
                             from sedes order by nombre""")]
    f["estados"] = [{k: limpio(v) for k, v in s.items()} for s in
                    q(cn, "select id, nombre, activo from estados order by nombre")]

    f["horarios_por_sede"] = [{k: limpio(v) for k, v in s.items()} for s in
        q(cn, """select se.nombre as sede,
                        count(distinct h.especialista_id) as especialistas_con_horario,
                        count(*) as franjas,
                        min(h.desde)::text as abre, max(h.hasta)::text as cierra
                   from horarios h join sedes se on se.id=h.sede_id
                  group by 1 order by 1""")]

    esp_sede = q(cn, """select se.nombre as sede, count(*) as especialistas
                          from especialista_sedes es join sedes se on se.id=es.sede_id
                          join especialistas e on e.id=es.especialista_id
                         where e.activo group by 1 order by 1""")
    f["especialistas_por_sede"] = [{k: limpio(v) for k, v in s.items()} for s in esp_sede]

    # ── conteos de citas: agregados, sin una sola cita identificable ──────
    f["citas_por_canal"] = [{k: limpio(v) for k, v in s.items()} for s in
        q(cn, """select coalesce(nullif(canal,''),'(sin canal)') as canal, count(*) as n,
                        min(fecha)::text as desde, max(fecha)::text as hasta
                   from citas group by 1 order by 2 desc""")]
    f["citas_por_estado"] = [{k: limpio(v) for k, v in s.items()} for s in
        q(cn, """select coalesce(e.nombre,'(sin estado)') as estado, count(*) as n
                   from citas c left join estados e on e.id=c.estado_id
                  group by 1 order by 2 desc""")]
    f["citas_por_mes"] = [{k: limpio(v) for k, v in s.items()} for s in
        q(cn, """select to_char(fecha,'YYYY-MM') as mes, count(*) as n
                   from citas where fecha >= current_date - interval '6 months'
                  group by 1 order by 1""")]

    # ── el entorno del proceso: si están puestas, no lo que valen ─────────
    f["variables"] = {}
    for v in VARIABLES:
        hay = os.getenv(v)
        f["variables"][v] = ("(puesta, no se copia su valor)" if v in SECRETAS and hay
                             else (hay if hay else "sin poner"))
    return f


def legible(f, sin_nombres):
    L = []
    w = L.append
    w("═" * 70)
    w("  FOTO DE LA AGENDA — " + f["tomada"])
    w("═" * 70)
    w("")
    w("  Esto es lo que se llevaría el archivo .json. NO incluye ningún dato")
    w("  de clientas: ni nombres, ni cédulas, ni teléfonos, ni correos, ni el")
    w("  contenido de ninguna cita. Solo configuración y conteos.")
    if sin_nombres:
        w("  Los nombres de las especialistas van cambiados por «Especialista N».")
    w("")
    w("─ EL MOTOR " + "─" * 58)
    for k, v in f["postgres"].items():
        w(f"   {k:<22} {v}")
    w("")
    h = f["huecos_del_dia"]
    w("─ LA FUNCIÓN QUE REPARTE EL DÍA " + "─" * 38)
    w(f"   existe                              {h['existe']}")
    w(f"   paso por defecto                    {h['paso_por_defecto']} min")
    w(f"   filtra por quién realiza el servicio {h['filtra_por_especialista_servicios']}")
    marca = "SÍ" if h["tiene_el_arreglo_de_hora_colombia"] else "NO  ← ojo"
    w(f"   tiene el arreglo de hora Colombia   {marca}")
    if not h["tiene_el_arreglo_de_hora_colombia"]:
        w("      Sin ese arreglo, la agenda esconde cupos por la mañana y")
        w("      ofrece horas ya pasadas por la noche.")
    w("")
    w("─ SERVICIOS " + "─" * 58)
    act = [s for s in f["servicios"] if s["activo"]]
    w(f"   {len(act)} activos de {len(f['servicios'])}")
    dur = Counter(s["duracion"] for s in act)
    w("   duraciones: " + ", ".join(f"{k} min ×{v}" for k, v in sorted(dur.items())))
    if f["servicios_repetidos"]:
        w("   ⚠ nombres repetidos con duraciones distintas:")
        for r in f["servicios_repetidos"]:
            w(f"        «{r['nombre']}» ×{r['veces']} → {r['duraciones']} min")
    else:
        w("   ✓ ningún nombre repetido")
    desfase = [d for d in f["duracion_maestro_vs_citas"] if not d["cuadra"]]
    if desfase:
        w("   ⚠ el maestro no coincide con lo que duran las citas:")
        for d in desfase:
            w(f"        {d['servicio'][:38]:<40} maestro {d['maestro']} · "
              f"de verdad {d['lo_que_mas_dura']} ({d['citas_asi']} de {d['total_citas']})")
    else:
        w("   ✓ todos los maestros coinciden con sus citas")
    w("")
    w("─ QUIÉN HACE QUÉ " + "─" * 53)
    sin = [x for x in f["quien_hace_que"] if x["activa"] and x["sin_marcar_nada"]]
    con = [x for x in f["quien_hace_que"] if x["activa"] and not x["sin_marcar_nada"]]
    w(f"   {len(con)} con servicios marcados · {len(sin)} sin marcar nada")
    for x in con:
        w(f"      {x['especialista'][:34]:<36} {len(x['servicios'])} servicios")
    if sin:
        w("   ⚠ estas, por la regla de la agenda, realizan TODOS los servicios:")
        for x in sin:
            w(f"        {x['especialista']}")
    w("")
    w("─ SEDES Y HORARIOS " + "─" * 51)
    for s in f["sedes"]:
        d = "(sin dirección cargada)" if s["sin_direccion"] else s["direccion"][:44]
        w(f"   {s['nombre'][:30]:<32} {d}")
    for x in f["horarios_por_sede"]:
        w(f"   {x['sede'][:30]:<32} {x['especialistas_con_horario']} con horario, "
          f"{x['franjas']} franjas, {x['abre']}–{x['cierra']}")
    w("")
    w("─ CITAS (solo conteos) " + "─" * 47)
    for c in f["citas_por_canal"]:
        w(f"   {c['canal'][:22]:<24} {c['n']:>6}   {c['desde']} → {c['hasta']}")
    w("")
    for c in f["citas_por_estado"]:
        w(f"   {c['estado'][:22]:<24} {c['n']:>6}")
    w("")
    w("─ VARIABLES DEL PANEL " + "─" * 48)
    for k, v in f["variables"].items():
        w(f"   {k:<30} {v}")
    w("")
    w("═" * 70)
    w("  Si algo de esto no le gusta, no mande el archivo.")
    w("═" * 70)
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="Foto de la agenda, sin datos de clientas")
    ap.add_argument("--sin-nombres", action="store_true",
                    help="cambia los nombres de las especialistas por «Especialista N»")
    a = ap.parse_args()
    cn = conectar()
    try:
        f = tomar(cn, a.sin_nombres)
    finally:
        cn.close()

    txt = legible(f, a.sin_nombres)
    print(txt)
    pj = os.path.join(SALIDA, "foto-produccion.json")
    pt = os.path.join(SALIDA, "foto-produccion.txt")
    with open(pj, "w", encoding="utf-8") as fh:
        json.dump(limpio(f), fh, ensure_ascii=False, indent=1)
    with open(pt, "w", encoding="utf-8") as fh:
        fh.write(txt + "\n")

    # Red de seguridad: si por lo que sea se coló algo que parece una cédula o
    # un celular colombiano, se avisa fuerte en vez de dejarlo pasar callado.
    crudo = json.dumps(limpio(f), ensure_ascii=False)
    sospechas = []
    if re.search(r'"(documento|telefono|celular|correo|email)"\s*:', crudo):
        sospechas.append("hay una clave que se llama documento/telefono/correo")
    if re.search(r"\b3\d{9}\b", crudo):
        sospechas.append("hay algo con forma de celular colombiano")
    if re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", crudo):
        sospechas.append("hay algo con forma de correo")
    print()
    if sospechas:
        print("  ⚠ REVISE ANTES DE MANDARLO:")
        for s in sospechas:
            print("      · " + s)
    else:
        print("  ✓ revisado: no hay cédulas, celulares ni correos en el archivo.")
    print(f"  Escritos:\n      {pt}   ← léalo primero\n      {pj}   ← este es el que me manda")
    return 0


if __name__ == "__main__":
    sys.exit(main())
