#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprueba que el prompt ACTIVO ya trae las reglas nuevas."""
import sys

sys.path.insert(0, "/root/universo/recepcionista")
from dotenv import load_dotenv     # noqa: E402
load_dotenv()

import herramientas                # noqa: E402

bloque = herramientas.BLOQUE_PROMPT
i = bloque.find("## Cuándo NO sigues tú")
print("=== REGLAS DE ESCALAMIENTO EN EL PROMPT ACTIVO ===")
print(bloque[i:i + 1200] if i >= 0 else "NO ENCONTRADO")

print()
print("=== DESCRIPCION DE LA HERRAMIENTA pasar_a_asesor ===")
for t in herramientas.HERRAMIENTAS:
    if t["function"]["name"] == "pasar_a_asesor":
        print(t["function"]["description"])
        print("motivos permitidos:",
              t["function"]["parameters"]["properties"]["motivo"]["enum"])
