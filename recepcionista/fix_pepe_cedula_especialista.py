#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pepe: identificar por cedula + consultar agenda de una especialista.

1. agenda_helper: actualizar_cliente() y horario_especialista()
2. herramientas:
   - buscar_cliente (antes buscar_cliente_por_telefono): acepta cedula
   - actualizar_cliente (nuevo)
   - ver_agenda_especialista (nuevo)
   - el dispatcher y el prompt
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


# ═══════════════════════ 1) agenda_helper ═══════════════════════════════════
aplicar(BASE + "agenda_helper.py", [(
    'async def citas_del_cliente(cliente_id: str) -> dict:',
    'async def actualizar_cliente(cliente_id: str, **campos) -> dict:\n'
    '    """Corrige la ficha de un cliente que YA existe. Manda solo lo que cambia."""\n'
    '    limpio = {k: v for k, v in campos.items() if v not in (None, "")}\n'
    '    if not limpio:\n'
    '        return {"ok": False, "error": "SIN_CAMBIOS",\n'
    '                "mensaje": "No me dijiste qué dato hay que cambiar."}\n'
    '    r = await _llamar("PUT", f"/clientes/{cliente_id}", limpio)\n'
    '    if not r["ok"]:\n'
    '        return r\n'
    '    return {"ok": True, "cliente": r["datos"]}\n'
    '\n'
    '\n'
    'async def citas_del_cliente(cliente_id: str) -> dict:'
), (
    'async def apartar_cupo(especialista_id: str, sede_id: str, fecha: str, hora: str,',
    'def _proximos_dias(dias: int) -> list:\n'
    '    """Fechas de hoy en adelante, en formato AAAA-MM-DD.\n'
    '    Se ancla a las 12:00 para que un cambio de hora no corra el día."""\n'
    '    h = time.localtime()\n'
    '    base = time.mktime((h.tm_year, h.tm_mon, h.tm_mday, 12, 0, 0, 0, 0, -1))\n'
    '    return [time.strftime("%Y-%m-%d", time.localtime(base + i * 86400))\n'
    '            for i in range(max(1, min(int(dias), 30)))]\n'
    '\n'
    '\n'
    'async def horario_especialista(especialista: str, fecha: str = None,\n'
    '                               dias: int = 7, sede: str = None,\n'
    '                               servicio: str = None) -> dict:\n'
    '    """¿Esta especialista trabaja ese día? ¿A qué horas tiene cupo?\n'
    '\n'
    '    Sin fecha revisa los próximos `dias` y devuelve solo los días en que\n'
    '    trabaja, para poder decir «el lunes no, pero el martes sí».\n'
    '    """\n'
    '    ep = await resolver_especialista(especialista)\n'
    '    if not ep["ok"]:\n'
    '        return ep\n'
    '    sd = await resolver_sede(sede) if sede else {"ok": True, "id": None}\n'
    '    if not sd["ok"]:\n'
    '        return sd\n'
    '    sv = await resolver_servicio(servicio) if servicio else {"ok": True, "id": None}\n'
    '    if not sv["ok"]:\n'
    '        return sv\n'
    '\n'
    '    fechas = [fecha] if fecha else _proximos_dias(dias)\n'
    '    salida = []\n'
    '    for f in fechas:\n'
    '        params = {"especialista": ep["id"], "fecha": f, "paso": PASO_MINUTOS}\n'
    '        if sd.get("id"):\n'
    '            params["sede"] = sd["id"]\n'
    '        if sv.get("id"):\n'
    '            params["servicio"] = sv["id"]\n'
    '        r = await _llamar("GET", "/agenda-especialista", params=params)\n'
    '        if not r["ok"]:\n'
    '            return r\n'
    '        d = r["datos"] or {}\n'
    '        franjas = d.get("franjas") or []\n'
    '        libres = [h.get("inicio") for h in (d.get("libres") or [])\n'
    '                  if str(h.get("inicio", ""))[-2:] in ("00", "30")]\n'
    '        if not franjas:\n'
    '            # si preguntó por un día puntual hay que poder decir «no trabaja»\n'
    '            if fecha:\n'
    '                salida.append({"fecha": f, "trabaja": False})\n'
    '            continue\n'
    '        fr = franjas[0]\n'
    '        alm = ("%s a %s" % (fr["alm_desde"], fr["alm_hasta"])\n'
    '               if fr.get("alm_desde") and fr.get("alm_hasta") else None)\n'
    '        salida.append({\n'
    '            "fecha": f, "trabaja": True, "sede": fr.get("sede"),\n'
    '            "horario": "%s a %s" % (fr.get("desde"), fr.get("hasta")),\n'
    '            "almuerzo": alm, "libres": libres[:6],\n'
    '            "hay_mas_horas": len(libres) > 6,\n'
    '            "origen": fr.get("origen")})\n'
    '\n'
    '    return {"ok": True, "especialista": ep["nombre"],\n'
    '            "especialista_id": ep["id"],\n'
    '            "consulta": fecha or ("próximos %d días" % len(fechas)),\n'
    '            "dias": salida}\n'
    '\n'
    '\n'
    'async def apartar_cupo(especialista_id: str, sede_id: str, fecha: str, hora: str,'
)], "agenda_helper.py")

