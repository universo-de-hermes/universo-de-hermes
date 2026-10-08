#!/usr/bin/env python3
# Formulario: quita ejemplos + valida obligatorios (version con regex tolerante).
import io, re, shutil, hashlib, sys, subprocess

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

print("=== texto REAL alrededor de guardarCliente (repr) ===")
i = h.find('function guardarCliente')
print(repr(h[i:i + 130]) if i >= 0 else "NO ENCONTRADO")

PLACEHOLDERS = [
    ('placeholder:"María"',             'placeholder:"Escriba su nombre"'),
    ('placeholder:"Gómez"',             'placeholder:"Escriba su apellido"'),
    ('placeholder:"1043449759"',        'placeholder:"Escriba su número de documento"'),
    ('placeholder:"3004168458"',        'placeholder:"Escriba su celular"'),
    ('placeholder:"nombre@correo.com"', 'placeholder:"Escriba su correo"'),
]

AYUDA = (
    'function faltaDatos(n){'
    'var d=String(n.documento||"").replace(/\\D/g,""),t=String(n.telefono||"").replace(/\\D/g,""),'
    'c=String(n.correo||"").trim(),nom=String(n.primer_nombre||"").trim(),ape=String(n.primer_apellido||"").trim();'
    'if(!d)return "Falta el número de documento.";'
    'if(d.length<6||d.length>11)return "Revise el número de documento: debe tener entre 6 y 11 dígitos.";'
    'if(!n.tipo_doc)return "Escoja el tipo de documento.";'
    'if(nom.length<2)return "Falta su nombre.";'
    'if(ape.length<2)return "Falta su apellido.";'
    'if(t.length<10)return "El celular debe tener 10 dígitos.";'
    'if(!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]{2,}$/.test(c))return "Revise el correo, por favor.";'
    'return "";}'
)
PAT = re.compile(r'function\s+guardarCliente\s*\(\s*\)\s*\{\s*var\s+n\s*=\s*S\.nuevo;\s*conCarga\(')

print(f"\narchivo: {len(h)} caracteres")
print("ancla regex calza:", len(PAT.findall(h)), "vez/veces")
if not PAT.findall(h):
    print("ABORTO: no encontre el ancla"); sys.exit(1)
if len(PAT.findall(h)) != 1:
    print("ABORTO: mas de una"); sys.exit(1)

nuevo = h
for viejo, rep in PLACEHOLDERS:
    c = nuevo.count(viejo)
    print(f"  {'OK' if c == 1 else 'FALLO':<6} {c} x  {viejo[:44]}")
    if c != 1:
        print("ABORTO"); sys.exit(1)
    nuevo = nuevo.replace(viejo, rep, 1)

REEMPLAZO = (AYUDA +
             '/* Los seis campos son obligatorios: si falta uno no se sigue, y se dice cual. */ '
             'function guardarCliente(){ var n = S.nuevo; var falta = faltaDatos(n);'
             ' if (falta){ S.error = falta; pintar(); return; } S.error = ""; conCarga(')
nuevo, k = PAT.subn(lambda m: REEMPLAZO, nuevo, count=1)
print("  OK   validacion insertada:", k == 1)

shutil.copy(RUTA, RUTA + '.pre-formulario.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)

print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} caracteres (+{len(nuevo)-len(h)})")
print(f"llaves {nuevo.count('{')}/{nuevo.count('}')} balanceadas: {nuevo.count('{')==nuevo.count('}')}")
print(f"md5 {hashlib.md5(nuevo.encode()).hexdigest()[:12]}  bytes {len(nuevo.encode('utf-8'))}")

bloques = re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', nuevo, re.S | re.I)
io.open('/tmp/form_check.js', 'w', encoding='utf-8').write("\n;\n".join(bloques))
r = subprocess.run(['node', '--check', '/tmp/form_check.js'], capture_output=True, text=True)
print(f"node --check rc={r.returncode} {r.stderr.strip()[:200]}")

print("\n=== textos de ejemplo ahora ===")
for ph in re.findall(r'placeholder:"([^"]*)"', nuevo):
    print(f"   · «{ph}»")
print("  validacion presente:", "faltaDatos" in nuevo)
print("  respaldo: autoservicio.html.pre-formulario.bak")
