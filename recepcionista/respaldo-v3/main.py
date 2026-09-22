# =============================================
# Recepcionista CJ MEDICAL - Pepe
# Bot de Telegram con IA vía OpenRouter
# =============================================

import asyncio
import json
import logging
import os
import re
import sys
from datetime import datetime, timedelta

from dotenv import load_dotenv

# ── Base de datos compartida con el CRM ──
sys.path.insert(0, os.path.dirname(__file__))
from crm.database import (
    init_db, get_or_create_client, save_message, get_client_detail,
    get_conversation, update_client_status, update_client_data, create_appointment
)
from openai import OpenAI
from anthropic import Anthropic
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from whatsapp_client import WhatsAppClient

# ── Estado en vivo para Command Center ──
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
try:
    from status.tracker import update_agent_status
    _STATUS_OK = True
except ImportError:
    _STATUS_OK = False
    def update_agent_status(*a, **kw): pass

# ── Cargar variables de entorno ──
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# ── Logging ──
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ── Cliente OpenRouter (fallback) ──
ai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
    default_headers={
        "HTTP-Referer": "https://cjmedical.com",
        "X-Title": "CJ Medical - Recepcionista Pepe",
    },
)

# ── Cliente OpenRouter (DeepSeek V4 Flash - primario) ──
# Anthropic deshabilitado por falta de créditos
anthropic_client = None

# ── Selección de modelo ──
PRIMARY_MODEL = "gpt-4o-mini"
FALLBACK_MODEL = "openai/gpt-4o-mini"

# ── Fecha actual en español ──
DIAS_ES = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
FECHA_HOY = datetime.now().strftime("%d/%m/%Y")
DIA_SEMANA = DIAS_ES[datetime.now().weekday()]

# ── Calcular fechas para los próximos 14 días ──
hoy = datetime.now()
prox = []
for i in range(14):
    d = hoy + timedelta(days=i)
    prox.append((DIAS_ES[d.weekday()], d.strftime("%d/%m/%Y")))

# Generar mapa completo de fechas
FECHAS_LINEAS = [f"Hoy es {DIA_SEMANA} {FECHA_HOY}."]
FECHAS_LINEAS.append(f"- mañana = {prox[1][1]} ({prox[1][0]})")
FECHAS_LINEAS.append(f"- pasado mañana = {prox[2][1]} ({prox[2][0]})")
# Para cada día, buscar "este [día]" (próxima ocurrencia en 0-6) y "próximo [día]" (en 7-13)
for d_name in DIAS_ES:
    # "este [día]" = primera ocurrencia en los próximos 7 días (incluyendo hoy)
    for i in range(0, 7):
        if prox[i][0] == d_name:
            label = "hoy" if i == 0 else f"este {d_name}" if i <= 6 else f"próximo {d_name}"
            FECHAS_LINEAS.append(f"- {'hoy' if i==0 else f'este {d_name}'} = {prox[i][1]} ({prox[i][0]})")
            break
    # "próximo [día]" = la siguiente semana (días 7-13)
    for i in range(7, 14):
        if prox[i][0] == d_name:
            FECHAS_LINEAS.append(f"- próximo {d_name} = {prox[i][1]} ({prox[i][0]})")
            break

FECHAS_AYUDA = "\n".join(FECHAS_LINEAS)

# =============================================
# SISTEMA - CONOCIMIENTO COMPLETO DE CJ MEDICAL
# =============================================

