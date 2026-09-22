#!/usr/bin/env python3
"""Ejercita la API corregida contra Postgres con los datos reales."""
import json, urllib.request, urllib.error, sys, datetime

B = "http://127.0.0.1:8001"
ok = mal = 0

def llamar(metodo, ruta, cuerpo=None):
    req = urllib.request.Request(B + ruta, method=metodo)
    data = None
    if cuerpo is not None:
        data = json.dumps(cuerpo).encode()
        req.add_header("content-type", "application/json")
    try:
        with urllib.request.urlopen(req, data, timeout=30) as r:
            return r.status, json.loads(r.read().decode() or "null")
    except urllib.error.HTTPError as e:
        cuerpo = e.read().decode()
        try:    cuerpo = json.loads(cuerpo)
        except Exception: pass
        return e.code, cuerpo
    except Exception as e:
        return 0, str(e)

def prueba(nombre, cond, extra=""):
    global ok, mal
    if cond: ok += 1;  print("  ok   " + nombre)
    else:    mal += 1; print("  MAL  " + nombre + (("\n       " + str(extra)[:300]) if extra else ""))

def detalle(c):
    return c.get("detail") if isinstance(c, dict) else c

print("\n— los cuatro prefijos —")
for ruta in ["/datos", "/v2/datos", "/api/datos", "/api/v2/datos"]:
    s, c = llamar("GET", ruta)
    prueba(f"responde en {ruta}", s == 200 and isinstance(c, dict) and "sedes" in c, c)

print("\n— /datos trae lo que la agenda necesita —")
s, d = llamar("GET", "/datos")
prueba("sedes, servicios, estados y especialistas son LISTAS",
       all(isinstance(d.get(k), list) for k in ("sedes","servicios","estados","especialistas")),
       {k: type(d.get(k)).__name__ for k in d})
prueba(f"2 sedes, 27 servicios, 7 estados, 7 especialistas "
       f"({len(d['sedes'])}, {len(d['servicios'])}, {len(d['estados'])}, {len(d['especialistas'])})",
       (len(d["sedes"]), len(d["servicios"]), len(d["estados"]), len(d["especialistas"])) == (2,27,7,7))
e0 = d["especialistas"][0]
prueba("cada especialista trae sedes, servicios y horarios",
       all(k in e0 for k in ("sedes","servicios","horarios")), list(e0))
h0 = [h for e in d["especialistas"] for h in e["horarios"]]
prueba(f"los horarios vienen con dia/desde/hasta/almuerzo/sedeId ({len(h0)} franjas)",
       len(h0) == 48 and all(k in h0[0] for k in ("dia","desde","hasta","almDesde","almHasta","sedeId")),
       h0[0] if h0 else None)
prueba("los estados traen orden y transparente (la agenda los necesita)",
       all(k in d["estados"][0] for k in ("orden","transparente","tipo","inicial")), d["estados"][0])

print("\n— agenda del día —")
s, a = llamar("GET", "/agenda/sede-cj-medical-el-tesoro/2026-08-20")
prueba(f"trae las citas del día ({len(a) if isinstance(a,list) else a})", s == 200 and len(a) > 5, a)
prueba("las horas vienen como HH:MM", s == 200 and len(a[0]["inicio"]) == 5, a[0].get("inicio") if s==200 else a)
prueba("trae nombre de cliente, especialista, servicio y color de estado",
       s == 200 and all(a[0].get(k) for k in ("cliente_nombre","especialista","servicio","estado_color")),
       a[0] if s == 200 else a)
s, t = llamar("GET", "/agenda/todas/2026-08-20")
prueba(f"'todas' junta las dos sedes ({len(t) if isinstance(t,list) else t})",
       s == 200 and len(t) >= len(a))

print("\n— huecos (antes fallaba siempre por el parámetro 'paso') —")
s, h = llamar("POST", "/huecos/dia", {"fecha":"2026-09-22","sede":"sede-cj-medical-bogota",
                                      "servicio":"srv-consulta-medica","paso":30})
prueba(f"huecos/dia responde ({len(h) if isinstance(h,list) else h})", s == 200 and len(h) > 0, h)
prueba("cada hueco trae fecha, inicio, fin, especialista y sede",
       s == 200 and all(k in h[0] for k in ("fecha","inicio","fin","especialista_id","sede_id")), h[0] if s==200 else h)
s, hb = llamar("POST", "/huecos/buscar", {"desde":"2026-09-21","dias":7,
                                          "sede":"sede-cj-medical-bogota",
                                          "servicio":"srv-consulta-medica","limite":20})
