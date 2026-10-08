#!/usr/bin/env python3
# Inventario del panel: pantallas y textos que ve la clienta. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S | re.I))
print(f"JS: {len(js)} caracteres\n")

print("=" * 74)
print("  A. LA FRASE QUE NO QUIERE (y como esta puesta)")
print("=" * 74)
for m in re.finditer(r'Agende su cita|av[ií]senos|sin hacer fila|que ya lleg', h):
    a, b = max(0, m.start() - 300), m.end() + 200
    print("  ..." + re.sub(r'\s+', ' ', h[a:b]) + "...")
    print()

print("=" * 74)
print("  B. PANTALLAS (estados) DEL PANEL")
print("=" * 74)
vistos = []
for m in re.finditer(r'\bir\("([a-z_0-9]+)"', js):
    if m.group(1) not in vistos:
        vistos.append(m.group(1))
print("   ", vistos)
print()
print("   funciones pantalla* / v*():")
for m in re.finditer(r'function\s+([a-zA-Z_0-9]*[Pp]antalla[a-zA-Z_0-9]*|v[A-Z][a-zA-Z_0-9]*)\s*\(', js):
    print("     -", m.group(1))

print()
print("=" * 74)
print("  C. TEXTOS QUE VE LA CLIENTA (frases del JS)")
print("=" * 74)
frases = []
for m in re.finditer(r'"([^"\\\n]{6,140})"', js):
    t = m.group(1)
    if re.search(r'[áéíóúñ¿¡]|\b(de|el|la|su|con|para|que|una|los|las|por|sin)\b', t, re.I) \
       and not re.search(r'[{};]|px|rgba|px\)|^\d|://|api/|font-|grid|flex', t, re.I):
        frases.append(t)
seen = set()
for f in frases:
    if f in seen:
        continue
    seen.add(f)
    print("   ·", f)
print(f"\n   total de frases distintas: {len(seen)}")