SYSTEM_PROMPT = f"""
# IDENTIDAD

Eres Pepe, el asistente de CJ Medical, departamento médico para el cuidado de tus cejas.

NO te presentes como "Pepe" ni como "recepcionista virtual" a menos que el cliente te pregunte explícitamente "¿quién eres?" o "¿cómo te llamas?". En el saludo inicial simplemente da la bienvenida sin presentarte.

CJ Medical es un departamento médico especializado en la salud, cuidado y recuperación de tus cejas.

Tiene dos sedes:
- Bogotá: Sede Chico Norte — Cra 11A #96-51 Edificio Oficity Local 102
- Medellín: Parque Comercial El Tesoro, Sótano 4 Plaza Norte, Cra 25A #1a sur - 45, Local 6100, Medellín

Hoy es {FECHA_HOY} ({DIA_SEMANA}).

{FECHAS_AYUDA}

# REGLA CRÍTICA: USO DE FECHAS

NO adivines fechas. Usa los datos de FECHAS_AYUDA.
- Si el cliente dice "viernes" busca en la lista cuándo cae viernes
- Si el cliente dice "mañana" es la fecha que dice la lista
- "próximo [día]" = el [día] de la semana siguiente
- Siempre usa las fechas exactas de la lista, no inventes

# REGLA FUNDAMENTAL

SÍ PUEDES AGENDAR CITAS. Tu función es: 1) Preparar solicitud, 2) Obtener confirmación del cliente, 3) La cita se agenda automáticamente y le envías confirmación.

Cuando el cliente confirme todos los datos:
✅ Di "Tu cita ha sido agendada exitosamente. Te esperamos."
✅ Di "Tu cita está confirmada."

IMPORTANTE: Si el cliente pide explícitamente hablar con un asesor humano, dile que lo transfieres y responde con la palabra "TRANSFERIR_ASESOR" en tu respuesta.

# PERSONAL

Medellín — C.C. El Tesoro:
- Valentina Vaquero — Cosmetóloga
- Dra. Julieth Arias — Médica
- Dr. Jorge Cueter — Médico

Bogotá — Chico Norte:
- Laura Martínez — Cosmetóloga
- Dr. Jorge Cueter — Médico

# HORARIOS

Lunes a viernes: 9:00 a. m. – 6:00 p. m.
Sábados: 9:00 a. m. – 4:00 p. m.
Domingos y festivos: No hay atención.
Anticipación mínima: 30 minutos (pero no significa que haya disponibilidad — el asesor verifica).

# FLUJO DE CAPTURA

Orden prioritario para nueva solicitud:
1. Ciudad
2. Sede (solo hay una por ciudad, se asigna automáticamente)
3. Servicio
4. Fecha
5. Hora
6. Nombre completo
7. Número celular
8. Correo electrónico
9. Documento de identidad

REGLAS CLAVE DEL FLUJO:
- Si el cliente ya dio un dato, NO lo vuelvas a preguntar
- Sé conversacional, no parezcas un formulario
- Responde primero las preguntas del cliente antes de continuar el flujo
- Si el cliente da toda la info de golpe, aprovéchala y solo pide lo faltante

# CATÁLOGO DE SERVICIOS COMPLETO

## Terapia de Revitalización
Terapia de revitalización folicular en cejas. Ayuda a prevenir la caída de los pelitos de las cejas, aporta y estimula el crecimiento, para que comiences a cuidar tus cejas de forma especializada.
- Bogotá: Laura Martínez (Cosmetóloga) | Medellín: Valentina Vaquero (Cosmetóloga)
- Duración: 30 min | Precio: $80.000 COP

## Masaje Relajante
Una experiencia sensorial diseñada para liberar tensiones, mejorar la circulación y recuperar el equilibrio físico y mental.
- ❌ No disponible en Bogotá
- ✅ Medellín: Valentina Vaquero (Cosmetóloga) | 1h 30min | $190.000 COP
- Si cliente de Bogotá lo pide: informa que solo en Medellín.

## Carbon Peel
Tratamiento láser que reduce poros, controla la grasa y unifica el tono de la piel. Efecto inmediato sin tiempo de recuperación.
- Bogotá: Laura Martínez (Cosmetóloga) | Medellín: Valentina Vaquero (Cosmetóloga)
- Duración: 1h
- 1 sesión: $150.000 COP
- Paquete 4 sesiones: $500.000 COP (ahorras $100.000)

## Hidrafacial
Limpieza, exfoliación, extracción e hidratación en un solo protocolo. Piel luminosa e hidratada de forma inmediata.
- Bogotá: Laura Martínez (Cosmetóloga) | Medellín: Valentina Vaquero (Cosmetóloga)
- Duración: 1h 30min
- Hidrafacial Básico: $275.000 COP
- Hidrafacial Plus (2 sesiones): $440.000 COP (protocolo avanzado de hidratación profunda)

## Casmara
Tratamiento profesional con máscaras Casmara. Hidratación, nutrición y efecto tensor para una piel visiblemente más joven.
- ❌ No disponible en Bogotá
- ✅ Medellín (C.C. El Tesoro): Valentina Vaquero (Cosmetóloga) | Precio: $360.000 COP
- Si cliente de Bogotá lo pide: informa que solo en Medellín.

## Peeling Químico
Exfoliación química controlada para renovar la piel en profundidad. Mejora manchas, textura y firmeza del rostro. Requiere valoración médica previa.
- ❌ No disponible en Bogotá
- ✅ Medellín: Dra. Julieth Arias (Médica) — sujeto a valoración médica | 1h | $330.000 COP
- Si cliente de Bogotá lo pide: informa que solo en Medellín con valoración médica.

## Depilación Láser
- Bogotá: Laura Martínez (Cosmetóloga) | Medellín: Valentina Vaquero (Cosmetóloga)
- Regla: si piden depilación, pregunta primero qué zona antes de dar precio.
- Precios por sesión: XS $60.000 | S $100.000 | M $150.000 | L $220.000 | XL $350.000
- Paquetes 8 sesiones: XS $360.000 | S $600.000 | M $840.000 | L $1.400.000 | XL $2.000.000
- Mantenimiento: XS $45.000 | S $75.000 | M $110.000 | L $180.000 | XL $260.000
- Depilación Nasal: $20.000 — solo Valentina Vaquero en Medellín (C.C. El Tesoro)
- Zonas: XS (bozo, entrecejo, patillas, línea alba) | S (axilas, bikini simple, dedos) | M (bikini completo, antebrazo, pantorrilla) | L (piernas completas, espalda, pecho, brazos) | XL (cuerpo completo)

## Remoción de Micropigmentación
- Bogotá: Dr. Jorge Cueter (Médico) | Medellín: Dr. Jorge Cueter / Dra. Julieth Arias (Médicos)
- Duración: 30 min
- Precios: 1 sesión $800.000 | 2 sesiones $1.200.000 | 3 sesiones $1.600.000 | 4 sesiones $1.900.000
- No determines cuántas sesiones necesita. Di: "El número de sesiones depende de la valoración del profesional."

## Valoración Inicial Médica
Permite que el médico valore al paciente y determine el tratamiento adecuado.
- Bogotá: Dr. Jorge Cueter (Médico) | Medellín: Dr. Jorge Cueter / Dra. Julieth Arias (Médicos)
- Duración: 1h | Precio: $100.000 COP
- Si preguntan "¿qué tratamiento necesito?": deriva a valoración médica.

## Botox
Aplicación de toxina botulínica para tratar líneas de expresión y arrugas dinámicas. Resultado suavizador y preventivo bajo supervisión médica.
- Bogotá: Dr. Jorge Cueter (Médico) | Medellín: Dr. Jorge Cueter / Dra. Julieth Arias (Médicos)
- Duración: 30 min | Precio: $25.000 COP por unidad
- No determines cuántas unidades necesita. Di: "La cantidad de unidades depende de la zona a tratar y será determinada por el médico."

## Radiofrecuencia Fraccionada
Tecnología de radiofrecuencia fraccionada de alta intensidad para estimular el colágeno, mejorar la textura y tensar la piel. Sin tiempo de recuperación.
- ❌ No disponible en Bogotá
- ✅ Medellín: Dr. Jorge Cueter (Médico) | Precio: $540.000 COP

## RF Fraccionada + Exosomas
La sinergia más avanzada: Radiofrecuencia Fraccionada de Alta Intensidad combinada con Exosomas regeneradores. Efecto antiedad y regenerativo superior.
- ❌ No disponible en Bogotá
- ✅ Medellín: Dr. Jorge Cueter (Médico) | Precio: $1.200.000 COP

Cuando diga su nombre: "Mucho gusto, [NOMBRE]" y continúa con el flujo.

Cuando el cliente mencione "terapia" o "terapia de cejas", siempre se refiere a "Terapia de Revitalización". No preguntes qué terapia, es esa.

# REGLA CRÍTICA: MEMORIA DE CIUDAD Y SEDE

Una vez que el cliente diga su ciudad (Bogotá o Medellín), esa ciudad NO cambia por el resto de la conversación.
- Si el cliente dice "Medellín" → la sede es C.C. El Tesoro. PUNTO. No la cambies a Chico Norte.
- Si el cliente dice "Bogotá" → la sede es Chico Norte. PUNTO. No la cambies a El Tesoro.
- Si el cliente corrige la ciudad, actualízala. Pero si no la corrige, mantén la que dijo originalmente.
- En el resumen final, la ciudad y sede deben coincidir con lo que el cliente dijo, NO con lo que tú asumas.

# CIUDAD Y SEDE

Pregunta: "¿Desde qué ciudad nos estás contactando: Bogotá o Medellín?"

Si es Bogotá: "Perfecto. En Bogotá contamos con nuestra sede de Chico Norte."
Si es Medellín: "Perfecto. En Medellín contamos con nuestra sede ubicada en el Centro Comercial El Tesoro."

No preguntes sede si solo hay una en esa ciudad.

# RESUMEN FINAL

Cuando todos los datos estén completos, muestra un mensaje limpio y profesional:

Excelente, [NOMBRE]. Antes de agendar tu cita, quiero confirmar que toda la información esté correcta:

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

# CONFIRMACIÓN

Si el cliente confirma la cita después de que el asesor le haya enviado una confirmación:
responde algo como: "Qué bien, [nombre]. Su cita de [servicio] para el [fecha] a las [hora] en [sede] ha sido confirmada. Te esperamos. Si necesitas agendar otro servicio o tienes alguna duda, estoy aquí para ayudarte."

IMPORTANTE: No debes decir que la cita quedó agendada si el asesor no ha confirmado. Pero si el asesor ya confirmó y el cliente dice "sí confirmo", entonces SÍ puedes decir que está confirmada.

Si el cliente corrige: actualiza solo ese dato y muestra resumen de nuevo.

# CLIENTE CON CITA EXISTENTE

Si un cliente ya tiene una cita agendada y vuelve a escribir:
- Si dice "quiero mover mi cita" o "reprogramar": inicia flujo de reprogramación y la cita vuelve a "pendiente" para que el asesor gestione.
- Si dice "quiero cancelar": inicia flujo de cancelación.
- Si dice "quiero agendar otro servicio": puedes agendar un nuevo servicio aunque ya tenga otra cita. No hay problema con tener múltiples citas de servicios diferentes.
- Siempre informa al cliente sobre su cita existente cuando sea relevante.

Ejemplo:
Cliente: "Quiero agendar otro servicio"
Pepe: "Claro. Veo que ya tienes una cita de Carbon Peel para el sábado. ¿Qué servicio adicional te gustaría agendar?"

# MÚLTIPLES CITAS

El cliente puede tener varias citas agendadas al mismo tiempo (ej: Carbon Peel y Depilación Láser). No hay restricción. Cada nueva solicitud de cita sigue el flujo normal: ciudad → sede → servicio → fecha → hora → datos → resumen → asesor.

# ESCALAMIENTO A ASESOR

Pasa a humano cuando:
- Cliente lo solicite
- Cancelación definitiva
- Problema con cita existente
- Queja
- Situación médica compleja
- Cliente pida diagnóstico
- Pregunta fuera de tu conocimiento
- Problema de pago

# MÚLTIPLES SERVICIOS

Si el cliente quiere varios servicios:
1. Identifica cada servicio y sus precios individuales
2. Muestra el subtotal estimado sumando los precios
3. IMPORTANTE: Verifica si los servicios pueden realizarse el mismo día o requieren espaciado
4. Aclara que es un estimado: "Este es un valor estimado. El asesor confirmará los precios finales y verificará la programación."

# REGLA DE ESPACIADO ENTRE SERVICIOS

Algunos tratamientos faciales NO pueden realizarse el mismo día y requieren un intervalo mínimo:

- Carbon Peel + Hidrafacial: deben realizarse con 15 días de diferencia (no el mismo día)
- Carbon Peel + Peeling Químico: deben espaciarse (consultar con asesor)
- Peeling Químico + Hidrafacial: deben espaciarse (consultar con asesor)
- Los tratamientos con láser o químicos en general no se combinan el mismo día con otros faciales

Si el cliente pide servicios que no pueden hacerse juntos, informa:
"Estos dos tratamientos son faciales y requieren un intervalo de [X] días entre uno y otro. ¿Te gustaría agendar primero uno y dejar el otro para después? El asesor te confirmará la mejor programación."

Ejemplo:
Cliente: "Quiero Carbon Peel e Hidrafacial"
Pepe: "Claro 😊 El Carbon Peel ($150.000) y el Hidrafacial Básico ($275.000) dan un total estimado de $425.000. Sin embargo, estos dos tratamientos faciales deben realizarse con 15 días de diferencia. Podemos agendar primero el Carbon Peel y programar el Hidrafacial para 15 días después. ¿Te parece bien?"

# REPROGRAMACIÓN

Si pide cambiar cita: pregunta nueva fecha y hora, luego resumen → confirmación → asesor.

# CANCELACIÓN

Si pide cancelar: pregunta si reprogramar o cancelar definitivamente.
- Reprogramar: nueva fecha y hora → resumen → asesor.
- Cancelar definitivamente: transferir a asesor.

# PQRS (QUEJAS, PETICIONES, RECLAMOS, SUGERENCIAS)

Si el cliente expresa una queja, reclamo, está inconforme o tiene un problema:
1. No intentes resolverlo con IA
2. Responde: "Entiendo, voy a escalar su caso al área de PQRS para que un asesor humano lo atienda personalmente. En breve se comunicarán con usted."
3. Automáticamente se cambiará al estado PQRS y un asesor lo manejará desde el CRM.
4. Mientras esté en PQRS, la IA solo responderá que un asesor se comunicará con el cliente.

# REGLAS ABSOLUTAS

1. Nunca inventes información
2. Nunca inventes disponibilidad
3. Nunca confirmes una cita que no haya sido agendada por un asesor
4. Siempre prioriza CIUDAD → SEDE → SERVICIO → FECHA → HORA
5. Después recopila NOMBRE → CELULAR → CORREO → DOCUMENTO
6. Nunca vuelvas a preguntar información ya proporcionada
7. NUNCA saludes como si fuera la primera vez si ya estás en medio de una conversación. Si el cliente ya te dio su nombre, no le preguntes "¿Con quién tengo el gusto de hablar?" otra vez.
8. Si el cliente ya eligió ciudad, sede, servicio, fecha u hora, NO preguntes esas cosas de nuevo. Continúa desde donde iba la conversación.
9. Nunca diagnostiques
10. Nunca determines unidades de Botox
11. Nunca determines número de sesiones de micropigmentación
12. Nunca garantices resultados médicos o estéticos
13. Si un servicio no está disponible en la sede, informa y ofrece alternativa
14. Si no sabes algo, no lo inventes — escala a asesor
15. Antes de entregar al asesor, muestra resumen completo y pide confirmación
16. Tus respuestas deben ser conversacionales y naturales, no un interrogatorio
17. Usa emojis 😊 para mantener un tono cálido

# TONO

Profesional, amable, natural, comercial (sin presionar), claro y eficiente. Trata a los clientes de "tú".

# REGLAS DE ESTILO OBLIGATORIAS

1. NO uses emojis en tus respuestas EXCEPTO en el mensaje de resumen final (cuando pides confirmar los datos del cliente). Ahí SÍ puedes usar emojis sutiles y elegantes.
2. NO uses asteriscos (*) ni negritas ni cursivas ni ningún formato markdown. Solo texto plano.
3. NO uses "podemos" ni "te podemos" ni "vamos a". Usa "puede ser", "puedes", "se puede agendar".
4. NO digas "Podemos ser mañana" ni "Podemos el lunes". Di: "Puede ser mañana" o "Se puede agendar para el lunes".
5. El tono debe ser amable y profesional, pero sin exceso de formalismo.
6. NO saludes con emoji. Solo texto.
7. Escribe siempre con ORTOGRAFÍA PERFECTA. Tildes, signos de interrogación y exclamación, comas, puntos. Cada mensaje debe estar bien escrito. La ortografía es fundamental para el servicio al cliente.

# FORMATO DEL RESUMEN FINAL (con emojis permitidos)

Cuando todos los datos estén completos, muestra un mensaje limpio y profesional así:

Excelente, [NOMBRE]. Antes de agendar tu cita, quiero confirmar que toda la información esté correcta:

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

Usa estos emojis SOLO en este mensaje de confirmación. En el resto de la conversación no uses emojis.
"""
# ── Fin del SYSTEM_PROMPT ──


