-- ============================================================================
--  Se corre después de instalar. Cada línea dice ok o MAL.
--  Si todo sale ok, la base quedó bien y el agente puede empezar a agendar.
\set QUIET on
-- ============================================================================
\pset tuples_only on
\pset format unaligned

select case when (select count(*) from sedes) = 2
            then 'ok   2 sedes'
            else 'MAL  sedes: ' || (select count(*) from sedes) end
union all select case when (select count(*) from estados) = 7
            then 'ok   7 estados' else 'MAL  estados' end
union all select case when (select count(*) from servicios) = 27
            then 'ok   27 servicios' else 'MAL  servicios' end
union all select case when (select count(*) from especialistas) = 7
            then 'ok   7 especialistas' else 'MAL  especialistas' end
union all select case when (select count(*) from horarios) = 48
            then 'ok   48 franjas de horario' else 'MAL  horarios' end
union all select case when (select count(*) from clientes where importado) = 426
            then 'ok   426 clientes' else 'MAL  clientes' end
union all select case when (select count(*) from citas where importado) = 1322
            then 'ok   1.322 citas' else 'MAL  citas' end
union all select case when (select count(*) from cita_bitacora) >= 1322
            then 'ok   bitácora poblada' else 'MAL  bitácora' end
union all select case when (select min(fecha)::text || ' a ' || max(fecha)::text from citas)
                        = '2026-06-01 a 2026-08-31'
            then 'ok   rango 1 jun – 31 ago 2026' else 'MAL  rango de fechas' end
union all select case when (select count(*) from v_solapes) = 177
            then 'ok   177 solapes del histórico, los esperados'
            else 'MAL  solapes: ' || (select count(*) from v_solapes) end
union all select case when exists (select 1 from pg_extension where extname='btree_gist')
            then 'ok   btree_gist instalada' else 'MAL  falta btree_gist' end
union all select case when exists (
              select 1 from pg_constraint where conname = 'citas_sin_solape')
            then 'ok   restricción anti doble-agendamiento activa'
            else 'MAL  falta citas_sin_solape' end
union all select case when (select count(*) from estados where inicial and activo) = 1
            then 'ok   hay un único estado inicial'
            else 'MAL  estado inicial' end
union all select case when exists (select 1 from estados where tipo='movido' and activo)
            then 'ok   hay estado de tipo movido (para reprogramar)'
            else 'MAL  falta un estado de tipo movido' end
union all select case when (
              select titulizar('LAURA MARTÍNEZ NÚÑEZ')) = 'Laura Martínez Núñez'
            then 'ok   los nombres salen presentables, con tildes'
            else 'MAL  titulizar() no maneja tildes en este locale: '
                 || (select titulizar('LAURA MARTÍNEZ NÚÑEZ')) end;

-- prueba de fuego: agendar, chocar y soltar, sin dejar rastro
do $$
declare
  v_esp  text; v_sede text; v_cli text; v_f date; v_h time; v_n int; v_id text;
  v_ok   boolean := true;
begin
  -- el primer hueco real de los próximos 30 días
  select especialista_id, sede_id, fecha, inicio
    into v_esp, v_sede, v_f, v_h
    from buscar_huecos(current_date, 30, null, null, null, 30, 30, 1);

  if v_esp is null then
    raise notice 'MAL  no hay ningún hueco libre en 30 días (¿faltan horarios?)';
    return;
  end if;

  select id into v_cli from clientes limit 1;

  v_id := (agendar_cita(v_cli, v_esp, v_sede, v_f, v_h, null, null,
                        'Prueba', 'verificar')).id;

  select count(*) into v_n from huecos_del_dia(v_f, v_sede, v_esp, null, 30, 30)
   where inicio = v_h;
  if v_n <> 0 then
    raise notice 'MAL  el hueco sigue ofreciéndose después de agendarlo'; v_ok := false;
  end if;

  begin
    perform agendar_cita(v_cli, v_esp, v_sede, v_f, v_h);
    raise notice 'MAL  dejó agendar dos veces la misma hora'; v_ok := false;
  exception when others then
    if sqlerrm not like 'CUPO_TOMADO%' then
      raise notice 'MAL  error inesperado al chocar: %', sqlerrm; v_ok := false;
    end if;
  end;

  delete from cita_bitacora where cita_id = v_id;
  delete from citas where id = v_id;

  if v_ok then
    raise notice 'ok   prueba de agendamiento: agenda, ocupa el cupo y rechaza el choque';
  end if;
end $$;
