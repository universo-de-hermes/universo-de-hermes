#!/usr/bin/env python3
# TODAS las reglas que pintan un boton, con su @media. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
css = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S | re.I))

# recorrer el CSS llevando el @media abierto
i = 0
pila = []
tope = []
print("=== REGLAS QUE PINTAN ALGO CON 'btn' (o parecido) ===")
for m in re.finditer(r'@media([^{]*)\{|([^{}@]{1,300}?)\{([^{}]*)\}|\}', css):
    tok = m.group(0)
    if tok == '}':
        if pila:
            pila.pop()
        continue
    if m.group(1) is not None:
        pila.append('@media' + m.group(1).strip()[:70])
        continue
    sel = (m.group(2) or '').strip()
    cuerpo = m.group(3) or ''
    if not sel or sel.startswith('@'):
        continue
    limpio = re.sub(r'/\*.*?\*/', '', sel, flags=re.S).strip().split('\n')[-1].strip()
    if not re.search(r'\.btn|button', limpio):
        continue
    if not re.search(r'background|color\s*:|box-shadow|opacity', cuerpo):
        continue
    ctx = ' >> '.join(pila[-2:]) if pila else '(raiz)'
    print(f"\n  [{limpio[:70]}]")
    print(f"     contexto: {ctx}")
    print("     " + re.sub(r'\s+', ' ', cuerpo).strip()[:300])

print("\n\n=== ORDEN en el archivo (lo de abajo gana a igual especificidad) ===")
for m in re.finditer(r'([^{}@]{1,300}?)\{([^{}]*)\}', css):
    limpio = re.sub(r'/\*.*?\*/', '', m.group(1), flags=re.S).strip().split('\n')[-1].strip()
    if re.search(r'\.btn(?![a-z-])', limpio) and 'background' in m.group(2):
        print(f"   caracter {m.start():>6}  [{limpio[:60]}]  ->  {re.search(r'background[^;]*', m.group(2)).group(0)[:60]}")