# ── Bienvenida (según spec) ──
WELCOME_MESSAGE = (
    "Bienvenido a CJ Medical, departamento médico especializado en la salud, cuidado y recuperación de tus cejas.\n\n"
    "¿Con quién tengo el gusto de hablar?"
)


# ── Comando /start ──
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Resetear historial para empezar de nuevo
    user_id = str(user.id)
    if "chat_history" in context.bot_data and user_id in context.bot_data["chat_history"]:
        context.bot_data["chat_history"][user_id] = []
    logger.info(f"Usuario inició chat: {user.full_name} (@{user.username})")
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode="Markdown")


# ── Comando /help ──
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Comandos disponibles:*\n\n"
        "/start - Iniciar conversación con Pepe\n"
        "/help - Mostrar esta ayuda\n"
        "/horario - Ver horarios de atención\n"
        "/sedes - Ver ubicaciones de nuestras sedes\n"
        "/servicios - Ver nuestro catálogo de servicios\n"
        "/asesor - Hablar con un asesor humano",
        parse_mode="Markdown",
    )


# ── Comando /horario ──
async def horario(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🕐 *Horarios de Atención CJ Medical*\n\n"
        "📅 *Lunes a viernes:* 9:00 a. m. – 6:00 p. m.\n"
        "📅 *Sábados:* 9:00 a. m. – 4:00 p. m.\n"
        "🚫 *Domingos y festivos:* No hay atención\n\n"
        "⏱ *Anticipación:* Mínimo 30 minutos para solicitar cita.\n\n"
        "_*Nota:_ La disponibilidad real la verifica un asesor humano._",
        parse_mode="Markdown",
    )


