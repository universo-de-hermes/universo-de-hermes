#!/usr/bin/env python3
# Pone el boton del inicio (.toque) en color CLARO con contraste.
import io, re, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

m = re.search(r'(#bienvenida\s+\.toque\s*\{)([^{}]*)(\})', h, re.S)
if not m:
    print("ABORTO: no encontre la regla #bienvenida .toque"); sys.exit(1)

cuerpo = m.group(2)
print("=== ANTES ===")
print(cuerpo.strip()[:320])

n1 = cuerpo.count('background:var(--glass)')
n2 = cuerpo.count('color:var(--ink)')
print(f"\nbackground:var(--glass) x{n1}   color:var(--ink) x{n2}")
if n1 != 1 or n2 != 1:
    print("ABORTO: no calzan exactamente 1"); sys.exit(1)

nuevo_cuerpo = (cuerpo
                .replace('background:var(--glass)', 'background:var(--acento)')
                .replace('color:var(--ink)', 'color:var(--acento-ink)'))

nuevo = h[:m.start()] + m.group(1) + nuevo_cuerpo + m.group(3) + h[m.end():]
shutil.copy(RUTA, RUTA + '.pre-toque-claro.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)

print("\n=== DESPUES ===")
print(nuevo_cuerpo.strip()[:320])
print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} caracteres")
print(f"llaves {nuevo.count('{')}/{nuevo.count('}')} balanceadas: {nuevo.count('{')==nuevo.count('}')}")
print(f"md5 {hashlib.md5(nuevo.encode()).hexdigest()[:12]}  bytes {len(nuevo.encode('utf-8'))}")
print(f"respaldo: {RUTA}.pre-toque-claro.bak")
