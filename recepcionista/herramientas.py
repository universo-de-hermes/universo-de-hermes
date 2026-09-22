"""
Las manos de Pepe: las herramientas con las que agenda de verdad.

Formato de function calling de OpenAI, que es con lo que corre hoy
(`gpt-4o-mini` vía `ai_client`). Si algún día vuelve Claude, las mismas
definiciones sirven cambiando "parameters" por "input_schema".

Se usa así desde main.py:

    from herramientas import HERRAMIENTAS, ejecutar, BLOQUE_PROMPT

    response = ai_client.chat.completions.create(
        model=PRIMARY_MODEL, messages=messages,
        tools=HERRAMIENTAS, tool_choice="auto", ...)

En COMO-CONECTAR-PEPE.md está el bucle completo, paso a paso.
"""
import json

import agenda_helper as ag

# ──────────────────────────────────────────────────── qué puede hacer ─────
HERRAMIENTAS = [
    {"type": "function", "function": {
        "name": "buscar_cliente",
        "description": (
            "Busca la ficha del cliente en la agenda. Primero se busca por el "
            "teléfono desde el que escribe (eso va solo). Antes de pedirle "
            "datos, búscalo por la CÉDULA: si ya existe, se le muestran sus "
            "datos y NO se le vuelven a pedir. El documento manda sobre el "
            "teléfono. Devuelve la ficha completa (nombre, documento, "
            "teléfono y correo)."),
        "parameters": {"type": "object", "properties": {
            "documento": {"type": "string",
                          "description": "Cédula, solo números. Es lo más confiable."},
            "telefono": {"type": "string",
                         "description": "Con o sin indicativo; da igual el formato."},
            "nombre": {"type": "string",
                       "description": "Solo si no tiene documento ni teléfono."}},
            "required": []}}},

    {"type": "function", "function": {
        "name": "actualizar_cliente",
        "description": (
            "Corrige los datos de un cliente que YA existe. Se usa solo "
            "cuando, después de mostrarle su ficha, el cliente dice que algo "
            "está mal o quiere cambiarlo. Manda solo los campos que cambian."),
        "parameters": {"type": "object", "properties": {
            "cliente_id": {"type": "string",
                           "description": "El que devolvió buscar_cliente."},
            "primer_nombre": {"type": "string"},
            "segundo_nombre": {"type": "string"},
            "primer_apellido": {"type": "string"},
            "segundo_apellido": {"type": "string"},
            "telefono": {"type": "string"},
            "correo": {"type": "string"}},
            "required": ["cliente_id"]}}},

    {"type": "function", "function": {
        "name": "registrar_cliente",
        "description": (
            "Crea la ficha de un cliente nuevo. Solo cuando la búsqueda por "
            "teléfono no encontró a nadie. Si el documento ya existe, no "
            "duplica: devuelve la ficha que había."),
        "parameters": {"type": "object", "properties": {
            "documento": {"type": "string", "description": "Cédula, solo números."},
            "primer_nombre": {"type": "string"},
            "primer_apellido": {"type": "string"},
            "telefono": {"type": "string"},
            "correo": {"type": "string"}},
            "required": ["documento", "primer_nombre", "primer_apellido", "telefono"]}}},

    {"type": "function", "function": {
        "name": "ver_horas_libres",
        "description": (
            "Las horas realmente disponibles. Ya descuenta el horario de cada "
            "especialista, el almuerzo, las citas tomadas y los cupos apartados, "
            "y ya respeta lo que dura el servicio. Devuelve las horas cada 30 "
            "minutos (en punto o y media), que es como agenda CJ Medical. "
            "NUNCA ofrezcas una hora que no venga de aquí. Sin fecha, busca en "
            "los próximos días."),
        "parameters": {"type": "object", "properties": {
            "servicio": {"type": "string",
                         "description": "Como lo dijo el cliente: «depilación láser zona M», «botox»…"},
            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro» (Medellín)."},
            "fecha": {"type": "string",
                      "description": "AAAA-MM-DD si el cliente pidió un día puntual. Si no, omitir."},
            "dias": {"type": "integer",
                     "description": "Cuántos días mirar cuando no hay fecha. Por defecto 7."},
            "especialista": {"type": "string",
                             "description": "Solo si el cliente pidió a alguien en particular."}},
            "required": ["servicio", "sede"]}}},

    {"type": "function", "function": {
        "name": "ver_agenda_especialista",
        "description": (
            "Mira la agenda de UNA especialista: si trabaja ese día, su "
            "horario (con el almuerzo) y sus horas libres reales. Se usa "
            "cuando el cliente pregunta por alguien puntual («¿Valentina "
            "trabaja el lunes?», «quiero con Valentina»). Si no le das fecha, "
            "revisa los próximos días y te dice cuáles trabaja. NUNCA digas "
            "si alguien trabaja o no sin haber llamado esta herramienta."),
        "parameters": {"type": "object", "properties": {
            "especialista": {"type": "string",
                             "description": "Como lo dijo el cliente: «Valentina», «Dra. Arias»."},
            "fecha": {"type": "string",
                      "description": "AAAA-MM-DD si preguntó por un día puntual."},
            "dias": {"type": "integer",
                     "description": "Cuántos días revisar cuando no hay fecha. Por defecto 7."},
            "servicio": {"type": "string",
                         "description": "Solo si ya se sabe qué servicio quiere."},
            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro»."}},
            "required": ["especialista"]}}},

    {"type": "function", "function": {
        "name": "apartar_hora",
        "description": (
            "Aparta la hora por unos minutos mientras terminan de hablar. Se "
            "llama APENAS el cliente diga que le sirve una hora, ANTES de "
            "pedirle datos. Sin esto, otra conversación puede quedarse con esa "
            "hora y toca decirle que ya no está. La especialista, la sede y el "
            "servicio se pueden mandar por NOMBRE (como los dijo el cliente): "
            "no hace falta acordarse de los ids."),
        "parameters": {"type": "object", "properties": {
            "especialista": {"type": "string", "description": "«Valentina», «Dra. Arias»…"},
            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro»."},
            "servicio": {"type": "string", "description": "Como lo dijo el cliente."},
            "especialista_id": {"type": "string", "description": "Opcional, si lo tienes."},
            "sede_id": {"type": "string", "description": "Opcional."},
            "servicio_id": {"type": "string", "description": "Opcional."},
            "fecha": {"type": "string", "description": "AAAA-MM-DD"},
            "hora": {"type": "string", "description": "HH:MM"},
            "minutos": {"type": "integer", "description": "Por defecto 10."}},
            "required": ["fecha", "hora"]}}},

    {"type": "function", "function": {
        "name": "agendar_cita",
        "description": (
            "Deja la cita agendada de verdad, en estado Pendiente. NO se llama "
            "hasta haberle mostrado al cliente el resumen completo de sus datos y "
            "que él haya dicho que están correctos. Si el cupo estaba apartado, se "
            "manda la reserva para no perderlo."),
        "parameters": {"type": "object", "properties": {
            "cliente_id": {"type": "string",
                           "description": "El que devolvió buscar_cliente (opcional)."},
            "documento": {"type": "string",
                          "description": "Cédula del cliente. Sirve en vez de cliente_id."},
            "telefono": {"type": "string",
                         "description": "Celular del cliente, si no tienes el documento."},
            "especialista": {"type": "string",
                             "description": "«Valentina», «Dra. Arias»: el nombre basta."},
            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro»."},
            "servicio": {"type": "string",
                         "description": "Como lo dijo el cliente: «carbon peel»."},
            "especialista_id": {"type": "string", "description": "Opcional."},
            "sede_id": {"type": "string", "description": "Opcional."},
            "servicio_id": {"type": "string", "description": "Opcional."},
            "fecha": {"type": "string", "description": "AAAA-MM-DD"},
            "hora": {"type": "string", "description": "HH:MM"},
            "reserva": {"type": "string", "description": "La que devolvió apartar_hora."},
            "notas": {"type": "string", "description": "Lo que el cliente pidió tener en cuenta."},
            "cliente_confirmo": {"type": "boolean",
                "description": ("true SOLO si ya le mostraste el resumen completo "
                                "(ciudad, sede, servicio, fecha, hora, nombre, celular, "
                                "correo, documento) y el cliente respondió que está "
                                "correcto. Si todavía no lo has hecho, no llames esta "
                                "herramienta: muestra el resumen primero.")}},
            "required": ["fecha", "hora", "cliente_confirmo"]}}},

    {"type": "function", "function": {
        "name": "ver_citas_del_cliente",
        "description": "Las próximas citas de un cliente, para confirmarlas, moverlas o cancelarlas.",
        "parameters": {"type": "object", "properties": {
            "cliente_id": {"type": "string"}}, "required": ["cliente_id"]}}},

    {"type": "function", "function": {
        "name": "confirmar_cita",
        "description": (
            "Pasa la cita de Pendiente a Confirmado. Se llama cuando el cliente "
            "responde que sí va, después de que le mandaste el mensaje de cita "
            "agendada. Toda cita nace en Pendiente: solo la confirmación del "
            "cliente la mueve."),
        "parameters": {"type": "object", "properties": {
            "cita_id": {"type": "string"}}, "required": ["cita_id"]}}},

    {"type": "function", "function": {
        "name": "cancelar_cita",
        "description": (
            "Cancela y libera la hora al instante para que otro la tome. "
            "Se pregunta el motivo antes, con cariño, no como interrogatorio."),
        "parameters": {"type": "object", "properties": {
            "cita_id": {"type": "string"},
            "motivo": {"type": "string"}}, "required": ["cita_id"]}}},

    {"type": "function", "function": {
        "name": "reprogramar_cita",
        "description": (
            "Mueve la cita a otra fecha u hora. La anterior queda marcada como "
            "reprogramada, no se borra. Primero hay que mirar horas libres."),
        "parameters": {"type": "object", "properties": {
            "cita_id": {"type": "string"},
            "fecha": {"type": "string", "description": "AAAA-MM-DD"},
            "hora": {"type": "string", "description": "HH:MM"},
            "especialista_id": {"type": "string", "description": "Solo si cambia."},
            "sede_id": {"type": "string", "description": "Solo si cambia."},
            "motivo": {"type": "string"}},
            "required": ["cita_id", "fecha", "hora"]}}},

    {"type": "function", "function": {
        "name": "pasar_a_asesor",
        "description": (
            "Pasa la conversación a una persona del equipo. SOLO se usa en "
            "tres casos: (1) el cliente pide expresamente hablar con una "
            "persona o un asesor; (2) el cliente está molesto o pone una "
            "queja, un reclamo o una petición (PQRS); (3) el cliente insiste "
            "en algo que no puedes resolver tú (por ejemplo un pago) y además "
            "se nota molesto. NO la uses por dudas que puedas responder, ni "
            "porque una herramienta falló. Después de llamarla, se le avisa al "
            "cliente que un asesor lo va a contactar."),
        "parameters": {"type": "object", "properties": {
            "motivo": {"type": "string",
                       "enum": ["lo_pidio", "pqrs", "queja", "molesto", "pago",
                                "otro"]},
            "resumen": {"type": "string",
                        "description": "Dos o tres frases para que el asesor no empiece de cero."}},
            "required": ["motivo", "resumen"]}}},
]


# ───────────────────────────────────────────────────────── el despacho ────
MOTIVOS = {
    "lo_pidio": "El cliente pidió hablar con una persona",
    "pqrs": "PQRS",
    "queja": "Queja o reclamo",
    "no_entiende": "La conversación se enredó",
    "medico": "Consulta médica o diagnóstico",
    "pago": "Problema de pago",
    "otro": "Otro",
}


_ID_PREFIJO = {"especialista": "esp-", "sede": "sede-", "servicio": "srv-"}


async def _resolver_uno(valor, tipo: str) -> dict:
    """Devuelve {'ok', 'id'} a partir del id o del nombre."""
    v = str(valor or "").strip()
    if not v:
        return {"ok": True, "id": None}
    if v.startswith(_ID_PREFIJO.get(tipo, "\0")):
        return {"ok": True, "id": v}
    f = {"especialista": ag.resolver_especialista,
         "sede": ag.resolver_sede,
         "servicio": ag.resolver_servicio}[tipo]
    r = await f(v)
    if not r.get("ok"):
        return r
    return {"ok": True, "id": r["id"]}


async def _resolver_cita(a: dict) -> dict:
    """Especialista, sede y servicio: acepta el nombre o el id.

    El modelo no ve los resultados de sus herramientas entre mensajes, así
    que no se puede confiar en que se acuerde de los ids: se resuelven aquí.
    """
    salida = {}
    for campo, tipo, etiqueta in (("especialista", "especialista", "la especialista"),
                                  ("sede", "sede", "la sede"),
                                  ("servicio", "servicio", "el servicio")):
        r = await _resolver_uno(a.get(campo) or a.get(campo + "_id"), tipo)
        if not r.get("ok"):
            return r
        if not r.get("id"):
            return {"ok": False, "error": "FALTA_" + tipo.upper(),
                    "mensaje": "Me falta %s para agendar." % etiqueta}
        salida[campo + "_id"] = r["id"]
    return {"ok": True, **salida}


async def _resolver_cliente(a: dict, ctx: dict) -> dict:
    """cliente_id, o la cédula, o el teléfono."""
    cid = str(a.get("cliente_id") or "").strip()
    if cid.startswith("cl-"):
        return {"ok": True, "cliente_id": cid}
    documento = str(a.get("documento") or "").strip()
    telefono = str(a.get("telefono") or "").strip() or str(ctx.get("telefono") or "")
    r = await ag.buscar_cliente(telefono=telefono or None,
                                documento=documento or None)
    if not r["ok"]:
        return r
    cl = r["clientes"]
    if not cl:
        return {"ok": False, "error": "CLIENTE_NO_EXISTE",
                "mensaje": ("No encuentro al cliente en la agenda. Regístralo "
                            "primero con registrar_cliente.")}
    return {"ok": True, "cliente_id": cl[0]["id"]}


def _ficha(c: dict) -> dict:
    """La ficha del cliente como la necesita el modelo, sin ruido."""
    completo = " ".join(x for x in [c.get("primer_nombre"),
                                    c.get("segundo_nombre"),
                                    c.get("primer_apellido"),
                                    c.get("segundo_apellido")] if x)
    return {"cliente_id": c.get("id"),
            "nombre_completo": completo or c.get("documento"),
            "primer_nombre": c.get("primer_nombre"),
            "primer_apellido": c.get("primer_apellido"),
            "documento": c.get("documento"),
            "telefono": c.get("telefono"),
            "correo": c.get("correo")}


async def ejecutar(nombre: str, argumentos, contexto: dict = None) -> dict:
    """Corre la herramienta que pidió el modelo y devuelve el resultado.
    `contexto` puede traer {'telefono': …, 'escalar': callable}."""
    ctx = contexto or {}
    if isinstance(argumentos, str):
        try:
            argumentos = json.loads(argumentos or "{}")
        except Exception:
            return {"ok": False, "error": "ARGUMENTOS",
                    "mensaje": "No entendí los parámetros."}
    a = argumentos or {}

    try:
        if nombre in ("buscar_cliente", "buscar_cliente_por_telefono"):
            documento = str(a.get("documento") or "").strip()
            telefono = str(a.get("telefono") or "").strip()
            # sin documento ni telefono se usa el del chat
            if not documento and not telefono:
                telefono = ctx.get("telefono") or ""
            r = await ag.buscar_cliente(telefono=telefono or None,
                                        documento=documento or None,
                                        nombre=a.get("nombre") or None)
            if not r["ok"]:
                return r
            cl = r["clientes"]
            return {"ok": True, "encontrados": len(cl),
                    "clientes": [_ficha(c) for c in cl[:5]]}

        if nombre == "actualizar_cliente":
            r = await ag.actualizar_cliente(
                a["cliente_id"], primer_nombre=a.get("primer_nombre"),
                segundo_nombre=a.get("segundo_nombre"),
                primer_apellido=a.get("primer_apellido"),
                segundo_apellido=a.get("segundo_apellido"),
                telefono=a.get("telefono"), correo=a.get("correo"))
            if not r["ok"]:
                return r
            return {"ok": True, "actualizado": True,
                    "cliente": _ficha(r["cliente"] or {})}

        if nombre == "registrar_cliente":
            r = await ag.crear_cliente(
                documento=str(a.get("documento", "")).strip(),
                primer_nombre=a.get("primer_nombre", ""),
                primer_apellido=a.get("primer_apellido", ""),
                telefono=a.get("telefono") or ctx.get("telefono") or "",
                correo=a.get("correo", ""))
            if not r["ok"]:
                return r
            c = r["cliente"] or {}
            return {"ok": True, "cliente_id": c.get("id"),
                    "nombre": " ".join(x for x in [c.get("primer_nombre"),
                                                   c.get("primer_apellido")] if x)}

        if nombre == "ver_horas_libres":
            r = await ag.horas_libres(
                servicio=a.get("servicio", ""), sede=a.get("sede", ""),
                fecha=a.get("fecha"), dias=int(a.get("dias") or 7),
                especialista=a.get("especialista"))
            if not r["ok"]:
                return r
            # se recortan las opciones: ofrecerle 60 horas a alguien por WhatsApp
            # es peor que no ofrecerle ninguna
            dias = []
            for d in r["dias"][:5]:
                dias.append({"fecha": d["fecha"], "horas": d["horas"][:6],
                             "hay_mas": len(d["horas"]) > 6})
            return {"ok": True, "servicio": r["servicio"], "servicio_id": r["servicio_id"],
                    "sede": r["sede"], "sede_id": r["sede_id"],
                    "duracion_minutos": r["duracion"], "dias": dias,
                    "nota": "Ofrécele dos o tres, no la lista entera."}

        if nombre == "ver_agenda_especialista":
            return await ag.horario_especialista(
                especialista=a.get("especialista", ""),
                fecha=a.get("fecha"), dias=int(a.get("dias") or 7),
                sede=a.get("sede"), servicio=a.get("servicio"))

        if nombre == "apartar_hora":
            rc = await _resolver_cita(a)
            if not rc["ok"]:
                return rc
            return await ag.apartar_cupo(
                especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],
                fecha=a["fecha"], hora=a["hora"],
                servicio_id=rc["servicio_id"],
                minutos=int(a.get("minutos") or 10),
                referencia=ctx.get("telefono", ""))

        if nombre == "agendar_cita":
            if not a.get("cliente_confirmo"):
                return {"ok": False, "error": "FALTA_VALIDAR",
                        "mensaje": ("Todavía no puedes agendar: primero muéstrale al "
                                    "cliente el resumen completo de sus datos y espera "
                                    "a que responda que están correctos.")}
            rcl = await _resolver_cliente(a, ctx)
            if not rcl["ok"]:
                return rcl
            rc = await _resolver_cita(a)
            if not rc["ok"]:
                return rc
            return await ag.agendar(
                cliente_id=rcl["cliente_id"],
                especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],
                fecha=a["fecha"], hora=a["hora"],
                servicio_id=rc["servicio_id"], notas=a.get("notas", ""),
                reserva=a.get("reserva"))

        if nombre == "ver_citas_del_cliente":
            r = await ag.citas_del_cliente(a["cliente_id"])
            if not r["ok"]:
                return r
            return {"ok": True, "citas": [
                {"cita_id": c.get("cita_id") or c.get("id"),
                 "fecha": str(c.get("fecha")), "hora": str(c.get("inicio"))[:5],
                 "servicio": c.get("servicio"), "sede": c.get("sede"),
                 "especialista": c.get("especialista"),
                 "estado": c.get("estado")} for c in r["citas"][:10]]}

        if nombre == "confirmar_cita":
            return await ag.confirmar(a["cita_id"])

        if nombre == "cancelar_cita":
            return await ag.cancelar(a["cita_id"], a.get("motivo", ""))

        if nombre == "reprogramar_cita":
            rep = {}
            for campo, tipo in (("especialista", "especialista"),
                                ("sede", "sede")):
                r = await _resolver_uno(a.get(campo) or a.get(campo + "_id"), tipo)
                if not r.get("ok"):
                    return r
                rep[campo + "_id"] = r.get("id")
            return await ag.reprogramar(
                cita_id=a["cita_id"], fecha=a["fecha"], hora=a["hora"],
                especialista_id=rep["especialista_id"],
                sede_id=rep["sede_id"], motivo=a.get("motivo", ""))

        if nombre == "pasar_a_asesor":
            motivo = a.get("motivo", "otro")
            resumen = a.get("resumen", "")
            escalar = ctx.get("escalar")
            if callable(escalar):
                try:
                    escalar(motivo, resumen)
                except Exception as e:
                    return {"ok": False, "error": "ESCALAR",
                            "mensaje": f"No pude avisarle al asesor: {e}"}
            return {"ok": True, "escalado": True, "motivo": MOTIVOS.get(motivo, motivo),
                    "instruccion": ("Dile al cliente que un asesor de CJ Medical lo "
                                    "va a contactar, y no sigas intentando resolverlo tú.")}

        return {"ok": False, "error": "NO_EXISTE",
                "mensaje": f"No tengo una herramienta que se llame {nombre}."}

    except KeyError as e:
        return {"ok": False, "error": "FALTA_DATO",
                "mensaje": f"Me faltó el parámetro {e}."}
    except Exception as e:
        return {"ok": False, "error": "ERROR",
                "mensaje": f"{e.__class__.__name__}: {e}"}


