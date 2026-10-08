#!/usr/bin/env python3
"""Quién realiza qué: verlo, llenarlo de una vez y comprobar que quedó bien.

En la agenda esto se edita en Especialistas → «Servicios que realiza», que es
donde debe editarse el día a día. Este script es para la primera carga, que a
mano son 7 especialistas × 27 servicios, y para revisar después que no quedó
ningún hueco.

    python3 servicios-por-especialista.py --ver
    python3 servicios-por-especialista.py --plantilla cuadre.csv
    (se llena el archivo, poniendo x donde sí)
    python3 servicios-por-especialista.py --aplicar cuadre.csv          # ensayo
    python3 servicios-por-especialista.py --aplicar cuadre.csv --de-verdad

La regla de la agenda, que este script respeta: una especialista **sin
ningún** servicio marcado hace TODOS. Por eso una tabla vacía no se ve como
un error —se ve como «todas hacen todo»— y es justo lo que descuadra la
tablet de clientas.
"""
import argparse
import csv
import os
import sys

DB = os.getenv("DATABASE_URL", "")


def conectar():
    if not DB:
        sys.exit("Falta DATABASE_URL, p. ej.:\n"
                 "  DATABASE_URL=postgresql://usuario@localhost/cjmedical "
                 "python3 servicios-por-especialista.py --ver")
    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        sys.exit("Falta psycopg2:  pip3 install psycopg2-binary")
    cn = psycopg2.connect(DB)
    cn.autocommit = False
    return cn


def leer(cn):
    import psycopg2.extras
    with cn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
        cur.execute("""select id, trim(nombres||' '||apellidos) as nombre
                         from especialistas where activo order by 2""")
        esps = [dict(r) for r in cur.fetchall()]
        cur.execute("select id, nombre from servicios where activo order by nombre")
        servs = [dict(r) for r in cur.fetchall()]
        cur.execute("select especialista_id, servicio_id from especialista_servicios")
        pares = {(r[0], r[1]) for r in cur.fetchall()}
    return esps, servs, pares


def ver(cn):
    esps, servs, pares = leer(cn)
    print(f"\n{len(esps)} especialistas activas · {len(servs)} servicios activos · "
          f"{len(pares)} asignaciones\n")
    sin_nada, huerfanos = [], []
    for e in esps:
        mios = sorted(s["nombre"] for s in servs if (e["id"], s["id"]) in pares)
        if not mios:
            sin_nada.append(e["nombre"])
            print(f"  {e['nombre']}\n      (sin marcar nada → la agenda la ofrece "
                  f"para LOS {len(servs)} SERVICIOS)")
        else:
            print(f"  {e['nombre']}  —  {len(mios)} servicios")
            for m in mios:
                print(f"      · {m}")
    for s in servs:
        if not any((e["id"], s["id"]) in pares for e in esps):
            huerfanos.append(s["nombre"])

    print("\n" + "─" * 64)
    if sin_nada:
        print(f"⚠ {len(sin_nada)} especialista(s) sin nada marcado. Mientras estén\n"
              "  así, la tablet las ofrece para cualquier servicio:")
        for n in sin_nada:
            print("      · " + n)
    if huerfanos:
        print(f"\n⚠ {len(huerfanos)} servicio(s) que, si se marcan todas las demás,\n"
              "  se quedarían sin nadie que los realice:")
        for n in huerfanos:
            print("      · " + n)
    if not sin_nada and not huerfanos:
        print("✓ Todas las especialistas tienen servicios marcados y todos los\n"
              "  servicios tienen quién los realice.")
    return 1 if (sin_nada or huerfanos) else 0


def plantilla(cn, ruta):
    esps, servs, pares = leer(cn)
    if os.path.exists(ruta):
        sys.exit(f"«{ruta}» ya existe. Borre o cambie el nombre para no pisarlo.")
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["servicio"] + [e["nombre"] for e in esps])
        for s in servs:
            w.writerow([s["nombre"]] +
                       ["x" if (e["id"], s["id"]) in pares else "" for e in esps])
    print(f"Escrito «{ruta}»: {len(servs)} filas × {len(esps)} especialistas.\n"
          "Ábralo en Excel, ponga una x donde la especialista SÍ realiza ese\n"
          "servicio, guárdelo como CSV separado por punto y coma, y luego:\n"
          f"  python3 {os.path.basename(__file__)} --aplicar {ruta}")
    return 0


