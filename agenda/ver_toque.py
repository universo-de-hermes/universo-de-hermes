#!/usr/bin/env python3
# Ver y arreglar el boton del inicio (.toque) y demas botones oscuros. SOLO LECTURA + parche.
import io, re, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()
css = "\n".join(re.findall(r'<style[^>]*>(.*?)</style>', h, re.S | re.I))

print("=== REGLA de #bienvenida .toque (tal cual) ===")
m = re.search(r'#bienvenida\s+\.toque\s*\{([^{}]*)\}', css)
if m:
    print("   " + re.sub(r'\s+', ' ', m.group(1)).strip()[:400])
else:
    print("   NO ENCONTRADA; buscando otras:")
    for mm in re.finditer(r'([^{}]{1,160}?)\{([^{}]*)\}', css):
        s = re.sub(r'/\*.*?\*/', '', mm.group(1), flags=re.S).strip().split('\n')[-1].strip()
        if 'toque' in s:
            print(f"   [{s}]  {re.sub(chr(92)+chr(115)+'+', ' ', mm.group(2)).strip()[:220]}")

print("\n=== los demas botones: fondo y color de letra ===")
for mm in re.finditer(r'([^{}]{1,200}?)\{([^{}]*)\}', css):
    s = re.sub(r'/\*.*?\*/', '', mm.group(1), flags=re.S).strip().split('\n')[-1].strip()
    if not re.match(r'^(\.btn|\.opcion|\.toque|header button|\.teclas button|\.cal)', s):
        continue
    bg = re.search(r'background[a-z-]*\s*:\s*([^;]*)', mm.group(2))
    col = re.search(r'(?<![-a-z])color\s*:\s*([^;]*)', mm.group(2))
    if not bg:
        continue
    print(f"   [{s[:52]:<52}] fondo={bg.group(1).strip()[:26]:<26} letra={(col.group(1).strip() if col else '(hereda)')[:18]}")
