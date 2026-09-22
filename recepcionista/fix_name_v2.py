with open("/root/universo/recepcionista/main.py", "r") as f:
    c = f.read()

# ===== FIX 1: Permitir nombre de 1 palabra cuando el actual es placeholder =====
# El problema: "Camila" (1 palabra) no sobreescribe "Juan jo" (Telegram display name)
# La solución: permitir si el nombre actual tiene 1 palabra o menos (placeholder)
old = """        if extracted and len(extracted) > 2 and len(extracted) < 40 and extracted not in ("!", "😊"):
            # Verificar que sea un nombre real (solo letras, espacios, puntos)
            # SOLO actualizar si tiene 2+ palabras (nombre + apellido) - no sobreescribir "Juan Otero" con "Juan"
            words = extracted.split()
            if len(words) >= 2 and re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s.]+$', extracted) and extracted != (client.get("name") or ""):
                update_client_data(client["id"], name=extracted)"""

new = """        if extracted and len(extracted) > 2 and len(extracted) < 40 and extracted not in ("!", "😊"):
            # Verificar que sea un nombre real (solo letras, espacios, puntos)
            current_words = len((client.get("name") or "").split())
            words = extracted.split()
            # Permitir si:
            # - 2+ palabras (nombre+apellido), o
            # - 1 palabra pero el nombre actual tiene solo 1 palabra o es placeholder (Telegram)
            if (len(words) >= 2 or (len(words) == 1 and current_words <= 1)) and re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s.]+$', extracted) and extracted != (client.get("name") or ""):
                update_client_data(client["id"], name=extracted)"""

if old in c:
    c = c.replace(old, new)
    print("✅ Fix 1: Nombres de 1 palabra actualizan si el actual es placeholder")
else:
    print("❌ Fix 1: No encontrado")

# ===== FIX 2: La fecha "mañana" - mejorar detección =====
# El problema: el cliente dice "Mañana 3 pm" y Pepe dice "10 de septiembre" cuando debería ser "9"
# El SYSTEM_PROMPT tiene fechas correctas, pero DeepSeek V4 Pro las ignora.
# Refuerzo la instrucción de fechas en el prompt.

old2 = """# REGLA CRÍTICA: USO DE FECHAS

NO adivines fechas. Usa los datos de FECHAS_AYUDA.
- Si el cliente dice \"viernes\" busca en la lista cuándo cae viernes
- Si el cliente dice \"mañana\" es la fecha que dice la lista
- \"próximo [día]\" = el [día] de la semana siguiente
- Siempre usa las fechas exactas de la lista, no inventes"""

new2 = """# REGLA CRÍTICA: USO DE FECHAS - ¡MUY IMPORTANTE!

NO adivines fechas. Usa SIEMPRE los datos de FECHAS_AYUDA.
- Si el cliente dice \"mañana\" = la fecha exacta que aparece en FECHAS_AYUDA como \"mañana\". NO la calcules.
- Si el cliente dice hoy = la fecha que dice FECHAS_AYUDA como \"Hoy es\"
- Si el cliente dice \"viernes\" busca en la lista cuándo cae viernes
- \"próximo [día]\" = el [día] de la semana siguiente
- IMPORTANTE: Nunca inventes fechas. Usa exclusivamente la lista FECHAS_AYUDA.
- Si el cliente dice \"Mañana 9 de septiembre\" significa que para él mañana es 9. Verifica FECHAS_AYUDA y responde con la fecha correcta."""

if old2 in c:
    c = c.replace(old2, new2)
    print("✅ Fix 2: Instrucción de fechas reforzada")
else:
    print("❌ Fix 2: No encontrado")

with open("/root/universo/recepcionista/main.py", "w") as f:
    f.write(c)
print("✅ Archivo guardado")