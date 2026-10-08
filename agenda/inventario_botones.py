#!/usr/bin/env python3
# Inventario de TODOS los botones. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S | re.I))
css = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S | re.I))


def limpiar(sel):
    return re.sub(r'/\*.*?\*/', '', sel, flags=re.S).strip().split('\n')[-1].strip()


def aplastar(t):
    return re.sub(r'\s+', ' ', t).strip()


print("=== BOTONES creados por el panel (clase -> texto) ===")
vistos = []
for m in re.finditer(r'h\(\s*"button"\s*,\s*\{([^}]{0,240})\}\s*,\s*"([^"]{0,60})"', js):
    props, txt = m.group(1), m.group(2)
    cl = re.search(r'class\s*:\s*"([^"]*)"', props)
    cl = cl.group(1) if cl else '(sin clase)'
    extra = ''
    if 'disabled' in props:
        extra = '  [se apaga segun condicion]'
    key = (cl, txt[:30])
    if key in vistos:
        continue
    vistos.append(key)
    print(f"   {cl:<24} «{txt}»{extra}")

print("\n=== BOTONES en el HTML ===")
for m in re.finditer(r'<button([^>]*)>([^<]{0,60})', h):
    print(f"   «{m.group(2).strip()}»   {aplastar(m.group(1))[:60]}")

print("\n=== QUIEN USA TEXTO OSCURO (--acento-ink) ===")
for m in re.finditer(r'([^{}]{1,200}?)\{([^{}]*acento-ink[^{}]*)\}', css):
    print(f"   [{limpiar(m.group(1))[:70]}]")
    print(f"      {aplastar(m.group(2))[:180]}")

print("\n=== REGLAS QUE PINTAN FONDO OSCURO (glass) A UN BOTON ===")
for m in re.finditer(r'([^{}]{1,200}?)\{([^{}]*background\s*:\s*var\(--glass[^{}]*)\}', css):
    s = limpiar(m.group(1))
    if 'btn' in s or 'button' in s:
        bg = re.search(r'background\s*:[^;]*', m.group(2))
        print(f"   [{s[:64]}]  {bg.group(0) if bg else ''}")
