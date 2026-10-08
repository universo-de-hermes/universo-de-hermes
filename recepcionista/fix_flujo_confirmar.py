#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flujo riguroso: confirmar sin inventarse ids + regla de auto-confirmado +
la tarjeta del CRM se mueve a Agendado.

1. confirmar_cita / cancelar_cita / reprogramar_cita ya NO exigen cita_id:
   basta la cédula del cliente y la herramienta busca su cita. Era el fallo de
   «Confirmo» → «la cita ya no existe» (el modelo se inventaba el id).

2. Regla de CJ Medical: una cita para HOY o MAÑANA queda CONFIRMADA sola; de
   pasado mañana en adelante queda PENDIENTE esperando que el cliente confirme.

3. La tarjeta del CRM se mueve a la columna «Agendados» apenas la cita queda
   puesta (antes se quedaba en «Leads Nuevos» para siempre).

4. El mensaje de rescate ya no manda al cliente donde un asesor por un fallo
   técnico.
"""
import io
import sys

BASE = "/root/universo/recepcionista/"


def leer(ruta):
    t = io.open(ruta, "r", encoding="utf-8", newline="").read()
    crlf = "\r\n" in t
    return t.replace("\r\n", "\n"), crlf


def escribir(ruta, texto, crlf):
    if crlf:
        texto = texto.replace("\n", "\r\n")
    io.open(ruta, "w", encoding="utf-8", newline="").write(texto)


def aplicar(ruta, cambios, etiqueta):
    txt, crlf = leer(ruta)
    for i, (viejo, nuevo) in enumerate(cambios, 1):
        n = txt.count(viejo)
        if n != 1:
            print("ABORTO en %s cambio %d: %d coincidencia(s)" % (etiqueta, i, n))
            print("--- buscaba ---")
            print(viejo[:400])
            sys.exit(1)
        txt = txt.replace(viejo, nuevo)
    escribir(ruta, txt, crlf)
    print("%s: %d cambio(s)" % (etiqueta, len(cambios)))


# ═══════════ 1) agenda_helper: encontrar la cita del cliente ════════════════
aplicar(BASE + "agenda_helper.py", [(
    '# ─────────────────────────────────────────────────────── horas y citas ────',
    'async def cita_del_cliente(cliente_id: str, fecha: str = None,\n'
    '                           hora: str = None) -> dict:\n'
    '    """La cita del cliente: la que coincida con fecha/hora, o la próxima.\n'
    '\n'
    '    Sirve para confirmar, cancelar o mover sin depender del cita_id: el\n'
    '    modelo no ve los resultados de sus herramientas entre mensajes, así que\n'
    '    no se puede confiar en que se acuerde del id.\n'
    '    """\n'
    '    r = await citas_del_cliente(cliente_id)\n'
    '    if not r["ok"]:\n'
    '        return r\n'
    '    citas = r["citas"] or []\n'
    '    if fecha:\n'
    '        del_dia = [c for c in citas if str(c.get("fecha"))[:10] == str(fecha)[:10]]\n'
    '        if del_dia:\n'
    '            citas = del_dia\n'
    '    if hora:\n'
    '        con_hora = [c for c in citas if str(c.get("inicio"))[:5] == str(hora)[:5]]\n'
    '        if con_hora:\n'
    '            citas = con_hora\n'
    '    if not citas:\n'
    '        return {"ok": False, "error": "CITA_NO_EXISTE",\n'
    '                "mensaje": "Ese cliente no tiene citas próximas."}\n'
    '    c = citas[0]\n'
    '    return {"ok": True, "cita_id": c.get("cita_id") or c.get("id"),\n'
    '            "fecha": str(c.get("fecha"))[:10],\n'
    '            "hora": str(c.get("inicio"))[:5],\n'
    '            "servicio": c.get("servicio"), "sede": c.get("sede"),\n'
    '            "especialista": c.get("especialista"),\n'
    '            "estado": c.get("estado")}\n'
    '\n'
    '\n'
    '# ─────────────────────────────────────────────────────── horas y citas ────'
)], "agenda_helper.py")

