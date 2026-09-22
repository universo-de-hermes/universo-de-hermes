#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arregla el 500 al crear/editar clientes en la agenda.

Causa: el formulario manda sede_id="" ("Sin preferencia") y la base tiene
FK clientes_sede_id_fkey -> sedes(id). '' no existe en sedes => violacion de
clave foranea => HTTPException(500) via traducir().

Arreglo:
  1) _actualizar(): "" del formulario se guarda como NULL (un campo vacio no
     es un valor). Seguro: las unicas columnas NOT NULL sin default son id,
     documento, sedes.nombre y servicios.nombre, y todas las cubre `exige`.
  2) ClienteEditar: agrega los campos que el formulario si ofrece pero el
     modelo no aceptaba (Pydantic los descartaba en silencio): tipo_doc,
     ciudad, genero, tipo_cliente, dia_nac, mes_nac.
"""
import io
import sys

RUTA = "/root/universo/agenda/agenda_api.py"

s = io.open(RUTA, encoding="utf-8").read()

# ── 1) vacio -> NULL en _actualizar ──────────────────────────────────────────
viejo_campos = "    campos = {k: v for k, v in req.dict().items() if v is not None}"
nuevo_campos = '''    # Un "" que llega del formulario no es un valor: se guarda como NULL.
    # Antes viajaba como '' y la clave foranea clientes_sede_id_fkey reventaba
    # con un 500 al crear un cliente sin "sede preferida" (el combo manda "").
    campos = {k: (None if v == "" else v)
              for k, v in req.dict().items() if v is not None}'''

if s.count(viejo_campos) != 1:
    print("ABORTO: no encontre la linea de campos (%d coincidencias)"
          % s.count(viejo_campos))
    sys.exit(1)
s = s.replace(viejo_campos, nuevo_campos)

# ── 2) campos que faltaban en ClienteEditar ──────────────────────────────────
viejo_cli = """    correo: Optional[str] = None; sede_id: Optional[str] = None
    notas: Optional[str] = None"""
nuevo_cli = """    correo: Optional[str] = None; sede_id: Optional[str] = None
    notas: Optional[str] = None
    tipo_doc: Optional[str] = None; ciudad: Optional[str] = None
    genero: Optional[str] = None; tipo_cliente: Optional[str] = None
    dia_nac: Optional[int] = None; mes_nac: Optional[int] = None"""

if s.count(viejo_cli) != 1:
    print("ABORTO: no encontre el bloque de ClienteEditar (%d coincidencias)"
          % s.count(viejo_cli))
    sys.exit(1)
s = s.replace(viejo_cli, nuevo_cli)

io.open(RUTA, "w", encoding="utf-8").write(s)
print("PATCH APLICADO OK")