# ── Comando /sedes ──
async def sedes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📍 *Nuestras Sedes*\n\n"
        "🏙️ *Bogotá — Chico Norte*\n"
        "   Cra 11A #96-51 · Edificio Oficity · Local 102\n\n"
        "🏙️ *Medellín — C.C. El Tesoro*\n"
        "   Parque Comercial El Tesoro, Sótano 4 Plaza Norte · Cra 25A #1a sur - 45 · Local 6100\n\n"
        "¿Desde qué ciudad nos escribes? 😊",
        parse_mode="Markdown",
    )


# ── Comando /servicios ──
async def servicios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✨ *Catálogo de Servicios CJ Medical*\n\n"
        "1️⃣ *Terapia de Revitalización* — $80.000 (30 min)\n"
        "2️⃣ *Masaje Relajante* — $190.000 *Solo Medellín*\n"
        "3️⃣ *Carbon Peel* — $150.000 / Paq.4 $500.000\n"
        "4️⃣ *Hidrafacial* Básico $275.000 / Plus $440.000\n"
        "5️⃣ *Casmara* — $360.000 *Solo Medellín*\n"
        "6️⃣ *Peeling Químico* — $330.000 *Solo Medellín*\n"
        "7️⃣ *Depilación Láser* — Desde $60.000 según zona\n"
        "8️⃣ *Depilación Nasal* — $20.000 *Solo Medellín*\n"
        "9️⃣ *Remoción Micropigmentación* — Desde $800.000\n"
        "🔟 *Valoración Médica* — $100.000\n"
        "1️⃣1️⃣ *Botox* — $25.000/unidad\n"
        "1️⃣2️⃣ *Radiofrecuencia* — $540.000 *Solo Medellín*\n"
        "1️⃣3️⃣ *RF + Exosomas* — $1.200.000 *Solo Medellín*\n\n"
        "¿Te gustaría agendar alguno de estos? 😊",
        parse_mode="Markdown",
    )


# ── Comando /asesor ──
async def asesor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔄 Estoy transfiriendo tu consulta a un *asesor humano* de CJ Medical.\n\n"
        "En breve alguien de nuestro equipo se comunicará contigo para ayudarte.\n\n"
        "¡Gracias por tu paciencia! 😊",
        parse_mode="Markdown",
    )


# ── Llamar a la IA ──
def clean_response(text: str) -> str:
    """Solo limpia asteriscos y guiones bajos (markdown). No toca emojis ni saltos de línea."""
    import re
    text = re.sub(r'\*+', '', text)
    text = re.sub(r'_+', '', text)
    return text.strip()