# ═══════════ 2) herramientas: resolvers + schemas + dispatcher ══════════════
aplicar(BASE + "herramientas.py", [
    # import de time
    ('import json\n\nimport agenda_helper as ag',
     'import json\nimport time\n\nimport agenda_helper as ag'),
    # helper de dias
    ('_ID_PREFIJO = {"especialista": "esp-", "sede": "sede-", "servicio": "srv-"}',
     '_ID_PREFIJO = {"especialista": "esp-", "sede": "sede-", "servicio": "srv-"}\n'
     '\n'
     '\n'
     'def _dias_hasta(fecha) -> int:\n'
     '    """Días que faltan de hoy a esa fecha (AAAA-MM-DD). None si no se\n'
     '    entiende. Se ancla a las 12:00 para que el cambio de hora no corra\n'
     '    el día."""\n'
     '    try:\n'
     '        f = time.strptime(str(fecha)[:10], "%Y-%m-%d")\n'
     '    except Exception:\n'
     '        return None\n'
     '    h = time.localtime()\n'
     '    d1 = time.mktime((h.tm_year, h.tm_mon, h.tm_mday, 12, 0, 0, 0, 0, -1))\n'
     '    d2 = time.mktime((f.tm_year, f.tm_mon, f.tm_mday, 12, 0, 0, 0, 0, -1))\n'
     '    return int(round((d2 - d1) / 86400))'),
    # resolver del cita_id
    ('async def _resolver_cliente(a: dict, ctx: dict) -> dict:',
     'async def _resolver_cita_id(a: dict, ctx: dict) -> dict:\n'
     '    """El cita_id, o la cita del cliente que coincida con fecha/hora.\n'
     '\n'
     '    El modelo no ve los resultados de sus herramientas entre mensajes: si\n'
     '    se le pide el cita_id, se lo inventa. Por eso se resuelve aquí.\n'
     '    """\n'
     '    cid = str(a.get("cita_id") or "").strip()\n'
     '    if cid.startswith("c-"):\n'
     '        return {"ok": True, "cita_id": cid}\n'
     '    rcl = await _resolver_cliente(a, ctx)\n'
     '    if not rcl["ok"]:\n'
     '        return rcl\n'
     '    r = await ag.cita_del_cliente(rcl["cliente_id"],\n'
     '                                  fecha=a.get("cita_fecha") or a.get("fecha"),\n'
     '                                  hora=a.get("cita_hora") or a.get("hora"))\n'
     '    if not r["ok"]:\n'
     '        return r\n'
     '    return {"ok": True, "cita_id": r["cita_id"]}\n'
     '\n'
     '\n'
     'async def _resolver_cliente(a: dict, ctx: dict) -> dict:'),
    # schema confirmar_cita
    ('        "name": "confirmar_cita",\n'
     '        "description": (\n'
     '            "Pasa la cita de Pendiente a Confirmado. Se llama cuando el cliente "\n'
     '            "responde que sí va, después de que le mandaste el mensaje de cita "\n'
     '            "agendada. Toda cita nace en Pendiente: solo la confirmación del "\n'
     '            "cliente la mueve."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "cita_id": {"type": "string"}}, "required": ["cita_id"]}}},',
     '        "name": "confirmar_cita",\n'
     '        "description": (\n'
     '            "Pasa la cita de Pendiente a Confirmado. Se llama cuando el cliente "\n'
     '            "responde que sí va. Basta con la CÉDULA del cliente: la "\n'
     '            "herramienta busca su cita sola. Si el cliente tiene varias citas "\n'
     '            "próximas, manda también la fecha o la hora de la que confirma."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "cita_id": {"type": "string", "description": "Opcional, si lo tienes."},\n'
     '            "documento": {"type": "string", "description": "Cédula del cliente."},\n'
     '            "telefono": {"type": "string", "description": "Celular, si no hay cédula."},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD, si tiene varias citas."},\n'
     '            "hora": {"type": "string", "description": "HH:MM, si tiene varias citas."}},\n'
     '            "required": []}}},'),
    # schema cancelar_cita
    ('        "name": "cancelar_cita",\n'
     '        "description": (\n'
     '            "Cancela y libera la hora al instante para que otro la tome. "\n'
     '            "Se pregunta el motivo antes, con cariño, no como interrogatorio."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "cita_id": {"type": "string"},\n'
     '            "motivo": {"type": "string"}}, "required": ["cita_id"]}}},',
     '        "name": "cancelar_cita",\n'
     '        "description": (\n'
     '            "Cancela y libera la hora al instante para que otro la tome. "\n'
     '            "Se pregunta el motivo antes, con cariño, no como interrogatorio. "\n'
     '            "Basta con la CÉDULA del cliente: la herramienta busca su cita."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "cita_id": {"type": "string", "description": "Opcional, si lo tienes."},\n'
     '            "documento": {"type": "string", "description": "Cédula del cliente."},\n'
     '            "telefono": {"type": "string"},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD, si tiene varias citas."},\n'
     '            "hora": {"type": "string", "description": "HH:MM, si tiene varias citas."},\n'
     '            "motivo": {"type": "string"}}, "required": []}}},'),
    # schema reprogramar_cita
    ('        "name": "reprogramar_cita",\n'
     '        "description": (\n'
     '            "Mueve la cita a otra fecha u hora. La anterior queda marcada como "\n'
     '            "reprogramada, no se borra. Primero hay que mirar horas libres."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "cita_id": {"type": "string"},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD"},',
     '        "name": "reprogramar_cita",\n'
     '        "description": (\n'
     '            "Mueve la cita a otra fecha u hora. La anterior queda marcada como "\n'
     '            "reprogramada, no se borra. Primero hay que mirar horas libres. "\n'
     '            "Basta con la CÉDULA del cliente: la herramienta busca su cita. "\n'
     '            "OJO: aquí «fecha» y «hora» son las NUEVAS, no las de la cita "\n'
     '            "actual."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "cita_id": {"type": "string", "description": "Opcional, si lo tienes."},\n'
     '            "documento": {"type": "string", "description": "Cédula del cliente."},\n'
     '            "telefono": {"type": "string"},\n'
     '            "cita_fecha": {"type": "string",\n'
     '                           "description": "La fecha que tiene hoy la cita, si tiene varias."},\n'
     '            "cita_hora": {"type": "string",\n'
     '                          "description": "La hora que tiene hoy la cita, si tiene varias."},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD (la nueva)"},'),
    # dispatcher: confirmar
    ('        if nombre == "confirmar_cita":\n'
     '            return await ag.confirmar(a["cita_id"])',
     '        if nombre == "confirmar_cita":\n'
     '            r = await _resolver_cita_id(a, ctx)\n'
     '            if not r["ok"]:\n'
     '                return r\n'
     '            return await ag.confirmar(r["cita_id"])'),
    # dispatcher: cancelar
    ('        if nombre == "cancelar_cita":\n'
     '            return await ag.cancelar(a["cita_id"], a.get("motivo", ""))',
     '        if nombre == "cancelar_cita":\n'
     '            r = await _resolver_cita_id(a, ctx)\n'
     '            if not r["ok"]:\n'
     '                return r\n'
     '            return await ag.cancelar(r["cita_id"], a.get("motivo", ""))'),
    # dispatcher: reprogramar
    ('            return await ag.reprogramar(\n'
     '                cita_id=a["cita_id"], fecha=a["fecha"], hora=a["hora"],',
     '            rcid = await _resolver_cita_id(a, ctx)\n'
     '            if not rcid["ok"]:\n'
     '                return rcid\n'
     '            return await ag.reprogramar(\n'
     '                cita_id=rcid["cita_id"], fecha=a["fecha"], hora=a["hora"],'),
    # dispatcher: agendar + auto-confirmado
    ('            return await ag.agendar(\n'
     '                cliente_id=rcl["cliente_id"],\n'
     '                especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],\n'
     '                fecha=a["fecha"], hora=a["hora"],\n'
     '                servicio_id=rc["servicio_id"], notas=a.get("notas", ""),\n'
     '                reserva=a.get("reserva"))',
     '            r = await ag.agendar(\n'
     '                cliente_id=rcl["cliente_id"],\n'
     '                especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],\n'
     '                fecha=a["fecha"], hora=a["hora"],\n'
     '                servicio_id=rc["servicio_id"], notas=a.get("notas", ""),\n'
     '                reserva=a.get("reserva"))\n'
     '            if not r.get("ok"):\n'
     '                return r\n'
     '            # Regla de CJ Medical: si la cita es para hoy o para mañana queda\n'
     '            # CONFIRMADA sola; de pasado mañana en adelante queda PENDIENTE\n'
     '            # esperando que el cliente confirme.\n'
     '            dias = _dias_hasta(a.get("fecha"))\n'
     '            if dias is not None and 0 <= dias <= 1:\n'
     '                rc2 = await ag.confirmar(r["cita_id"])\n'
     '                if rc2.get("ok"):\n'
     '                    r["estado"] = rc2.get("estado")\n'
     '                    r["confirmada_sola"] = True\n'
     '                    r["nota"] = ("Quedó CONFIRMADA sola porque es para hoy o "\n'
     '                                 "para mañana: dile que ya está confirmada y "\n'
     '                                 "que lo esperamos. NO le pidas que confirme.")\n'
     '                else:\n'
     '                    r["nota"] = ("Quedó en Pendiente. Pídele que confirme su "\n'
     '                                 "asistencia.")\n'
     '            else:\n'
     '                r["nota"] = ("Quedó PENDIENTE porque es de pasado mañana en "\n'
     '                             "adelante: pídele que confirme su asistencia.")\n'
     '            return r'),
    # prompt: pasos 8 y 9
    ('8. MANDA LA CONFIRMACIÓN. Apenas quede agendada, escríbele el detalle de la\n'
     '   cita: servicio, fecha, hora, sede y especialista, y pídele que confirme su\n'
     '   asistencia. La cita nace en estado PENDIENTE.\n'
     '\n'
     '9. CUANDO EL CLIENTE CONFIRME, muévela a CONFIRMADO. Si responde que sí va\n'
     '   —«confirmo», «allá estaré», «sí señor»—, llama a confirmar_cita y recién ahí\n'
     '   dile:\n'
     '\n'
     '   «Qué bien, [nombre]. Su cita de [servicio] para el [fecha] a las [hora] en\n'
     '   [sede] ha sido confirmada. Te esperamos. Si necesitas agendar otro servicio\n'
     '   o tienes alguna duda, estoy aquí para ayudarte.»\n'
     '\n'
     '   Toda cita se queda en Pendiente mientras el cliente no confirme. No la des\n'
     '   por confirmada tú solo.',
     '8. MANDA LA CONFIRMACIÓN. Apenas quede agendada, escríbele el detalle de la\n'
     '   cita: servicio, fecha, hora, sede y especialista. El estado depende de la\n'
     '   fecha, y esto lo hace la herramienta sola:\n'
     '\n'
     '   - Si es para HOY o para MAÑANA: queda CONFIRMADA automáticamente. Dile que\n'
     '     ya quedó confirmada y que lo esperamos. NO le pidas que confirme.\n'
     '   - Si es de PASADO MAÑANA en adelante: queda PENDIENTE. Pídele que confirme\n'
     '     su asistencia.\n'
     '\n'
     '9. CUANDO EL CLIENTE CONFIRME, muévela a CONFIRMADO. Si responde que sí va\n'
     '   —«confirmo», «allá estaré», «sí señor»—, llama a confirmar_cita con la\n'
     '   CÉDULA del cliente (la herramienta busca su cita sola) y recién ahí dile:\n'
     '\n'
     '   «Qué bien, [nombre]. Su cita de [servicio] para el [fecha] a las [hora] en\n'
     '   [sede] ha sido confirmada. Te esperamos. Si necesitas agendar otro servicio\n'
     '   o tienes alguna duda, estoy aquí para ayudarte.»\n'
     '\n'
     '   Una cita de pasado mañana en adelante se queda en Pendiente mientras el\n'
     '   cliente no confirme. No la des por confirmada tú solo.')
], "herramientas.py")

