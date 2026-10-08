#!/usr/bin/env bash
# Corre el auditor de pantallas SIN dejar basura.
# OJO: el auditor necesita la TABLET ABIERTA (mi bateria la cierra al terminar),
# si no, se queda esperando la bienvenida y se cae por timeout.
set -u
cd /root/universo/agenda/_paquete2/tools || exit 1
set -a; . /root/universo/agenda/.api_env; set +a
export PANEL_CORREO=jhotas96@gmail.com
export PANEL_CLAVE=TzEi4LntP6I8TC

LIMPIAR=/home/claude/limpiar-prueba.py

echo "=== abrir la tablet ==="
/root/universo/agenda/venv/bin/python /root/universo/agenda/abrir_tablet.py el-tesoro

echo ""
echo "=== limpieza previa ==="
for d in 999000777 999000444; do python3 "$LIMPIAR" "$d" 2>&1 | tail -1; done

echo ""
echo "=== auditoria de pantallas ==="
node auditar-pantallas.js 2>&1 | tail -30

echo ""
echo "=== limpieza posterior ==="
for d in 999000777 999000444; do python3 "$LIMPIAR" "$d" 2>&1 | tail -1; done

echo ""
echo "=== foto de la base ==="
/root/universo/agenda/venv/bin/python /root/universo/agenda/estado_final.py 2>&1 | tail -6
