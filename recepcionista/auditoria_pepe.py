#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria completa del sistema Pepe (CRM + agendamiento + agente).

Revisa que todo funcione COMO UNO SOLO:
  1. Los 4 servicios del VPS
  2. Pepe: modelo, herramientas, prompt
  3. La agenda (Postgres por la API 8001)
  4. El CRM: login, columnas del pipeline, indicadores
  5. El paso a paso del pipeline: un cliente recorre las 4 columnas
  6. Apagar/prender la IA y la respuesta del asesor

  cd /root/universo/recepcionista && ./venv/bin/python auditoria_pepe.py
"""
import asyncio
import os
import subprocess
import sys

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import httpx                                  # noqa: E402
from crm.database import get_connection       # noqa: E402

CRM = "http://127.0.0.1:8000"
AGENDA = "http://127.0.0.1:8001"

OK, MAL = [], []
CID = None


def chk(cond, texto, detalle=""):
    (OK if cond else MAL).append(texto)
    print("  %s %s%s" % ("OK  " if cond else "FALLA", texto,
                         ("  -> " + str(detalle)) if detalle else ""))


def limpiar():
    if not CID:
        return
    con = get_connection()
    con.execute("DELETE FROM pending_replies WHERE client_id = ?", (CID,))
    con.execute("DELETE FROM pipeline_log WHERE client_id = ?", (CID,))
    con.execute("DELETE FROM messages WHERE client_id = ?", (CID,))
    con.execute("DELETE FROM clients WHERE id = ?", (CID,))
    con.commit()
    con.close()
    print("\n  limpieza: ficha de prueba borrada (id %s)" % CID)


async def principal():
    global CID

    # ── 1. SERVICIOS ──
    print("\n" + "=" * 76)
    print("1. LOS CUATRO SERVICIOS DEL VPS")
    print("=" * 76)
    for s in ("pepe", "crm", "agenda-api", "webui-backend"):
        r = subprocess.run(["systemctl", "is-active", s],
                           capture_output=True, text=True)
        chk(r.stdout.strip() == "active", "%s activo" % s, r.stdout.strip())

    # ── 2. PEPE ──
    print("\n" + "=" * 76)
    print("2. PEPE (el agente)")
    print("=" * 76)
    import main as m
    import herramientas as h
    chk(len(h.HERRAMIENTAS) == 12, "12 herramientas cargadas",
        len(h.HERRAMIENTAS))
    chk(m.PRIMARY_MODEL == "deepseek/deepseek-v4-pro", "modelo DeepSeek V4 Pro",
        m.PRIMARY_MODEL)
    p = m.prompt_de_hoy()
    chk(len(p) > 20000, "el prompt se arma bien", "%d caracteres" % len(p))
    nombres = [t["function"]["name"] for t in h.HERRAMIENTAS]
    print("      herramientas: %s" % ", ".join(nombres))

    # ── 3. AGENDA ──
    print("\n" + "=" * 76)
    print("3. LA AGENDA (Postgres)")
    print("=" * 76)
    tok = os.environ["API_TOKEN"]
    async with httpx.AsyncClient(timeout=30) as c:
        r = await c.get(AGENDA + "/datos", headers={"X-API-Token": tok})
    d = r.json() if r.status_code == 200 else {}
    chk(r.status_code == 200, "la API responde", r.status_code)
    chk(len(d.get("estados") or []) > 0, "estados", len(d.get("estados") or []))
    chk(len(d.get("sedes") or []) == 2, "sedes", len(d.get("sedes") or []))
    chk(len(d.get("servicios") or []) > 10, "servicios",
        len(d.get("servicios") or []))
    chk(len(d.get("especialistas") or []) == 4, "especialistas activas",
        [e.get("nombres") for e in (d.get("especialistas") or [])])

    # OJO: las citas NO vienen en /datos (que trae sedes, servicios, estados y
    # especialistas). Se piden aparte con /citas: al principio el test las
    # buscaba donde no estaban y marcaba una falla que no existia.
    async with httpx.AsyncClient(timeout=30) as c:
        rc = await c.get(AGENDA + "/citas", headers={"X-API-Token": tok})
    citas = rc.json() if rc.status_code == 200 else []
    if isinstance(citas, dict):
        citas = citas.get("citas", [])
    chk(rc.status_code == 200 and len(citas) > 0, "citas en la agenda",
        "%d citas" % len(citas))

    # ── 4. CRM ──
    print("\n" + "=" * 76)
    print("4. EL CRM (login, columnas, indicadores)")
    print("=" * 76)
    async with httpx.AsyncClient(base_url=CRM, timeout=30,
                                 follow_redirects=False) as c:
        r = await c.post("/login", data={"username": "admin",
                                         "password": "admin123"})
        chk(r.status_code == 302 and "advisor" in r.cookies,
            "login con admin/admin123", r.status_code)
        c.cookies.update(r.cookies)

        r = await c.get("/dashboard")
        chk(r.status_code == 200, "el panel carga", r.status_code)

        # las 4 columnas tienen que responder
        cols = [("leads_nuevos", "Leads Nuevos"),
                ("pendientes_agendar", "Pendientes por Agendar"),
                ("agendados", "Agendados"),
                ("no_interesados", "No Interesados")]
        for clave, nombre in cols:
            r = await c.get("/api/clients", params={"status": clave})
            chk(r.status_code == 200, "columna «%s» responde" % nombre,
                "%s clientes" % len(r.json()) if r.status_code == 200
                else r.status_code)

        r = await c.get("/api/pipeline/stats")
        chk(r.status_code == 200, "indicadores del pipeline",
            r.json() if r.status_code == 200 else r.status_code)

        # ── 5. PASO A PASO POR LAS COLUMNAS ──
        print("\n" + "=" * 76)
        print("5. UN CLIENTE RECORRE EL PASO A PASO")
        print("=" * 76)
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO clients (telegram_id, name, phone, status, channel) "
                    "VALUES ('auditoria_test', 'Auditoria Pepe', '3000000000', "
                    "'nuevo', 'telegram')")
        CID = cur.lastrowid
        con.commit()
        con.close()
        print("      ficha de prueba creada (id %s, estado «nuevo»)" % CID)

        r = await c.get("/api/clients", params={"status": "leads_nuevos"})
        ids = [x["id"] for x in r.json()]
        chk(CID in ids, "aparece en «Leads Nuevos»", "estado inicial")

        pasos = [("pendiente", "pendientes_agendar", "Pendientes por Agendar"),
                 ("agendado", "agendados", "Agendados"),
                 ("no_interesado", "no_interesados", "No Interesados")]
        for estado_db, columna, nombre in pasos:
            rr = await c.post("/api/clients/%s/status" % CID,
                              json={"status": estado_db, "note": "auditoria"})
            ok1 = rr.status_code == 200
            rl = await c.get("/api/clients", params={"status": columna})
            ids = [x["id"] for x in rl.json()]
            chk(ok1 and CID in ids,
                "se mueve a «%s»" % nombre,
                "POST %s / columna %s" % (rr.status_code, CID in ids))

        # historial del pipeline
        r = await c.get("/api/clients/%s" % CID)
        det = r.json()
        chk(len(det.get("pipeline_log") or []) >= 3,
            "queda el historial de movimientos",
            len(det.get("pipeline_log") or []))

        # ── 6. IA Y RESPUESTA DEL ASESOR ──
        print("\n" + "=" * 76)
        print("6. APAGAR LA IA Y RESPONDER COMO ASESOR")
        print("=" * 76)
        r = await c.post("/api/clients/%s/toggle-ai" % CID)
        con = get_connection()
        v = dict(con.execute("SELECT ai_disabled, channel FROM clients WHERE id = ?",
                             (CID,)).fetchone())
        con.close()
        chk(r.status_code == 200 and v["ai_disabled"],
            "el boton apaga la IA (Pepe deja de contestar)", v)

        r = await c.post("/api/clients/%s/reply" % CID,
                         json={"content": "Hola, le escribo del equipo de CJ Medical."})
        con = get_connection()
        fila = con.execute("SELECT content, sent FROM pending_replies "
                           "WHERE client_id = ? ORDER BY id DESC LIMIT 1",
                           (CID,)).fetchone()
        msj = con.execute("SELECT channel FROM messages WHERE client_id = ? "
                          "AND role = 'advisor' ORDER BY id DESC LIMIT 1",
                          (CID,)).fetchone()
        con.close()
        chk(r.status_code == 200 and fila,
            "la respuesta del asesor se encola para enviar",
            dict(fila) if fila else None)
        if msj:
            chk(msj["channel"] == v["channel"],
                "el mensaje del asesor guarda el canal real",
                "%s (canal del cliente: %s)" % (msj["channel"], v["channel"]))

        r = await c.post("/api/clients/%s/toggle-ai" % CID)
        con = get_connection()
        v2 = dict(con.execute("SELECT ai_disabled FROM clients WHERE id = ?",
                              (CID,)).fetchone())
        con.close()
        chk(not v2["ai_disabled"], "el boton vuelve a prender la IA", v2)

    # ── RESUMEN ──
    print("\n" + "=" * 76)
    print("RESUMEN:  %d OK   /   %d fallas" % (len(OK), len(MAL)))
    print("=" * 76)
    for x in MAL:
        print("  FALLA: %s" % x)
    return 1 if MAL else 0


if __name__ == "__main__":
    try:
        codigo = asyncio.run(principal())
    finally:
        limpiar()
    sys.exit(codigo)
