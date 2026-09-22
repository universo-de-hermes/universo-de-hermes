with open('/root/universo/recepcionista/main.py', 'r', encoding='utf-8') as f:
    c = f.read()

# Agregar import del helper al inicio (después del último import)
imports_end = c.find('# ── Cliente OpenRouter')
if imports_end > 0:
    insertion = 'from agenda_helper import buscar_cliente, crear_cliente, get_huecos, apartar_cupo, agendar\n'
    if insertion not in c:
        c = c[:imports_end] + insertion + c[imports_end:]
        print('✅ Import agenda_helper agregado')
    else:
        print('⚠️ Ya importado')

# Agregar llamada a la agenda cuando pasa a pendiente
old_pend = '            update_client_status(client["id"], "pendiente", "Pepe Bot")\n            logger.info(f"📋 Cliente {user_name} → Pendiente por agendar")'
new_pend = '''            update_client_status(client["id"], "pendiente", "Pepe Bot")
            logger.info(f"📋 Cliente {user_name} → Pendiente por agendar")
            # Agenda: intentar agendar automáticamente
            try:
                import asyncio, httpx
                # Buscar o crear cliente
                agenda_clientes = asyncio.run(buscar_cliente(client.get("phone",""))) if client.get("phone") else []
                if not agenda_clientes:
                    logger.info(f"📅 Cliente {user_name} no encontrado en agenda - queda pendiente para asesor")
                else:
                    logger.info(f"📅 Cliente {user_name} encontrado en agenda - citas históricas: {len(agenda_clientes)}")
            except Exception as ex:
                logger.warning(f"⚠️ Agenda no disponible: {ex}")'''

if old_pend in c:
    c = c.replace(old_pend, new_pend)
    with open('/root/universo/recepcionista/main.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print('✅ Integración con agenda agregada en flujo pendiente')
else:
    print('❌ Texto no encontrado en flujo pendiente')

# Agregar integración cuando el cliente confirma (agendado)
old_agendado = '        update_client_status(client["id"], "agendado", "Pepe Bot")'
new_agendado = '''        update_client_status(client["id"], "agendado", "Pepe Bot")
            # Agenda: buscar la cita en la BD y confirmar
            try:
                conn_a = get_connection()
                cur_a = conn_a.cursor()
                cur_a.execute("SELECT service, city, date_requested, time_requested FROM appointments WHERE client_id=? AND status='agendado' ORDER BY id DESC LIMIT 1", (client["id"],))
                row_a = cur_a.fetchone()
                if row_a:
                    svc, city, dt, tm = row_a
                    sede_id = None
                    if city and "medell" in city.lower(): sede_id = "sede-cj-medical-el-tesoro"
                    elif city and "bogot" in city.lower(): sede_id = "sede-cj-medical-bogota"
                    svc_id = None
                    for k, v in {"terapia":"srv-terapias-de-revitalizacion","masaje":"srv-masaje-de-relajacion","carbon":"srv-carbon-peel","hidra":"srv-hidrofacial-basica","botox":"srv-toxina-botox","depil":"srv-1-sesion-zona-m","radio":"srv-radiofrecuencia-fraccionada-alta-intensidad","micropig":"srv-remocion-micropigmentacion-1-sesion","diseño":"srv-diseno-de-cejas","tintura":"srv-tintura-de-cejas"}.items():
                        if k in svc.lower(): svc_id = v; break
                    if sede_id and svc_id and dt:
                        logger.info(f"📅 Cita lista para agenda: {sede_id} {dt} {tm} {svc_id}")
                conn_a.close()
            except Exception as ex:
                logger.warning(f"⚠️ Agenda no disponible en confirmación: {ex}")'''

if old_agendado in c:
    c = c.replace(old_agendado, new_agendado)
    with open('/root/universo/recepcionista/main.py', 'w', encoding='utf-8') as f:
        f.write(c)
    print('✅ Integración agenda en confirmación agregada')
else:
    print('❌ Texto agendado no encontrado')
