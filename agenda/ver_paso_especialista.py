#!/usr/bin/env python3
# ¿El panel salta el paso de especialista? SOLO LECTURA.
import io, re
h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S | re.I))

print("=== donde se decide pasar a «especialista» ===")
for m in re.finditer(r'especialista', js):
    a = max(0, m.start() - 220)
    frag = re.sub(r'\s+', ' ', js[a:m.end() + 200])
    if 'ir("especialista")' in frag or 'ir("resumen")' in frag or 'soloUno' in frag or 'length===1' in frag or 'length === 1' in frag:
        print("   ..." + frag + "...")
        print()

print("=== la funcion vEspecialista ===")
m = re.search(r'function vEspecialista\([^)]*\)\s*\{', js)
if m:
    print("   " + re.sub(r'\s+', ' ', js[m.start():m.start() + 1100])[:1100])
