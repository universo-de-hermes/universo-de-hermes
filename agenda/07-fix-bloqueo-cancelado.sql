-- ============================================================================
--  Arreglo: un bloqueo CANCELADO debe liberar el cupo.
--
--  citas_calcular_ocupa() forzaba ocupa_cupo := true para todo tipo='bloqueo',
--  sin mirar el estado. Resultado: anular un bloqueo (una incapacidad que ya
--  no fue, una cita médica que se movió) no devolvía el horario a la agenda,
--  y ese rango quedaba muerto para siempre.
--
--  Ahora un bloqueo cancelado libera el cupo, igual que una cita.
--  Un bloqueo en cualquier otro estado (abierto, atendido, ausente) lo ocupa,
--  porque para eso está.
-- ============================================================================

create or replace function citas_calcular_ocupa()
returns trigger
language plpgsql
as $fn$
declare t text;
begin
  select tipo into t from estados where id = new.estado_id;
  t := coalesce(t, 'abierto');

  if new.tipo = 'bloqueo' then
    -- un bloqueo cancelado ya no bloquea nada
    new.ocupa_cupo := (t <> 'cancelado');
  else
    new.ocupa_cupo := t not in ('movido','cancelado');
  end if;

  return new;
end;
$fn$;

-- Recalcular los bloqueos que ya existen (el trigger solo corre al insertar o
-- actualizar, así que los viejos se quedaron con el valor anterior).
update citas c
   set ocupa_cupo = (coalesce(e.tipo,'abierto') <> 'cancelado')
  from estados e
 where e.id = c.estado_id
   and c.tipo = 'bloqueo'
   and c.ocupa_cupo is distinct from (coalesce(e.tipo,'abierto') <> 'cancelado');

select 'bloqueos que ocupan cupo' as que, count(*)::text as n
  from citas where tipo='bloqueo' and ocupa_cupo
union all
select 'bloqueos cancelados (ya no ocupan)', count(*)::text
  from citas c join estados e on e.id=c.estado_id
 where c.tipo='bloqueo' and not c.ocupa_cupo;
