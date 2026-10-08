#!/usr/bin/env bash
# Regresion de los arneses de Claude despues de tocar tiempo, direccion y nombres.
set -u
cd /root/universo/agenda/_paquete2/tools || exit 1
set -a; . /root/universo/agenda/.api_env; set +a
export PANEL_CORREO=jhotas96@gmail.com
export PANEL_CLAVE=TzEi4LntP6I8TC
export AUTOSERVICIO_TOPE_CLIENTE=500

LIMPIAR=/home/claude/limpiar-prueba.py
for d in 999000444 999000777; do python3 "$LIMPIAR" "$d" >/dev/null 2>&1; done

# La tablet tiene que estar ABIERTA: los arneses de navegador y mi bateria la
# necesitan asi. (Cuidado: probar_panel.py la CIERRA al terminar.)
echo "=== abriendo la tablet ==="
/root/universo/agenda/venv/bin/python /root/universo/agenda/abrir_tablet.py el-tesoro

echo "################ 1. probar-agenda.js ################"
node probar-agenda.js 2>&1 | tail -12

echo ""
echo "################ 2. probar-tablet.js ################"
node probar-tablet.js 2>&1 | tail -8

echo ""
echo "################ 3. probar-ios9.js ################"
node probar-ios9.js 2>&1 | tail -8

echo ""
echo "##### limpieza #####"
for d in 999000444 999000777; do python3 "$LIMPIAR" "$d" 2>&1 | tail -1; done

echo ""
echo "################ 4. mi bateria (probar_panel.py) ################"
cd /root/universo/agenda
/root/universo/agenda/venv/bin/python probar_panel.py 2>&1 | tail -10

echo ""
echo "################ 5. auditor de CSS ################"
/root/universo/agenda/venv/bin/python _paquete2/tools/auditar-css.py /var/www/html/autoservicio.html 2>&1 | tail -3
/root/universo/agenda/venv/bin/python _paquete2/tools/auditar-css.py /var/www/html/agenda.html 2>&1 | tail -3

echo ""
echo "################ 6. PRODUCCION == ENTREGA DE CLAUDE? ################"
md5sum /var/www/html/agenda.html /var/www/html/autoservicio.html /root/universo/agenda/autoservicio.py
echo "   (esperado: autoservicio.py f5dab68cd530; los HTML cambian por mis cambios)"

echo ""
echo "################ 7. FOTO DE LA BASE ################"
/root/universo/agenda/venv/bin/python /root/universo/agenda/estado_final.py