def ask_pepe(user_message: str, history: list = None) -> str:
    """Envía el mensaje a Anthropic (Claude Opus 5) o OpenRouter (fallback)."""
    # ── Reportar estado en vivo ──
    update_agent_status("recep", doing="Atendiendo cliente", task=user_message[:80], status="active", walk_x=0, walk_z=-0.9)
    # También activar wa-sender si toca enviar algo
    update_agent_status("wa-sender", doing="Preparando envío", status="idle")

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Agregar historial reciente (últimos 5 intercambios)
    if history:
        for msg in history[-20:]:
            messages.append(msg)

    messages.append({"role": "user", "content": user_message})

    # ── DeepSeek V4 Flash via OpenRouter (con fallback GPT-4o-mini) ──
    try:
        response = ai_client.chat.completions.create(
            model=PRIMARY_MODEL,
            messages=messages,
            max_tokens=1200,
            temperature=0.7,
        )
        update_agent_status("recep", doing="Cliente atendido", task="Esperando próximo mensaje", status="idle", walk_x=None, walk_z=None)
        return clean_response(response.choices[0].message.content)
    except Exception as e:
        logger.error(f"Error con DeepSeek V4: {e}, usando fallback GPT-4o-mini")
        try:
            response = ai_client.chat.completions.create(
                model=FALLBACK_MODEL,
                messages=messages,
                max_tokens=1200,
                temperature=0.7,
            )
            update_agent_status("recep", doing="Cliente atendido", task="Esperando próximo mensaje", status="idle", walk_x=None, walk_z=None)
            return clean_response(response.choices[0].message.content)
        except Exception as e2:
            logger.error(f"Error al llamar a OpenRouter: {e2}")
            return (
                "Lo siento, estoy teniendo problemas para conectarme en este momento. "
                "Por favor, intenta de nuevo en unos segundos o usa /asesor para hablar "
                "directamente con un miembro del equipo de CJ Medical."
            )


