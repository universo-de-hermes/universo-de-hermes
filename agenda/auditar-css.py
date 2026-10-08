#!/usr/bin/env python3
"""Qué del CSS no entiende Safari 12, y qué de eso no tiene respuesto.

La regla que se comprueba es la de Hermes: el valor simple va ANTES del
moderno, en la MISMA regla. Así el navegador viejo se queda con el primero y
el nuevo lo pisa con el segundo. Lo que no cumpla eso sale marcado.

    python3 auditar-css.py autoservicio.html

Sale con código 1 si algo quedó sin respaldo, para poder meterlo en el build.
"""
import re
import sys

# lo que no entiende Safari 12.1.2 (el iPad de El Tesoro), y desde cuándo existe
MODERNO = {
    "color-mix(":  "Safari 16.2",
    "clamp(":      "Safari 13.1",
    "dvh":         "Safari 15.4",
    "aspect-ratio": "Safari 15",
}
# propiedades donde gap NO funciona en Safari 12 (en grid sí, en flex no)
FLEX = re.compile(r"display\s*:\s*(flex|inline-flex)")


def reglas(css):
    """Parte el CSS en (selector, cuerpo) sin meterse dentro de @media/@supports."""
    fuera = []
    i, n = 0, len(css)
    while i < n:
        j = css.find("{", i)
        if j < 0:
            break
        sel = css[i:j].strip()
        if sel.startswith("@"):
            # bloque con llaves adentro: se baja un nivel y se sigue
            k, prof = j, 0
            while k < n:
                if css[k] == "{":
                    prof += 1
                elif css[k] == "}":
                    prof -= 1
                    if prof == 0:
                        break
                k += 1
            fuera.append((sel, css[j + 1:k], True))
            fuera += reglas(css[j + 1:k])
            i = k + 1
            continue
        k = css.find("}", j)
        if k < 0:
            break
        fuera.append((sel, css[j + 1:k], False))
        i = k + 1
    return fuera


def declaraciones(cuerpo):
    """Las declaraciones de un cuerpo, en orden, como (propiedad, valor)."""
    out = []
    for d in cuerpo.split(";"):
        if ":" not in d:
            continue
        p, _, v = d.partition(":")
        p = p.strip().lower()
        if p and not p.startswith("/*"):
            out.append((p, v.strip()))
    return out


def auditar(ruta):
    html = open(ruta, encoding="utf-8").read()
    css = "\n".join(re.findall(r"<style>(.*?)</style>", html, re.S))
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)

    # La capa de respaldo de Hermes vive en «@supports not (…)» y vuelve a
    # declarar la misma propiedad para el mismo selector. Así que lo que
    # protege de verdad es el par (selector, propiedad), no el texto entero.
    # Un «@supports (…)» en positivo es el camino moderno, no un respaldo: no
    # cuenta.
    respaldadas = set()
    for sel, cuerpo, es_arroba in reglas(css):
        if not es_arroba or not re.match(r"@supports\s+not\b", sel):
            continue
        for s2, c2, arroba2 in reglas(cuerpo):
            if arroba2:
                continue
            for p2, _ in declaraciones(c2):
                for uno in s2.split(","):
                    respaldadas.add((uno.strip(), p2))

    faltan, bien = [], 0
    for sel, cuerpo, es_arroba in reglas(css):
        if es_arroba:
            continue
        decs = declaraciones(cuerpo)

        def hay_respaldo(prop):
            return any((uno.strip(), prop) in respaldadas for uno in sel.split(","))

        for idx, (prop, val) in enumerate(decs):
            for marca, desde in MODERNO.items():
                if marca not in val:
                    continue
                # ¿hay antes, en esta misma regla, la MISMA propiedad sin lo moderno?
                hay = any(p == prop and not any(m in v for m in MODERNO)
                          for p, v in decs[:idx])
                if hay or hay_respaldo(prop):
                    bien += 1
                else:
                    faltan.append((sel, prop, val[:54], marca.rstrip("("), desde))

        # gap en flex: Safari 12 lo ignora y todo queda pegado
        if FLEX.search(cuerpo):
            for prop, val in decs:
                if prop in ("gap", "row-gap", "column-gap") and not hay_respaldo(prop):
                    faltan.append((sel, prop, val[:54], "gap en flex", "Safari 14.1"))

    print(f"  {bien} usos modernos CON respaldo")
    if not faltan:
        print("  ✓ ninguno sin respaldo")
        return 0
    print(f"  ✗ {len(faltan)} SIN respaldo:\n")
    ancho = max(len(f[0]) for f in faltan)
    for sel, prop, val, que, desde in faltan:
        print(f"    {sel:<{min(ancho,44)}}  {prop}: {val}")
        print(f"    {'':<{min(ancho,44)}}  └─ {que} · llega en {desde}")
    return 1


if __name__ == "__main__":
    ruta = sys.argv[1] if len(sys.argv) > 1 else "autoservicio.html"
    sys.exit(auditar(ruta))
