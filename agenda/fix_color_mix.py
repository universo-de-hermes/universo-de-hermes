#!/usr/bin/env python3
# Agrega un RESPALDO antes de cada color-mix() (que iOS 12.5.8 no entiende).
# El navegador moderno usa la 2a declaracion; el iPad se queda con la 1a.
import io, re, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()
antes_md5 = hashlib.md5(h.encode()).hexdigest()

PARCHES = [
    # (patron, reemplazo, que arregla)
    (r'(\.btn\.pri\s*\{[^}]*?)background:',
     r'\1background:var(--acento);background:',
     'BOTON PRINCIPAL (Continuar) — fondo solido si no hay color-mix'),

    (r'(\.aviso\s*\{[^}]*?)background:',
     r'\1background:var(--glass);background:',
     'aviso de error — fondo visible'),

    (r'(\.aviso\.ok\s*\{[^}]*?)background:',
     r'\1background:var(--glass);background:',
     'aviso bueno — fondo visible'),

    (r'(\.aviso\.nota\s*\{[^}]*?)background:',
     r'\1background:var(--glass);background:',
     'aviso nota — fondo visible'),

    (r'(#modal\s*\{[^}]*?)background:',
     r'\1background:rgba(0,0,0,.45);background:',
     'fondo del modal (oscurecer la pagina)'),

    (r'(\.opcion\[aria-pressed="true"\]\s*\{[^}]*?)box-shadow:',
     r'\1box-shadow:inset 0 0 0 1.5px var(--acento),var(--shadow-sm);box-shadow:',
     'opcion escogida — anillo visible'),

    (r'(\.cal \.dias button\.on\s*\{[^}]*?)box-shadow:',
     r'\1box-shadow:inset 0 0 0 1.5px var(--acento),var(--shadow-sm);box-shadow:',
     'dia escogido en el calendario — anillo visible'),
]

print(f"archivo {RUTA}  ({len(h)} bytes, md5 {antes_md5[:12]})\n")
nuevo = h
fallos = []
for pat, rep, desc in PARCHES:
    m = list(re.finditer(pat, nuevo))
    print(f"  {len(m)} coincidencia(s)  <- {desc}")
    if len(m) != 1:
        fallos.append(desc)
        continue
    nuevo = re.sub(pat, rep, nuevo, count=1)

if fallos:
    print("\n*** NO calzaron: " + "; ".join(fallos))
    print("*** NO se toco el archivo.")
    sys.exit(1)

shutil.copy(RUTA, RUTA + '.pre-colormix.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)
print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} bytes  (+{len(nuevo)-len(h)})")
print(f"md5 nuevo: {hashlib.md5(nuevo.encode()).hexdigest()[:12]}")
print(f"respaldo : {RUTA}.pre-colormix.bak")

print("\n=== comprobacion: cada respaldo quedo ANTES de su color-mix ===")
for pat, rep, desc in PARCHES:
    sel = pat.split(r'\s*\{')[0].replace('\\', '')
    for m in re.finditer(r'([^{}]*)\{([^{}]*)\}', nuevo):
        if 'color-mix(' in m.group(2) and sel.strip('.#') in m.group(1):
            cuerpo = m.group(2)
            cm = cuerpo.find('color-mix(')
            print(f"  [{m.group(1).strip()[:52]}]")
            print(f"      ...{cuerpo[max(0,cm-150):cm][-150:].strip()}")
            break
