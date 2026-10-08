#!/usr/bin/env python3
# Instala el paquete de Claude Pro Y vuelve a aplicar los arreglos de botones claros.
import io, re, os, shutil, hashlib, subprocess, sys

WEB = '/var/www/html/autoservicio.html'
PY = '/root/universo/agenda/autoservicio.py'

print("=" * 74)
print("  ANTES (produccion actual)")
print("=" * 74)
for f in (WEB, PY):
    b = open(f, 'rb').read()
    print(f"  {f}  {len(b)} bytes  md5 {hashlib.md5(b).hexdigest()[:12]}")

# ---- 1. respaldos y copia del paquete ----
shutil.copy(WEB, WEB + '.pre-claude.bak')
shutil.copy(PY, PY + '.pre-claude.bak')

INC_HTML = '/root/universo/agenda/_paquete/autoservicio.html'
INC_PY = '/root/universo/agenda/_paquete/autoservicio.py'
h = io.open(INC_HTML, encoding='utf-8').read()
p = io.open(INC_PY, encoding='utf-8').read()
print(f"\n  paquete de Claude:  html {len(h)} caracteres · py {len(p)} caracteres del original")

# ---- 2. RE-APLICAR los 3 arreglos de botones claros ----
print("\n" + "=" * 74)
print("  RE-APLICANDO BOTONES CLAROS SOBRE EL PAQUETE")
print("=" * 74)
fallos = []

# a) color robusto
v = "background:var(--acento);background:linear-gradient(180deg,"
if h.count(v) == 1:
    h = h.replace(v, "background-color:var(--acento);background-image:linear-gradient(180deg,", 1)
    print("  OK   (a) .btn.pri: color robusto")
elif h.count("background-color:var(--acento)") == 1:
    print("  --   (a) ya estaba")
else:
    print(f"  FALLO (a): {h.count(v)} coincidencias"); fallos.append('a')

# b) estado apagado CLARO
v2 = ".btn.pri[disabled]{opacity:1;background:var(--glass-3);color:var(--ink-2);box-shadow:inset 0 1px 0 var(--glass-hi),var(--shadow-sm)}"
n2 = ".btn.pri[disabled]{opacity:1;background:var(--ink-2);color:var(--acento-ink);box-shadow:inset 0 1px 0 rgba(255,255,255,.45),var(--shadow-sm);border-color:transparent}"
if h.count(v2) == 1:
    h = h.replace(v2, n2, 1)
    print("  OK   (b) boton APAGADO: claro y legible")
else:
    print(f"  FALLO (b): {h.count(v2)} coincidencias  <<<< revisar")
    fallos.append('b')

# c) boton del inicio (.toque) CLARO
m = re.search(r'(#bienvenida\s+\.toque\s*\{)([^{}]*)(\})', h, re.S)
if m and 'background:var(--glass)' in m.group(2):
    cuerpo = m.group(2).replace('background:var(--glass)', 'background:var(--acento)').replace('color:var(--ink)', 'color:var(--acento-ink)')
    h = h[:m.start()] + m.group(1) + cuerpo + m.group(3) + h[m.end():]
    print("  OK   (c) boton del inicio (.toque): claro")
elif m:
    print(f"  --   (c) .toque ya no usa vidrio (fondo: {re.search(r'background[a-z-]*:[^;]*', m.group(2)).group(0) if re.search(r'background[a-z-]*:[^;]*', m.group(2)) else '?'})")
else:
    print("  FALLO (c): no encontre la regla .toque"); fallos.append('c')

# ---- 3. escribir ----
io.open(WEB, 'w', encoding='utf-8').write(h)
io.open(PY, 'w', encoding='utf-8').write(p)
print("\n  instalado: html y .py")

print("\n" + "=" * 74)
print("  VERIFICACION DEL ARCHIVO FINAL")
print("=" * 74)
b = io.open(WEB, encoding='utf-8').read()
checks = [
    ("tema oscuro fijo",        'data-theme="dark"'),
    ("frase de la bienvenida fuera", None),
    ("boton apagado claro",     "btn.pri[disabled]{opacity:1;background:var(--ink-2)"),
    ("color robusto",           "background-color:var(--acento)"),
    ("gesto en los DOS logos",  "querySelectorAll"),
    ("blob-c calido",           "--blob-c:rgba(152,118,104"),
    ("sendBeacon",              "sendBeacon"),
]
for etq, pat in checks:
    if pat is None:
        sigue = 'Agende su cita o avísenos' in b
        print(f"  {'OK' if not sigue else 'FALLO':<6} {etq}: {'todavia esta' if sigue else 'no esta'}")
    else:
        print(f"  {'OK' if pat in b else 'FALLO':<6} {etq}")
print(f"  llaves balanceadas: {b.count('{') == b.count('}')} ({b.count('{')}/{b.count('}')})")
print(f"  bytes finales: {len(b.encode('utf-8'))}  md5 {hashlib.md5(b.encode()).hexdigest()[:12]}")

print("\n" + "=" * 74)
print("  EL .py DE CLAUDE")
print("=" * 74)
for pat, etq in (("AUTOSERVICIO_PASO", "PASO del panel (debe decir 30)"), ("DOC_MIN", "DOC_MIN"), ("DOC_MAX", "DOC_MAX"), ("direccion_de", "direccion_de")):
    encontrado = re.findall(pat + r'[^\n]{0,60}', p)
    print(f"  {etq}: {encontrado[:2] if encontrado else 'NO'}")
print(f"  llaves balanceadas: {p.count('{') == p.count('}')}")
print(f"  compila: ", end="")
try:
    compile(p, PY, 'exec'); print("SI")
except SyntaxError as e:
    print(f"NO -> {e}")

if fallos:
    print(f"\n*** FALTARON LOS ARREGLOS: {fallos}")
    print("*** el .py NO se instalo todavia")
    sys.exit(1)
print("\n>>> listo para instalar el .py")
