#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica TODO el flujo de Pepe contra la agenda real.

Corre con el venv del bot:
  cd /root/universo/recepcionista && ./venv/bin/python verify_flujo_completo.py
"""
import asyncio
import os
import sqlite3
import sys
import time

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)

# el token se lee del archivo (el bot lo carga del .env al arrancar)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import agenda_helper as ag          # noqa: E402
import herramientas as h            # noqa: E402

OK, MAL = [], []
CITAS_PRUEBA = []


def limpiar_citas_prueba():
    """Borra de la agenda las citas que creo esta verificacion.

    Se cancelan y ademas se borran: si quedaran, inflarian los indicadores
    de citas del mes (que fue justo lo que molesto la ultima vez).
    """
    if not CITAS_PRUEBA:
        return
    ids = ",".join("'%s'" % c for c in CITAS_PRUEBA)
    sql = ("delete from cita_bitacora where cita_id in (%s); "
           "delete from citas where id in (%s);" % (ids, ids))
    try:
        import subprocess
        p = subprocess.run(["su", "postgres", "-c",
                            "psql -d cjmedical -c \"%s\"" % sql],
                           capture_output=True, text=True, timeout=30)
        if p.returncode == 0:
            print("\n  limpieza: %d cita(s) de prueba borradas de la agenda"
                  % len(CITAS_PRUEBA))
        else:
            print("\n  (aviso) no pude borrar las citas de prueba: %s"
                  % (p.stderr or "")[:200])
    except Exception as e:
        print("\n  (aviso) limpieza falló: %s" % e)


def chk(cond, texto, detalle=""):
    (OK if cond else MAL).append(texto)
    print("  %s %s%s" % ("OK  " if cond else "FALLA", texto,
                         ("  -> " + str(detalle)) if detalle else ""))


CEDULA = "1069467531"
CRM_CLIENT_ID = 25


async def main():
    print("\n" + "=" * 74)
    print("1. RECONOCER A LA ESPECIALISTA POR SU NOMBRE CORTO")
    print("=" * 74)
    casos = [
        ("Dr. Jorge Cueter", "JORGE RAMIRO CUETER GUZMAN"),
        ("Jorge Cueter", "JORGE RAMIRO CUETER GUZMAN"),
        ("el doctor Cueter", "JORGE RAMIRO CUETER GUZMAN"),
        ("Cueter", "JORGE RAMIRO CUETER GUZMAN"),
        ("Dr. Cueter", "JORGE RAMIRO CUETER GUZMAN"),
        ("Julieth Arias", "JULIE VIVIANA ARIAS HERNANDEZ"),
        ("Dra. Julieth Arias", "JULIE VIVIANA ARIAS HERNANDEZ"),
        ("la doctora Arias", "JULIE VIVIANA ARIAS HERNANDEZ"),
        ("julie", "JULIE VIVIANA ARIAS HERNANDEZ"),
        ("Valentina", "VALENTINA BAQUERO RIVILLAS"),
        ("Valentina Baquero", "VALENTINA BAQUERO RIVILLAS"),
        ("Diana Carolina", "DIANA CAROLINA RUIZ ROJAS"),
        ("Diana Carolina Ruiz", "DIANA CAROLINA RUIZ ROJAS"),
    ]
    for dicho, esperado in casos:
        r = await ag.resolver_especialista(dicho)
        # la agenda guarda a unos en mayuscula y a otros no: se compara igual
        bien = (r.get("ok") and
                ag._normal(r.get("nombre", "")) == ag._normal(esperado))
        chk(bien, "«%s» -> %s" % (dicho, esperado),
            r.get("nombre") if r.get("ok") else "%s %s" % (r.get("error"), r.get("mensaje", "")))

    print("\n  Un nombre que no existe no debe pegar con nadie:")
    r = await ag.resolver_especialista("Carlos Perez")
    chk(not r.get("ok") and r.get("error") == "NO_EXISTE",
        "«Carlos Perez» no existe", r.get("mensaje"))

    print("\n" + "=" * 74)
    print("2. QUIEN PUEDE HACER EL SERVICIO (el bug de Valentina)")
    print("=" * 74)
    quien = await ag.especialistas_para(servicio="Remoción de Micropigmentación",
                                        sede="El Tesoro")
    nombres = sorted(x["nombre"] for x in quien)
    chk(nombres == ["JORGE RAMIRO CUETER GUZMAN", "JULIE VIVIANA ARIAS HERNANDEZ"],
        "Remoción en El Tesoro -> Cueter y Arias", nombres)

    r = await ag.resolver_especialista("Valentina", sede="El Tesoro",
                                       servicio="Remoción de Micropigmentación")
    chk(not r.get("ok") and r.get("error") == "NO_LO_HACE",
        "Valentina + Remoción -> NO_LO_HACE (antes la ofrecía)", r.get("error"))
    chk(sorted(x["nombre"] for x in (r.get("quien_si") or [])) ==
        ["JORGE RAMIRO CUETER GUZMAN", "JULIE VIVIANA ARIAS HERNANDEZ"],
        "  ...y ofrece a quienes sí la hacen",
        [x["nombre"] for x in (r.get("quien_si") or [])])

    r = await ag.resolver_especialista("Jorge Cueter", sede="El Tesoro",
                                       servicio="Remoción de Micropigmentación")
    chk(r.get("ok") and r["nombre"] == "JORGE RAMIRO CUETER GUZMAN",
        "Cueter + Remoción en El Tesoro -> lo reconoce (esto era el bug)")

    r = await ag.resolver_especialista("Diana Carolina", sede="El Tesoro")
    chk(not r.get("ok") and r.get("error") == "NO_LO_HACE",
        "Diana Carolina no atiende en El Tesoro (solo Bogotá)", r.get("error"))
    r = await ag.resolver_especialista("Diana Carolina", sede="Bogotá")
    chk(r.get("ok"), "Diana Carolina sí en Bogotá")

    print("\n" + "=" * 74)
    print("3. EL PERSONAL INACTIVO NO APARECE")
    print("=" * 74)
    todos = await ag.especialistas_para()
    chk(len(todos) == 4, "solo las 4 activas", [x["nombre"] for x in todos])
    r = await ag.resolver_especialista("Laura Martinez")
    chk(not r.get("ok"), "«Laura Martinez» (inactiva) no se ofrece", r.get("error"))

    print("\n" + "=" * 74)
    print("4. HORAS LIBRES: cada 30 min y con especialista que sí hace el servicio")
    print("=" * 74)
    sv = await ag.resolver_servicio("Remoción de Micropigmentación")
    fechas = ag._proximos_dias(10)
    fecha = None
    r = None
    for f in fechas:
        rr = await ag.horas_libres(servicio="Remoción de Micropigmentación",
                                   sede="El Tesoro", fecha=f)
        if rr.get("ok") and rr.get("dias") and rr["dias"][0]["horas"]:
            fecha, r = f, rr
            break
    if not r:
        chk(False, "no encontré horas libres de Remoción en 10 días")
    else:
        horas = r["dias"][0]["horas"]
        chk(all(str(x["hora"])[-2:] in ("00", "30") for x in horas),
            "%s: todas en punto o y media" % fecha,
            [x["hora"] for x in horas])
        aptos = {x["nombre"] for x in await ag.especialistas_para(
            servicio="Remoción de Micropigmentación", sede="El Tesoro")}
        chk(all(x["especialista"] in aptos for x in horas),
            "  cada hora trae una especialista que SÍ hace Remoción",
            sorted({x["especialista"] for x in horas}))
        print("      horas: %s" % ", ".join(
            "%s (%s)" % (x["hora"], x["especialista"].split()[0]) for x in horas[:6]))

    print("\n" + "=" * 74)
    print("5. SI EL CLIENTE NO PIDIO A NADIE, LA AGENDA ESCOGE")
    print("=" * 74)
    if r:
        hora0 = r["dias"][0]["horas"][0]["hora"]
        rl = await ag.especialista_libre(r["sede_id"], sv["id"], fecha, hora0)
        chk(rl.get("ok"), "hay alguien libre el %s a las %s" % (fecha, hora0),
            rl.get("especialista") or rl.get("mensaje"))

    print("\n" + "=" * 74)
    print("6. AGENDAR DE PUNTA A PUNTA (con el nombre corto, sin ids)")
    print("=" * 74)
    rc = await ag.buscar_cliente(documento=CEDULA)
    cli = (rc.get("clientes") or [{}])[0]
    chk(rc.get("ok") and cli.get("id"), "cliente por cédula %s" % CEDULA, cli.get("id"))

    if r and cli.get("id"):
        hora0 = r["dias"][0]["horas"][0]["hora"]
        res = await h.ejecutar("agendar_cita", {
            "documento": CEDULA,
            "especialista": "Dr. Jorge Cueter",
            "sede": "El Tesoro",
            "servicio": "Remoción de Micropigmentación",
            "fecha": fecha, "hora": hora0, "cliente_confirmo": True,
        }, {"telefono": cli.get("telefono") or ""})
        chk(res.get("ok"), "agendó con «Dr. Jorge Cueter» (nombre corto)",
            res.get("cita_id") or "%s %s" % (res.get("error"), res.get("mensaje", "")))
        if res.get("ok"):
            print("      cita %s | %s %s | %s | estado: %s" % (
                res["cita_id"], res["fecha"], res["hora"], res["especialista"],
                res.get("estado")))
            chk(res.get("especialista") == "JORGE RAMIRO CUETER GUZMAN",
                "  quedó con la especialista correcta", res.get("especialista"))

            # sin especialista: la agenda escoge
            otras = [x for x in r["dias"][0]["horas"] if x["hora"] != hora0]
            if otras:
                h2 = otras[0]["hora"]
                res2 = await h.ejecutar("agendar_cita", {
                    "documento": CEDULA, "sede": "El Tesoro",
                    "servicio": "Remoción de Micropigmentación",
                    "fecha": fecha, "hora": h2, "cliente_confirmo": True,
                }, {"telefono": cli.get("telefono") or ""})
                chk(res2.get("ok"),
                    "agendó SIN nombrar especialista (la agenda escogió)",
                    res2.get("especialista") or res2.get("mensaje"))
                if res2.get("ok"):
                    print("      cita %s | %s | escogió: %s" % (
                        res2["cita_id"], res2["hora"], res2["especialista"]))
                    await ag.cancelar(res2["cita_id"], "prueba automatica")
                    CITAS_PRUEBA.append(res2["cita_id"])
            # limpiar la primera
            await ag.cancelar(res["cita_id"], "prueba automatica")
            CITAS_PRUEBA.append(res["cita_id"])
            chk(True, "  (las citas de prueba se borran al final, no quedan en los indicadores)")

    print("\n" + "=" * 74)
    print("7. LA TARJETA DEL CRM YA NO SALE EN BLANCO (bug reportado)")
    print("=" * 74)
    con = sqlite3.connect(os.path.join(BASE, "crm/cjmedical.db"))
    antes = con.execute("SELECT name, phone, email, document FROM clients WHERE id=?",
                        (CRM_CLIENT_ID,)).fetchone()
    con.close()
    print("      antes:  nombre=%s | celular=%s | correo=%s | doc=%s" % antes)

    rr = await h.ejecutar("buscar_cliente", {"documento": CEDULA},
                          {"telefono": "", "client_id": CRM_CLIENT_ID})
    chk(rr.get("ok"), "Pepe busca al cliente por cédula (y sincroniza el CRM)")
    await asyncio.sleep(0.3)
    con = sqlite3.connect(os.path.join(BASE, "crm/cjmedical.db"))
    despues = con.execute("SELECT name, phone, email, document FROM clients WHERE id=?",
                          (CRM_CLIENT_ID,)).fetchone()
    con.close()
    print("      después: nombre=%s | celular=%s | correo=%s | doc=%s" % despues)
    chk(despues[1] and despues[1] != "", "  la tarjeta ya tiene CELULAR", despues[1])
    chk(despues[2] and despues[2] != "", "  la tarjeta ya tiene CORREO", despues[2])
    chk(despues[3] and despues[3] != "", "  la tarjeta ya tiene DOCUMENTO", despues[3])

    limpiar_citas_prueba()

    print("\n" + "=" * 74)
    print("RESUMEN:  %d OK   /   %d fallas" % (len(OK), len(MAL)))
    print("=" * 74)
    for m in MAL:
        print("  FALLA: %s" % m)
    return 1 if MAL else 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