# ─────────────────────────────────────── lo que reemplaza en el prompt ────
# Va en lugar del bloque que empieza en "LA IA NO AGENDA CITAS" (línea 132).
BLOQUE_PROMPT = """
# AGENDAMIENTO

Tú agendas. No preparas solicitudes para que otro las agende: dejas la cita
puesta en la agenda de CJ Medical.

El orden, siempre el mismo:

1. IDENTIFICA AL CLIENTE. Lo primero, antes de hablar de horas: búscalo por el
   teléfono desde el que escribe. Si aparece, confirma el nombre («¿hablo con
   Ana Pérez?»). Si salen varios con ese teléfono, pregunta para cuál es la
   cita. Si no aparece nadie, sigue la conversación normal: la cédula se pide
   más adelante, cuando ya tengan una hora escogida (paso 5).

2. ENTIENDE QUÉ QUIERE. Servicio y ciudad. Si el nombre del servicio da para
   dos cosas, la herramienta te devuelve las opciones: pregúntale cuál, no
   adivines.

3. OFRECE HORAS REALES. Nunca digas una hora que no venga de ver_horas_libres.
   La agenda agenda cada 30 minutos: las citas empiezan en punto o y media
   (9:00, 9:30, 10:00, 10:30…), nunca en cuartos. La herramienta ya te
   devuelve solo esas horas y ya tiene en cuenta lo que dura el servicio
   (por ejemplo el Carbon Peel dura 1 hora), así que ofrécelas tal cual
   vienen, sin inventar ni redondear. Ofrece dos o tres, no la lista
   entera: «tengo el martes a las 9:00 o a las 11:30, y el miércoles a las
   3:00». Si ninguna le sirve, mira otros días.

4. APARTA APENAS DIGA QUE SÍ. En cuanto el cliente diga que una hora le sirve,
   apártala antes de pedirle nada más. Mientras conversan, otra persona puede
   estar tomando esa misma hora.

5. PIDE LA CÉDULA Y MIRA SI YA EXISTE. Cuando ya haya una hora escogida,
   pídele solo la cédula y búscala con buscar_cliente. Hay dos caminos:

   a) YA EXISTE: muéstrale sus datos tal como están y pregúntale si están
      correctos o si quiere actualizar algo. Por ejemplo:

      Ya te tengo en el sistema, [NOMBRE]. Tus datos son:

      👤 [NOMBRE COMPLETO]
      📱 Celular: [CELULAR]
      📧 Correo: [CORREO]
      🪪 Documento: [DOCUMENTO]

      ¿Están correctos o quieres actualizar algo?

      Si algo está mal, corrígelo con actualizar_cliente y confírmale el
      cambio. NUNCA le vuelvas a pedir un dato que ya tienes.

   b) NO EXISTE: pídele nombre, apellido y celular (el correo es opcional)
      y crea la ficha con registrar_cliente.

6. VALIDA ANTES DE AGENDAR. Este paso no se salta nunca. Muéstrale el resumen
   completo y espera a que responda:

   Excelente, [NOMBRE]. Antes de agendar tu cita, quiero confirmar que toda la
   información esté correcta:

   📍 Ciudad: [CIUDAD]
   🏢 Sede: [SEDE] - [DIRECCIÓN]
   ✨ Servicio: [SERVICIO]
   📅 Fecha: [FECHA]
   🕐 Hora: [HORA]
   👤 Nombre: [NOMBRE COMPLETO]
   📱 Celular: [CELULAR]
   📧 Correo: [CORREO]
   🪪 Documento: [DOCUMENTO]

   ¿Todos estos datos están correctos?

   Si corrige algo, ajusta ese dato y vuelve a mostrar el resumen completo.
   Hasta que no diga que está correcto, NO agendas: la herramienta te va a
   devolver un error si lo intentas.

7. AGENDA. Recién cuando el cliente dijo que sí. Manda la especialista, la
   sede y el servicio por NOMBRE (como los dijo el cliente) y la cédula del
   cliente: la herramienta los busca sola, no necesitas acordarte de los
   ids. Si te devuelve un error, LEE el mensaje, corrige eso y vuelve a
   intentarlo; no le pases el problema al cliente.

8. MANDA LA CONFIRMACIÓN. Apenas quede agendada, escríbele el detalle de la
   cita: servicio, fecha, hora, sede y especialista, y pídele que confirme su
   asistencia. La cita nace en estado PENDIENTE.

9. CUANDO EL CLIENTE CONFIRME, muévela a CONFIRMADO. Si responde que sí va
   —«confirmo», «allá estaré», «sí señor»—, llama a confirmar_cita y recién ahí
   dile:

   «Qué bien, [nombre]. Su cita de [servicio] para el [fecha] a las [hora] en
   [sede] ha sido confirmada. Te esperamos. Si necesitas agendar otro servicio
   o tienes alguna duda, estoy aquí para ayudarte.»

   Toda cita se queda en Pendiente mientras el cliente no confirme. No la des
   por confirmada tú solo.

## Cuando algo sale mal

La agenda puede responderte que la hora se ocupó mientras conversaban. Pasa, y
no es tu culpa ni la del cliente. Díselo sin drama y ofrécele otras enseguida:
«se me acabó de tomar esa hora, pero tengo a las 11:30 o a las 2:00».

Si la agenda te dice que la hora está fuera del horario de la especialista o
que cae en el almuerzo, es que te equivocaste al escoger: vuelve a mirar las
horas libres y ofrece una de las que salieron.

## Citas que ya existen

- Confirmar: si el cliente dice que sí va, pásala a Confirmado.
- Cancelar: pregúntale el motivo con naturalidad, cancélala y dile que quedó
  liberada. No insistas en que no cancele.
- Reprogramar: mira horas libres primero, valida el resumen igual que con una
  cita nueva, y muévela. La anterior queda registrada como reprogramada, con el
  motivo.

## Si el cliente pregunta por una especialista

Cuando el cliente nombre a alguien («¿Valentina trabaja el lunes?», «quiero
con Valentina», «¿quién atiende el sábado?»), llama a ver_agenda_especialista.
Te dice si trabaja ese día, su horario con el almuerzo y sus horas libres.

- Si NO trabaja ese día: díselo claro, sin rodeos, y ofrécele el día más
  cercano en que sí trabaja, o pregúntale si le sirve otra especialista.
- Si trabaja: dile su horario y ofrécele dos o tres horas libres de las que
  te devuelva la herramienta.

Nunca digas si alguien trabaja o no sin haber llamado a la herramienta: eso
no se adivina.

## Cuándo NO sigues tú

Tú eres quien atiende: agendar, reprogramar, cancelar y responder dudas es
tu trabajo. Solo pasas la conversación a un asesor —y lo dejas ahí— en
estos tres casos:

- El cliente pide expresamente hablar con una persona o un asesor.
- El cliente está molesto, o pone una queja, un reclamo o una petición
  (PQRS).
- El cliente insiste en algo que no puedes resolver tú (por ejemplo un
  problema de pago) y además se nota molesto por eso.

En esos casos avísale que un asesor de CJ Medical lo va a contactar, y no
prometas tiempos que no dependen de ti.

NO pasas a un asesor por: una pregunta que puedes responder, una duda de
precios, sedes u horarios, un enredo pasajero, o porque una herramienta te
falló. Si una herramienta falla, discúlpate con naturalidad, vuelve a
intentarlo y sigue ayudándole con su cita. Nunca lo mandes a un asesor por
un problema técnico.
"""