# ── Manejar mensajes de texto ──
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = update.message.text.strip()
    telegram_id = str(user.id)
    user_name = user.full_name or user.first_name or "Cliente"
    logger.info(f"Mensaje de {user_name}: {text[:60]}...")

    # ── Guardar en base de datos ──
    # Obtener o crear cliente
    client = get_or_create_client(telegram_id, user_name)

    # Actualizar nombre si el cliente no tiene nombre aún (primera vez)
    if not client.get("name") or client["name"] == "Cliente":
        update_client_data(client["id"], name=user_name)

    # Guardar mensaje del cliente en DB
    save_message(client["id"], "client", text, channel="telegram")

    # Si es nuevo, cambiar a "en_conversacion"
    if client["status"] == "nuevo":
        update_client_status(client["id"], "en_conversacion", "Pepe Bot")

    # Mostrar "escribiendo..." mientras la IA procesa
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing",
    )

    # Recuperar historial del contexto (almacenado por usuario en memoria)
    user_id = str(user.id)
    if "chat_history" not in context.bot_data:
        context.bot_data["chat_history"] = {}
    if user_id not in context.bot_data["chat_history"]:
        context.bot_data["chat_history"][user_id] = []

    history = context.bot_data["chat_history"][user_id]

    # ── Verificar si el cliente tiene mensajes en DB (no es nuevo) ──
    db_conversation = get_conversation(client["id"])
    db_user_msgs = [m for m in db_conversation if m['role'] in ('client', 'user')]
    is_new_client = client['status'] in ('nuevo',) or len(db_user_msgs) <= 1

    # Si el historial en memoria está vacío pero el cliente tiene mensajes en DB, reconstruir desde DB
    if len(history) <= 1 and not is_new_client:
        db_history = []
        for msg in db_conversation:
            if msg['role'] in ('client', 'user'):
                db_history.append({"role": "user", "content": msg['content']})
            elif msg['role'] == 'bot':
                db_history.append({"role": "assistant", "content": msg['content']})
        if db_history:
            # Mantener últimos 20 intercambios
            context.bot_data["chat_history"][user_id] = db_history[-30:]
            history = context.bot_data["chat_history"][user_id]
            logger.info(f"♻️ Historial reconstruido desde DB: {len(history)} mensajes para {user_name}")

    # ── Obtener respuesta de Pepe ──
    if is_new_client:
        reply = WELCOME_MESSAGE
        logger.info(f"👋 Primer mensaje de {user_name} - bienvenida CJ Medical")
    else:
        # Si el cliente está en PQRS o el asesor desactivó la IA, respuesta manual
        # Si el cliente confirmó (dijo "si" y está pendiente), responder confirmación directamente
        text_lower = text.lower()
        confirm_words = ["confirmo", "confirmado", "confirmada", "confirmo asistencia", "sí confirmo", "si confirmo"]
        affirm_words = ["sí", "si", "ok", "okey", "okay", "bueno", "dale", "listo", "procedo", "procede", "perfecto", "de acuerdo", "está bien", "esta bien"]
        is_yes = bool(re.search(r'\bs[ií]\b', text_lower)) and len(text_lower.split()) <= 3
        is_confirm_phrase = any(p in text_lower for p in confirm_words)
        words = text_lower.strip().split()
        is_affirm = len(words) <= 3 and any(w in affirm_words or text_lower.strip() in affirm_words for w in words)
        is_confirm_yes = is_yes or is_confirm_phrase or is_affirm
        
        if client["status"] == "pqrs" or client.get("ai_disabled"):
            if client["status"] == "pqrs":
                reply = "Su caso ha sido remitido al area de PQRS de CJ Medical. Un asesor humano se comunicara con usted lo antes posible para atender su solicitud. Agradecemos su paciencia."
                logger.info(f"🚨 Cliente {user_name} en PQRS - respuesta automática")
            else:
                reply = "La asistencia virtual esta desactivada para su caso. Un asesor humano de CJ Medical se comunicara con usted para atender su solicitud. Gracias por su comprension."
                logger.info(f"🔇 Cliente {user_name} con IA desactivada - respuesta automática")
        elif is_confirm_yes and client["status"] == "pendiente":
            # El cliente confirmó la cita después de que el asesor envió confirmación
            reply = f"Que bien, {client.get('name') or '!'} Su cita ha sido confirmada. Te esperamos en CJ Medical. Si necesitas agendar otro servicio o tienes alguna duda, estoy aqui para ayudarte."
            logger.info(f"✅ Cliente {user_name} confirmó cita - respuesta automática")
        else:
            # Pepe espera 5s para sentirse más humano
            await asyncio.sleep(5)
            reply = ask_pepe(text, history)

    # ── Extraer datos del cliente de sus propios mensajes ──
    # Si el cliente menciona un número de teléfono, email o documento, guardarlo
    email_from_user = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)
    if email_from_user and not client.get("email"):
        update_client_data(client["id"], email=email_from_user.group(0))
        logger.info(f"📧 Email capturado: {email_from_user.group(0)}")
    # Teléfono: número de 7-15 dígitos, priorizar los que empiezan con 3 (celular Colombia)
    all_nums = re.findall(r'\b(\d{7,15})\b', text)
    for num in all_nums:
        if not client.get("phone") and (num.startswith('3') and len(num) == 10):
            update_client_data(client["id"], phone=num)
            logger.info(f"📱 Teléfono capturado: {num}")
    # Documento: números de 5-15 dígitos que NO sean teléfono
    for num in all_nums:
        if not client.get("document"):
            if not client.get("phone") or num != client.get("phone"):
                if len(num) >= 5 and not (num.startswith('3') and len(num) == 10):
                    update_client_data(client["id"], document=num)
                    logger.info(f"🪪 Documento capturado: {num}")

    # ── Guardar en DB la respuesta del bot ──
    save_message(client["id"], "bot", reply, channel="telegram")

    # ── Detectar resumen de cita → guardar datos y pasar a "pendiente" ──
    if "Antes de enviar" in reply or "toda la información esté correcta" in reply or "toda la información de tu solicitud" in reply or "resumen de tu solicitud" in reply:
        # Extraer datos de la cita del resumen de Pepe (sin emojis - clean_response los elimina)
        city_m = re.search(r"ciudad:\s*(.+)", reply, re.IGNORECASE)
        loc_m = re.search(r"sede:\s*(.+)", reply, re.IGNORECASE)
        svc_m = re.search(r"servicio:\s*(.+)", reply, re.IGNORECASE)
        date_m = re.search(r"fecha:\s*(.+)", reply, re.IGNORECASE)
        time_m = re.search(r"hora:\s*(.+)", reply, re.IGNORECASE)
        name_m = re.search(r"nombre:\s*(.+)", reply, re.IGNORECASE)
        phone_m = re.search(r"celular:\s*(.+)", reply, re.IGNORECASE)
        email_m = re.search(r"correo:\s*(.+)", reply, re.IGNORECASE)
        doc_m = re.search(r"documento:\s*(.+)", reply, re.IGNORECASE)
        # Actualizar datos del cliente
        if name_m: update_client_data(client["id"], name=name_m.group(1).strip().title())
        if phone_m: update_client_data(client["id"], phone=phone_m.group(1).strip())
        if email_m: update_client_data(client["id"], email=email_m.group(1).strip())
        if doc_m: update_client_data(client["id"], document=doc_m.group(1).strip())
        # Guardar cita en appointments con especialista auto-detectado
        if svc_m or city_m or date_m or time_m:
            svc_str = svc_m.group(1).strip() if svc_m else ""
            city_str = city_m.group(1).strip() if city_m else ""
            prof = None
            s_lower = svc_str.lower()
            c_lower = city_str.lower()
            if "terapia" in s_lower: prof = "Valentina Vaquero" if "medell" in c_lower else "Laura Martínez"
            elif "masaje" in s_lower: prof = "Valentina Vaquero"
            elif "carbon" in s_lower: prof = "Valentina Vaquero" if "medell" in c_lower else "Laura Martínez"
            elif "hidra" in s_lower: prof = "Valentina Vaquero" if "medell" in c_lower else "Laura Martínez"
            elif "casmara" in s_lower: prof = "Valentina Vaquero"
            elif "peeling" in s_lower: prof = "Dra. Julieth Arias"
            elif "depil" in s_lower: prof = "Valentina Vaquero" if "medell" in c_lower else "Laura Martínez"
            elif "micropigment" in s_lower: prof = "Dr. Jorge Cueter" if "bogot" in c_lower else "Dra. Julieth Arias"
            elif "valoracion" in s_lower or "valoración" in s_lower: prof = "Dr. Jorge Cueter"
            elif "botox" in s_lower: prof = "Dr. Jorge Cueter"
            elif "radiofrecuencia" in s_lower: prof = "Dr. Jorge Cueter"
            elif "exosomas" in s_lower: prof = "Dr. Jorge Cueter"
            create_appointment(client["id"], {
                "city": city_str,
                "location": loc_m.group(1).strip() if loc_m else None,
                "service": svc_str,
                "professional": prof,
                "date": date_m.group(1).strip() if date_m else None,
                "time": time_m.group(1).strip() if time_m else None,
            })
            logger.info(f"📅 Cita guardada para {user_name}")
        # Pasar a pendiente
        if "asesor de CJ Medical verificará" in reply or "agendará la cita" in reply:
            update_client_status(client["id"], "pendiente", "Pepe Bot")
            logger.info(f"📋 Cliente {user_name} → Pendiente por agendar")

    # ── Detectar confirmación del cliente → pasar a "agendado" ──
    text_lower = text.lower()
    # Palabras y frases de confirmación
    confirm_words = ["confirmo", "confirmado", "confirmada", "confirmo asistencia", "sí confirmo", "si confirmo"]
    affirm_words = ["sí", "si", "ok", "okey", "okay", "bueno", "dale", "listo", "procedo", "procede", "perfecto", "de acuerdo", "está bien", "esta bien"]
    # Detectar "sí" o "si" como palabra completa
    is_yes = bool(re.search(r'\bs[ií]\b', text_lower)) and len(text_lower.split()) <= 3
    # Detectar frases de confirmación explícitas
    is_confirm_phrase = any(p in text_lower for p in confirm_words)
    # Detectar afirmaciones cortas (ok, bien, bueno, dale, listo, etc)
    words = text_lower.strip().split()
    is_affirm = len(words) <= 3 and any(w in affirm_words or text_lower.strip() in affirm_words for w in words)
    is_confirm = is_yes or is_confirm_phrase or is_affirm
    if is_confirm and client["status"] == "pendiente":
        update_client_status(client["id"], "agendado", "Pepe Bot")
        conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
        conn.execute("UPDATE appointments SET status = 'agendado' WHERE client_id = ? AND status = 'pendiente'", (client["id"],))
        conn.commit()
        conn.close()
        logger.info(f"✅ Cliente {user_name} confirmó cita → Agendado")
        # Agendar automáticamente en la agenda PostgreSQL
        try:
            conn_a = get_connection()
            cur_a = conn_a.cursor()
            cur_a.execute("SELECT service, city, date_requested, time_requested, professional FROM appointments WHERE client_id=? AND status='agendado' ORDER BY id DESC LIMIT 1", (client["id"],))
            row_a = cur_a.fetchone()
            if row_a:
                svc, city, dt, tm, prof = row_a
                sede_id = None
                if city and "medell" in city.lower(): sede_id = "sede-cj-medical-el-tesoro"
                elif city and "bogot" in city.lower(): sede_id = "sede-cj-medical-bogota"
                svc_map = {"terapia":"srv-terapias-de-revitalizacion","masaje":"srv-masaje-de-relajacion","carbon":"srv-carbon-peel","hidra":"srv-hidrofacial-basica","botox":"srv-toxina-botox","depil":"srv-1-sesion-zona-m","radio":"srv-radiofrecuencia-fraccionada-alta-intensidad","micropig":"srv-remocion-micropigmentacion-1-sesion","diseno":"srv-diseno-de-cejas","tintura":"srv-tintura-de-cejas"}
                svc_id = None
                for k, v in svc_map.items():
                    if k in svc.lower(): svc_id = v; break
                if sede_id and svc_id and dt:
                    import httpx
                    esp_id = None
                    if prof:
                        esp_map = {"valentina":"esp-valentina-rivillas-baquero-42","julie":"esp-julie-viviana-arias-hernandez-20","jorge":"esp-jorge-ramiro-cueter-guzman-17","laura":"esp-laura-marithza-martinez-martinez-23","manuela":"esp-manuela-betancur-agudelo-28","diana":"esp-diana-carolina-ruiz-rojas","martha":"esp-martha-isabel-lopez-suarez"}
                        for k, v in esp_map.items():
                            if k in prof.lower(): esp_id = v; break
                    if not esp_id:
                        r = httpx.post("http://127.0.0.1:8001/huecos/buscar", json={"sede":sede_id,"servicio":svc_id,"dias":14,"limite":1}, timeout=5)
                        huecos = r.json()
                        if huecos:
                            esp_id = huecos[0]["especialista_id"]
                            if not tm: tm = huecos[0]["inicio"][:5]
                    if esp_id:
                        r = httpx.post("http://127.0.0.1:8001/cupos/apartar", json={"especialista":esp_id,"sede":sede_id,"fecha":str(dt)[:10],"inicio":str(tm)[:5],"servicio":svc_id,"referencia":"pepe-bot"}, timeout=5)
                        rid = r.json().get("id","")
                        r2 = httpx.post("http://127.0.0.1:8001/citas/agendar", json={"cliente_id":"","especialista":esp_id,"sede":sede_id,"fecha":str(dt)[:10],"inicio":str(tm)[:5],"servicio":svc_id,"canal":"WhatsApp","por":"pepe","reserva":rid}, timeout=5)
                        if r2.status_code == 200:
                            httpx.post("http://127.0.0.1:8001/citas/estado", json={"cita_id":r2.json().get("id",""),"estado":"est-confirmado","por":"pepe"}, timeout=5)
                            logger.info(f"Cita agendada automaticamente por Pepe: {dt} {tm} {svc}")
            conn_a.close()
        except Exception as ex:
            logger.warning(f"Agenda no disponible: {ex}")

    # ── Detectar solicitud de reprogramación → pasar a "pendiente" ──
    if any(p in text.lower() for p in ["mover mi cita", "reprogramar", "cambiar mi cita", "cancelar"]) and client["status"] == "agendado":
        update_client_status(client["id"], "pendiente", "Pepe Bot")
        logger.info(f"🔄 Cliente {user_name} solicita cambio → Pendiente")

    # ── Detectar queja/reclamo → pasar a "pqrs" ──
    pqrs_keywords = ["queja", "reclamo", "petición", "sugerencia", "me quejo", "inconforme", "devolución", "problema con la cita", "mala atención", "error en", "cobro indebido"]
    if any(p in text.lower() for p in pqrs_keywords):
        update_client_status(client["id"], "pqrs", "Pepe Bot")
        logger.info(f"🚨 Cliente {user_name} → PQRS (queja/reclamo)")

    # ── Extraer nombre completo del resumen final ("👤 Nombre: Juan Hernández") ──
    # Tiene prioridad sobre cualquier otro patrón porque ahí el cliente ya dio nombre y apellido.
    summary_name_match = re.search(r"👤\s*Nombre:\s*([^\n\r]+)", reply)
    if summary_name_match:
        full_from_summary = summary_name_match.group(1).strip().title()
        if (
            full_from_summary
            and 3 < len(full_from_summary) < 60
            and re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s.]+$', full_from_summary)
            and len(full_from_summary.split()) >= len((client.get("name") or "").split())
        ):
            if full_from_summary != (client.get("name") or ""):
                update_client_data(client["id"], name=full_from_summary)
                logger.info(f"📝 Nombre completo tomado del resumen final: {client.get('name')} → {full_from_summary}")
                client["name"] = full_from_summary

    # ── Extraer nombre del cliente de la respuesta de Pepe ──
    # Patrones: "Mucho gusto, [NOMBRE]", "Gracias, [NOMBRE]", "Listo, [NOMBRE]", "Perfecto, [NOMBRE]"
    name_match = re.search(r"(?:Mucho\s+gusto|Gracias|Listo|Perfecto|Excelente)[^,]*,\s*([^.¡!:\n]+)", reply, re.IGNORECASE)
    if name_match:
        extracted = name_match.group(1).strip().title()
        # Filtrar saludos genéricos y frases muy largas
        if extracted and len(extracted) > 2 and len(extracted) < 40 and extracted not in ("!", "😊"):
            # Verificar que sea un nombre real (solo letras, espacios, puntos)
            if re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s.]+$', extracted) and extracted != (client.get("name") or ""):
                update_client_data(client["id"], name=extracted)
                logger.info(f"📝 Nombre actualizado: {client.get('name')} → {extracted}")

    # ── Extraer nombre tambien de los mensajes del cliente ──
    # Si el cliente dice "mi nombre es [NOMBRE COMPLETO]" o "soy [NOMBRE COMPLETO]"
    user_name_patterns = [
        r"(?:mi\s+nombre\s+es|me\s+llamo|soy\s+el|soy\s+la|soy)\s+([A-Za-zÁÉÍÓÚáéíóúÑñ]+\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)",
        r"(?:nombre\s+completo\s+(?:es|:)\s*)([A-Za-zÁÉÍÓÚáéíóúÑñ]+\s+[A-Za-zÁÉÍÓÚáéíóúÑñ]+)",
    ]
    if not client.get("name") or len(client.get("name","").split()) < 2:
        for pattern in user_name_patterns:
            user_name_match = re.search(pattern, text, re.IGNORECASE)
            if user_name_match:
                full_name = user_name_match.group(1).strip().title()
                if len(full_name) > 3 and len(full_name) < 50:
                    if re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s.]+$', full_name):
                        update_client_data(client["id"], name=full_name)
                        logger.info(f"📝 Nombre completo extraído del cliente: {full_name}")
                        break

    # Guardar en historial en memoria
    history.append({"role": "user", "content": text})
    history.append({"role": "assistant", "content": reply})

    # Limitar historial (últimos 20 mensajes)
    if len(history) > 30:
        history = history[-30:]
        context.bot_data["chat_history"][user_id] = history

    await update.message.reply_text(reply)


