with open("/root/universo/recepcionista/main.py", "r") as f:
    c = f.read()

# ===== 1. SYSTEM_PROMPT - Quitar referencias a asesor =====
c = c.replace(
    "Antes de enviar tu solicitud a nuestro asesor, quiero confirmar",
    "Antes de agendar tu cita, quiero confirmar"
)

c = c.replace(
    "LA IA NO AGENDA CITAS. Tu funci\u00f3n es SOLO preparar la solicitud. El asesor humano verifica disponibilidad, agenda en el sistema y confirma con el cliente.",
    "S\u00cd PUEDES AGENDAR CITAS. Tu funci\u00f3n es: 1) Preparar solicitud, 2) Obtener confirmaci\u00f3n del cliente, 3) La cita se agenda autom\u00e1ticamente y le env\u00edas confirmaci\u00f3n."
)

c = c.replace(
    'Nunca digas:\n\u274c "Tu cita qued\u00f3 agendada."\n\u274c "Tu cita est\u00e1 confirmada."\n\u274c "Te esperamos el viernes."\n\nDebes decir: "Perfecto. Ya tengo toda la informaci\u00f3n de tu solicitud. En unos minutos un asesor de CJ Medical verificar\u00e1 la disponibilidad y se encargar\u00e1 de confirmar tu reserva."',
    'Cuando el cliente confirme todos los datos:\n\u2705 Di "Tu cita ha sido agendada exitosamente. Te esperamos."\n\u2705 Di "Tu cita est\u00e1 confirmada."\n\nIMPORTANTE: Si el cliente pide expl\u00edcitamente hablar con un asesor humano, dile que lo transfieres y responde con la palabra "TRANSFERIR_ASESOR" en tu respuesta.'
)

c = c.replace(
    "Perfecto. Ya tengo toda la informaci\u00f3n de tu solicitud. En unos minutos un asesor de CJ Medical verificar\u00e1 la disponibilidad y se encargar\u00e1 de confirmar tu reserva.",
    "Perfecto. Enseguida proceso el agendamiento de tu cita."
)

c = c.replace("verificar\u00e1 la disponibilidad", "agendar\u00e1 la cita")

c = c.replace(
    "Un asesor humano de CJ Medical se comunicar\u00e1 con usted para atender su solicitud. Gracias por su comprensi\u00f3n.",
    "Por favor espera mientras proceso tu solicitud."
)

# ===== 2. Cuando cliente confirma, agendar en agenda API =====
old = '        if \"asesor de CJ Medical verificar\u00e1\" in reply or \"verificar\u00e1 la disponibilidad\" in reply:\n            update_client_status(client[\"id\"], \"pendiente\", \"Pepe Bot\")\n            logger.info(f\"\U0001f4cb Cliente {user_name} \u2192 Pendiente por agendar\")'
new = '''        if "cita va a quedar agendada" in reply or "agendar\u00e1 la cita" in reply or "proceso el agendamiento" in reply:
            update_client_status(client["id"], "pendiente", "Pepe Bot")
            logger.info(f"\U0001f4cb Cliente {user_name} \u2192 Pendiente por agendar")'''

c = c.replace(old, new)

# ===== 3. En la confirmaci\u00f3n (cliente dice s\u00ed), agendar autom\u00e1ticamente =====
old2 = '''    if is_confirm and client["status"] == "pendiente":
        update_client_status(client["id"], "agendado", "Pepe Bot")
        conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
        conn.execute("UPDATE appointments SET status = 'agendado' WHERE client_id = ? AND status = 'pendiente'", (client["id"],))
        conn.commit()
        conn.close()
        logger.info(f"\u2705 Cliente {user_name} confirm\u00f3 cita \u2192 Agendado")'''

new2 = '''    if is_confirm and client["status"] == "pendiente":
        update_client_status(client["id"], "agendado", "Pepe Bot")
        conn = __import__("crm.database", fromlist=["get_connection"]).get_connection()
        conn.execute("UPDATE appointments SET status = 'agendado' WHERE client_id = ? AND status = 'pendiente'", (client["id"],))
        conn.commit()
        conn.close()
        logger.info(f"\u2705 Cliente {user_name} confirm\u00f3 cita \u2192 Agendado")
        # Agendar autom\u00e1ticamente en la agenda PostgreSQL
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
            logger.warning(f"Agenda no disponible: {ex}")'''

if old2 in c:
    c = c.replace(old2, new2)
    print("OK: Confirmacion ahora agenda automaticamente")
else:
    print("FAIL: No se encontro old2")
    # Show what's around there
    import re
    m = re.search(r'if is_confirm and client.*pendiente.*update_client_status.*agendado.*logger', c, re.DOTALL)
    if m:
        print(f"Found: {repr(m.group()[:200])}")

with open("/root/universo/recepcionista/main.py", "w") as f:
    f.write(c)
print("OK: Guardado")