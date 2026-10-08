#!/usr/bin/env python3
# Ver como arranca el tema en las 2 paginas. SOLO LECTURA.
import io, re

for f in ('/var/www/html/autoservicio.html', '/var/www/html/agenda.html'):
    h = io.open(f, encoding='utf-8', errors='replace').read()
    print("=" * 72)
    print(" ", f, f"({len(h)} bytes)")
    print("=" * 72)
    m = re.search(r'<html[^>]*>', h)
    print("  <html> tag:", (m.group(0)[:160] if m else "NO ENCONTRADO"))

    print("\n  --- donde aparece data-theme / toggleTema ---")
    vistos = []
    for mm in re.finditer(r'data-theme|toggleTema', h):
        a, b = max(0, mm.start() - 70), mm.end() + 90
        frag = h[a:b].replace("\n", " ")
        if any(frag[:50] == v[:50] for v in vistos):
            continue
        vistos.append(frag)
        print(f"    @{mm.start():>7}  ...{frag}...")
        if len(vistos) >= 14:
            print("    (mas...)")
            break

    print("\n  --- JS que corre al cargar (init) ---")
    for mm in re.finditer(r'DOMContentLoaded|window\.onload', h):
        a, b = max(0, mm.start() - 40), mm.end() + 260
        print(f"    @{mm.start():>7}  {h[a:b]}".replace("\n", " ")[:300])
        print()
    print()
