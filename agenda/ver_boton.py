#!/usr/bin/env python3
# Como esta pintado el boton Continuar. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8', errors='replace').read()

print("=== apariciones de 'Continuar' ===")
for m in re.finditer(r'Continuar', h):
    a, b = max(0, m.start() - 260), m.end() + 160
    print("   ..." + h[a:b].replace("\n", " ") + "...")
    print()

print("=== REGLAS CSS de botones principales ===")
for m in re.finditer(r'([^{}]{0,140})\{([^{}]*(?:--acento|principal|primary|\.sig|\.btn)[^{}]*)\}', h):
    sel, cuerpo = m.group(1).strip()[-100:], m.group(2).strip()
    if 'background' in cuerpo or 'color' in cuerpo or 'acento' in cuerpo:
        print(f"   [{sel}]")
        print(f"      {cuerpo[:220]}")
        print()
