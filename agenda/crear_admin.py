#!/usr/bin/env python3
"""
Crea o actualiza una persona con acceso a la agenda.

    python3 crear_admin.py                      # pregunta todo
    python3 crear_admin.py --listar             # muestra quién tiene acceso
    python3 crear_admin.py --correo ana@cj.co --rol operador

La contraseña se pide por teclado y no se ve mientras se escribe; no se pasa
por parámetro a propósito, para que no quede en el historial del shell ni en
los logs del servidor.
"""
import argparse
import getpass
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agenda_api_v3 import cursor, hash_clave  # noqa: E402


def slug(texto):
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t or "usuario"


def listar():
    with cursor() as cur:
        cur.execute("""select id, nombre, correo, rol, canal, activo, ultimo_acceso
                         from usuarios order by nombre""")
        filas = cur.fetchall()
    if not filas:
        print("Todavía no hay nadie con acceso.")
        return
    print(f"{'NOMBRE':28} {'CORREO':30} {'ROL':10} {'ACTIVO':7} ÚLTIMO ACCESO")
    for u in filas:
        print("%-28s %-30s %-10s %-7s %s" % (
            (u["nombre"] or "")[:28], (u["correo"] or "")[:30], u["rol"],
            "sí" if u["activo"] else "no",
            u["ultimo_acceso"].strftime("%Y-%m-%d %H:%M") if u["ultimo_acceso"] else "—"))


def main():
    ap = argparse.ArgumentParser(description="Acceso a la agenda CJ Medical")
    ap.add_argument("--listar", action="store_true", help="muestra quién tiene acceso")
    ap.add_argument("--nombre")
    ap.add_argument("--correo")
    ap.add_argument("--rol", choices=["admin", "operador"], default="admin")
    ap.add_argument("--canal", default="Recepcionista")
    args = ap.parse_args()

    if args.listar:
        return listar()

    nombre = args.nombre or input("Nombre completo: ").strip()
    correo = (args.correo or input("Correo (con esto entra): ")).strip().lower()
    if not nombre or not correo:
        sys.exit("Hace falta nombre y correo.")
    if "@" not in correo:
        sys.exit("Ese correo no parece un correo.")

    with cursor() as cur:
        cur.execute("select * from usuarios where lower(correo)=%s", (correo,))
        existe = cur.fetchone()

    if existe:
        print(f"Ya existe: {existe['nombre']} ({existe['rol']}).")
        if input("¿Le cambio la contraseña? [s/N] ").strip().lower() not in ("s", "si", "sí"):
            return

    clave = getpass.getpass("Contraseña (mínimo 8 caracteres): ")
    if len(clave) < 8:
        sys.exit("La contraseña debe tener al menos 8 caracteres.")
    if clave != getpass.getpass("Repítela: "):
        sys.exit("Las dos contraseñas no coinciden.")

    h = hash_clave(clave)
    uid = existe["id"] if existe else "u-" + slug(nombre)

    with cursor() as cur:
        if existe:
            cur.execute("""update usuarios set clave_hash=%s, activo=true
                            where id=%s""", (h, uid))
            cur.execute("delete from sesiones where usuario_id=%s", (uid,))
            print(f"Contraseña actualizada para {nombre}. Sus sesiones se cerraron.")
        else:
            cur.execute("""insert into usuarios(id,nombre,correo,rol,canal,
                                                clave_hash,activo)
                           values(%s,%s,%s,%s,%s,%s,true)""",
                        (uid, nombre, correo, args.rol, args.canal, h))
            print(f"Listo: {nombre} entra con {correo} como {args.rol}.")

    print("\nDesde este momento la agenda pide usuario y contraseña.")


if __name__ == "__main__":
    main()