# ═══════════════════════ 2) herramientas ════════════════════════════════════
aplicar(BASE + "herramientas.py", [(
    # --- herramienta de busqueda ---
    '        "name": "buscar_cliente_por_telefono",\n'
    '        "description": (\n'
    '            "Busca la ficha del cliente por el teléfono desde el que escribe. "\n'
    '            "SIEMPRE es lo primero que se hace antes de agendar. Si aparece, "\n'
    '            "confirma el nombre con el cliente antes de seguir. Si no aparece, "\n'
    '            "recién ahí se le piden los datos."),\n'
    '        "parameters": {"type": "object", "properties": {\n'
    '            "telefono": {"type": "string",\n'
    '                         "description": "Con o sin indicativo; da igual el formato."}},\n'
    '            "required": ["telefono"]}}},',
    '        "name": "buscar_cliente",\n'
    '        "description": (\n'
    '            "Busca la ficha del cliente en la agenda. Primero se busca por el "\n'
    '            "teléfono desde el que escribe (eso va solo). Antes de pedirle "\n'
    '            "datos, búscalo por la CÉDULA: si ya existe, se le muestran sus "\n'
    '            "datos y NO se le vuelven a pedir. El documento manda sobre el "\n'
    '            "teléfono. Devuelve la ficha completa (nombre, documento, "\n'
    '            "teléfono y correo)."),\n'
    '        "parameters": {"type": "object", "properties": {\n'
    '            "documento": {"type": "string",\n'
    '                          "description": "Cédula, solo números. Es lo más confiable."},\n'
    '            "telefono": {"type": "string",\n'
    '                         "description": "Con o sin indicativo; da igual el formato."},\n'
    '            "nombre": {"type": "string",\n'
    '                       "description": "Solo si no tiene documento ni teléfono."}},\n'
    '            "required": []}}},\n'
    '\n'
    '    {"type": "function", "function": {\n'
    '        "name": "actualizar_cliente",\n'
    '        "description": (\n'
    '            "Corrige los datos de un cliente que YA existe. Se usa solo "\n'
    '            "cuando, después de mostrarle su ficha, el cliente dice que algo "\n'
    '            "está mal o quiere cambiarlo. Manda solo los campos que cambian."),\n'
    '        "parameters": {"type": "object", "properties": {\n'
    '            "cliente_id": {"type": "string",\n'
    '                           "description": "El que devolvió buscar_cliente."},\n'
    '            "primer_nombre": {"type": "string"},\n'
    '            "segundo_nombre": {"type": "string"},\n'
    '            "primer_apellido": {"type": "string"},\n'
    '            "segundo_apellido": {"type": "string"},\n'
    '            "telefono": {"type": "string"},\n'
    '            "correo": {"type": "string"}},\n'
    '            "required": ["cliente_id"]}}},'
), (
    # --- herramienta nueva: agenda de una especialista ---
    '    {"type": "function", "function": {\n'
    '        "name": "apartar_hora",',
    '    {"type": "function", "function": {\n'
    '        "name": "ver_agenda_especialista",\n'
    '        "description": (\n'
    '            "Mira la agenda de UNA especialista: si trabaja ese día, su "\n'
    '            "horario (con el almuerzo) y sus horas libres reales. Se usa "\n'
    '            "cuando el cliente pregunta por alguien puntual («¿Valentina "\n'
    '            "trabaja el lunes?», «quiero con Valentina»). Si no le das fecha, "\n'
    '            "revisa los próximos días y te dice cuáles trabaja. NUNCA digas "\n'
    '            "si alguien trabaja o no sin haber llamado esta herramienta."),\n'
    '        "parameters": {"type": "object", "properties": {\n'
    '            "especialista": {"type": "string",\n'
    '                             "description": "Como lo dijo el cliente: «Valentina», «Dra. Arias»."},\n'
    '            "fecha": {"type": "string",\n'
    '                      "description": "AAAA-MM-DD si preguntó por un día puntual."},\n'
    '            "dias": {"type": "integer",\n'
    '                     "description": "Cuántos días revisar cuando no hay fecha. Por defecto 7."},\n'
    '            "servicio": {"type": "string",\n'
    '                         "description": "Solo si ya se sabe qué servicio quiere."},\n'
    '            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro»."}},\n'
    '            "required": ["especialista"]}}},\n'
    '\n'
    '    {"type": "function", "function": {\n'
    '        "name": "apartar_hora",'
), (
    # --- dispatcher: buscar ---
    '        if nombre == "buscar_cliente_por_telefono":\n'
    '            r = await ag.buscar_cliente(telefono=a.get("telefono") or ctx.get("telefono"))\n'
    '            if not r["ok"]:\n'
    '                return r\n'
    '            cl = r["clientes"]\n'
    '            return {"ok": True, "encontrados": len(cl), "clientes": [\n'
    '                {"cliente_id": c["id"],\n'
    '                 "nombre": " ".join(x for x in [c.get("primer_nombre"),\n'
    '                                                c.get("primer_apellido")] if x),\n'
    '                 "documento": c.get("documento"),\n'
    '                 "telefono": c.get("telefono")} for c in cl[:5]]}',
    '        if nombre in ("buscar_cliente", "buscar_cliente_por_telefono"):\n'
    '            documento = str(a.get("documento") or "").strip()\n'
    '            telefono = str(a.get("telefono") or "").strip()\n'
    '            # sin documento ni telefono se usa el del chat\n'
    '            if not documento and not telefono:\n'
    '                telefono = ctx.get("telefono") or ""\n'
    '            r = await ag.buscar_cliente(telefono=telefono or None,\n'
    '                                        documento=documento or None,\n'
    '                                        nombre=a.get("nombre") or None)\n'
    '            if not r["ok"]:\n'
    '                return r\n'
    '            cl = r["clientes"]\n'
    '            return {"ok": True, "encontrados": len(cl),\n'
    '                    "clientes": [_ficha(c) for c in cl[:5]]}\n'
    '\n'
    '        if nombre == "actualizar_cliente":\n'
    '            r = await ag.actualizar_cliente(\n'
    '                a["cliente_id"], primer_nombre=a.get("primer_nombre"),\n'
    '                segundo_nombre=a.get("segundo_nombre"),\n'
    '                primer_apellido=a.get("primer_apellido"),\n'
    '                segundo_apellido=a.get("segundo_apellido"),\n'
    '                telefono=a.get("telefono"), correo=a.get("correo"))\n'
    '            if not r["ok"]:\n'
    '                return r\n'
    '            return {"ok": True, "actualizado": True,\n'
    '                    "cliente": _ficha(r["cliente"] or {})}'
), (
    # --- dispatcher: agenda de la especialista ---
    '        if nombre == "apartar_hora":',
    '        if nombre == "ver_agenda_especialista":\n'
    '            return await ag.horario_especialista(\n'
    '                especialista=a.get("especialista", ""),\n'
    '                fecha=a.get("fecha"), dias=int(a.get("dias") or 7),\n'
    '                sede=a.get("sede"), servicio=a.get("servicio"))\n'
    '\n'
    '        if nombre == "apartar_hora":'
), (
    # --- helper _ficha ---
    'async def ejecutar(nombre: str, argumentos, contexto: dict = None) -> dict:',
    'def _ficha(c: dict) -> dict:\n'
    '    """La ficha del cliente como la necesita el modelo, sin ruido."""\n'
    '    completo = " ".join(x for x in [c.get("primer_nombre"),\n'
    '                                    c.get("segundo_nombre"),\n'
    '                                    c.get("primer_apellido"),\n'
    '                                    c.get("segundo_apellido")] if x)\n'
    '    return {"cliente_id": c.get("id"),\n'
    '            "nombre_completo": completo or c.get("documento"),\n'
    '            "primer_nombre": c.get("primer_nombre"),\n'
    '            "primer_apellido": c.get("primer_apellido"),\n'
    '            "documento": c.get("documento"),\n'
    '            "telefono": c.get("telefono"),\n'
    '            "correo": c.get("correo")}\n'
    '\n'
    '\n'
    'async def ejecutar(nombre: str, argumentos, contexto: dict = None) -> dict:'
)], "herramientas.py (herramientas)")

