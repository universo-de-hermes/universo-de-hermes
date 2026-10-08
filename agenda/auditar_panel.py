#!/usr/bin/env python3
# Auditoria: (a) que aparato es la tablet, (b) que CSS/JS moderno NO entiende.
import io, re, subprocess, collections

print("=" * 74)
print("  A. QUE APARATO ENTRA AL PANEL (User-Agent del log de nginx)")
print("=" * 74)
uas = collections.Counter()
for log in ('/var/log/nginx/access.log', '/var/log/nginx/access.log.1'):
    try:
        txt = io.open(log, encoding='utf-8', errors='replace').read()
    except Exception:
        continue
    for linea in txt.splitlines():
        if 'autoservicio' in linea or 'agenda.html' in linea:
            m = re.search(r'"([^"]*)"\s*$', linea)
            if m:
                uas[m.group(1)[:170]] += 1
if not uas:
    print("   (no se encontro nada; probando con el log completo)")
    try:
        txt = io.open('/var/log/nginx/access.log', encoding='utf-8', errors='replace').read()
        for linea in txt.splitlines()[-4000:]:
            m = re.search(r'"([^"]*)"\s*$', linea)
            if m:
                uas[m.group(1)[:170]] += 1
    except Exception as e:
        print("   error:", e)
for ua, n in uas.most_common(12):
    print(f"   {n:>5} x  {ua}")

print()
print("=" * 74)
print("  B. CSS/JS MODERNO EN EL PANEL (lo que un aparato viejo NO entiende)")
print("=" * 74)
h = io.open('/var/www/html/autoservicio.html', encoding='utf-8', errors='replace').read()

CSS = {
    'color-mix(          (2023)': r'color-mix\(',
    ':has(                (2022)': r':has\(',
    ':is( / :where(       (2021)': r':(?:is|where)\(',
    'display:grid         (2017)': r'display\s*:\s*grid',
    'grid-template        (2017)': r'grid-template',
    'gap:  en flex         (2020)': r'[;{]\s*gap\s*:',
    'aspect-ratio         (2021)': r'aspect-ratio\s*:',
    'clamp(               (2020)': r'clamp\(',
    'inset:               (2021)': r'[;{]\s*inset\s*:',
    'min()/max() en CSS   (2020)': r'[;:(]\s*(?:min|max)\(\s*(?:[0-9]|var\()',
    'backdrop-filter SIN -webkit': r'(?<!-webkit-)backdrop-filter\s*:',
    'object-fit           (2016)': r'object-fit\s*:',
    'dvh / svh / lvh      (2022)': r'\d(?:dvh|svh|lvh)',
    'place-items          (2017)': r'place-(?:items|content)\s*:',
    '@supports': r'@supports',
}
JS = {
    '=>  (flecha)         (ES6/Safari10)': r'=>',
    '`  (plantilla)       (ES6/Safari10)': r'`',
    'let / const          (ES6)': r'\b(?:let|const)\s',
    'async / await        (Safari10.1)': r'\b(?:async|await)\b',
    'fetch(               (Safari10.1)': r'\bfetch\(',
    'Object.assign        (Safari9)': r'Object\.assign',
    'Array.from           (Safari9)': r'Array\.from',
    '.padStart/.padEnd    (Safari10)': r'\.pad(?:Start|End)\(',
    '?. / ??              (Safari13.1)': r'\?\.|\?\?',
    '.includes(           (Safari9)': r'\.includes\(',
    '...spread            (ES6)': r'\.\.\.',
    'for...of             (ES6)': r'for\s*\([^)]*\bof\b',
    'class                (ES6)': r'\bclass\s+\w+\s*\{',
    'URLSearchParams      (Safari10.1)': r'URLSearchParams',
    'IntersectionObserver (Safari12.1)': r'IntersectionObserver',
}

def escanear(titulo, tabla):
    print(f"\n  --- {titulo} ---")
    for etq, pat in tabla.items():
        n = len(re.findall(pat, h))
        if n:
            marca = "  <<<< OJO" if n > 0 else ""
            print(f"    {n:>4} x  {etq}{marca}")
    faltan = [e for e, p in tabla.items() if not re.search(p, h)]
    print("    (no aparece:) " + ", ".join(f.split()[0] for f in faltan))

escanear("CSS", CSS)
escanear("JAVASCRIPT", JS)
