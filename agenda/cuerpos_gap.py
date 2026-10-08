#!/usr/bin/env python3
# Cuerpo completo de cada contenedor con gap en flex. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
css = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S | re.I))

OBJETIVO = ['header', '.hoja', '.fila', '.opcion', 'label.campo', '.dato',
            '.cargando', '#modal .caja', '#modal .fila', '#bienvenida .marca',
            '#bienvenida .abajo', '#llave .caja', '.cal .cab', '.teclas']

for m in re.finditer(r'([^{}]{1,240}?)\{([^{}]*)\}', css):
    sel = m.group(1).strip()
    if sel.startswith('@'):
        continue
    limpio = re.sub(r'/\*.*?\*/', '', sel, flags=re.S).strip().split('\n')[-1].strip()
    if limpio not in OBJETIVO:
        continue
    cuerpo = re.sub(r'\s+', ' ', m.group(2)).strip()
    dirn = re.search(r'flex-direction\s*:\s*(\w+)', cuerpo)
    disp = re.search(r'display\s*:\s*([\w-]+)', cuerpo)
    wrap = re.search(r'flex-wrap\s*:\s*(\w+)', cuerpo)
    gap = re.search(r'(?<![-a-z])gap\s*:\s*([^;}]+)', cuerpo)
    print(f"[{limpio}]")
    print(f"   display={disp.group(1) if disp else '-'}  direccion={dirn.group(1) if dirn else 'row(por defecto)'}"
          f"  wrap={wrap.group(1) if wrap else '-'}  gap={gap.group(1).strip() if gap else '-'}")
    print(f"   {cuerpo[:230]}")
    print()
