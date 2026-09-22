-- 08 - Franjas de trabajo de un especialista en una fecha concreta.
--
-- Para qué: el bot necesita responder «¿Valentina trabaja el lunes?» y «¿a qué
-- horas?». huecos_del_dia() solo devuelve las horas LIBRES, y de ahí no se
-- puede distinguir «no trabaja» de «trabaja pero está lleno».
--
-- Misma regla que huecos_del_dia: el horario puntual de esa fecha manda y
-- reemplaza al semanal; si no hay puntual, se usa el horario semanal del día.
-- OJO: si algún día cambia esa regla, hay que cambiarla en los dos lados.
--
-- p_servicio sirve para no listar especialistas que no hacen ese servicio.

create or replace function franjas_del_dia(
    p_fecha        date,
    p_sede         text default null,
    p_especialista text default null,
    p_servicio     text default null)
returns table(especialista_id text,
              sede_id         text,
              desde           time,
              hasta           time,
              alm_desde       time,
              alm_hasta       time,
              origen          text)
language sql
stable
as $$
  with esps as (
    select e.id
    from especialistas e
    where e.activo
      and (p_especialista is null or e.id = p_especialista)
      and (p_sede is null or exists (
             select 1 from especialista_sedes s
             where s.especialista_id = e.id and s.sede_id = p_sede))
      -- sin servicios asignados = hace todos (misma regla que la web)
      and (p_servicio is null
           or not exists (select 1 from especialista_servicios x
                          where x.especialista_id = e.id)
           or exists (select 1 from especialista_servicios x
                      where x.especialista_id = e.id and x.servicio_id = p_servicio))
  )
  select h.especialista_id, h.sede_id, h.desde, h.hasta,
         h.alm_desde, h.alm_hasta, 'semanal'::text
    from horarios h
    join esps on esps.id = h.especialista_id
   where h.dia = extract(dow from p_fecha)::int
     and (p_sede is null or h.sede_id = p_sede)
     and not exists (
       select 1 from horarios_fecha hf
       where hf.especialista_id = h.especialista_id
         and hf.sede_id         = h.sede_id
         and hf.fecha           = p_fecha)
  union all
  select h.especialista_id, h.sede_id, h.desde, h.hasta,
         h.alm_desde, h.alm_hasta, 'puntual'::text
    from horarios_fecha h
    join esps on esps.id = h.especialista_id
   where h.fecha = p_fecha
     and (p_sede is null or h.sede_id = p_sede)
   order by 1, 3
$$;
