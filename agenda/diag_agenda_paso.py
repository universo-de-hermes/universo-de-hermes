#!/usr/bin/env python3
# Donde la agenda pide horas y con que paso. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/agenda.html', encoding='utf-8', errors='replace').read()
print(f"agenda.html {len(h)} bytes\n")

print("=== TODAS las apariciones de 'paso' ===")
for m in re.finditer(r'paso', h):
    a, b = max(0, m.start() - 110), m.end() + 110
    print("   ..." + h[a:b].replace("\n", " ") + "...")
    print()

print("=== DONDE PIDE HUECOS (url / funcion) ===")
for m in re.finditer(r'huecos[^"\')\s]{0,40}', h):
    a, b = max(0, m.start() - 140), m.end() + 140
    print("   ..." + h[a:b].replace("\n", " ") + "...")
    print()

print("=== NUMEROS '15' CERCA DE HORA/PASO/DURACION ===")
for m in re.finditer(r'.{80}\|15|15\b.{80}', h):
    frag = m.group(0).replace("\n", " ")
    if any(k in frag.lower() for k in ('paso', 'hora', 'duracion', 'duración', 'min')):
        print("   ..." + frag + "...")
        print()
