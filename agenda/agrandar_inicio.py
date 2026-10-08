#!/usr/bin/env python3
# Agranda el INICIO (Bienvenida) para que se lea desde lejos.
# Cambia en los DOS lados: el diseno moderno (clamp) y la capa vieja (vmin),
# con los mismos numeros, para que se vean identicos.
import io, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

CAMBIOS = [
    # (viejo, nuevo, que)
    # ── diseno moderno (clamp) ──
    ("clamp(30px,6.6vmin,58px)",  "clamp(34px,10vmin,104px)",  "TITULO (moderno)"),
    ("clamp(58px,11vmin,116px)",  "clamp(64px,15vmin,180px)",  "logo (moderno)"),
    ("clamp(15px,2.5vmin,23px)",  "clamp(17px,3.6vmin,42px)",  "subtitulo (moderno)"),
    ("clamp(14px,2.2vmin,20px)",  "clamp(16px,3.2vmin,36px)",  "frase (moderno)"),
    ("clamp(17px,2.8vmin,24px)",  "clamp(19px,4.4vmin,46px)",  "boton texto (moderno)"),
    ("clamp(18px,2.6vmin,26px) clamp(34px,6vmin,58px)",
     "clamp(20px,3.4vmin,40px) clamp(38px,7.5vmin,96px)",      "boton caja (moderno)"),
    ("clamp(24px,5vmin,64px)",    "clamp(26px,5.4vmin,72px)",  "relleno (moderno)"),
    ("clamp(18px,3.4vmin,40px)",  "clamp(20px,4.4vmin,60px)",  "separacion filas (moderno)"),
    # ── capa de compatibilidad (vmin, mismos numeros) ──
    ("#bienvenida img{height:11vmin}",              "#bienvenida img{height:15vmin}",              "logo (compat)"),
    ("#bienvenida h1{font-size:6.6vmin}",           "#bienvenida h1{font-size:10vmin}",            "TITULO (compat)"),
    ("#bienvenida .sub{font-size:2.5vmin}",         "#bienvenida .sub{font-size:3.6vmin}",         "subtitulo (compat)"),
    ("#bienvenida .quehace{font-size:2.2vmin}",     "#bienvenida .quehace{font-size:3.2vmin}",     "frase (compat)"),
    ("#bienvenida .toque{font-size:2.8vmin;padding:2.6vmin 6vmin}",
     "#bienvenida .toque{font-size:4.4vmin;padding:3.4vmin 7.5vmin}",                              "boton (compat)"),
    ("#bienvenida{padding:5vmin;row-gap:3.4vmin}",  "#bienvenida{padding:5.4vmin;row-gap:4.4vmin}", "relleno (compat)"),
]

print(f"archivo: {len(h)} caracteres\n")
fallos = []
nuevo = h
for viejo, rep, que in CAMBIOS:
    n = nuevo.count(viejo)
    print(f"  {'OK' if n == 1 else 'ABORTO':<7} {n} x  {que}")
    if n != 1:
        fallos.append(que); continue
    nuevo = nuevo.replace(viejo, rep, 1)

if fallos:
    print("\n*** no calzaron: " + "; ".join(fallos) + " — NO se toco nada.")
    sys.exit(1)

shutil.copy(RUTA, RUTA + '.pre-grande.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)
print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} caracteres (+{len(nuevo)-len(h)})")
print(f"llaves {nuevo.count('{')}/{nuevo.count('}')}  balanceadas: {nuevo.count('{')==nuevo.count('}')}")
print(f"md5 {hashlib.md5(nuevo.encode()).hexdigest()[:12]}  bytes {len(nuevo.encode('utf-8'))}")
print(f"respaldo: {RUTA}.pre-grande.bak")

# ── cuanto queda en cada tablet ──
print("\n=== TAMANO RESULTANTE ===")
for w, hh, etq in ((1280, 800, 'Xiaomi Pad / Samsung Tab (horizontal)'),
                   (1024, 768, 'iPad viejo (horizontal)'),
                   (800, 1280, 'tablet en vertical')):
    vmin = min(w, hh)
    titulo = min(max(34, 10 * vmin / 100), 104)
    logo = min(max(64, 15 * vmin / 100), 180)
    boton = min(max(19, 4.4 * vmin / 100), 46)
    alto = logo + titulo + (3.6 * vmin / 100) + (2 * 3.2 * vmin / 100) + (boton + 2 * 3.4 * vmin / 100)
    print(f"  {etq}  {w}x{hh}")
    print(f"     titulo {titulo:.0f}px · logo {logo:.0f}px · boton {boton:.0f}px · contenido ~{alto:.0f}px de {hh}px")