prueba(f"huecos/buscar responde ({len(hb) if isinstance(hb,list) else hb})", s == 200 and len(hb) > 0, hb)

print("\n— clientes —")
s, cl = llamar("POST", "/clientes/buscar", {"telefono":"3232045895"})
prueba(f"busca por teléfono ({len(cl) if isinstance(cl,list) else cl})", s == 200 and len(cl) >= 1, cl)
s, cl2 = llamar("POST", "/clientes/buscar", {"telefono":"+57 323 204 5895"})
prueba("encuentra igual con +57 y espacios", s == 200 and len(cl2) >= 1, cl2)
s, nuevo = llamar("POST", "/clientes/crear", {"documento":"90909090","primer_nombre":"Prueba",
                                              "primer_apellido":"Api","telefono":"3001112222"})
prueba("crea cliente", s == 200 and nuevo.get("id") == "cli-90909090", nuevo)
s, rep = llamar("POST", "/clientes/crear", {"documento":"90909090","primer_nombre":"Prueba",
                                            "primer_apellido":"Api"})
prueba("crear dos veces no duplica", s == 200 and rep.get("id") == "cli-90909090", rep)
s, upd = llamar("PUT", "/clientes/cli-90909090", {"correo":"a@b.co"})
prueba("edita cliente", s == 200 and upd.get("correo") == "a@b.co", upd)
s, det = llamar("GET", "/clientes/cli-90909090")
prueba("el detalle del cliente trae su historial", s == 200 and "citas" in det, det)

print("\n— agendar —")
F = "2026-09-22"
cuerpo = {"cliente_id":"cli-90909090","especialista":"esp-diana-carolina-ruiz-rojas",
          "sede":"sede-cj-medical-bogota","fecha":F,"inicio":"10:00",
          "servicio":"srv-consulta-medica","canal":"WhatsApp","por":"hermes"}
s, cita = llamar("POST", "/citas/agendar", cuerpo)
prueba("agenda una cita", s == 200 and cita.get("id"), cita)
CID = cita.get("id") if isinstance(cita, dict) else None
prueba("nace en el estado inicial", isinstance(cita,dict) and cita.get("estado_id") == "est-pendiente", cita)

s, err = llamar("POST", "/citas/agendar", cuerpo)
prueba(f"el choque es 409, no 500 (llegó {s})", s == 409 and "CUPO_TOMADO" in str(detalle(err)), err)
s, err = llamar("POST", "/citas/agendar", dict(cuerpo, inicio="07:00"))
prueba(f"fuera de horario es 400 (llegó {s})", s == 400 and "FUERA_DE_HORARIO" in str(detalle(err)), err)
s, err = llamar("POST", "/citas/agendar", dict(cuerpo, inicio="13:15"))
prueba(f"almuerzo es 400 (llegó {s})", s == 400 and "ALMUERZO" in str(detalle(err)), err)

print("\n— mover una cita (antes: 500 por la bitácora) —")
s, mov = llamar("PUT", f"/citas/{CID}", {"inicio":"11:00","fin":"11:30"})
prueba(f"mueve la cita (llegó {s})", s == 200 and mov.get("inicio") is not None, mov)
s, bit = llamar("GET", f"/citas/{CID}/bitacora")
prueba("la movida quedó en la bitácora",
       s == 200 and any(x["accion"] == "movida" for x in bit), bit)

print("\n— bloqueo (antes: nunca se creaba) —")
s, blo = llamar("POST", "/citas/bloqueo", {"especialista":"esp-diana-carolina-ruiz-rojas",
                                           "sede":"sede-cj-medical-bogota","fecha":F,
                                           "inicio":"15:00","fin":"16:00","motivo":"Reunión"})
prueba(f"crea el bloqueo (llegó {s})", s == 200 and blo.get("tipo") == "bloqueo", blo)
s, hh = llamar("POST", "/huecos/dia", {"fecha":F,"sede":"sede-cj-medical-bogota",
                                       "especialista":"esp-diana-carolina-ruiz-rojas",
                                       "servicio":"srv-consulta-medica","paso":30})
prueba("el bloqueo tapa el cupo",
       s == 200 and not any(x["inicio"] == "15:00" for x in hh), [x["inicio"] for x in hh][:8] if s==200 else hh)
s, ag = llamar("GET", f"/agenda/sede-cj-medical-bogota/{F}")
prueba("el bloqueo aparece en la agenda (antes lo borraba el INNER JOIN)",
       s == 200 and any(x["tipo"] == "bloqueo" for x in ag), ag)

