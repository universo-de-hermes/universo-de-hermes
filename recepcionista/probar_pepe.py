#!/usr/bin/env python3
"""Las herramientas de Pepe contra la agenda real, como si estuviera
conversando por WhatsApp."""
import asyncio, os, sys, json

# Cargar el .env real para usar el AGENDA_API y el API_TOKEN de verdad.
# Sin esto la prueba usa un token inventado y, con la autenticación activa,
# todo lo que venga después del bloque del token falla.
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env"))
except Exception:
    pass

os.environ.setdefault("AGENDA_API", "http://127.0.0.1:8001")
os.environ.setdefault("API_TOKEN", "prueba-token-1234")
TOKEN_REAL = os.environ.get("API_TOKEN", "")

import agenda_helper as ag
import herramientas as H

ok = mal = 0
def prueba(n, c, extra=""):
    global ok, mal
    if c: ok += 1;  print("  ok   " + n)
    else: mal += 1; print("  MAL  " + n + (("\n       " + str(extra)[:400]) if extra else ""))

escalados = []
CTX = {"telefono": "573232045895",
       "escalar": lambda motivo, resumen: escalados.append((motivo, resumen))}

async def usar(nombre, **args):
    return await H.ejecutar(nombre, args, CTX)

async def main():
    print("\n— el token —")
    d = await ag.datos()
    prueba(f"lee los maestros con el token ({len(d.get('servicios',[]))} servicios)",
           len(d.get("servicios", [])) == 27, d.keys())
    os.environ["API_TOKEN"] = "token-inventado"
    import importlib; importlib.reload(ag); importlib.reload(H)
    r = await ag.buscar_cliente(telefono="3232045895")
    prueba("con un token malo lo dice claro, no se queda callado",
           r["ok"] is False and r["error"] == "SIN_SESION", r)
    os.environ["API_TOKEN"] = TOKEN_REAL
    importlib.reload(ag); importlib.reload(H)

    print("\n— «hola, quiero depilación láser» —")
    r = await usar("buscar_cliente_por_telefono", telefono="573232045895")
    prueba(f"encuentra al cliente por el teléfono con indicativo ({r.get('encontrados')})",
           r["ok"] and r["encontrados"] >= 1, r)
    CLI = r["clientes"][0]["cliente_id"]
    print("       →", r["clientes"][0]["nombre"])

    r = await usar("ver_horas_libres", servicio="depilación láser zona m",
                   sede="el tesoro", dias=10)
    prueba(f"le ofrece horas reales ({len(r.get('dias',[]))} días)",
           r["ok"] and len(r["dias"]) > 0, r)
    prueba("y recorta la lista para no marear por WhatsApp",
           r["ok"] and all(len(d["horas"]) <= 6 for d in r["dias"]))
    D0 = r["dias"][0]; H0 = D0["horas"][0]
    SRV, SEDE = r["servicio_id"], r["sede_id"]
    print(f"       → {r['servicio']} en {r['sede']}: {D0['fecha']} a las {H0['hora']} con {H0['especialista']}")

    print("\n— «esa me sirve» —")
    r = await usar("apartar_hora", especialista_id=H0["especialista_id"], sede_id=SEDE,
                   servicio_id=SRV, fecha=D0["fecha"], hora=H0["hora"], minutos=10)
    prueba("aparta la hora mientras siguen hablando", r["ok"] and r.get("reserva"), r)
    RES = r.get("reserva")

    r2 = await usar("ver_horas_libres", servicio="depilación láser zona m",
                    sede="el tesoro", fecha=D0["fecha"],
                    especialista=H0["especialista"])
    libres = [h["hora"] for d in r2.get("dias", []) for h in d["horas"]]
    prueba("y esa hora deja de ofrecerse con esa especialista",
           H0["hora"] not in libres, libres[:6])

    print("\n— validar antes de agendar —")
    r = await usar("agendar_cita", cliente_id=CLI, especialista_id=H0["especialista_id"],
                   sede_id=SEDE, servicio_id=SRV, fecha=D0["fecha"], hora=H0["hora"],
                   reserva=RES, cliente_confirmo=False)
    prueba("sin que el cliente valide el resumen, NO agenda",
           r["ok"] is False and r["error"] == "FALTA_VALIDAR", r)
    prueba("y le dice al modelo qué hacer primero",
           "resumen" in r.get("mensaje", "").lower(), r)
    r = await usar("agendar_cita", cliente_id=CLI, especialista_id=H0["especialista_id"],
                   sede_id=SEDE, servicio_id=SRV, fecha=D0["fecha"], hora=H0["hora"],
                   reserva=RES)
    prueba("tampoco si se le olvida mandar el campo",
           r["ok"] is False and r["error"] == "FALTA_VALIDAR", r)

    print("\n— «sí, todo correcto» → cerrar la cita —")
    r = await usar("agendar_cita", cliente_id=CLI, especialista_id=H0["especialista_id"],
                   sede_id=SEDE, servicio_id=SRV, fecha=D0["fecha"], hora=H0["hora"],
                   reserva=RES, cliente_confirmo=True, notas="Pidió que la llamen antes")
    prueba("agenda y devuelve el detalle en palabras", r["ok"] and r.get("cita_id"), r)
    CITA = r.get("cita_id")
    if r["ok"]:
        print(f"       → {r['servicio']} · {r['fecha']} {r['hora']} · {r['especialista']} · {r['sede']}")

    print("\n— otra conversación pide la misma hora —")
    r = await usar("agendar_cita", cliente_id=CLI, especialista_id=H0["especialista_id"],
                   sede_id=SEDE, servicio_id=SRV, fecha=D0["fecha"], hora=H0["hora"],
                   cliente_confirmo=True)
    prueba("el choque llega con nombre y frase amable, no vacío",
           r["ok"] is False and r["error"] == "CUPO_TOMADO"
           and "acaba de ocuparse" in r["mensaje"], r)

    print("\n— «¿qué citas tengo?» —")
    r = await usar("ver_citas_del_cliente", cliente_id=CLI)
    prueba(f"lista sus próximas citas ({len(r.get('citas',[]))})",
           r["ok"] and any(c["cita_id"] == CITA for c in r["citas"]), r)

    print("\n— la cita nace Pendiente y solo el cliente la confirma —")
    r = await usar("ver_citas_del_cliente", cliente_id=CLI)
    esta = [c for c in r.get("citas", []) if c["cita_id"] == CITA]
    prueba(f"nace en Pendiente ({esta[0]['estado'] if esta else '?'})",
           esta and esta[0]["estado"] == "Pendiente", r)
    r = await usar("confirmar_cita", cita_id=CITA)
    prueba(f"cuando el cliente confirma, pasa a Confirmado ({r.get('estado')})",
           r["ok"] and r.get("estado") == "Confirmado", r)
    r = await usar("ver_citas_del_cliente", cliente_id=CLI)
    esta = [c for c in r.get("citas", []) if c["cita_id"] == CITA]
    prueba("y así queda en la agenda, que es lo que ve la recepcionista",
           esta and esta[0]["estado"] == "Confirmado", r)

    print("\n— mover y cancelar —")

    r = await usar("ver_horas_libres", servicio="depilación láser zona m",
                   sede="el tesoro", fecha=D0["fecha"])
    otra = [h for d in r.get("dias", []) for h in d["horas"]][0]
    r = await usar("reprogramar_cita", cita_id=CITA, fecha=D0["fecha"],
                   hora=otra["hora"], motivo="Le salió una reunión")
    prueba(f"la mueve a otra hora ({otra['hora']})", r["ok"] and r.get("cita_id") != CITA, r)
    NUEVA = r.get("cita_id")

    r = await usar("cancelar_cita", cita_id=NUEVA, motivo="Se enfermó")
    prueba("la cancela", r["ok"], r)
    r = await usar("ver_horas_libres", servicio="depilación láser zona m",
                   sede="el tesoro", fecha=D0["fecha"])
    libres = [h["hora"] for d in r.get("dias", []) for h in d["horas"]]
    prueba("y la hora vuelve a estar libre para otro", otra["hora"] in libres, libres[:6])

    print("\n— cliente nuevo —")
    r = await usar("buscar_cliente_por_telefono", telefono="3001234599")
    prueba("no encuentra a nadie con ese teléfono", r["ok"] and r["encontrados"] == 0, r)
    r = await usar("registrar_cliente", documento="1122334455", primer_nombre="Sara",
                   primer_apellido="Gómez", telefono="3001234599", correo="sara@correo.com")
    prueba("lo registra", r["ok"] and r.get("cliente_id"), r)
    r2 = await usar("registrar_cliente", documento="1122334455", primer_nombre="Sara",
                    primer_apellido="Gómez", telefono="3001234599")
    prueba("y registrarlo dos veces no lo duplica",
           r2["ok"] and r2["cliente_id"] == r["cliente_id"], r2)

    print("\n— cuando el nombre del servicio da para varios —")
    r = await usar("ver_horas_libres", servicio="cejas", sede="el tesoro")
    prueba("no adivina: devuelve las opciones para preguntar",
           r["ok"] is False and r["error"] == "AMBIGUO" and len(r.get("opciones", [])) > 1, r)
    print("       →", [o["nombre"] for o in r.get("opciones", [])])

    r = await usar("ver_horas_libres", servicio="casmara", sede="el tesoro")
    prueba("un servicio que no existe lo dice, con la lista de los que sí",
           r["ok"] is False and r["error"] == "NO_EXISTE" and r.get("opciones"), r)

    r = await usar("ver_horas_libres", servicio="botox", sede="el tesoro")
    prueba("pero «botox» sí lo resuelve solo",
           r["ok"] and r["servicio_id"] == "srv-toxina-botox", r)
    r = await usar("ver_horas_libres", servicio="masaje", sede="medellín")
    prueba("y «masaje» en «medellín» también",
           r["ok"] and r["servicio_id"] == "srv-masaje-de-relajacion"
           and r["sede_id"] == "sede-cj-medical-el-tesoro", r)

    print("\n— cuando toca un humano —")
    r = await usar("pasar_a_asesor", motivo="pqrs",
                   resumen="Reclama que le cobraron dos veces la sesión de agosto.")
    prueba("escala y avisa que no siga intentando",
           r["ok"] and r.get("escalado") and "no sigas" in r["instruccion"], r)
    prueba("y el CRM se entera", len(escalados) == 1 and escalados[0][0] == "pqrs", escalados)

    print("\n— recordatorios del día siguiente —")
    r = await ag.citas_de_manana()
    prueba("puede salir a confirmar las de mañana", r["ok"] and "citas" in r,
           {k: v for k, v in r.items() if k != "citas"})

    print("\n— las herramientas están bien declaradas —")
    nombres = [h["function"]["name"] for h in H.HERRAMIENTAS]
    prueba(f"hay {len(nombres)} herramientas", len(nombres) == 10, nombres)
    prueba("todas tienen descripción y parámetros",
           all(h["function"].get("description") and h["function"].get("parameters")
               for h in H.HERRAMIENTAS))
    prueba("agendar_cita exige la validación del cliente",
           "cliente_confirmo" in [h for h in H.HERRAMIENTAS
                                  if h["function"]["name"] == "agendar_cita"][0]
               ["function"]["parameters"]["required"])
    prueba("el esquema es JSON válido para OpenAI",
           json.dumps(H.HERRAMIENTAS) and all(
               h["function"]["parameters"]["type"] == "object" for h in H.HERRAMIENTAS))
    r = await H.ejecutar("herramienta_que_no_existe", {}, CTX)
    prueba("una herramienta inventada no revienta nada", r["ok"] is False, r)
    r = await H.ejecutar("agendar_cita", '{"cliente_id":"x"}', CTX)
    prueba("y si faltan parámetros lo dice", r["ok"] is False, r)

    print(f"\n{ok} ok, {mal} mal")
    return 1 if mal else 0

sys.exit(asyncio.run(main()))
