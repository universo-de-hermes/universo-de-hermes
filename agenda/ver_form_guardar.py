#!/usr/bin/env python3
# guardarCliente y el mecanismo de avisos. SOLO LECTURA.
import io, re

html = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S | re.I))


def aplasta(t):
    return re.sub(r'\s+', ' ', t).strip()


for nom in ('guardarCliente', 'function avisar', 'function mal', 'function problema',
            'obligatorio', 'errores'):
    for m in re.finditer(r'(function\s+' + re.escape(nom.replace('function ', '')) + r'\s*\()', js):
        print(f"=== {nom} ===")
        print("   " + aplasta(js[m.start():m.start() + 900])[:900])
        print()
        break

print("=" * 74)
print("  ¿como muestra el panel un mensaje al cliente?")
print("=" * 74)
for m in re.finditer(r'class:"aviso', js):
    print("   " + aplasta(js[max(0, m.start() - 180):m.end() + 220])[:390])
    print()

print("=" * 74)
print("  ¿hay algo que marque un campo como invalido?")
print("=" * 74)
for m in re.finditer(r'\.mal\b|\.err\b|aria-invalid|:invalid|campo\.mal', html):
    print("   ..." + aplasta(html[max(0, m.start() - 90):m.end() + 130]) + "...")
    break
print("   reglas CSS con 'mal' o 'err':", len(re.findall(r'\.(?:mal|err)\b', html)))
