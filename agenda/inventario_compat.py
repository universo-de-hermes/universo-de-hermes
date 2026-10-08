#!/usr/bin/env python3
# Inventario EXACTO para la capa de compatibilidad. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
# solo la parte CSS (dentro de <style> ... </style>)
css = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S | re.I))
print(f"CSS: {len(css)} caracteres\n")

# reglas planas (ignorando @media/@supports por ahora, pero marcando si estan dentro)
reglas = []
for m in re.finditer(r'([^{}]{1,220}?)\{([^{}]*)\}', css):
    sel = m.group(1).strip()
    if sel.startswith('@'):
        continue
    reglas.append((m.start(), sel, m.group(2)))

print("=" * 74)
print("  A. gap: EN FLEX  (iOS 12 lo ignora -> hay que emularlo con margenes)")
print("=" * 74)
for pos, sel, cuerpo in reglas:
    if 'display:flex' in cuerpo.replace(' ', ''):
        g = re.search(r'gap\s*:\s*([^;}]+)', cuerpo)
        if g:
            print(f"   [{sel[-72:]}]")
            print(f"        gap:{g.group(1).strip()}")

print()
print("=" * 74)
print("  B. gap: en reglas SIN display (heredan flex del padre)")
print("=" * 74)
for pos, sel, cuerpo in reglas:
    if 'flex' not in cuerpo and 'grid' not in cuerpo:
        g = re.search(r'gap\s*:\s*([^;}]+)', cuerpo)
        if g:
            print(f"   [{sel[-72:]}]  gap:{g.group(1).strip()}")

print()
print("=" * 74)
print("  C. clamp()  (iOS 12 se pierde la declaracion entera)")
print("=" * 74)
for pos, sel, cuerpo in reglas:
    for d in re.findall(r'([a-z-]+)\s*:\s*([^;]*clamp\([^;]*)', cuerpo):
        print(f"   [{sel[-66:]}]")
        print(f"        {d[0]}: {d[1].strip()[:110]}")

print()
print("=" * 74)
print("  D. aspect-ratio / dvh / svh / lvh")
print("=" * 74)
for pos, sel, cuerpo in reglas:
    for d in re.findall(r'([a-z-]+)\s*:\s*([^;]*(?:aspect-ratio|\d(?:dvh|svh|lvh))[^;]*)', cuerpo):
        print(f"   [{sel[-66:]}]  {d[0]}: {d[1].strip()[:80]}")

print()
print("=" * 74)
print("  E. color-mix() QUE AUN NO TENGA RESPALDO")
print("=" * 74)
for pos, sel, cuerpo in reglas:
    if 'color-mix(' not in cuerpo:
        continue
    # busca si hay una declaracion previa del mismo tipo sin color-mix
    faltan = []
    for m2 in re.finditer(r'(?<![-a-z])(background|box-shadow|border|border-color|color)\s*:\s*([^;]*)', cuerpo):
        if 'color-mix(' in m2.group(2):
            antes = cuerpo[:m2.start()]
            if not re.search(r'(?<![-a-z])' + m2.group(1) + r'\s*:', antes):
                faltan.append(m2.group(1))
    print(f"   [{sel[-66:]}]  sin respaldo: {faltan if faltan else 'ninguna (ya tiene)'}")
