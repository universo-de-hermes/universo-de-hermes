#!/usr/bin/env python3
# Muestra el gesto de cerrar en el archivo INSTALADO. SOLO LECTURA.
import io, re
h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
print("querySelectorAll aparece:", h.count('querySelectorAll'), "veces\n")
for m in re.finditer(r'empieza|pointerdown', h):
    a = max(0, m.start() - 260)
    frag = re.sub(r'\s+', ' ', h[a:m.end() + 380])
    print("   ..." + frag + "...")
    print()
    break
print("=== donde se engancha el gesto ===")
for m in re.finditer(r'forEach\(function\(sel\)', h):
    a = max(0, m.start() - 330)
    print("   ..." + re.sub(r'\s+', ' ', h[a:m.end() + 420]) + "...")
    break
