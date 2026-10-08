#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arregla las respuestas VACIAS de Pepe (y de paso lo acelera).

Que pasaba:
  DeepSeek V4 Pro es un modelo de RAZONAMIENTO: antes de contestar "piensa"
  (gasto 459-916 tokens en las pruebas). Si ese razonamiento se come el
  limite de `max_tokens` (1200), la respuesta vuelve SIN TEXTO y el cliente
  recibe un mensaje en blanco. Se vio en la conversacion de prueba: Pepe
  respondio vacio dos veces y la cita nunca se agendo.

Arreglo, en tres partes:
  1. `reasoning: {"enabled": False}`: medido con el prompt real, da la MISMA
     calidad de respuesta y baja de 4.9 s a 2.0 s (y de paso no gasta tokens
     pensando, que era la causa del vacio).
  2. `max_tokens` de 1200 a 3000: margen para los argumentos de herramienta.
  3. Red de seguridad: si el texto final sale vacio, se reintenta con el
     modelo de respaldo. Un cliente NUNCA puede recibir un mensaje en blanco.
"""
import os
import shutil

MP = "/root/universo/recepcionista/main.py"
b = MP + ".pre-vacio.bak"
if not os.path.exists(b):
    shutil.copy2(MP, b)
    print("  respaldo: %s" % os.path.basename(b))

with open(MP, encoding="utf-8", newline="") as f:
    bruto = f.read()
crlf = "\r\n" in bruto
t = bruto.replace("\r\n", "\n")
CAMBIOS = []


def cambiar(viejo, nuevo, etiqueta):
    global t
    if t.count(viejo) != 1:
        raise SystemExit("  X '%s' aparece %d veces" % (etiqueta, t.count(viejo)))
    t = t.replace(viejo, nuevo)
    print("  ok %s" % etiqueta)
    CAMBIOS.append(etiqueta)


# ── 1. la constante de razonamiento ──
cambiar('PRIMARY_MODEL = "deepseek/deepseek-v4-pro"',
       'PRIMARY_MODEL = "deepseek/deepseek-v4-pro"\n'
       '# DeepSeek V4 Pro es de RAZONAMIENTO: "piensa" antes de contestar y esos\n'
       '# tokens salen del mismo presupuesto que la respuesta. Medido con el\n'
       '# prompt real: apagarlo da la MISMA calidad y baja de 4.9 s a 2.0 s, y\n'
       '# evita que la respuesta vuelva vacia. En None se deja de mandar.\n'
       'REASONING = {"enabled": False}',
       "constante REASONING")

# ── 2. la llamada al modelo principal ──
cambiar('''        try:
            resp = ai_client.chat.completions.create(
                model=PRIMARY_MODEL, messages=messages,
                tools=HERRAMIENTAS, tool_choice="auto",
                max_tokens=1200, temperature=0.7)''',
       '''        try:
            extra = {"reasoning": REASONING} if REASONING else {}
            resp = ai_client.chat.completions.create(
                model=PRIMARY_MODEL, messages=messages,
                tools=HERRAMIENTAS, tool_choice="auto",
                max_tokens=3000, temperature=0.7, **extra)''',
       "llamada al principal con reasoning y max_tokens 3000")

# ── 3. la red de seguridad contra el vacio ──
cambiar('''        msg = resp.choices[0].message
        if not getattr(msg, "tool_calls", None):
            update_agent_status("recep", doing="Cliente atendido",
                                task="Esperando próximo mensaje", status="idle",
                                walk_x=None, walk_z=None)
            return clean_response(msg.content or "")''',
       '''        msg = resp.choices[0].message
        if not getattr(msg, "tool_calls", None):
            final = clean_response(msg.content or "")
            if not final.strip():
                # El modelo devolvio la respuesta en blanco. Un cliente NUNCA
                # puede recibir un mensaje vacio: se reintenta con el respaldo.
                logger.warning("Respuesta VACIA del modelo principal: "
                               "reintento con %s" % FALLBACK_MODEL)
                try:
                    resp2 = ai_client.chat.completions.create(
                        model=FALLBACK_MODEL, messages=messages,
                        tools=HERRAMIENTAS, tool_choice="auto",
                        max_tokens=1500, temperature=0.7)
                    m2 = resp2.choices[0].message
                    if getattr(m2, "tool_calls", None):
                        # el respaldo pidio una herramienta: se le corre y el
                        # bucle sigue, para que cierre la idea el mismo
                        messages.append(m2.model_dump(exclude_none=True))
                        for tc in m2.tool_calls:
                            resultado = await ejecutar_herramienta(
                                tc.function.name, tc.function.arguments, contexto)
                            messages.append({
                                "role": "tool", "tool_call_id": tc.id,
                                "content": json.dumps(resultado,
                                                      ensure_ascii=False,
                                                      default=str)})
                        continue
                    final = clean_response(m2.content or "")
                except Exception as e:
                    logger.error("El reintento tambien fallo: %s" % e)
                if not final.strip():
                    final = ("Perdón, se me enredó algo por acá. ¿Me repites lo "
                             "último que me dijiste? Ya casi dejamos tu cita lista.")
            update_agent_status("recep", doing="Cliente atendido",
                                task="Esperando próximo mensaje", status="idle",
                                walk_x=None, walk_z=None)
            return final''',
       "red de seguridad: nunca responder vacio")

if crlf:
    t = t.replace("\n", "\r\n")
with open(MP, "w", encoding="utf-8", newline="") as f:
    f.write(t)

print("\n%d cambios aplicados." % len(CAMBIOS))
