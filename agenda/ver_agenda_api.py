#!/usr/bin/env python3
# Como esta armado agenda_api.py para pegar el endpoint /reservas. SOLO LECTURA.
import io, re

p = io.open('/root/universo/agenda/agenda_api.py', encoding='utf-8').read()
print("bytes:", len(p.encode('utf-8')))
print()
print("=== el router / app ===")
for m in re.finditer(r'^.*(APIRouter|FastAPI)\(.*$', p, re.M):
    print("  ", m.group(0).strip()[:160])
print()
print("=== guardianes de sesion / token (nombres exactos) ===")
for m in re.finditer(r'^(?:async )?def (\w*(?:sesion|token|guardi|clave|auth)\w*)\s*\(.*?\)\s*:', p, re.M | re.I):
    print("  ", m.group(1))
for m in re.finditer(r'Depends\((\w+)\)', p):
    pass
import collections
print("  Depends usados:", collections.Counter(re.findall(r'Depends\((\w+)\)', p)).most_common(8))
print()
print("=== helpers ===")
for nom in ('todos', 'uno', 'traducir', 'MARCAS'):
    print(f"  def {nom}:", 'SI' if re.search(r'^def %s\b' % nom, p, re.M) else 'NO')
print()
print("=== ejemplos de rutas (para copiar el estilo) ===")
rutas = re.findall(r'@\w+\.(get|post)\("([^"]+)"\)\s*\n(?:async )?def (\w+)\(([^)]{0,240})\)', p)
for metodo, ruta, fn, args in rutas[:14]:
    args1 = re.sub(r'\s+', ' ', args).strip()
    print(f"  {metodo.upper():<5} {ruta:<28} -> {fn}({args1[:150]})")
print("\n  total de rutas:", len(rutas))
print()
print("=== una ruta GET con Query, completa (molde) ===")
m = re.search(r'@\w+\.get\("/(?:citas|clientes)[^"]*"\)\s*\n(?:async )?def .*?(?=\n@|\Z)', p, re.S)
if m:
    print(re.sub(r'\n\s*', '\n  ', m.group(0).strip())[:900])
