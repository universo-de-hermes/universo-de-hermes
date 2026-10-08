#!/usr/bin/env python3
# Todos los botones con su clase. SOLO LECTURA.
import io, re

h = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S | re.I))

print("=== BOTONES creados por el panel (clase + texto) ===")
for m in re.finditer(r'h\(\s*"button"\s*,\s*\{', js):
    frag = js[m.start():m.start() + 500]
    cl = re.search(r'class\s*:\s*"([^"]*)"', frag)
    clase = cl.group(1) if cl else "(sin clase)"
    # el texto va antes de cerrar el h( ... )
    tx = re.findall(r'"([^"\n]{2,60})"', frag)
    print(f"   {clase:<22} | {tx[:3]}")

print("\n=== textos de accion y su clase mas cercana ===")
for t in ("Confirmar el cambio", "Sí, cancelar", "Sí, cerrarla", "Terminar",
          "Guardar y continuar", "Ya llegué", "Actualizar mis datos", "Ver otro día"):
    idx = js.find(t)
    if idx < 0:
        print(f"   «{t}»  NO encontrado en el JS")
        continue
    frag = re.sub(r'\s+', ' ', js[max(0, idx - 400):idx + 60])
    cl = re.findall(r'class:\s*"([^"]*)"', frag)
    print(f"   «{t}»  ->  clases cerca: {cl}")