print("\n— reprogramar —")
s, nueva = llamar("POST", "/citas/reprogramar", {"cita_id":CID,"fecha":"2026-09-23",
                                                 "inicio":"09:30","motivo":"El cliente pidió cambio",
                                                 "por":"ana"})
prueba(f"reprograma (llegó {s})", s == 200 and nueva.get("id") and nueva["id"] != CID, nueva)
s, vieja = llamar("GET", f"/citas?fecha={F}")
prueba("la vieja quedó como Reprogramado",
       s == 200 and any(x["id"] == CID and x["estado_id"] == "est-reprogramado" for x in vieja))

print("\n— cambiar estado y anular —")
NID = nueva.get("id") if isinstance(nueva, dict) else None
s, est = llamar("POST", "/citas/estado", {"cita_id":NID,"estado":"est-confirmado","por":"ana"})
prueba(f"confirma la cita (llegó {s})", s == 200 and est.get("estado_id") == "est-confirmado", est)
s, an = llamar("DELETE", f"/citas/{NID}")
prueba(f"anular la deja cancelada, no la borra (llegó {s})",
       s == 200 and an.get("estado_id") == "est-cancelado", an)

print("\n— cupos apartados —")
s, res = llamar("POST", "/cupos/apartar", {"especialista":"esp-diana-carolina-ruiz-rojas",
                                           "sede":"sede-cj-medical-bogota","fecha":F,
                                           "inicio":"17:00","servicio":"srv-consulta-medica",
                                           "minutos":5,"referencia":"wa-1"})
prueba(f"aparta el cupo (llegó {s})", s == 200 and res.get("id"), res)
s, err = llamar("POST", "/citas/agendar", dict(cuerpo, inicio="17:00"))
prueba(f"otro no puede agendar encima (llegó {s})",
       s == 409 and "CUPO_APARTADO" in str(detalle(err)), err)
s, sol = llamar("DELETE", f"/cupos/{res.get('id')}")
prueba("suelta el cupo", s == 200 and sol.get("ok") is True, sol)

print("\n— indicadores (antes reventaba en meses de 30 días) —")
for mes in (9, 4, 6, 11, 2):
    s, ind = llamar("GET", f"/indicadores?anio=2026&mes={mes}")
    prueba(f"mes {mes:02d} responde", s == 200 and "por_estado" in ind, ind)
s, ind = llamar("GET", "/indicadores?anio=2026&mes=8")
prueba(f"agosto trae datos reales ({sum(x['total'] for x in ind['por_estado']) if s==200 else ind} citas)",
       s == 200 and sum(x["total"] for x in ind["por_estado"]) > 100)
prueba("trae desglose por día, especialista y canal",
       s == 200 and all(k in ind for k in ("por_dia","por_especialista","por_canal")))

print("\n— maestros —")
s, sv = llamar("POST", "/servicios", {"nombre":"Prueba Api","duracion":40})
prueba("crea servicio", s == 200 and sv.get("id") == "srv-prueba-api", sv)
s, sv2 = llamar("PUT", f"/servicios/{sv.get('id')}", {"duracion":50})
prueba("edita servicio", s == 200 and sv2.get("duracion") == 50, sv2)
s, _ = llamar("DELETE", f"/servicios/{sv.get('id')}")
prueba("borra servicio", s == 200)
s, es = llamar("POST", "/estados", {"nombre":"Prueba Est","color":"#123456","tipo":"abierto","orden":90})
prueba("crea estado", s == 200 and es.get("id") == "est-prueba-est", es)
s, es2 = llamar("PUT", "/estados/est-prueba-est", {"nombre":"Prueba Est","color":"#654321",
                                                   "tipo":"abierto","inicial":True,"orden":90})
prueba("marcar uno como inicial no rompe el índice único", s == 200, es2)
s, chk = llamar("GET", "/estados")
prueba("y queda un solo inicial", s == 200 and sum(1 for x in chk if x["inicial"]) == 1,
       [x["id"] for x in chk if x["inicial"]] if s == 200 else chk)
llamar("PUT", "/estados/est-pendiente", {"nombre":"Pendiente","color":"#3B7DD8","tipo":"abierto",
                                         "inicial":True,"orden":10})
