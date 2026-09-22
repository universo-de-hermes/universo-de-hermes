#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica el arreglo del 500 al guardar clientes en la agenda."""
import json
import pathlib
import urllib.error
import urllib.request

TOK = pathlib.Path("/root/universo/agenda/.api_token").read_text().strip()
BASE = "http://127.0.0.1:8001/api/v2"
CID = "cl_test_hermes"


def call(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        BASE + path, data=data, method=method,
        headers={"Content-Type": "application/json", "x-api-token": TOK})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, r.read().decode()[:500]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:500]
    except Exception as e:
        return "ERR", str(e)[:300]


print("=== 1) CREAR cliente con sede_id='' (el caso que fallaba con 500) ===")
print(call("PUT", "/clientes/" + CID, {
    "tipo_doc": "Cedula de Ciudadania", "documento": "99887766",
    "primer_nombre": "Prueba", "segundo_nombre": "", "primer_apellido": "Hermes",
    "segundo_apellido": "", "telefono": "3000000000", "correo": "",
    "ciudad": "Medellin", "genero": "", "sede_id": "", "notas": "",
    "dia_nac": None, "mes_nac": None}))

print()
print("=== 2) EDITAR ese mismo cliente (UPDATE) con sede_id='' ===")
print(call("PUT", "/clientes/" + CID, {
    "primer_nombre": "Prueba Editada", "sede_id": "", "ciudad": "Bogota"}))

print()
print("=== 3) CREAR otro cliente CON sede valida (no debe romper) ===")
print(call("PUT", "/clientes/cl_test_hermes2", {
    "documento": "99887755", "primer_nombre": "Con", "primer_apellido": "Sede",
    "telefono": "3000000001", "sede_id": "sede-cj-medical-bogota"}))

print()
print("=== 4) LEER el primero (ver sede_id y ciudad) ===")
print(call("GET", "/clientes/" + CID))
