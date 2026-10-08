#!/usr/bin/env python3
# Fija el tema OSCURO por defecto (para la tablet, que con iOS 9 no puede
# elegir). En su PC, si ya eligio un tema a mano, ese manda.
import shutil, hashlib, subprocess, io, re

VIEJO = b'<html lang="es">'
NUEVO = b'<html lang="es" data-theme="dark">'

ARCHIVOS = ('/var/www/html/autoservicio.html', '/var/www/html/agenda.html')

for f in ARCHIVOS:
    print("=" * 70)
    print(" ", f)
    b = open(f, 'rb').read()
    md5a = hashlib.md5(b).hexdigest()
    n = b.count(VIEJO)
    print(f"  tamano {len(b)}  md5 {md5a[:12]}")
    print(f"  '<html lang=\"es\">' aparece {n} vez/veces")
    if n != 1:
        print("  ABORTO: no calza exactamente 1. No se toco nada.")
        continue
    if NUEVO in b:
        print("  YA ESTABA. Nada que hacer.")
        continue
    shutil.copy(f, f + '.pre-tema-dark.bak')
    open(f, 'wb').write(b.replace(VIEJO, NUEVO, 1))
    b2 = open(f, 'rb').read()
    print(f"  APLICADO: {len(b2)} bytes (+{len(b2) - len(b)}), md5 {hashlib.md5(b2).hexdigest()[:12]}")
    print(f"  respaldo: {f}.pre-tema-dark.bak")
    print(f"  etiqueta ahora: {re.search(rb'<html[^>]*>', b2).group(0).decode()}")

print()
print("=" * 70)
print("  VERIFICACION: sintaxis del JS (la pagina no puede quedar en blanco)")
print("=" * 70)
for f in ARCHIVOS:
    txt = io.open(f, encoding='utf-8', errors='replace').read()
    bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", txt, re.S | re.I)
    io.open('/tmp/check_tema.js', 'w', encoding='utf-8').write("\n;\n".join(bloques))
    # node no esta en el VPS? probamos
    try:
        r = subprocess.run(["node", "--check", "/tmp/check_tema.js"],
                           capture_output=True, text=True, timeout=60)
        print(f"  {f.split('/')[-1]:<24} node --check rc={r.returncode} {r.stderr.strip()[:120]}")
    except FileNotFoundError:
        print(f"  {f.split('/')[-1]:<24} node NO disponible aqui")
