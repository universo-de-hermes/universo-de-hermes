with open("/root/universo/recepcionista/main.py", "r") as f:
    c = f.read()

# Fix: Solo actualizar nombre si el extraído tiene 2+ palabras (nombre+apellido)
# Esto evita que "Juan" sobreescriba "Juan Otero"

old = """        if extracted and len(extracted) > 2 and len(extracted) < 40 and extracted not in ("!", "😊"):
            # Verificar que sea un nombre real (solo letras, espacios, puntos)
            if re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s.]+$', extracted) and extracted != (client.get("name") or ""):
                update_client_data(client["id"], name=extracted)"""

new = """        if extracted and len(extracted) > 2 and len(extracted) < 40 and extracted not in ("!", "😊"):
            # Verificar que sea un nombre real (solo letras, espacios, puntos)
            # SOLO actualizar si tiene 2+ palabras (nombre + apellido) - no sobreescribir "Juan Otero" con "Juan"
            words = extracted.split()
            if len(words) >= 2 and re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\\s.]+$', extracted) and extracted != (client.get("name") or ""):
                update_client_data(client["id"], name=extracted)"""

if old in c:
    c = c.replace(old, new)
    with open("/root/universo/recepcionista/main.py", "w") as f:
        f.write(c)
    print("✅ Fix aplicado - nombres de 1 palabra ya no sobreescriben nombres completos")
else:
    print("❌ Texto no encontrado")
    # Debug
    lines = c.split("\n")
    for i, l in enumerate(lines, 1):
        if "extracted != (client.get" in l:
            start = max(0, i-4)
            end = min(len(lines), i+2)
            for j in range(start, end):
                print(f"  Line {j+1}: {repr(lines[j])}")