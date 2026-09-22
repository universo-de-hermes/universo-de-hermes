with open("/root/universo/recepcionista/main.py", "r") as f:
    c = f.read()

# ===== FIX 3: Timezone Colombia =====
# El VPS está en UTC, pero el usuario está en Colombia (UTC-5)
old3 = "from datetime import datetime, timedelta"
new3 = "from datetime import datetime, timedelta\nfrom datetime import timezone"

if old3 in c:
    c = c.replace(old3, new3)
    print("✅ Fix 3a: Import timezone")
else:
    print("❌ Fix 3a: No encontrado")

# Cambiar datetime.now() por datetime.now(timezone.utc) - 5 horas
old3b = "hoy = datetime.now()"
new3b = "hoy = datetime.now(timezone.utc) - timedelta(hours=5)  # UTC-5 Colombia"

if old3b in c:
    c = c.replace(old3b, new3b)
    print("✅ Fix 3b: Timezone Colombia (UTC-5)")
else:
    print("❌ Fix 3b: No encontrado, buscando...")
    if "FECHA_HOY = datetime.now()" in c:
        print("  Encontrado: FECHA_HOY")

# También cambiar FECHA_HOY
old3c = "FECHA_HOY = datetime.now().strftime(\"%d/%m/%Y\")"
new3c = "FECHA_HOY = (datetime.now(timezone.utc) - timedelta(hours=5)).strftime(\"%d/%m/%Y\")"
if old3c in c:
    c = c.replace(old3c, new3c)
    print("✅ Fix 3c: FECHA_HOY en Colombia")
else:
    print("❌ Fix 3c: No encontrado")

# Cambiar DIA_SEMANA
old3d = "DIA_SEMANA = DIAS_ES[datetime.now().weekday()]"
new3d = "DIA_SEMANA = DIAS_ES[(datetime.now(timezone.utc) - timedelta(hours=5)).weekday()]"
if old3d in c:
    c = c.replace(old3d, new3d)
    print("✅ Fix 3d: DIA_SEMANA en Colombia")
else:
    print("❌ Fix 3d: No encontrado")

with open("/root/universo/recepcionista/main.py", "w") as f:
    f.write(c)
print("✅ Archivo guardado con timezone Colombia")