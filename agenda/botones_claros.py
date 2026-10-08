#!/usr/bin/env python3
# Los botones de accion SIEMPRE claros (encendidos y apagados).
import io, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

CAMBIOS = [
    # 1) mas robusto: background-color + background-image (asi el color NUNCA se pierde)
    ("background:var(--acento);background:linear-gradient(180deg,",
     "background-color:var(--acento);background-image:linear-gradient(180deg,",
     "boton encendido: el color ya no se pierde"),

    # 2) el estado APAGADO ahora es CLARO, no vidrio oscuro
    (".btn.pri[disabled]{opacity:1;background:var(--glass-3);color:var(--ink-2);"
     "box-shadow:inset 0 1px 0 var(--glass-hi),var(--shadow-sm)}",
     ".btn.pri[disabled]{opacity:1;background:var(--ink-2);color:var(--acento-ink);"
     "box-shadow:inset 0 1px 0 rgba(255,255,255,.45),var(--shadow-sm);border-color:transparent}",
     "boton APAGADO: claro y legible (antes vidrio oscuro)"),

    # 3) el texto de los botones que se apagan no debe quedar oscuro sobre oscuro
    ("btn.pri[disabled]", "btn.pri[disabled]", "control: la regla existe"),
]

print(f"archivo: {len(h)} caracteres\n")
fallos = []
nuevo = h
for viejo, rep, que in CAMBIOS:
    n = nuevo.count(viejo)
    ok = n == 1
    print(f"  {'OK' if ok else 'ABORTO':<7} {n} x  {que}")
    if not ok:
        fallos.append(que)
        continue
    nuevo = nuevo.replace(viejo, rep, 1)

if fallos:
    print("\n*** no calzaron: " + "; ".join(fallos) + " — NO se toco nada.")
    sys.exit(1)

shutil.copy(RUTA, RUTA + '.pre-botones-claros.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)
print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} caracteres (+{len(nuevo)-len(h)})")
print(f"llaves {nuevo.count('{')}/{nuevo.count('}')} balanceadas: {nuevo.count('{')==nuevo.count('}')}")
print(f"md5 {hashlib.md5(nuevo.encode()).hexdigest()[:12]}  bytes {len(nuevo.encode('utf-8'))}")
print(f"respaldo: {RUTA}.pre-botones-claros.bak")
print("\n=== como quedaron ===")
import re
for sel in ('.btn.pri{', '.btn.pri[disabled]{'):
    m = re.search(re.escape(sel) + r'[^}]*\}', nuevo)
    print("  " + (m.group(0) if m else sel + " NO ENCONTRADO")[:230])
