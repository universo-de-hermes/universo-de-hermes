-- Limpieza de datos de prueba dejados por probar_api.py
-- Deja la base en el estado original + Valentina reactivada

BEGIN;

-- 1. Reactivar a Valentina (desactivada por las pruebas)
UPDATE especialistas SET activo = true WHERE id = 'esp-valentina-rivillas-baquero-42';

-- 2. Borrar citas de prueba (bitacora primero por FK)
DELETE FROM cita_bitacora WHERE cita_id IN (
  SELECT id FROM citas
  WHERE tipo = 'bloqueo'
     OR cliente_id IN ('cli-90909090','cli-999999998','cli-999999999')
     OR id IN ('c_6711f455afa1426f83a95d3a1bec7551')
);
DELETE FROM citas
  WHERE tipo = 'bloqueo'
     OR cliente_id IN ('cli-90909090','cli-999999998','cli-999999999')
     OR id IN ('c_6711f455afa1426f83a95d3a1bec7551');

-- 3. Borrar reservas de prueba
DELETE FROM reservas WHERE referencia LIKE '%prueba%' OR referencia LIKE 'test%' OR especialista_id LIKE 'esp_local%';

-- 4. Borrar clientes de prueba
DELETE FROM clientes WHERE id IN ('cli-90909090','cli-999999998','cli-999999999')
   OR documento IN ('90909090','999999998','999999999');

-- 5. Borrar especialistas de prueba y sus dependencias
DELETE FROM horarios WHERE especialista_id IN ('esp-ana-prueba','esp_local_1','esp_local_2');
DELETE FROM especialista_sedes WHERE especialista_id IN ('esp-ana-prueba','esp_local_1','esp_local_2');
DELETE FROM especialista_servicios WHERE especialista_id IN ('esp-ana-prueba','esp_local_1','esp_local_2');
DELETE FROM especialistas WHERE id IN ('esp-ana-prueba','esp_local_1','esp_local_2');

-- 6. Borrar estados y servicios de prueba
DELETE FROM estados WHERE id NOT IN ('est-pendiente','est-confirmado','est-cumplido','est-realizado','est-reprogramado','est-incumplido','est-cancelado');
DELETE FROM servicios WHERE id NOT LIKE 'srv-%';

-- 7. Borrar usuarios de prueba si los hubiera
DELETE FROM sesiones WHERE usuario_id LIKE 'u-prueba%';
DELETE FROM usuarios WHERE id LIKE 'u-prueba%';

COMMIT;

-- Verificacion
SELECT 'especialistas activos' AS que, count(*)::text AS n FROM especialistas WHERE activo
UNION ALL SELECT 'horarios', count(*)::text FROM horarios
UNION ALL SELECT 'citas futuras', count(*)::text FROM citas WHERE fecha >= CURRENT_DATE
UNION ALL SELECT 'clientes', count(*)::text FROM clientes
UNION ALL SELECT 'servicios', count(*)::text FROM servicios
UNION ALL SELECT 'estados', count(*)::text FROM estados;