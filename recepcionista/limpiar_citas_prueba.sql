\echo 'Citas de prueba de la PRIMERA corrida de verificacion:'
select id, fecha, to_char(inicio,'HH24:MI') as hora, estado_id
  from citas where id in ('c_ccac0ef0a6d34ca6aae336c3e399eb5d',
                          'c_a769a433cab348a0a94135b19cbf4955');

delete from cita_bitacora where cita_id in ('c_ccac0ef0a6d34ca6aae336c3e399eb5d',
                                            'c_a769a433cab348a0a94135b19cbf4955');
delete from citas where id in ('c_ccac0ef0a6d34ca6aae336c3e399eb5d',
                               'c_a769a433cab348a0a94135b19cbf4955');

\echo ''
\echo 'Citas que quedan creadas por Pepe (canal Agente IA):'
select count(*) as total from citas where asignada_por ilike 'pepe';
