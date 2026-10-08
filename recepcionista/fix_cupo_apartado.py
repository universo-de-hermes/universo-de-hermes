#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
La cita NUNCA se creaba: «CUPO_APARTADO: Otra persona está tomando esa hora».

La cadena:
  1. Pepe aparta la hora con `apartar_hora` -> se crea una reserva viva.
  2. Pepe llama a `agendar_cita` y NO manda el id de la reserva.
  3. La funcion `agendar_cita` de Postgres revisa las reservas vivas y, como
     `p_reserva` viene nulo, ve la reserva de Pepe MISMO como si fuera de
     otra conversacion -> levanta CUPO_APARTADO.
  4. La cita no se crea nunca.

Por que no manda el id: es la trampa de siempre — el modelo NO ve los
resultados de sus herramientas entre mensajes, asi que no puede acordarse de
un id que le devolvieron dos turnos antes.

Arreglo: la reserva se BUSCA sola por la referencia (el telefono con el que
se aparto), que es un dato que la herramienta si tiene.

  1. agenda_api.py    - endpoint GET /cupos/vigente
  2. agenda_helper.py - agendar() busca la reserva si no se la mandan
  3. herramientas.py  - le pasa la referencia del cliente al agendar
"""
import os
import shutil

BASE = "/root/universo/recepcionista"
AGA = "/root/universo/agenda"
CAMBIOS = []
CRLF = {}


def leer(p):
    with open(p, encoding="utf-8", newline="") as f:
        bruto = f.read()
    CRLF[p] = "\r\n" in bruto
    if CRLF[p]:
        print("  (aviso) %s usa CRLF" % os.path.basename(p))
    return bruto.replace("\r\n", "\n")


def escribir(p, t):
    if CRLF.get(p):
        t = t.replace("\n", "\r\n")
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(t)


def respaldar(p, marca):
    b = p + marca
    if not os.path.exists(b):
        shutil.copy2(p, b)
        print("  respaldo: %s" % os.path.basename(b))


def cambiar(t, viejo, nuevo, etiqueta):
    if t.count(viejo) != 1:
        raise SystemExit("  X '%s' aparece %d veces" % (etiqueta, t.count(viejo)))
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)
    return t.replace(viejo, nuevo)


# ══════════════════════════════════════════ 1. agenda_api.py (el endpoint) ══
API = os.path.join(AGA, "agenda_api.py")
print("\n== agenda_api.py ==")
t = leer(API)
respaldar(API, ".pre-cupo-vigente.bak")

NUEVO_EP = '''@r.get("/cupos/vigente")
def cupos_vigente(referencia: str, fecha: str = None, inicio: str = None):
    """La reserva VIVA de este cliente para ese día.

    Existe porque quien agenda no siempre manda el id de la reserva que acaba
    de apartar (un modelo no recuerda los resultados de sus herramientas
    entre mensajes). Sin esto, `agendar_cita` ve esa misma reserva como si
    fuera de otra conversación y responde CUPO_APARTADO: la cita nunca se
    crea. Se busca por `referencia`, que es un dato que sí se tiene.
    """
    filas = todos("""select id, to_char(inicio, 'HH24:MI') as inicio,
                            to_char(fecha, 'YYYY-MM-DD') as fecha
                       from reservas
                      where referencia = %s and expira_en > now()
                        and (%s is null or fecha = %s::date)
                      order by expira_en desc""",
                  (referencia, fecha, fecha))
    if not filas:
        return {}
    if inicio:
        for f in filas:
            if str(f.get("inicio"))[:5] == str(inicio)[:5]:
                return f
    return filas[0]


@r.delete("/cupos/{reserva}")'''

t = cambiar(t, '@r.delete("/cupos/{reserva}")', NUEVO_EP,
            "endpoint GET /cupos/vigente")
escribir(API, t)


# ══════════════════════════════════════ 2. agenda_helper.py (busca sola) ════
AH = os.path.join(BASE, "agenda_helper.py")
print("\n== agenda_helper.py ==")
t = leer(AH)
respaldar(AH, ".pre-cupo-vigente.bak")

t = cambiar(t, '''                  canal: str = "Agente IA", por: str = "Pepe") -> dict:
    if not especialista_id:
        rl = await especialista_libre(sede_id, servicio_id, fecha, hora)
        if not rl["ok"]:
            return rl
        especialista_id = rl["especialista_id"]
    cuerpo = {"cliente_id": cliente_id, "especialista": especialista_id,''',
'''                  canal: str = "Agente IA", por: str = "Pepe",
                  referencia: str = "") -> dict:
    if not especialista_id:
        rl = await especialista_libre(sede_id, servicio_id, fecha, hora)
        if not rl["ok"]:
            return rl
        especialista_id = rl["especialista_id"]
    if not reserva and referencia:
        # La reserva que el mismo aparto bloquea la cita si no se manda: la
        # funcion de Postgres la ve como de otra conversacion y responde
        # CUPO_APARTADO. Como el id no se puede recordar, se busca aqui por
        # la referencia (el telefono con el que se aparto).
        rv = await _llamar("GET", "/cupos/vigente",
                           params={"referencia": referencia, "fecha": fecha,
                                   "inicio": hora})
        if rv["ok"] and (rv["datos"] or {}).get("id"):
            reserva = rv["datos"]["id"]
    cuerpo = {"cliente_id": cliente_id, "especialista": especialista_id,''',
            "agendar() busca la reserva por referencia")
escribir(AH, t)


# ═════════════════════════════ 3. herramientas.py (pasa la referencia) ══════
HR = os.path.join(BASE, "herramientas.py")
print("\n== herramientas.py ==")
t = leer(HR)
respaldar(HR, ".pre-cupo-vigente.bak")

t = cambiar(t, '''                servicio_id=rc["servicio_id"], notas=a.get("notas", ""),
                reserva=a.get("reserva"))''',
'''                servicio_id=rc["servicio_id"], notas=a.get("notas", ""),
                reserva=a.get("reserva"),
                referencia=ctx.get("telefono", ""))''',
            "agendar_cita pasa la referencia del cliente")
escribir(HR, t)

print("\n%d cambios aplicados." % len(CAMBIOS))