# ═══════════════════════ 3) el prompt ═══════════════════════════════════════
aplicar(BASE + "herramientas.py", [(
    '   cita. Si no aparece nadie, sigue la conversación normal y pídele los datos\n'
    '   más adelante, cuando ya tengan una hora escogida.',
    '   cita. Si no aparece nadie, sigue la conversación normal: la cédula se pide\n'
    '   más adelante, cuando ya tengan una hora escogida (paso 5).'
), (
    '5. COMPLETA LOS DATOS si es cliente nuevo: cédula, nombre y apellido. El correo\n'
    '   es opcional.',
    '5. PIDE LA CÉDULA Y MIRA SI YA EXISTE. Cuando ya haya una hora escogida,\n'
    '   pídele solo la cédula y búscala con buscar_cliente. Hay dos caminos:\n'
    '\n'
    '   a) YA EXISTE: muéstrale sus datos tal como están y pregúntale si están\n'
    '      correctos o si quiere actualizar algo. Por ejemplo:\n'
    '\n'
    '      Ya te tengo en el sistema, [NOMBRE]. Tus datos son:\n'
    '\n'
    '      👤 [NOMBRE COMPLETO]\n'
    '      📱 Celular: [CELULAR]\n'
    '      📧 Correo: [CORREO]\n'
    '      🪪 Documento: [DOCUMENTO]\n'
    '\n'
    '      ¿Están correctos o quieres actualizar algo?\n'
    '\n'
    '      Si algo está mal, corrígelo con actualizar_cliente y confírmale el\n'
    '      cambio. NUNCA le vuelvas a pedir un dato que ya tienes.\n'
    '\n'
    '   b) NO EXISTE: pídele nombre, apellido y celular (el correo es opcional)\n'
    '      y crea la ficha con registrar_cliente.'
), (
    '## Cuándo NO sigues tú',
    '## Si el cliente pregunta por una especialista\n'
    '\n'
    'Cuando el cliente nombre a alguien («¿Valentina trabaja el lunes?», «quiero\n'
    'con Valentina», «¿quién atiende el sábado?»), llama a ver_agenda_especialista.\n'
    'Te dice si trabaja ese día, su horario con el almuerzo y sus horas libres.\n'
    '\n'
    '- Si NO trabaja ese día: díselo claro, sin rodeos, y ofrécele el día más\n'
    '  cercano en que sí trabaja, o pregúntale si le sirve otra especialista.\n'
    '- Si trabaja: dile su horario y ofrécele dos o tres horas libres de las que\n'
    '  te devuelva la herramienta.\n'
    '\n'
    'Nunca digas si alguien trabaja o no sin haber llamado a la herramienta: eso\n'
    'no se adivina.\n'
    '\n'
    '## Cuándo NO sigues tú'
)], "herramientas.py (prompt)")

print()
import py_compile
for f in ("agenda_helper.py", "herramientas.py"):
    py_compile.compile(BASE + f, doraise=True)
    print("  sintaxis OK:", f)
