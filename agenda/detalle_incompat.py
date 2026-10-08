#!/usr/bin/env python3
# Detalle fino: cada declaracion que iOS 12.5.8 se salta. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8', errors='replace').read()

def reglas(txt):
    """Devuelve (selector, cuerpo) de cada regla CSS."""
    out = []
    for m in re.finditer(r'([^{}]{1,200}?)\{([^{}]*)\}', txt):
        out.append((m.group(1).strip()[-110:], m.group(2)))
    return out

regs = reglas(h)
print(f"total reglas CSS: {len(regs)}\n")

print("=" * 74)
print("  1. color-mix()  — lo que deja el boton SIN FONDO")
print("=" * 74)
for sel, cuerpo in regs:
    if 'color-mix(' in cuerpo:
        for decl in re.findall(r'([a-z-]+)\s*:\s*([^;]*color-mix[^;]*)', cuerpo):
            print(f"   [{sel}]")
            print(f"      {decl[0]}: {decl[1][:150]}")
        print()

print("=" * 74)
print("  2. gap:  — separado por FLEX (malo) vs GRID (esta bien)")
print("=" * 74)
flex, grid, otro = [], [], []
for sel, cuerpo in regs:
    if re.search(r'[;{]\s*gap\s*:', cuerpo):
        g = re.search(r'gap\s*:\s*([^;}]+)', cuerpo).group(1).strip()
        if 'display:flex' in cuerpo or 'flex' in cuerpo:
            flex.append((sel, g))
        elif 'display:grid' in cuerpo or 'grid' in cuerpo:
            grid.append((sel, g))
        else:
            otro.append((sel, g))
print(f"   con FLEX (iOS 12 los ignora): {len(flex)}")
for sel, g in flex[:14]:
    print(f"      [{sel[:70]}]  gap:{g[:40]}")
print(f"   con GRID (si sirven): {len(grid)}")
print(f"   sin display explicito (depende del padre): {len(otro)}")
for sel, g in otro[:8]:
    print(f"      [{sel[:70]}]  gap:{g[:40]}")

print()
print("=" * 74)
print("  3. backdrop-filter  (falta el -webkit-)")
print("=" * 74)
n = 0
for sel, cuerpo in regs:
    if 'backdrop-filter' in cuerpo and '-webkit-backdrop-filter' not in cuerpo:
        val = re.search(r'(?<!-webkit-)backdrop-filter\s*:\s*([^;}]+)', cuerpo)
        print(f"   [{sel[:80]}]  {val.group(1)[:60] if val else ''}")
        n += 1
print("   total:", n)

print()
print("=" * 74)
print("  4. inset: / aspect-ratio / dvh")
print("=" * 74)
for token in ('inset', 'aspect-ratio', r'\d(?:dvh|svh|lvh)'):
    for sel, cuerpo in regs:
        for m in re.finditer(r'([a-z-]+)\s*:\s*([^;]*(?:' + token + r')[^;]*)', cuerpo):
            print(f"   [{sel[:70]}]  {m.group(1)}: {m.group(2)[:90]}")
