#!/usr/bin/env python3
# 1) Arregla el gesto de cerrar la tablet (estaba pegado al logo invisible).
# 2) Cambia el azul lavanda (--blob-c) por un tono calido.
import io, re, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

CAMBIOS = [
    ('["#bienvenida img", "header img"]',
     '["#bienvenida img", "header img.solo-claro", "header img.solo-oscuro"]',
     "GESTO DE CERRAR: atado al logo VISIBLE (antes: solo-claro, oculto)", 1),

    ('--blob-c:rgba(110,146,158,.36)',
     '--blob-c:rgba(126,108,101,.30)',
     "AZUL LAVANDA: cambiado a tono calido", 2),
]

print(f"archivo: {len(h)} caracteres\n")
fallos = []
nuevo = h
for viejo, rep, que, esperado in CAMBIOS:
    n = nuevo.count(viejo)
    ok = n == esperado
    print(f"  {'OK' if ok else 'ABORTO':<7} {n} (esperaba {esperado})  {que}")
    if not ok:
        fallos.append(que); continue
    nuevo = nuevo.replace(viejo, rep)

if fallos:
    print("\n*** no calzaron: " + "; ".join(fallos) + " — NO se toco nada.")
    sys.exit(1)

shutil.copy(RUTA, RUTA + '.pre-gesto-blob.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)
print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} caracteres")
print(f"llaves {nuevo.count('{')}/{nuevo.count('}')} balanceadas: {nuevo.count('{')==nuevo.count('}')}")
print(f"md5 {hashlib.md5(nuevo.encode()).hexdigest()[:12]}  bytes {len(nuevo.encode('utf-8'))}")
print(f"respaldo: {RUTA}.pre-gesto-blob.bak")

print("\n=== comprobacion ===")
print("  gesto:", re.search(r'\["#bienvenida img".{0,80}', nuevo).group(0))
print("  blob-c ahora:", set(re.findall(r'--blob-c:[^;]*', nuevo)))
