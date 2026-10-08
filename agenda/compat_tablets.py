#!/usr/bin/env python3
# Capa de compatibilidad para tablets antiguas (iPad iOS 12 / Safari 12).
# No cambia NADA en navegadores modernos: todo va dentro de @supports not (...).
import io, re, shutil, hashlib, sys

RUTA = '/var/www/html/autoservicio.html'

BLOQUE = """
/* ══════════════════════════════════════════════════════════════════════════
   CAPA DE COMPATIBILIDAD — tablets antiguas (iPad iOS 12 / Safari 12 y antes)

   Safari 12 no entiende:  gap en flexbox · clamp() · 100dvh
   Aquí se les da un equivalente, para que la tablet vieja se vea igual de bien
   que las nuevas. TODO va dentro de @supports not (aspect-ratio:1), que es
   falso en cualquier navegador moderno: en la tablet nueva y en el PC esta
   capa NO se activa y no cambia absolutamente nada.
   ══════════════════════════════════════════════════════════════════════════ */
@supports not (aspect-ratio:1){

  /* ── 1. gap en flexbox → márgenes (siempre al lado, nunca en los bordes) ── */
  header{gap:0}                header>*{margin-right:16px}        header>*:last-child{margin-right:0}
  .fila{gap:0}                 .fila>*{margin-right:14px;margin-bottom:14px}
                               .fila>*:last-child{margin-right:0}
  .dato{gap:0}                 .dato>*{margin-right:20px}         .dato>*:last-child{margin-right:0}
  .cargando{gap:0}             .cargando>*{margin-right:14px}     .cargando>*:last-child{margin-right:0}
  .cal .cab{gap:0}             .cal .cab>*{margin-right:10px}     .cal .cab>*:last-child{margin-right:0}
  #modal .fila{gap:0}          #modal .fila>*{margin-right:12px;margin-bottom:12px}
                               #modal .fila>*:last-child{margin-right:0}

  .hoja{gap:0}                 .hoja>*{margin-bottom:22px}        .hoja>*:last-child{margin-bottom:0}
  .opcion{gap:0}               .opcion>*{margin-bottom:5px}       .opcion>*:last-child{margin-bottom:0}
  label.campo{gap:0}           label.campo>*{margin-bottom:7px}   label.campo>*:last-child{margin-bottom:0}
  #modal .caja{gap:0}          #modal .caja>*{margin-bottom:18px} #modal .caja>*:last-child{margin-bottom:0}
  #llave .caja{gap:0}          #llave .caja>*{margin-bottom:16px} #llave .caja>*:last-child{margin-bottom:0}
  #bienvenida .marca{gap:0}    #bienvenida .marca>*{margin-bottom:14px}
                               #bienvenida .marca>*:last-child{margin-bottom:0}
  #bienvenida .abajo{gap:0}    #bienvenida .abajo>*{margin-bottom:16px}
                               #bienvenida .abajo>*:last-child{margin-bottom:0}

  /* ── 2. altura de la pantalla (100dvh no existe en iOS 12) ── */
  #bienvenida{height:100vh}

  /* ── 3. clamp() → valor fijo equivalente ── */
  #bienvenida{padding:40px;row-gap:26px}
  #bienvenida img{height:80px}
  #bienvenida h1{font-size:42px}
  #bienvenida .sub{font-size:18px}
  #bienvenida .quehace{font-size:16px}
  #bienvenida .toque{font-size:20px;padding:22px 46px}
  #modal .caja{padding:30px}
  #modal h2{font-size:23px}
  #modal p{font-size:16px}

  /* ── 4. los avisos: sin color-mix() se quedan sin borde ── */
  .aviso{border:1px solid var(--line)}
  .aviso.ok{border-color:rgba(111,199,156,.55)}
}
"""

h = io.open(RUTA, encoding='utf-8').read()
if 'CAPA DE COMPATIBILIDAD' in h:
    print("YA ESTA APLICADA. Nada que hacer."); sys.exit(0)

# localizar el <style> grande (el que tiene .btn.pri)
punto = None
for m in re.finditer(r'<style[^>]*>', h):
    cierre = h.find('</style>', m.end())
    if '.btn.pri{' in h[m.end():cierre]:
        punto = cierre
        break
if punto is None:
    print("ABORTO: no encontre el <style> principal"); sys.exit(1)

nuevo = h[:punto] + BLOQUE + h[punto:]
shutil.copy(RUTA, RUTA + '.pre-compat.bak')
io.open(RUTA, 'w', encoding='utf-8').write(nuevo)

print(f"punto de insercion: caracter {punto} (justo antes del </style> principal)")
print(f"APLICADO: {len(h)} -> {len(nuevo)} caracteres  (+{len(nuevo)-len(h)})")
print(f"md5 nuevo: {hashlib.md5(nuevo.encode()).hexdigest()[:12]}")
print(f"respaldo : {RUTA}.pre-compat.bak")

# comprobaciones
print("\n=== COMPROBACIONES ===")
print("  llaves { } balanceadas:",
      nuevo.count('{') == nuevo.count('}'), f"({nuevo.count('{')} abre, {nuevo.count('}')} cierra)")
print("  aparece 'CAPA DE COMPATIBILIDAD':", nuevo.count('CAPA DE COMPATIBILIDAD'))
print("  va DENTRO del <style>:", punto < nuevo.find('CAPA DE COMPATIBILIDAD') < nuevo.find('</style>', punto))
print("  reglas nuevas de margen:", len(re.findall(r'margin-(?:right|bottom):\d+px', BLOQUE)))
print(f"  tamano en bytes: {len(nuevo.encode('utf-8'))}")
