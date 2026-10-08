#!/usr/bin/env python3
# Saca las dos paletas del panel y de la agenda. SOLO LECTURA.
import io, re

CLAVES = ('--bg', '--bg-2', '--glass', '--glass-2', '--glass-3', '--acento',
          '--acento-2', '--blob-a', '--blob-b', '--blob-c', '--texto', '--tinta',
          '--brand', '--sombra', 'color-scheme')


def bloques(css):
    """Devuelve (selectores, cuerpo) de cada regla que define variables de color."""
    out = []
    for m in re.finditer(r'([^{}@][^{}]*?)\{([^{}]*)\}', css):
        sel, cuerpo = m.group(1).strip(), m.group(2)
        if any(k + ':' in cuerpo for k in CLAVES):
            out.append((m.start(), sel[-90:], cuerpo))
    return out


for archivo in ('/var/www/html/autoservicio.html', '/var/www/html/agenda.html'):
    h = io.open(archivo, encoding='utf-8', errors='replace').read()
    print("=" * 74)
    print(" ", archivo)
    print("=" * 74)
    for pos, sel, cuerpo in bloques(h):
        antes = h[max(0, pos - 300):pos]
        media = re.findall(r'@media\s*\(prefers-color-scheme:\s*(\w+)\)', antes)
        etq = ("@media dark " if media else "") + sel
        vals = []
        for k in CLAVES:
            mm = re.search(re.escape(k) + r'\s*:\s*([^;}]+)', cuerpo)
            if mm:
                vals.append(f"{k}={mm.group(1).strip()[:34]}")
        if vals:
            print(f"\n  [{etq}]")
            for v in vals:
                print("      " + v)
    print()
