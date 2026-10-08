#!/usr/bin/env python3
# ¿El error de cruce se traduce a palabras? ¿Que refresca la agenda? SOLO LECTURA.
import io, re

print("=" * 74)
print("  1. ¿EL ERROR DE LA BASE SE TRADUCE A PALABRAS?")
print("=" * 74)
for ruta in ('/root/universo/agenda/agenda_api.py', '/root/universo/agenda/autoservicio.py'):
    txt = io.open(ruta, encoding='utf-8').read()
    print(f"\n  --- {ruta.split('/')[-1]}")
    m = re.search(r'def traducir\(.*?\n(?=\ndef |\n@|\nclass )', txt, re.S)
    if m:
        cuerpo = m.group(0)
        print("     " + re.sub(r'\n\s*', '\n     ', cuerpo.strip())[:1400])
    for pat, que in ((r'solape', 'menciona "solape"'), (r'23P01', 'menciona el codigo 23P01'),
                     (r'exclusion', 'menciona "exclusion"'), (r'ocupad|ocupar|acabó', 'mensaje de hora ocupada'),
                     (r'conflicting', 'menciona "conflicting"')):
        n = len(re.findall(pat, txt, re.I))
        if n:
            print(f"     {n} x  {que}")

print("\n" + "=" * 74)
print("  2. QUE REFRESCA LA AGENDA Y CADA CUANTO")
print("=" * 74)
a = io.open('/var/www/html/agenda.html', encoding='utf-8', errors='replace').read()
print("  REFRESCO:", re.findall(r'REFRESCO\s*=\s*[0-9]+', a))
m = re.search(r'function refrescarDia\(\s*\)\s*\{', a)
if m:
    print("  refrescarDia hace:")
    print("     " + re.sub(r'\s+', ' ', a[m.start():m.start() + 420]))
for pat, que in ((r'setInterval\([^,]{0,40}', 'setInterval'),
                 (r'>Recargar<|>Actualizar<|>Refrescar<', 'boton de recargar'),
                 (r'recargar|refrescar', 'palabra recargar/refrescar')):
    for mm in re.finditer(pat, a, re.I):
        print(f"     {que}: ...{re.sub(chr(92)+'s+', ' ', a[max(0,mm.start()-60):mm.end()+80])}...")
        break

print("\n" + "=" * 74)
print("  3. ¿LA AGENDA TIENE BOTON DE RECARGA? (controles del encabezado)")
print("=" * 74)
for mm in re.finditer(r'id="([a-z-]*(?:recarg|refresc|actualiz)[a-z-]*)"', a, re.I):
    print("   boton:", mm.group(1))
for mm in re.finditer(r'REFRESCO[A-Z_]*|[a-zA-Z]*sync[a-zA-Z]*', a):
    pass
print("   Ojo: 'refrescarDia' refresca SOLO la vista del dia.")
print("   ¿y el mes / los reportes?")
for nombre in ('refrescarMes', 'cargarMes', 'refrescarReporte', 'refrescarIndicadores'):
    print(f"     {nombre}: {'SI' if nombre in a else 'NO'}")
