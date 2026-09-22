#!/usr/bin/env python3
"""Crea el primer administrador de la agenda sin entrada interactiva.
Lee la contraseña de /root/.pwd_tmp y borra el archivo al terminar."""
import os
import sys
import secrets
import string

sys.path.insert(0, "/root/universo/agenda")
from agenda_api_v3 import cursor, hash_clave  # noqa

PWD_FILE = "/root/.pwd_tmp"

NOMBRE = "Juan Jose Otero"
CORREO = "jhotas96@gmail.com"
ROL = "admin"
CANAL = "Administrador"

# Generar contraseña si no existe el archivo
if not os.path.exists(PWD_FILE):
    alfabeto = string.ascii_letters + string.digits
    clave = "".join(secrets.choice(alfabeto) for _ in range(14))
    with open(PWD_FILE, "w") as f:
        f.write(clave)
    os.chmod(PWD_FILE, 0o600)

with open(PWD_FILE) as f:
    clave = f.read().strip()

h = hash_clave(clave)
uid = "u-juan-jose-otero"

with cursor() as cur:
    cur.execute("select id from usuarios where lower(correo)=%s", (CORREO,))
    existe = cur.fetchone()
    if existe:
        cur.execute("update usuarios set clave_hash=%s, activo=true, rol=%s where id=%s",
                    (h, ROL, existe["id"]))
        cur.execute("delete from sesiones where usuario_id=%s", (existe["id"],))
        print("Actualizado:", NOMBRE, CORREO)
    else:
        cur.execute("""insert into usuarios(id,nombre,correo,rol,canal,clave_hash,activo)
                       values(%s,%s,%s,%s,%s,%s,true)""",
                    (uid, NOMBRE, CORREO, ROL, CANAL, h))
        print("Creado:", NOMBRE, CORREO, "rol=" + ROL)

# Borrar el archivo de la contraseña
os.remove(PWD_FILE)
print("Archivo de contraseña borrado.")

print()
print("CONTRASEÑA:", clave)