# ═══════════ 3) main.py: la tarjeta del CRM + mensaje de rescate ════════════
aplicar(BASE + "main.py", [(
    '            logger.info(f"🔧 {tc.function.name} → {str(resultado)[:160]}")\n'
    '            messages.append({"role": "tool", "tool_call_id": tc.id,',
    '            logger.info(f"🔧 {tc.function.name} → {str(resultado)[:160]}")\n'
    '            # La tarjeta del CRM se mueve a «Agendados» apenas la cita queda\n'
    '            # puesta: antes el cliente se quedaba en «Leads Nuevos» para siempre.\n'
    '            if (tc.function.name == "agendar_cita" and client_id\n'
    '                    and isinstance(resultado, dict) and resultado.get("ok")):\n'
    '                try:\n'
    '                    update_client_status(client_id, "agendado", "Pepe Bot",\n'
    '                                         "Cita agendada en la agenda")\n'
    '                    logger.info(f"📊 Cliente {client_id} → Agendado en el CRM")\n'
    '                except Exception as e:\n'
    '                    logger.warning(f"No pude mover el cliente a agendado: {e}")\n'
    '            messages.append({"role": "tool", "tool_call_id": tc.id,'
), (
    '    return ("Déjame confirmar un detalle y te escribo en un momento. Si prefieres, "\n'
    '            "escribe /asesor para hablar con una persona del equipo.")',
    '    # Sin salida tras 4 vueltas: es un fallo técnico NUESTRO, no una razón\n'
    '    # para mandarle el cliente a un asesor.\n'
    '    return ("Perdón, se me enredó algo por acá. ¿Me repites lo último que me "\n'
    '            "dijiste? Ya casi dejamos tu cita lista.")'
)], "main.py")

print()
import py_compile
for f in ("agenda_helper.py", "herramientas.py", "main.py"):
    py_compile.compile(BASE + f, doraise=True)
    print("  sintaxis OK:", f)