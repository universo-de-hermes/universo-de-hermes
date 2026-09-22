-- Limpieza completa: datos de prueba de probar_api.py + probar_pepe.py
-- Deja la base como estaba: 7 especialistas activos, 48 horarios, 0 citas futuras

BEGIN;

-- 1. Reactivar especialistas reales desactivados por las pruebas
--    (Laura Martínez NO va aquí: ya no trabaja en CJ Medical)
UPDATE especialistas SET activo = true
 WHERE id IN ('esp-valentina-rivillas-baquero-42','esp-diana-carolina-ruiz-rojas',
              'esp-jorge-ramiro-cueter-guzman-17','esp-julie-viviana-arias-hernandez-20',
              'esp-manuela-betancur-agudelo-28',
              'esp-martha-isabel-lopez-suarez');

-- Laura Martínez ya no trabaja: queda desactivada siempre
UPDATE especialistas SET activo = false
 WHERE id = 'esp-laura-marithza-martinez-martinez-23';

-- 2. Citas de prueba (bitacora primero por FK)
DELETE FROM cita_bitacora WHERE cita_id IN (
  SELECT id FROM citas
  WHERE tipo = 'bloqueo'
     OR cliente_id IN ('cli-90909090','cli-999999998','cli-999999999',
                       'cli-1122334455','cli-1000084923')
     OR cliente_id IN (SELECT id FROM clientes WHERE documento IN
        ('90909090','999999998','999999999','1122334455','1000084923'))
);
DELETE FROM citas
  WHERE tipo = 'bloqueo'
     OR cliente_id IN ('cli-90909090','cli-999999998','cli-999999999',
                       'cli-1122334455','cli-1000084923')
     OR cliente_id IN (SELECT id FROM clientes WHERE documento IN
        ('90909090','999999998','999999999','1122334455','1000084923'));

-- 3. Reservas de prueba
DELETE FROM reservas WHERE referencia LIKE '%prueba%' OR referencia LIKE 'test%'
   OR referencia LIKE 'pepe%' OR especialista_id LIKE 'esp_local%' OR especialista_id LIKE 'esp-ana%';

-- 4. Clientes de prueba
DELETE FROM clientes WHERE documento IN ('90909090','999999998','999999999','1122334455','1000084923')
   OR id IN ('cli-90909090','cli-999999998','cli-999999999','cli-1122334455','cli-1000084923');

-- 5. Especialistas de prueba
DELETE FROM horarios WHERE especialista_id LIKE 'esp-ana-prueba' OR especialista_id LIKE 'esp_local%';
DELETE FROM especialista_sedes WHERE especialista_id LIKE 'esp-ana-prueba' OR especialista_id LIKE 'esp_local%';
DELETE FROM especialista_servicios WHERE especialista_id LIKE 'esp-ana-prueba' OR especialista_id LIKE 'esp_local%';
DELETE FROM especialistas WHERE id LIKE 'esp-ana-prueba' OR id LIKE 'esp_local%';

-- 6. Estados y servicios de prueba
DELETE FROM estados WHERE id NOT IN ('est-pendiente','est-confirmado','est-cumplido',
                                     'est-realizado','est-reprogramado','est-incumplido','est-cancelado');
DELETE FROM servicios WHERE id NOT LIKE 'srv-%';

-- 7. Usuarios de prueba
DELETE FROM sesiones WHERE usuario_id LIKE 'u-prueba%';
DELETE FROM usuarios WHERE id LIKE 'u-prueba%';

COMMIT;

SELECT 'especialistas activos' AS que, count(*)::text AS n FROM especialistas WHERE activo
UNION ALL SELECT 'horarios', count(*)::text FROM horarios
UNION ALL SELECT 'citas futuras', count(*)::text FROM citas WHERE fecha >= CURRENT_DATE
UNION ALL SELECT 'clientes', count(*)::text FROM clientes
UNION ALL SELECT 'servicios', count(*)::text FROM servicios
UNION ALL SELECT 'estados', count(*)::text FROM estados;