#!/usr/bin/env python3
"""El cupo apartado deja de echarle la culpa a otro.

1) El panel manda el id de SU PROPIA reserva -> si es la suya, se reusa (antes
   decia "alguien mas esta tomando esa hora", falso).
2) El servidor devuelve los SEGUNDOS que le quedan (calculados por Postgres).
3) El panel avisa "le guardamos esta hora 2:00" y, si se le vence, dice la
   verdad y le ofrece guardarsela otra vez.
"""
import io, shutil, subprocess, sys

PY = "/root/universo/agenda/autoservicio.py"
HT = "/var/www/html/autoservicio.html"

# ══════════════════════ 1. EL .py (el servidor) ═══════════════════════════
P1_VIEJO = '''    especialista: Optional[str] = None      # vacío = "me da igual"
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet'''
P1_NUEVO = '''    especialista: Optional[str] = None      # vacío = "me da igual"
    mio: Optional[str] = None    # la reserva que YA tiene apartada ella misma
    k: Optional[str] = None
    t: Optional[str] = None      # la llave de esta tablet'''

P2_VIEJO = '''        exigir_que_lo_haga(esp, req.servicio)
        r = uno("""select * from apartar_cupo(p_especialista=>%s, p_sede=>%s,
                        p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                        p_minutos=>%s, p_referencia=>%s, p_canal=>%s)""",
                (esp, sid, req.fecha[:10], req.hora[:5], req.servicio,
                 MIN_RESERVA, "autoservicio", CANAL), "No se pudo apartar")'''
P2_NUEVO = '''        exigir_que_lo_haga(esp, req.servicio)
        # Si esa hora ya la tiene apartada ELLA MISMA, no es que "alguien mas
        # la este tomando": se le devuelve la suya. Antes esto salia con un
        # mensaje falso que la asustaba y la mandaba a escoger otra hora sin
        # ninguna necesidad.
        r = None
        if req.mio:
            ya = todos("""select id, expira_en from reservas
                           where id=%s and especialista_id=%s and fecha=%s
                             and inicio=%s and expira_en > now()""",
                       (req.mio, esp, req.fecha[:10], req.hora[:5]))
            if ya:
                r = ya[0]
        if r is None:
            r = uno("""select * from apartar_cupo(p_especialista=>%s, p_sede=>%s,
                            p_fecha=>%s, p_inicio=>%s, p_servicio=>%s,
                            p_minutos=>%s, p_referencia=>%s, p_canal=>%s)""",
                    (esp, sid, req.fecha[:10], req.hora[:5], req.servicio,
                     MIN_RESERVA, "autoservicio", CANAL), "No se pudo apartar")'''

P3_VIEJO = '''    return {"ok": True, "reserva": str(r.get("id")), "especialista": esp,
            "expira_en": str(r.get("expira_en"))}'''
P3_NUEVO = '''    # Los segundos que le quedan los calcula Postgres: expira_en viene SIN zona
    # y si los contara el navegador le sumaria 5 horas (la trampa de siempre).
    seg = uno("""select greatest(0,
                        ceil(extract(epoch from (expira_en - now())))::int) as s
                   from reservas where id=%s""", (str(r.get("id")),), "Sin reserva")
    return {"ok": True, "reserva": str(r.get("id")), "especialista": esp,
            "expira_en": str(r.get("expira_en")), "segundos": int(seg["s"] or 0)}'''

# ══════════════════════ 2. EL HTML (el panel) ═════════════════════════════
H1_VIEJO = '''    servicio:S.servicio.id, fecha:S.fecha, hora:S.hora,
    especialista: esp ? esp.id : null
  }), function(j){
    S.reserva = j.reserva;'''
H1_NUEVO = '''    servicio:S.servicio.id, fecha:S.fecha, hora:S.hora,
    mio:S.reserva,          /* su propia reserva: si es la suya, no se queja */
    especialista: esp ? esp.id : null
  }), function(j){
    S.reserva = j.reserva;
    S.segundos = j.segundos || 0;
    S.cupoVencido = false;'''

H2_VIEJO = '''      S.especialista = elegida || {id:j.especialista, nombre:"La primera disponible"};
    }
    ir("resumen");
  });
}'''
H2_NUEVO = '''      S.especialista = elegida || {id:j.especialista, nombre:"La primera disponible"};
    }
    ir("resumen");
    arrancarRelojCupo();
  });
}'''

