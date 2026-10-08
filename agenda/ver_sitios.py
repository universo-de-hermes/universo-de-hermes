#!/usr/bin/env python3
"""[SOLO LECTURA] Los sitios exactos: tiempo del apartado y direcciones/nombres."""
import io, re, os

def bloque(path, desde, hasta, etq):
    print("=" * 70); print(etq, "->", path, "L%d-%d" % (desde, hasta)); print("=" * 70)
    t = io.open(path, encoding="utf-8", errors="replace").read().split("\n")
    for i in range(max(0, desde - 1), min(len(t), hasta)):
        print("%5d| %s" % (i + 1, t[i][:160]))
    print()

A = "/root/universo/agenda/autoservicio.py"
bloque(A, 1005, 1032, "PANEL: llamada a apartar_cupo (aqui vive el tiempo)")
bloque(A, 625, 660, "PANEL: nota del PASO / apartado")

print("=" * 70); print("PANEL: donde salen nombre y direccion de la sede"); print("=" * 70)
t = io.open(A, encoding="utf-8", errors="replace").read().split("\n")
for i, l in enumerate(t, 1):
    if re.search(r"Cra |direccion|NOMBRE_SEDE|nombre_de|sede_corta|El Tesoro|Bogot", l):
        print("%5d| %s" % (i, l[:170]))
print()

print("=" * 70); print("PEPE: su propia llamada a apartar_cupo"); print("=" * 70)
P = "/root/universo/recepcionista/agenda_helper.py"
t = io.open(P, encoding="utf-8", errors="replace").read().split("\n")
for i in range(635, 665):
    print("%5d| %s" % (i + 1, t[i][:160]))
print()

print("=" * 70); print("PANEL html: textos de la sede"); print("=" * 70)
H = "/var/www/html/autoservicio.html"
t = io.open(H, encoding="utf-8", errors="replace").read().split("\n")
for i, l in enumerate(t, 1):
    if re.search(r"Cra |Sótano|Plaza Norte|direccion|Tesoro|Bogot", l):
        print("%5d| %s" % (i, l.strip()[:170]))
print()

print("=" * 70); print("CRM: nombre/direccion de sedes"); print("=" * 70)
for base, _, files in os.walk("/root/universo/recepcionista"):
    if "venv" in base or "respaldo" in base:
        continue
    for f in files:
        if not f.endswith((".py", ".html")):
            continue
        p = os.path.join(base, f)
        try:
            t = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
        except Exception:
            continue
        for i, l in enumerate(t, 1):
            if re.search(r"Cra |Sótano|Plaza Norte|TESORO|Tesoro|direccion", l):
                print("%s:%d| %s" % (p.replace("/root/universo/recepcionista/", ""), i, l.strip()[:150]))