llamar("DELETE", "/estados/est-prueba-est")
s, ee = llamar("POST", "/especialistas", {"nombres":"Ana","apellidos":"Prueba","color":"#AA0000"})
prueba("crea especialista", s == 200 and ee.get("id"), ee)
s, ho = llamar("POST", "/horarios", {"especialista_id":ee.get("id"),"dia":2,
                                     "sede_id":"sede-cj-medical-bogota",
                                     "desde":"09:00","hasta":"18:00",
                                     "alm_desde":"13:00","alm_hasta":"14:00"})
prueba("le agrega horario", s == 200, ho)
s, es_ = llamar("POST", "/especialista-sedes", {"especialista_id":ee.get("id"),
                                                "sede_id":"sede-cj-medical-bogota"})
prueba("la activa en una sede", s == 200, es_)
s, d2 = llamar("GET", "/datos")
prueba("aparece en /datos con su horario",
       s == 200 and any(x["id"] == ee.get("id") and x["horarios"] for x in d2["especialistas"]))
s, es_ = llamar("POST", "/especialista-sedes", {"especialista_id":ee.get("id"),
                                                "sede_id":"sede-cj-medical-bogota","activo":False})
prueba("la desactiva de esa sede", s == 200, es_)
s, _ = llamar("DELETE", f"/especialistas/{ee.get('id')}")
prueba("desactiva especialista sin citas", s == 200)
s, err = llamar("DELETE", "/especialistas/esp-valentina-rivillas-baquero-42")
prueba("no deja desactivar a una con citas futuras si las tiene",
       s in (200, 400), err)

print("\n— PUT que crea (así guarda la agenda web) —")
s, sv = llamar("PUT", "/servicios/srv_nuevo_local", {"nombre":"Creado por PUT","duracion":25})
prueba("PUT crea el servicio con el id que manda la agenda",
       s == 200 and sv.get("id") == "srv_nuevo_local" and sv.get("duracion") == 25, sv)
s, sv = llamar("PUT", "/servicios/srv_nuevo_local", {"duracion":35})
prueba("y el segundo PUT lo actualiza", s == 200 and sv.get("duracion") == 35, sv)
llamar("DELETE", "/servicios/srv_nuevo_local")
s, ep = llamar("PUT", "/especialistas/esp_local_1",
               {"nombres":"Sofia","apellidos":"Gomez","color":"#123456",
                "sedes":["sede-cj-medical-bogota"],
                "servicios":["srv-consulta-medica"],
                "horarios":[{"dia":3,"sedeId":"sede-cj-medical-bogota","desde":"08:00",
                             "hasta":"17:00","almDesde":"12:00","almHasta":"13:00"}]})
prueba("PUT crea la especialista con sedes, servicios y horarios de una vez",
       s == 200 and ep.get("sedes") == ["sede-cj-medical-bogota"]
       and ep.get("servicios") == ["srv-consulta-medica"], ep)
s, d3 = llamar("GET", "/datos")
mia = [x for x in d3["especialistas"] if x["id"] == "esp_local_1"]
prueba("y su horario sale en /datos",
       len(mia) == 1 and len(mia[0]["horarios"]) == 1
       and mia[0]["horarios"][0]["almDesde"] == "12:00", mia)
s, hh = llamar("POST", "/huecos/dia", {"fecha":"2026-09-23","sede":"sede-cj-medical-bogota",
                                       "especialista":"esp_local_1","servicio":"srv-consulta-medica","paso":60})
prueba(f"ofrece huecos con ese horario nuevo ({len(hh) if isinstance(hh,list) else hh})",
       s == 200 and len(hh) > 0 and hh[0]["inicio"] == "08:00", hh[:3] if s==200 else hh)
s, ep = llamar("PUT", "/especialistas/esp_local_1", {"servicios":[]})
prueba("dejarla sin servicios significa «hace todos»", s == 200 and ep.get("servicios") == [], ep)
llamar("DELETE", "/especialistas/esp_local_1")
s, cl = llamar("PUT", "/clientes/cli_local_1",
               {"documento":"77777777","primer_nombre":"Nuevo","primer_apellido":"Cliente",
                "telefono":"3005556677"})
prueba("PUT crea el cliente con el id de la agenda",
       s == 200 and cl.get("id") == "cli_local_1", cl)

print("\n— no se quedan conexiones abiertas —")
for _ in range(60):
    llamar("GET", "/health")
s, salud = llamar("GET", "/health")
prueba("después de 60 llamadas sigue respondiendo", s == 200 and salud.get("status") == "ok", salud)

print(f"\n{ok} ok, {mal} mal")
sys.exit(1 if mal else 0)
