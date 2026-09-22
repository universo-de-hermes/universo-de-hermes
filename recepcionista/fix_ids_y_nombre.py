#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Por que no agendo y por que acorto el nombre.

BUG 1: el modelo NO ve los resultados de sus herramientas entre mensajes (el
historial que se le pasa solo lleva el texto). Cuando el cliente dice «Ok» o
«Si», el modelo ya perdio especialista_id / sede_id / servicio_id / cliente_id
y se los INVENTA. La agenda responde 500 ESPECIALISTA_NO_DISPONIBLE porque le
llego el nombre «Valentina Baquero» donde esperaba un id.

Arreglo: agendar_cita y apartar_hora aceptan NOMBRES (especialista, sede,
servicio) y la cedula/teléfono del cliente. El dispatcher los resuelve contra la
agenda antes de llamarla. Asi el modelo no necesita acordarse de nada.

BUG 2: la extraccion de nombre desde la respuesta de Pepe no miraba si el
nombre ya estaba completo, asi que «Ok» (= "Listo, Juan") lo acorto a «Juan».
"""
import io
import re
import sqlite3
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


aplicar(BASE + "herramientas.py", [
    # ── apartar_hora: nombres en vez de ids ──
    ('        "name": "apartar_hora",\n'
     '        "description": (\n'
     '            "Aparta la hora por unos minutos mientras terminan de hablar. Se "\n'
     '            "llama APENAS el cliente diga que le sirve una hora, ANTES de "\n'
     '            "pedirle datos. Sin esto, otra conversación puede quedarse con esa "\n'
     '            "hora y toca decirle que ya no está."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "especialista_id": {"type": "string", "description": "El que vino en ver_horas_libres."},\n'
     '            "sede_id": {"type": "string"},\n'
     '            "servicio_id": {"type": "string"},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD"},\n'
     '            "hora": {"type": "string", "description": "HH:MM"},\n'
     '            "minutos": {"type": "integer", "description": "Por defecto 10."}},\n'
     '            "required": ["especialista_id", "sede_id", "servicio_id", "fecha", "hora"]}}},',
     '        "name": "apartar_hora",\n'
     '        "description": (\n'
     '            "Aparta la hora por unos minutos mientras terminan de hablar. Se "\n'
     '            "llama APENAS el cliente diga que le sirve una hora, ANTES de "\n'
     '            "pedirle datos. Sin esto, otra conversación puede quedarse con esa "\n'
     '            "hora y toca decirle que ya no está. La especialista, la sede y el "\n'
     '            "servicio se pueden mandar por NOMBRE (como los dijo el cliente): "\n'
     '            "no hace falta acordarse de los ids."),\n'
     '        "parameters": {"type": "object", "properties": {\n'
     '            "especialista": {"type": "string", "description": "«Valentina», «Dra. Arias»…"},\n'
     '            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro»."},\n'
     '            "servicio": {"type": "string", "description": "Como lo dijo el cliente."},\n'
     '            "especialista_id": {"type": "string", "description": "Opcional, si lo tienes."},\n'
     '            "sede_id": {"type": "string", "description": "Opcional."},\n'
     '            "servicio_id": {"type": "string", "description": "Opcional."},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD"},\n'
     '            "hora": {"type": "string", "description": "HH:MM"},\n'
     '            "minutos": {"type": "integer", "description": "Por defecto 10."}},\n'
     '            "required": ["fecha", "hora"]}}},'),
    # ── agendar_cita: nombres y cedula ──
    ('            "cliente_id": {"type": "string"},\n'
     '            "especialista_id": {"type": "string"},\n'
     '            "sede_id": {"type": "string"},\n'
     '            "servicio_id": {"type": "string"},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD"},\n'
     '            "hora": {"type": "string", "description": "HH:MM"},\n'
     '            "reserva": {"type": "string", "description": "La que devolvió apartar_hora."},\n'
     '            "notas": {"type": "string", "description": "Lo que el cliente pidió tener en cuenta."},\n'
     '            "cliente_confirmo": {"type": "boolean",\n'
     '                "description": ("true SOLO si ya le mostraste el resumen completo "\n'
     '                                "(ciudad, sede, servicio, fecha, hora, nombre, celular, "\n'
     '                                "correo, documento) y el cliente respondió que está "\n'
     '                                "correcto. Si todavía no lo has hecho, no llames esta "\n'
     '                                "herramienta: muestra el resumen primero.")}},\n'
     '            "required": ["cliente_id", "especialista_id", "sede_id", "servicio_id",\n'
     '                         "fecha", "hora", "cliente_confirmo"]}}},',
     '            "cliente_id": {"type": "string",\n'
     '                           "description": "El que devolvió buscar_cliente (opcional)."},\n'
     '            "documento": {"type": "string",\n'
     '                          "description": "Cédula del cliente. Sirve en vez de cliente_id."},\n'
     '            "telefono": {"type": "string",\n'
     '                         "description": "Celular del cliente, si no tienes el documento."},\n'
     '            "especialista": {"type": "string",\n'
     '                             "description": "«Valentina», «Dra. Arias»: el nombre basta."},\n'
     '            "sede": {"type": "string", "description": "«Bogotá» o «El Tesoro»."},\n'
     '            "servicio": {"type": "string",\n'
     '                         "description": "Como lo dijo el cliente: «carbon peel»."},\n'
     '            "especialista_id": {"type": "string", "description": "Opcional."},\n'
     '            "sede_id": {"type": "string", "description": "Opcional."},\n'
     '            "servicio_id": {"type": "string", "description": "Opcional."},\n'
     '            "fecha": {"type": "string", "description": "AAAA-MM-DD"},\n'
     '            "hora": {"type": "string", "description": "HH:MM"},\n'
     '            "reserva": {"type": "string", "description": "La que devolvió apartar_hora."},\n'
     '            "notas": {"type": "string", "description": "Lo que el cliente pidió tener en cuenta."},\n'
     '            "cliente_confirmo": {"type": "boolean",\n'
     '                "description": ("true SOLO si ya le mostraste el resumen completo "\n'
     '                                "(ciudad, sede, servicio, fecha, hora, nombre, celular, "\n'
     '                                "correo, documento) y el cliente respondió que está "\n'
     '                                "correcto. Si todavía no lo has hecho, no llames esta "\n'
     '                                "herramienta: muestra el resumen primero.")}},\n'
     '            "required": ["fecha", "hora", "cliente_confirmo"]}}},'),
    # ── resolvers ──
    ('def _ficha(c: dict) -> dict:',
     '_ID_PREFIJO = {"especialista": "esp-", "sede": "sede-", "servicio": "srv-"}\n'
     '\n'
     '\n'
     'async def _resolver_uno(valor, tipo: str) -> dict:\n'
     '    """Devuelve {\'ok\', \'id\'} a partir del id o del nombre."""\n'
     '    v = str(valor or "").strip()\n'
     '    if not v:\n'
     '        return {"ok": True, "id": None}\n'
     '    if v.startswith(_ID_PREFIJO.get(tipo, "\\0")):\n'
     '        return {"ok": True, "id": v}\n'
     '    f = {"especialista": ag.resolver_especialista,\n'
     '         "sede": ag.resolver_sede,\n'
     '         "servicio": ag.resolver_servicio}[tipo]\n'
     '    r = await f(v)\n'
     '    if not r.get("ok"):\n'
     '        return r\n'
     '    return {"ok": True, "id": r["id"]}\n'
     '\n'
     '\n'
     'async def _resolver_cita(a: dict) -> dict:\n'
     '    """Especialista, sede y servicio: acepta el nombre o el id.\n'
     '\n'
     '    El modelo no ve los resultados de sus herramientas entre mensajes, así\n'
     '    que no se puede confiar en que se acuerde de los ids: se resuelven aquí.\n'
     '    """\n'
     '    salida = {}\n'
     '    for campo, tipo, etiqueta in (("especialista", "especialista", "la especialista"),\n'
     '                                  ("sede", "sede", "la sede"),\n'
     '                                  ("servicio", "servicio", "el servicio")):\n'
     '        r = await _resolver_uno(a.get(campo) or a.get(campo + "_id"), tipo)\n'
     '        if not r.get("ok"):\n'
     '            return r\n'
     '        if not r.get("id"):\n'
     '            return {"ok": False, "error": "FALTA_" + tipo.upper(),\n'
     '                    "mensaje": "Me falta %s para agendar." % etiqueta}\n'
     '        salida[campo + "_id"] = r["id"]\n'
     '    return {"ok": True, **salida}\n'
     '\n'
     '\n'
     'async def _resolver_cliente(a: dict, ctx: dict) -> dict:\n'
     '    """cliente_id, o la cédula, o el teléfono."""\n'
     '    cid = str(a.get("cliente_id") or "").strip()\n'
     '    if cid.startswith("cl-"):\n'
     '        return {"ok": True, "cliente_id": cid}\n'
     '    documento = str(a.get("documento") or "").strip()\n'
     '    telefono = str(a.get("telefono") or "").strip() or str(ctx.get("telefono") or "")\n'
     '    r = await ag.buscar_cliente(telefono=telefono or None,\n'
     '                                documento=documento or None)\n'
     '    if not r["ok"]:\n'
     '        return r\n'
     '    cl = r["clientes"]\n'
     '    if not cl:\n'
     '        return {"ok": False, "error": "CLIENTE_NO_EXISTE",\n'
     '                "mensaje": ("No encuentro al cliente en la agenda. Regístralo "\n'
     '                            "primero con registrar_cliente.")}\n'
     '    return {"ok": True, "cliente_id": cl[0]["id"]}\n'
     '\n'
     '\n'
     'def _ficha(c: dict) -> dict:'),
    # ── dispatcher: apartar_hora ──
    ('        if nombre == "apartar_hora":\n'
     '            return await ag.apartar_cupo(\n'
     '                especialista_id=a["especialista_id"], sede_id=a["sede_id"],\n'
     '                fecha=a["fecha"], hora=a["hora"], servicio_id=a["servicio_id"],\n'
     '                minutos=int(a.get("minutos") or 10),\n'
     '                referencia=ctx.get("telefono", ""))',
     '        if nombre == "apartar_hora":\n'
     '            rc = await _resolver_cita(a)\n'
     '            if not rc["ok"]:\n'
     '                return rc\n'
     '            return await ag.apartar_cupo(\n'
     '                especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],\n'
     '                fecha=a["fecha"], hora=a["hora"],\n'
     '                servicio_id=rc["servicio_id"],\n'
     '                minutos=int(a.get("minutos") or 10),\n'
     '                referencia=ctx.get("telefono", ""))'),
    # ── dispatcher: agendar_cita ──
    ('            return await ag.agendar(\n'
     '                cliente_id=a["cliente_id"], especialista_id=a["especialista_id"],\n'
     '                sede_id=a["sede_id"], fecha=a["fecha"], hora=a["hora"],\n'
     '                servicio_id=a["servicio_id"], notas=a.get("notas", ""),\n'
     '                reserva=a.get("reserva"))',
     '            rcl = await _resolver_cliente(a, ctx)\n'
     '            if not rcl["ok"]:\n'
     '                return rcl\n'
     '            rc = await _resolver_cita(a)\n'
     '            if not rc["ok"]:\n'
     '                return rc\n'
     '            return await ag.agendar(\n'
     '                cliente_id=rcl["cliente_id"],\n'
     '                especialista_id=rc["especialista_id"], sede_id=rc["sede_id"],\n'
     '                fecha=a["fecha"], hora=a["hora"],\n'
     '                servicio_id=rc["servicio_id"], notas=a.get("notas", ""),\n'
     '                reserva=a.get("reserva"))'),
    # ── dispatcher: reprogramar (especialista/sede por nombre) ──
    ('        if nombre == "reprogramar_cita":\n'
     '            return await ag.reprogramar(\n'
     '                cita_id=a["cita_id"], fecha=a["fecha"], hora=a["hora"],\n'
     '                especialista_id=a.get("especialista_id"),\n'
     '                sede_id=a.get("sede_id"), motivo=a.get("motivo", ""))',
     '        if nombre == "reprogramar_cita":\n'
     '            rep = {}\n'
     '            for campo, tipo in (("especialista", "especialista"),\n'
     '                                ("sede", "sede")):\n'
     '                r = await _resolver_uno(a.get(campo) or a.get(campo + "_id"), tipo)\n'
     '                if not r.get("ok"):\n'
     '                    return r\n'
     '                rep[campo + "_id"] = r.get("id")\n'
     '            return await ag.reprogramar(\n'
     '                cita_id=a["cita_id"], fecha=a["fecha"], hora=a["hora"],\n'
     '                especialista_id=rep["especialista_id"],\n'
     '                sede_id=rep["sede_id"], motivo=a.get("motivo", ""))'),
    # ── prompt: mandar por nombre y reintentar si falla ──
    ('7. AGENDA. Recién cuando el cliente dijo que sí.',
     '7. AGENDA. Recién cuando el cliente dijo que sí. Manda la especialista, la\n'
     '   sede y el servicio por NOMBRE (como los dijo el cliente) y la cédula del\n'
     '   cliente: la herramienta los busca sola, no necesitas acordarte de los\n'
     '   ids. Si te devuelve un error, LEE el mensaje, corrige eso y vuelve a\n'
     '   intentarlo; no le pases el problema al cliente.'),
], "herramientas.py")

