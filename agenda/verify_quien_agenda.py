#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprueba que la API ya entrega quien agendo la cita."""
import json
import pathlib
import urllib.error
import urllib.request

TOK = pathlib.Path("/root/universo/agenda/.api_token").read_text().strip()
BASE = "http://127.0.0.1:8001/api/v2"


def call(path):
    req = urllib.request.Request(
        BASE + path, headers={"accept": "application/json", "x-api-token": TOK})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:300]
    except Exception as e:
        return "ERR", str(e)[:300]


st, citas = call("/citas")
print("GET /citas ->", st)
if isinstance(citas, list):
    for c in citas[:5]:
        print("  cita", c.get("id"), "| fecha", c.get("fecha"),
              "| canal:", repr(c.get("canal")),
              "| asignada_por:", repr(c.get("asignada_por")),
              "| creado_por:", repr(c.get("creado_por")))
else:
    print("  ", citas)

st, us = call("/usuarios")
print()
print("GET /usuarios ->", st)
if isinstance(us, list):
    for u in us:
        print("  ", u.get("id"), "|", u.get("nombre"), "| canal:",
              repr(u.get("canal")), "| rol:", u.get("rol"))
else:
    print("  ", us)
