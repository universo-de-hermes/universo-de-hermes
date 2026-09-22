with open("/root/universo/recepcionista/main.py", "r") as f:
    c = f.read()
old = 'msg = f"{advisor_name or \'Asesor\'} de CJ Medical:\\n\\n{content}"'
new = "msg = content"
if old in c:
    c = c.replace(old, new)
    with open("/root/universo/recepcionista/main.py", "w") as f:
        f.write(c)
    print("✅ Reemplazado - mensaje limpio sin prefijo")
else:
    print("❌ Texto no encontrado")
    # Debug
    for i, line in enumerate(c.split("\n"), 1):
        if "msg = f" in line:
            print(f"  Line {i}: {repr(line)}")