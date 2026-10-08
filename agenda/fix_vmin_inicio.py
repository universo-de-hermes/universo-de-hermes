#!/usr/bin/env python3
# Corrige la capa de compatibilidad: valores fijos -> vmin (escala igual que el diseno).
# Y arregla el theme-color (era el color claro) para las tablets nuevas.
import io, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'
h = io.open(RUTA, encoding='utf-8').read()

CAMBIOS = [
    # (viejo, nuevo, que arregla)
    ("#bienvenida{padding:40px;row-gap:26px}",
     "#bienvenida{padding:5vmin;row-gap:3.4vmin}",
     "inicio: relleno (era fijo 40px)"),

    ("#bienvenida img{height:80px}",
     "#bienvenida img{height:11vmin}",
     "inicio: logo"),

    ("#bienvenida h1{font-size:42px}",
     "#bienvenida h1{font-size:6.6vmin}",
     "inicio: TITULO (era 42px, ahora escala)"),

    ("#bienvenida .sub{font-size:18px}",
     "#bienvenida .sub{font-size:2.5vmin}",
     "inicio: subtitulo"),

    ("#bienvenida .quehace{font-size:16px}",
     "#bienvenida .quehace{font-size:2.2vmin}",
     "inicio: frase"),

    ("#bienvenida .toque{font-size:20px;padding:22px 46px}",
     "#bienvenida .toque{font-size:2.8vmin;padding:2.6vmin 6vmin}",
     "inicio: boton Toque para empezar"),

    ("#bienvenida .marca>*{margin-bottom:14px}",
     "#bienvenida .marca>*{margin-bottom:2vmin}",
     "inicio: separacion marca"),

    ("#bienvenida .abajo>*{margin-bottom:16px}",
     "#bienvenida .abajo>*{margin-bottom:2.2vmin}",
     "inicio: separacion abajo"),

    ("#modal .caja{padding:30px}",
     "#modal .caja{padding:4.2vmin}",
     "modal: relleno"),

    ("#modal h2{font-size:23px}",
     "#modal h2{font-size:3.2vmin}",
     "modal: titulo"),

    ("#modal p{font-size:16px}",
     "#modal p{font-size:2.3vmin}",
     "modal: texto"),

    ('<meta name="theme-color" content="#EDF5F7">',
     '<meta name="theme-color" content="#181210">',
     "barra del navegador: era el color CLARO"),
]

print(f"archivo: {len(h)} caracteres\n")
fallos = []
nuevo = h
for viejo, rep, que in CAMBIOS:
    n = nuevo.count(viejo)
    estado = "OK" if n == 1 else "ABORTO"
    print(f"  {estado:<7} {n} x  {que}")
    if n != 1:
        fallos.append(que)
        continue
    nuevo = nuevo.replace(viejo, rep, 1)

if fallos:
    print("\n*** no calzaron: " + "; ".join(fallos) + " — NO se toco nada.")
    sys.exit(1)

shutil.copy(RUTA, RUTA + '.pre-vmin.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)
print(f"\nAPLICADO: {len(h)} -> {len(nuevo)} caracteres  (+{len(nuevo)-len(h)})")
print(f"llaves balanceadas: {nuevo.count('{') == nuevo.count('}')} ({nuevo.count('{')}/{nuevo.count('}')})")
print(f"md5 {hashlib.md5(nuevo.encode()).hexdigest()[:12]}   bytes {len(nuevo.encode('utf-8'))}")
print(f"respaldo: {RUTA}.pre-vmin.bak")
