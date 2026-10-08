#!/usr/bin/env python3
# Prueba del camino HTTP real (lo mismo que pide la tablet). SOLO LECTURA.
import json, urllib.request, urllib.error

tok = open('/root/universo/agenda/.api_token').read().strip()

def pedir(url, payload):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                headers={"x-api-token": tok,
                                         "Content-Type": "application/json"})
    try:
        r = urllib.request.urlopen(req, timeout=20)
        return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()
    except Exception as e:
        return "ERR", str(e)

for fecha in ("2026-10-01", "2026-10-02"):
    for ruta in ("/api/v2/huecos/dia", "/v2/huecos/dia"):
        cod, cuerpo = pedir("http://127.0.0.1:8001" + ruta,
                            {"fecha": fecha, "servicio": "srv-1-sesion-zona-m"})
        if cod == 200:
            try:
                d = json.loads(cuerpo)
                if isinstance(d, dict) and "detail" in d:
                    print(f"{ruta} {fecha}: 200 pero detail={d['detail'][:80]}")
                else:
                    horas = sorted({x.get("inicio") for x in d if isinstance(x, dict)})
                    print(f"{ruta} {fecha}: {len(horas)} horas {horas[:6]}")
            except Exception as e:
                print(f"{ruta} {fecha}: 200 crudo {cuerpo[:120]}")
            break
        else:
            print(f"{ruta} {fecha}: HTTP {cod} {cuerpo[:120]}")