# ── main.py: no acortar el nombre ──
aplicar(BASE + "main.py", [(
    "            if re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s.]+$', extracted) and extracted != (client.get(\"name\") or \"\"):\n"
    "                update_client_data(client[\"id\"], name=extracted)\n"
    "                logger.info(f\"📝 Nombre actualizado: {client.get('name')} → {extracted}\")",
    "            # No se acorta un nombre que ya está completo: con la respuesta\n"
    "            # «Ok» (= «Listo, Juan») quedó «Juan» en lugar del nombre entero.\n"
    "            actual = (client.get(\"name\") or \"\").strip()\n"
    "            if (re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s.]+$', extracted)\n"
    "                    and extracted != actual\n"
    "                    and len(extracted.split()) >= len(actual.split())):\n"
    "                update_client_data(client[\"id\"], name=extracted)\n"
    "                logger.info(f\"📝 Nombre actualizado: {actual} → {extracted}\")"
)], "main.py")

# ── restaurar el nombre del cliente ──
DB = BASE + "crm/cjmedical.db"
con = sqlite3.connect(DB)
cur = con.cursor()
cur.execute("select id, name from clients where name like 'Juan%'")
print()
print("clientes Juan*:", cur.fetchall())
cur.execute("update clients set name='Juan Jose Otero Villadiego' where id=22")
con.commit()
cur.execute("select id, name, status from clients")
print("clientes ahora:", cur.fetchall())
con.close()

print()
import py_compile
for f in ("herramientas.py", "main.py"):
    py_compile.compile(BASE + f, doraise=True)
    print("  sintaxis OK:", f)