#!/usr/bin/env python3
# HUMANO: como se traducen los errores del formulario. SOLO LECTURA.
import io, re

py = io.open('/root/universo/agenda/autoservicio.py', encoding='utf-8').read()
html = io.open('/var/www/html/autoservicio.html', encoding='utf-8').read()

print("=" * 74)
print("  HUMANO: error del servidor -> frase que lee la clienta")
print("=" * 74)
m = re.search(r'HUMANO\s*=\s*\{(.*?)\n\}', py, re.S)
print(m.group(0) if m else "NO ENCONTRADO")

print("\n" + "=" * 74)
print("  ¿Que pasa si falta el nombre, el celular o el correo?")
print("=" * 74)
for marca in ('NOMBRE', 'APELLIDO', 'TELEFONO', 'CORREO', 'DOC', 'TIPO'):
    en_humano = bool(re.search(r'"%s"' % marca, (m.group(1) if m else '')))
    print(f"   {marca:<10} {'SI esta en HUMANO ✅' if en_humano else 'NO esta -> cae al mensaje generico ❌'}")

print("\n" + "=" * 74)
print("  TEXTOS DE EJEMPLO ACTUALES (los que confunden)")
print("=" * 74)
for ph in re.findall(r'placeholder:"([^"]*)"', html):
    print(f"   · «{ph}»")

print("\n" + "=" * 74)
print("  ¿El panel valida en el navegador antes de mandar?")
print("=" * 74)
js = "\n".join(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', html, re.S | re.I))
m2 = re.search(r'"btn pri grande"[^)]{0,160}guardar[^)]{0,160}', js)
print("   boton guardar:", re.sub(r'\s+', ' ', m2.group(0))[:200] if m2 else "?")
print("   ¿valida algo antes de enviar?", "SI" if 'recogerFicha' in js or 'faltan' in js.lower() else "NO (manda y espera el error del servidor)")
print("   required en los inputs:", 'required' in js)
