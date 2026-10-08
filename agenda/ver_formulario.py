#!/usr/bin/env python3
# Como esta el formulario de clienta nueva. SOLO LECTURA.
import io, re

html = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()
py = io.open('/root/universo/agenda/autoservicio.py', encoding='utf-8').read()
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S | re.I))


def aplasta(t):
    return re.sub(r'\s+', ' ', t).strip()


print("=" * 74)
print("  1. TIPOS DE DOCUMENTO (lista y predeterminado)")
print("=" * 74)
for m in re.finditer(r'TIPOS_DOC\s*=\s*\[(.*?)\]', py, re.S):
    print("   " + aplasta(m.group(1))[:300])
print("   selección en el HTML:")
for m in re.finditer(r"#f-tipo|f-tipo|tipo_doc|tipoDoc", html):
    a, b = max(0, m.start() - 120), m.end() + 200
    print("     ..." + aplasta(html[a:b])[:280] + "...")
    break

print("\n" + "=" * 74)
print("  2. CAMPOS DEL FORMULARIO (etiqueta + texto de ejemplo)")
print("=" * 74)
# bloques de campo en el JS del formulario
for m in re.finditer(r'campo\(([^)]{0,320})\)', js):
    print("   campo(" + aplasta(m.group(1))[:250] + ")")
print()
print("   inputs creados en el JS:")
for m in re.finditer(r'h\("input"[^)]{0,340}\)', js):
    print("     " + aplasta(m.group(0))[:300])
print()
print("   etiquetas visibles del formulario:")
for m in re.finditer(r'"(Nombre|Apellido|Tipo de documento|Número de documento|Celular|Correo)"', html):
    a = max(0, m.start() - 90)
    print("     ..." + aplasta(html[a:m.end() + 120])[:230] + "...")

print("\n" + "=" * 74)
print("  3. VALIDACION antes de «Guardar y continuar»")
print("=" * 74)
for m in re.finditer(r'function\s+(recogerFicha|guardarFicha|validarFicha|vNuevo)\s*\([^)]*\)\s*\{', js):
    print(f"\n   --- {m.group(1)}()")
    print("   " + aplasta(js[m.start():m.start() + 1500])[:1500])

print("\n" + "=" * 74)
print("  4. VALIDACION EN EL SERVIDOR (as_guardar)")
print("=" * 74)
m = re.search(r'def as_guardar\(.*?\n(?=\n@|\ndef |\nclass )', py, re.S)
if m:
    print(aplasta(m.group(0))[:1700])

print("\n" + "=" * 74)
print("  5. MENSAJES QUE YA EXISTEN (para reusar el estilo)")
print("=" * 74)
for m in re.finditer(r'"(Escriba[^"]{0,90}|Falta[^"]{0,90}|Complete[^"]{0,90}|Siga[^"]{0,90})"', html):
    print("   ·", m.group(1))
