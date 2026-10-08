#!/usr/bin/env python3
"""UN SOLO NOMBRE Y UNA SOLA DIRECCION en los tres sistemas.

   Sede:     CJ Medical - El Tesoro   /   CJ Medical - Bogotá
   El Tesoro: Cra 25A #1a sur-45, LC 6100, Sótano 4 por la plaza de cines,
              Torre Norte, Medellín        (Parque Comercial, NO Centro Comercial)
   Bogotá:    Cra 11A #96-51, Edificio Oficity, Local 102, Chicó Norte, Bogotá
"""
import io, shutil, subprocess, sys

ET = "Cra 25A #1a sur-45, LC 6100, S\u00f3tano 4 por la plaza de cines, Torre Norte, Medell\u00edn"
BG = "Cra 11A #96-51, Edificio Oficity, Local 102, Chic\u00f3 Norte, Bogot\u00e1"

C = "/root/universo/recepcionista/crm/server.py"
M = "/root/universo/recepcionista/main.py"
H = "/root/universo/recepcionista/herramientas.py"

CAMBIOS = [
    # ── Pepe: el prompt del sistema ───────────────────────────────────────
    (M, "- Medell\u00edn: Parque Comercial El Tesoro, S\u00f3tano 4 Plaza Norte, Cra 25A #1a sur - 45, Local 6100, Medell\u00edn",
     "- Medell\u00edn: Parque Comercial El Tesoro \u2014 " + ET, "prompt: direccion de Medellin"),
    (M, "- Bogot\u00e1: Sede Chico Norte \u2014 Cra 11A #96-51 Edificio Oficity Local 102",
     "- Bogot\u00e1: Sede Chico Norte \u2014 " + BG, "prompt: direccion de Bogota"),
    (M, "nuestra sede ubicada en el Centro Comercial El Tesoro.", "nuestra sede ubicada en el Parque Comercial El Tesoro.",
     "prompt: Centro -> Parque Comercial"),
    # ── Pepe: el comando /sedes (lo que lee la clienta) ───────────────────
    (M, '"   Cra 11A #96-51 \u00b7 Edificio Oficity \u00b7 Local 102\\n\\n"',
     '"   ' + BG + '\\n\\n"', "/sedes: direccion de Bogota"),
    (M, '"🏙️ *Medell\u00edn \u2014 C.C. El Tesoro*\\n"',
     '"🏙️ *Medell\u00edn \u2014 Parque Comercial El Tesoro*\\n"', "/sedes: C.C. -> Parque Comercial"),
    (M, '"   Parque Comercial El Tesoro, S\u00f3tano 4 Plaza Norte \u00b7 Cra 25A #1a sur - 45 \u00b7 Local 6100\\n\\n"',
     '"   ' + ET + '\\n\\n"', "/sedes: direccion de Medellin"),
    # ── Pepe: el resumen que lee la clienta (separador sin guion) ─────────
    (H, "   🏢 Sede: [SEDE] - [DIRECCI\u00d3N]", "   🏢 Sede: [SEDE] \u00b7 [DIRECCI\u00d3N]",
     "resumen de Pepe: separador"),
    # ── El CRM ────────────────────────────────────────────────────────────
    (C, "addr='Cra 11A #96-51 Edificio Oficity Local 102'", "addr='" + BG + "'",
     "CRM: direccion de Bogota"),
    (C, "addr='Parque Comercial El Tesoro, S\u00f3tano 4 Plaza Norte, Cra 25A #1a sur - 45, Local 6100, Medell\u00edn'",
     "addr='" + ET + "'", "CRM: direccion de Medellin"),
    (C, "if(lo.indexOf(' - ')>=0)lo=lo.split(' - ')[0].trim();",
     "let _m=lo.split(/\\s*\u00b7\\s*/);if(_m.length<2)_m=lo.split(/\\s+-\\s+/);if(_m.length>1)lo=_m[0].trim();",
     "CRM: que el guion del nombre no lo corte"),
]

print("=== aplicando ===")
for ruta, viejo, nuevo, etq in CAMBIOS:
    src = io.open(ruta, encoding="utf-8").read()
    n = src.count(viejo)
    if n != 1:
        print("   ABORTO  %-42s (%d coincidencia/s)" % (etq, n))
        sys.exit(1)
    if not ruta.endswith(".bak"):
        shutil.copy2(ruta, ruta + ".pre-nombre-unico.bak")
    io.open(ruta, "w", encoding="utf-8", newline="").write(src.replace(viejo, nuevo))
    print("   OK      %s" % etq)

print("\n=== verificacion ===")
for f in (M, H, C):
    r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-m", "py_compile", f],
                       capture_output=True, text=True)
    print("   compila %-32s %s" % (f.split("/")[-1], "OK" if r.returncode == 0 else "MAL " + r.stderr[-300:]))

print("\n=== 'Plaza Norte' y 'Centro Comercial' que quedan ===")
for f in (M, H, C, "/root/universo/agenda/autoservicio.py"):
    t = io.open(f, encoding="utf-8", errors="replace").read()
    print("   %-22s Plaza Norte: %d   Centro Comercial: %d   C.C.: %d"
          % (f.split("/")[-1], t.count("Plaza Norte"), t.count("Centro Comercial"), t.count("C.C. ")))