# ── Tarea periódica: enviar respuestas de asesores pendientes ──
WHATSAPP_CLIENT = None  # Se asigna en init si WhatsApp está disponible

async def send_pending_replies(app: Application):
    """Revisa la tabla pending_replies y envía los mensajes al cliente por Telegram o WhatsApp."""
    import sqlite3
    from crm.database import DB_PATH, get_connection
    global WHATSAPP_CLIENT
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT pr.id, pr.client_id, pr.content, pr.advisor_name, c.telegram_id, c.phone
            FROM pending_replies pr
            JOIN clients c ON c.id = pr.client_id
            WHERE pr.sent = 0
            LIMIT 10
        """)
        pending = cursor.fetchall()
        for row in pending:
            reply_id, client_id, content, advisor_name, tg_id, phone = row
            try:
                msg = f"{advisor_name or 'Asesor'} de CJ Medical:\n\n{content}"
                sent = False

                # Intentar enviar por Telegram
                if tg_id:
                    try:
                        await app.bot.send_message(chat_id=int(tg_id), text=msg)
                        sent = True
                        logger.info(f"Respuesta enviada por Telegram a {tg_id}")
                    except Exception as e:
                        logger.warning(f"Telegram fallo para {tg_id}: {e}")

                # Si no tiene Telegram, intentar WhatsApp
                if not sent and phone and WHATSAPP_CLIENT is not None and WHATSAPP_CLIENT.status == "connected":
                    wa_phone = phone.strip()
                    if wa_phone.startswith("0"):
                        wa_phone = "57" + wa_phone[1:]
                    elif not wa_phone.startswith("57"):
                        wa_phone = "57" + wa_phone
                    await WHATSAPP_CLIENT.send_message(wa_phone, msg)
                    sent = True
                    logger.info(f"Respuesta enviada por WhatsApp a {wa_phone}")

                if sent:
                    conn.execute("UPDATE pending_replies SET sent = 1 WHERE id = ?", (reply_id,))
                    conn.commit()
            except Exception as e:
                logger.error(f"Error al enviar respuesta (id={reply_id}): {e}")
        conn.close()
    except Exception as e:
        logger.error(f"Error en pending_replies: {e}")


# ── Manejar mensajes de WhatsApp ──
async def handle_whatsapp_message(phone: str, text: str, timestamp: str):
    """Procesa un mensaje entrante de WhatsApp - misma logica que Telegram."""
    from crm.database import get_or_create_client, save_message, get_conversation
    global WHATSAPP_CLIENT

    if not text or not text.strip():
        return

    text = text.strip()
    client = get_or_create_client(phone, name=phone)
    if not client:
        logger.error(f"No se pudo crear cliente para {phone}")
        return

    # Guardar mensaje del cliente
    save_message(client["id"], text, "client")

    # Actualizar estado si es nuevo
    if client["status"] in ("nuevo",):
        from crm.database import update_client_status
        update_client_status(client["id"], "en_conversacion", "Pepe Bot")

    # Detectar PQRS
    pqrs_kw = ["queja","reclamo","peticion","sugerencia","me quejo","inconforme","devolucion","problema","mala atencion","cobro indebido"]
    if any(p in text.lower() for p in pqrs_kw):
        from crm.database import update_client_status
        update_client_status(client["id"], "pqrs", "Pepe Bot")
        logger.info(f"Cliente {phone} → PQRS (queja/reclamo)")

    # Obtener historial de conversacion
    history = get_conversation(client["id"])
    messages = []
    for msg in history[-20:]:
        role = "user" if msg["role"] == "client" else "assistant"
        messages.append({"role": role, "content": msg["content"]})

    # Obtener respuesta de la IA
    # Preparar historial para ask_pepe
    reply = ask_pepe(text, messages)

    # Guardar respuesta del bot
    save_message(client["id"], reply, "bot")

    # Enviar respuesta por WhatsApp
    if WHATSAPP_CLIENT and WHATSAPP_CLIENT.status == "connected":
        await WHATSAPP_CLIENT.send_message(phone, reply)
        logger.info(f"Mensaje enviado a {phone}: {reply[:60]}...")

# ── Manejar errores ──
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error en update {update}: {context.error}")
    if update and update.effective_message:
        await update.effective_message.reply_text(
            "Lo siento, ocurrió un error inesperado. Por favor, intenta de nuevo."
        )


# ── Main ──
def main():
    if not TELEGRAM_BOT_TOKEN:
        logger.error("❌ TELEGRAM_BOT_TOKEN no está configurado en .env")
        sys.exit(1)

    if not OPENROUTER_API_KEY:
        logger.error("❌ OPENROUTER_API_KEY no está configurada en .env")
        sys.exit(1)

    logger.info("🚀 Iniciando Pepe - Recepcionista CJ MEDICAL...")

    # ── Inicializar base de datos ──
    init_db()
    logger.info("🗄️ Base de datos inicializada")

    # ── Limpieza inicial: forzar cierre de sesiones colgadas ──
    async def cleanup_stale(app: Application):
        bot = app.bot
        logger.info("🧹 Limpiando sesiones previas de Telegram...")
        await bot.delete_webhook(drop_pending_updates=True)
        for _ in range(3):
            try:
                await asyncio.wait_for(bot.get_updates(offset=-1, timeout=0), timeout=2)
            except Exception:
                pass
            await asyncio.sleep(1)
        logger.info("✅ Sesiones limpiadas")

        # ── Iniciar WhatsApp ──
        # TEMPORAL: Deshabilitado para que Telegram funcione sin bloqueos
        # TODO: Implementar WhatsApp con EvolutionAPI en lugar de Playwright
        global WHATSAPP_CLIENT
        WHATSAPP_CLIENT = None
        logger.info("📱 WhatsApp deshabilitado temporalmente - usando solo Telegram")

        # ── Programar tarea periódica para enviar respuestas de asesores ──
        if app.job_queue:
            app.job_queue.run_repeating(send_pending_replies, interval=10, first=5)
            logger.info("⏰ Tarea de respuestas pendientes programada (cada 10s)")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).post_init(cleanup_stale).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("horario", horario))
    app.add_handler(CommandHandler("sedes", sedes))
    app.add_handler(CommandHandler("servicios", servicios))
    app.add_handler(CommandHandler("asesor", asesor))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    logger.info("✅ Pepe configurado. Iniciando polling...")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()