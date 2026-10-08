#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compara dos modelos con el flujo REAL de Pepe: mismo prompt, mismas
herramientas, mismas preguntas. Mide aciertos y tiempo.

  cd /root/universo/recepcionista && ./venv/bin/python comparar_modelos.py
"""
import asyncio
import os
import re
import sys
import time

BASE = "/root/universo/recepcionista"
os.chdir(BASE)
sys.path.insert(0, BASE)
os.environ["API_TOKEN"] = open("/root/universo/agenda/.api_token").read().strip()

import main as m                    # noqa: E402

MODELOS = ["mistralai/mistral-medium-3.1", "anthropic/claude-haiku-4.5",
           "deepseek/deepseek-v4-pro"]
NOMBRES = {"openai/gpt-4o-mini": "gpt-4o-mini",
           "openai/gpt-4.1-mini": "gpt-4.1-mini",
           "anthropic/claude-haiku-4.5": "haiku-4.5",
           "mistralai/mistral-medium-3.1": "mistral-3.1",
           "qwen/qwen3.8-flash": "qwen3.8-fl",
           "deepseek/deepseek-v4-flash": "v4-flash",
           "deepseek/deepseek-v4-pro": "v4-pro"}


def _nombre(modelo):
    """Nombre corto para la tabla; si no esta en el mapa, se recorta solo."""
    return NOMBRES.get(modelo, modelo.split("/")[-1][:13])
HERRAMIENTAS_USADAS = []

_original = m.ejecutar_herramienta


async def _espia(nombre, argumentos, contexto=None):
    HERRAMIENTAS_USADAS.append(nombre)
    return await _original(nombre, argumentos, contexto)


m.ejecutar_herramienta = _espia


def plano(t):
    return re.sub(r"\s+", " ", (t or "").lower()).strip()


# Cada caso: (titulo, pregunta, funcion que dice si la respuesta esta bien)
def rev_cueter(r, tools):
    p = plano(r)
    return (("cueter" in p)
            and not any(x in p for x in ("no tengo", "no está", "no esta",
                                         "no encuentro", "no lo tengo")))


def rev_valentina(r, tools):
    p = plano(r)
    niega = ("no" in p and "valentina" in p)
    ofrece = ("cueter" in p or "arias" in p)
    return niega and ofrece


def rev_sabado(r, tools):
    """Correcto: da el sabado mas cercano (26 sep) O pide la ciudad que
    falta antes de hablar de fechas (eso tambien es seguir el flujo)."""
    p = plano(r)
    if "26" in p and "septiembre" in p:
        return True
    return "ciudad" in p and ("bogot" in p or "medell" in p)


def rev_precio(r, tools):
    """El prompt dice Botox = $25.000 POR UNIDAD (los $540.000 son de
    Radiofrecuencia Fraccionada): los dos modelos acertaron y mi test no."""
    p = plano(r)
    return "25.000" in p or "25,000" in p or "25000" in p


def rev_horas(r, tools):
    """Sirve si ofrece una hora concreta, o si aparta la hora y pide la
    cedula (que es justo lo que manda el paso 4 del flujo)."""
    p = plano(r)
    if re.search(r"\b\d{1,2}:\d{2}\b", p):
        return True
    return ("apart" in p or "reserv" in p) and ("cédula" in p or "cedula" in p)


def rev_inventada(r, tools):
    """Tiene que decir que no la conoce Y ofrecer a las reales. Hay muchas
    formas de decir «no la conozco»: no vale quedarse con una sola."""
    p = plano(r)
    dice_no = any(x in p for x in (
        "no tengo", "no está", "no esta", "no encuentro", "no aparece",
        "no trabaja", "no está en nuestro", "no está en el equipo",
        "no hace parte", "no contamos", "no forma parte"))
    ofrece = any(x in p for x in ("cueter", "arias", "valentina", "diana"))
    return dice_no and ofrece


CASOS = [
    ("Reconoce al Dr. Cueter (nombre corto)",
     "¿El Dr. Cueter atiende el sábado en Medellín?", rev_cueter),
    ("Valentina NO hace remoción y dice quién sí",
     "¿Puedo hacerme la remoción de micropigmentación con Valentina en El Tesoro?",
     rev_valentina),
    ("«Próximo sábado» = el más cercano (26 sep)",
     "¿Tienes cita para botox el próximo sábado?", rev_sabado),
    ("Precio del botox sin equivocarse",
     "¿Cuánto cuesta el botox en Medellín?", rev_precio),
    ("Ofrece horas reales para agendar",
     "Quiero agendar botox en Medellín el 26 de septiembre a las 10 de la mañana",
     rev_horas),
    ("Especialista inventada: no la inventa, ofrece las reales",
     "¿Me puede atender la Dra. Gómez?", rev_inventada),
]


async def correr(modelo):
    m.PRIMARY_MODEL = modelo
    print("\n" + "=" * 76)
    print("MODELO: %s" % modelo)
    print("=" * 76)
    filas = []
    for titulo, pregunta, revisor in CASOS:
        HERRAMIENTAS_USADAS.clear()
        t0 = time.time()
        try:
            r = await m.ask_pepe(pregunta, history=[], telefono="3012466958",
                                 client_id=None)
        except Exception as e:
            r, dt = "ERROR: %s" % e, time.time() - t0
        else:
            dt = time.time() - t0
        bien = revisor(r, list(HERRAMIENTAS_USADAS))
        filas.append((titulo, bien, dt, list(HERRAMIENTAS_USADAS), r))
        print("\n  %s  %s  (%.1fs)" % ("OK   " if bien else "FALLA", titulo, dt))
        print("      herramientas: %s" % (HERRAMIENTAS_USADAS or "ninguna"))
        print("      dijo: %s" % plano(r)[:180])
    return filas


async def principal():
    resultados = {}
    for modelo in MODELOS:
        resultados[modelo] = await correr(modelo)

    print("\n\n" + "=" * 82)
    print("COMPARACION (%d casos, el flujo real de Pepe)" % len(CASOS))
    print("=" * 82)
    print("  %-40s %s" % ("CASO", "  ".join("%-13s" % _nombre(m)
                                             for m in MODELOS)))
    print("  " + "-" * 78)
    for i, (titulo, _, _) in enumerate(CASOS):
        celdas = []
        for modelo in MODELOS:
            f = resultados[modelo][i]
            celdas.append(("%s %.1fs" % ("OK   " if f[1] else "FALLA", f[2]))[:13])
        print("  %-40s %s" % (titulo[:40], "  ".join("%-13s" % c for c in celdas)))
    print("  " + "-" * 78)
    for modelo in MODELOS:
        f = resultados[modelo]
        aciertos = sum(1 for x in f if x[1])
        total = sum(x[2] for x in f)
        print("  %-16s %d/%d aciertos  |  %5.0fs en total  |  %5.1fs promedio"
              % (_nombre(modelo), aciertos, len(f), total, total / len(f)))


if __name__ == "__main__":
    asyncio.run(principal())
