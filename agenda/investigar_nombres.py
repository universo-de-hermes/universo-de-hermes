#!/usr/bin/env python3
"""[SOLO LECTURA] Donde estan escritos los nombres de las sedes a mano."""
import io, os, re

PATRON = re.compile(
    r"CJ ?MEDICAL ?[-–—]? ?(EL TESORO|BOGOT|TESORO)"
    r"|CJ Medical ?[-–—]? ?(El Tesoro|Bogot)"
    r"|CJ Medical Tesoro|CJ Medical Bogot", re.I)

RAICES = ["/root/universo/agenda", "/root/universo/recepcionista", "/var/www/html"]
SALTAR = ("node_modules", "/venv/", "respaldos", "respaldo", ".bak", "_paquete/",
          "_paquete2/", "site-packages", "instalar_", "fix_", ".orig")

vistos = {}
for raiz in RAICES:
    for base, dirs, files in os.walk(raiz):
        if any(s in base for s in SALTAR):
            continue
        for f in files:
            if not f.endswith((".py", ".html", ".js", ".sql", ".json")):
                continue
            p = os.path.join(base, f)
            if any(s in p for s in SALTAR):
                continue
            try:
                t = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
            except Exception:
                continue
            for i, l in enumerate(t, 1):
                if PATRON.search(l) and "titulizar" not in l and "debe quedar" not in l:
                    print("%-58s L%-5d %s" % (p.replace("/root/universo/", "").replace("/var/www/", ""), i, l.strip()[:120]))

print()
print("=== como se usa la columna bodega ===")
for raiz in ["/root/universo/agenda", "/root/universo/recepcionista"]:
    for base, dirs, files in os.walk(raiz):
        if any(s in base for s in SALTAR):
            continue
        for f in files:
            if not f.endswith((".py", ".html")):
                continue
            p = os.path.join(base, f)
            try:
                t = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
            except Exception:
                continue
            for i, l in enumerate(t, 1):
                if "bodega" in l.lower() and "bodegas" not in l.lower():
                    print("%-58s L%-5d %s" % (p.replace("/root/universo/", ""), i, l.strip()[:120]))
