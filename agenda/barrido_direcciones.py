#!/usr/bin/env python3
"""[SOLO LECTURA] Barrido de direcciones, 'Plaza Norte' y la sede que manda Pepe."""
import io, os, re

PAT = re.compile(r"Plaza Norte|Parque Comercial|Centro Comercial|Oficity|Cra ?25A|Cra ?11A|Sede:|Direcci[oó]n|direccion=|SOTANO|S\u00f3tano", re.I)
SALTAR = ("node_modules", "/venv/", "respaldos", "respaldo", ".bak", "_paquete/",
          "site-packages", ".orig", "_eliminado", "__pycache__", "instalar_", "fix_",
          "investigar_", "ver_", "verificar_", "probar_", "preparar_", "cpdb")

for raiz in ("/root/universo/recepcionista", "/root/universo/agenda"):
    for base, dirs, files in os.walk(raiz):
        if any(s in base for s in SALTAR):
            continue
        for f in files:
            if not f.endswith((".py", ".html", ".js", ".json")):
                continue
            p = os.path.join(base, f)
            if any(s in p for s in SALTAR):
                continue
            try:
                t = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
            except Exception:
                continue
            salida = []
            for i, l in enumerate(t, 1):
                if PAT.search(l):
                    salida.append("   L%-5d %s" % (i, l.strip()[:165]))
            if salida:
                print("### %s  (%d lineas)" % (p.replace("/root/universo/", ""), len(salida)))
                print("\n".join(salida[:16]))
                print()
