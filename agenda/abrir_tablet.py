#!/usr/bin/env python3
"""Abre la tablet de una sede (lo que hace recepcion con su usuario)."""
import io, json, sys, urllib.request, urllib.error

SEDE = sys.argv[1] if len(sys.argv) > 1 else "el-tesoro"
CORREO = sys.argv[2] if len(sys.argv) > 2 else "jhotas96@gmail.com"
CLAVE = sys.argv[3] if len(sys.argv) > 3 else "TzEi4LntP6I8TC"
url = "http://127.0.0.1:8001/api/v2/autoservicio/abrir"
req = urllib.request.Request(url, data=json.dumps({"sede": SEDE, "correo": CORREO,
                                                   "clave": CLAVE}).encode(),
                             headers={"content-type": "application/json"}, method="POST")
try:
    j = json.loads(urllib.request.urlopen(req, timeout=15).read())
    print("tablet %s abierta: %s (hasta %s)" % (SEDE, j.get("ok"), j.get("hasta")))
except urllib.error.HTTPError as e:
    print("no se pudo abrir:", e.code, e.read().decode()[:200])