H3_VIEJO = '''  v.appendChild(h("div",{class:"fila fin"},
    h("button",{class:"btn plano", onclick:function(){ soltarCupo(); ir("horas"); }},
      "Cambiar algo"),
    h("button",{class:"btn pri grande", onclick: reprog ? confirmarCambio : confirmarCita},
      reprog ? "Confirmar el cambio" : "Confirmar cita")));
}'''
H3_NUEVO = '''  /* Cuánto le queda al cupo lo dice el servidor (segundos); aquí solo se
     cuenta para abajo. Si se le vence, se le dice la VERDAD: antes el panel
     decía «alguien más está tomando esa hora», que era falso — era su propio
     tiempo el que se había acabado — y la dejaba asustada y confundida. */
  v.appendChild(S.cupoVencido
    ? h("div",{class:"aviso"},
        "Se nos pasó el tiempo que le guardamos esta hora. " +
        "¿Quiere que se la guarde otra vez?")
    : h("div",{class:"aviso nota"},
        h("span",{id:"cupo-reloj"},
           "Le guardamos esta hora " + mmss(S.segundos || 0))));
  v.appendChild(h("div",{class:"fila fin"},
    h("button",{class:"btn plano", onclick:function(){ soltarCupo(); ir("horas"); }},
      "Cambiar algo"),
    S.cupoVencido
      ? h("button",{class:"btn pri grande", onclick:volverAApartar},
          "Guardármela otra vez")
      : h("button",{class:"btn pri grande", onclick: reprog ? confirmarCambio : confirmarCita},
          reprog ? "Confirmar el cambio" : "Confirmar cita")));
}

/* ── el contador del cupo apartado ─────────────────────────────────────── */
var relojCupo = null;
function mmss(s){ var m = Math.floor(s / 60), r = s % 60; return m + ":" + (r < 10 ? "0" : "") + r; }
function pararRelojCupo(){ if (relojCupo){ clearInterval(relojCupo); relojCupo = null; } }
function arrancarRelojCupo(){
  pararRelojCupo();
  relojCupo = setInterval(function(){
    if (S.paso !== "resumen" || S.cupoVencido){ pararRelojCupo(); return; }
    S.segundos = Math.max(0, (S.segundos || 0) - 1);
    var rel = $("#cupo-reloj");
    if (!rel){ pararRelojCupo(); return; }
    rel.textContent = "Le guardamos esta hora " + mmss(S.segundos);
    if (S.segundos <= 0){ pararRelojCupo(); S.cupoVencido = true; pintar(); }
  }, 1000);
}
function volverAApartar(){
  S.cupoVencido = false;
  conCarga(pedir("/api/v2/autoservicio/reservar", {
    servicio:S.servicio.id, fecha:S.fecha, hora:S.hora, mio:S.reserva,
    especialista:S.especialista ? S.especialista.id : null
  }), function(j){
    S.reserva = j.reserva; S.segundos = j.segundos || 0;
    pintar(); arrancarRelojCupo();
  });
}'''

H4_VIEJO = '''function ir(paso){
  S.paso = paso; S.error = "";'''
H4_NUEVO = '''function ir(paso){
  if (paso !== "resumen") pararRelojCupo();
  S.paso = paso; S.error = "";'''

def aplicar(ruta, pares, binario=False):
    if binario:
        raw = open(ruta, "rb").read()
        shutil.copy2(ruta, ruta + ".pre-cupo-leal.bak")
        for viejo, nuevo, etq in pares:
            vb, nb = viejo.encode("utf-8"), nuevo.encode("utf-8")
            n = raw.count(vb)
            print("   %-52s %s" % (etq, "1 ok" if n == 1 else "ABORTO: %d" % n))
            if n != 1:
                raise SystemExit(1)
            raw = raw.replace(vb, nb)
        open(ruta, "wb").write(raw)
    else:
        s = io.open(ruta, encoding="utf-8").read()
        shutil.copy2(ruta, ruta + ".pre-cupo-leal.bak")
        for viejo, nuevo, etq in pares:
            n = s.count(viejo)
            print("   %-52s %s" % (etq, "1 ok" if n == 1 else "ABORTO: %d" % n))
            if n != 1:
                raise SystemExit(1)
            s = s.replace(viejo, nuevo)
        io.open(ruta, "w", encoding="utf-8", newline="").write(s)
    print("   respaldo:", ruta + ".pre-cupo-leal.bak")

print("=== 1. servidor (autoservicio.py) ===")
aplicar(PY, [(P1_VIEJO, P1_NUEVO, "ReservaReq: acepta `mio`"),
             (P2_VIEJO, P2_NUEVO, "reservar: reusa su propia reserva"),
             (P3_VIEJO, P3_NUEVO, "respuesta: manda `segundos`")])

print("\n=== 2. panel (autoservicio.html) ===")
aplicar(HT, [(H1_VIEJO, H1_NUEVO, "escoger: manda mio + guarda segundos"),
             (H2_VIEJO, H2_NUEVO, "escoger: arranca el contador"),
             (H3_VIEJO, H3_NUEVO, "resumen: aviso + boton de volver a apartar"),
             (H4_VIEJO, H4_NUEVO, "ir(): para el contador al salir")], binario=True)

print("\n=== 3. verificacion ===")
r = subprocess.run(["/root/universo/agenda/venv/bin/python", "-m", "py_compile", PY],
                   capture_output=True, text=True)
print("   servidor compila:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-400:])
h = io.open(HT, encoding="utf-8", errors="replace").read()
import re
bloques = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", h, re.S | re.I)
io.open("/tmp/chk_cupo.js", "w", encoding="utf-8").write("\n;\n".join(bloques))
r = subprocess.run(["node", "--check", "/tmp/chk_cupo.js"], capture_output=True, text=True)
print("   JS del panel:", "OK" if r.returncode == 0 else "MAL " + r.stderr[-400:])
print("   bytes del panel:", len(h.encode("utf-8")))
