#!/usr/bin/env python3
"""Hallazgos c, d y e de la auditoria del panel.
  c) Los servicios mas pedidos primero (medido con las citas reales).
  d) La pantalla "ya tiene una cita" dice QUE cita es en el subtitulo.
  e) «Me da igual» pasa al final, despues de los nombres.
"""
import io, shutil, subprocess, sys

PY = "/root/universo/agenda/autoservicio.py"
HT = "/var/www/html/autoservicio.html"

# ── c) el orden de los servicios ─────────────────────────────────────────
C_VIEJO = '''                     for s in todos("""select id, nombre, duracion from servicios
                                        where activo order by nombre""")'''
C_NUEVO = '''                     for s in todos("""select s.id, s.nombre, s.duracion
                                         from servicios s
                                         left join citas c on c.servicio_id = s.id
                                        where s.activo
                                        group by s.id, s.nombre, s.duracion
                                        /* Los mas pedidos primero: para
                                           encontrar «Toxina - Botox» habia que
                                           bajar 27 fichas en una tablet. */
                                        order by count(c.id) desc, s.nombre""")'''

# ── d) el subtitulo de la pantalla de la cita ────────────────────────────
D_VIEJO = '''  v.appendChild(titulo("Usted ya tiene una cita " + c.cuando,
    "Escoja qué desea hacer"));'''
D_NUEVO = '''  /* El subtítulo dice QUÉ cita es —servicio, día y hora— en vez de «Escoja
     qué desea hacer», que ya se entiende por los botones de abajo. */
  v.appendChild(titulo("Usted ya tiene una cita " + c.cuando,
    [c.servicio, c.fecha_larga, c.hora_larga].filter(Boolean).join(" · ")));'''

# ── e) «Me da igual» al final ────────────────────────────────────────────
E_VIEJO = '''  var rej = h("div",{class:"rejilla c2"});
  rej.appendChild(h("button",{class:"opcion", onclick:function(){ escoger(null); }},
    h("span",{class:"t"},"Me da igual"),
    h("span",{class:"d"},"La primera disponible")));
  S.libres.forEach(function(e){
    rej.appendChild(h("button",{class:"opcion", onclick:function(){ escoger(e); }},
      h("span",{class:"t"}, e.nombre),
      h("span",{class:"d"},"Disponible a esa hora")));
  });
  v.appendChild(rej);
}'''
E_NUEVO = '''  var rej = h("div",{class:"rejilla c2"});
  S.libres.forEach(function(e){
    rej.appendChild(h("button",{class:"opcion", onclick:function(){ escoger(e); }},
      h("span",{class:"t"}, e.nombre),
      h("span",{class:"d"},"Disponible a esa hora")));
  });
  /* «Me da igual» va AL FINAL: quien tiene una especialista de confianza la
     buscaba abajo, y antes salía arriba de todo. */
  rej.appendChild(h("button",{class:"opcion", onclick:function(){ escoger(null); }},
    h("span",{class:"t"},"Me da igual"),
    h("span",{class:"d"},"La primera disponible")));
  v.appendChild(rej);
}'''

def aplicar(ruta, pares, binario=False):
    if binario:
        raw = open(ruta, "rb").read()
        shutil.copy2(ruta, ruta + ".pre-hallazgos.bak")
        for viejo, nuevo, etq in pares:
            vb, nb = viejo.encode("utf-8"), nuevo.encode("utf-8")
            n = raw.count(vb)
            print("   %-46s %s" % (etq, "1 ok" if n == 1 else "ABORTO: %d" % n))
            if n != 1: raise SystemExit(1)
            raw = raw.replace(vb, nb)
        open(ruta, "wb").write(raw)
    else:
        s = io.open(ruta, encoding="utf-8").read()
        shutil.copy2(ruta, ruta + ".pre-hallazgos.bak")
        for viejo, nuevo, etq in pares:
            n = s.count(viejo)
            print("   %-46s %s" % (etq, "1 ok" if n == 1 else "ABORTO: %d" % n))
            if n != 1: raise SystemExit(1)
            s = s.replace(viejo, nuevo)
        io.open(ruta, "w", encoding="utf-8", newline="").write(s)

print("=== servidor (c: el orden de los servicios) ===")
aplicar(PY, [(C_VIEJO, C_NUEVO, "servicios: los mas pedidos primero")])

print("\n=== panel (d y e) ===")
aplicar(HT, [(D_VIEJO, D_NUEVO, "cita: subtitulo con servicio, dia y hora"),
             (E_VIEJO, E_NUEVO, "especialista: «Me da igual» al final")], binario=True)

print("\n=== verificacion ===")
r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-m", "py_compile", PY],
                   capture_output=True, text=True)
print("   servidor compila:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-400:])
import re
h = io.open(HT, encoding="utf-8", errors="replace").read()
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", h, re.S | re.I)
io.open("/tmp/chk_h.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk_h.js"], capture_output=True, text=True)
print("   JS del panel:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-400:])