def aplicar(cn, ruta, de_verdad):
    esps, servs, pares = leer(cn)
    por_esp = {e["nombre"].strip().lower(): e["id"] for e in esps}
    por_serv = {s["nombre"].strip().lower(): s["id"] for s in servs}

    with open(ruta, newline="", encoding="utf-8-sig") as f:
        filas = list(csv.reader(f, delimiter=";"))
    if not filas:
        sys.exit("El archivo está vacío.")
    cab = [c.strip() for c in filas[0][1:]]
    faltan = [c for c in cab if c.strip().lower() not in por_esp]
    if faltan:
        sys.exit("Estas columnas no coinciden con ninguna especialista activa:\n  "
                 + "\n  ".join(faltan))

    quiere, desconocidos = set(), []
    for fila in filas[1:]:
        if not fila or not fila[0].strip():
            continue
        sid = por_serv.get(fila[0].strip().lower())
        if not sid:
            desconocidos.append(fila[0].strip())
            continue
        for i, val in enumerate(fila[1:]):
            if i < len(cab) and val.strip().lower() in ("x", "s", "si", "sí", "1"):
                quiere.add((por_esp[cab[i].strip().lower()], sid))
    if desconocidos:
        print("⚠ Estas filas no coinciden con ningún servicio activo y se ignoran:")
        for d in desconocidos:
            print("      · " + d)

    nuevas, sobran = quiere - pares, pares - quiere
    nombre_e = {e["id"]: e["nombre"] for e in esps}
    nombre_s = {s["id"]: s["nombre"] for s in servs}
    print(f"\n{len(nuevas)} por agregar, {len(sobran)} por quitar.")
    for e, s in sorted(nuevas, key=lambda p: (nombre_e.get(p[0], ""), nombre_s.get(p[1], ""))):
        print(f"  +  {nombre_e.get(e)} → {nombre_s.get(s)}")
    for e, s in sorted(sobran, key=lambda p: (nombre_e.get(p[0], ""), nombre_s.get(p[1], ""))):
        print(f"  −  {nombre_e.get(e)} → {nombre_s.get(s)}")

    quedan_vacias = [nombre_e[e["id"]] for e in esps
                     if not any(p[0] == e["id"] for p in quiere)]
    if quedan_vacias:
        print("\n⚠ Estas quedarían sin nada marcado y la agenda las seguiría\n"
              "  ofreciendo para todos los servicios:")
        for n in quedan_vacias:
            print("      · " + n)

    if not de_verdad:
        print("\nEsto fue un ENSAYO: no se tocó la base.\n"
              "Para aplicarlo, repita el comando con  --de-verdad")
        return 0
    if not (nuevas or sobran):
        print("\nNo hay nada que cambiar.")
        return 0
    with cn.cursor() as cur:
        for e, s in sobran:
            cur.execute("delete from especialista_servicios "
                        "where especialista_id=%s and servicio_id=%s", (e, s))
        for e, s in nuevas:
            cur.execute("insert into especialista_servicios(especialista_id, servicio_id) "
                        "values (%s,%s) on conflict do nothing", (e, s))
    cn.commit()
    print(f"\nListo: {len(nuevas)} agregadas, {len(sobran)} quitadas.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Quién realiza qué, en CJ Medical")
    ap.add_argument("--ver", action="store_true", help="muestra el cuadre y los huecos")
    ap.add_argument("--plantilla", metavar="ARCHIVO.csv")
    ap.add_argument("--aplicar", metavar="ARCHIVO.csv")
    ap.add_argument("--de-verdad", action="store_true",
                    help="sin esto, --aplicar solo enseña lo que haría")
    a = ap.parse_args()
    cn = conectar()
    try:
        if a.plantilla:
            return plantilla(cn, a.plantilla)
        if a.aplicar:
            return aplicar(cn, a.aplicar, a.de_verdad)
        return ver(cn)
    finally:
        cn.close()


if __name__ == "__main__":
    sys.exit(main())
