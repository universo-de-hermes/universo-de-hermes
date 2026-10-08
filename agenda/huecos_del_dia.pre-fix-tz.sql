CREATE OR REPLACE FUNCTION public.huecos_del_dia(p_fecha date, p_sede text DEFAULT NULL::text, p_especialista text DEFAULT NULL::text, p_servicio text DEFAULT NULL::text, p_duracion integer DEFAULT NULL::integer, p_paso integer DEFAULT 15, p_margen integer DEFAULT 15)
 RETURNS TABLE(fecha date, inicio time without time zone, fin time without time zone, especialista_id text, sede_id text)
 LANGUAGE sql
 STABLE
AS $function$
  with parms as (
    select coalesce(p_duracion,
                    (select duracion from servicios where id = p_servicio),
                    30)                        as dur,
           greatest(coalesce(p_paso,15), 5)    as paso,
           extract(dow from p_fecha)::int      as dow
  ),
  esps as (
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
  ),
  franja as (
    -- horario semanal: se ignora si esa especialista tiene horario puntual
    -- para esa fecha Y esa sede (el puntual manda)
    select h.especialista_id, h.sede_id, h.desde, h.hasta,
           h.alm_desde, h.alm_hasta, p.dur, p.paso
    from horarios h
    join parms p on h.dia = p.dow
    join esps   on esps.id = h.especialista_id
    where (p_sede is null or h.sede_id = p_sede)
      and not exists (
        select 1 from horarios_fecha hf
        where hf.especialista_id = h.especialista_id
          and hf.sede_id         = h.sede_id
          and hf.fecha           = p_fecha)
    union all
    -- horario puntual de esa fecha: manda y reemplaza al semanal
    select h.especialista_id, h.sede_id, h.desde, h.hasta,
           h.alm_desde, h.alm_hasta, p.dur, p.paso
    from horarios_fecha h
    join parms p on true
    join esps   on esps.id = h.especialista_id
    where h.fecha = p_fecha
      and (p_sede is null or h.sede_id = p_sede)
  ),
  cand as (
    select f.especialista_id, f.sede_id, f.alm_desde, f.alm_hasta,
           (f.desde + (g.n           || ' minutes')::interval)::time as ini,
           (f.desde + ((g.n + f.dur) || ' minutes')::interval)::time as fin
    from franja f
    cross join lateral generate_series(
      0,
      greatest((extract(epoch from (f.hasta - f.desde)) / 60)::int - f.dur, -1),
      f.paso
    ) as g(n)
  )
  select p_fecha, c.ini, c.fin, c.especialista_id, c.sede_id
  from cand c
  where
    -- ya pasó (solo aplica si el día es hoy)
    not (p_fecha = current_date
         and (p_fecha + c.ini) < now() + (coalesce(p_margen,15) || ' minutes')::interval)
    -- almuerzo
    and not (c.alm_desde is not null and c.ini < c.alm_hasta and c.fin > c.alm_desde)
    -- citas que ocupan cupo (incluye bloqueos)
    and not exists (
      select 1 from citas ct
      where ct.especialista_id = c.especialista_id
        and ct.fecha = p_fecha
        and ct.ocupa_cupo
        and ct.inicio < c.fin and ct.fin > c.ini)
    -- cupos apartados que siguen vivos
    and not exists (
      select 1 from reservas r
      where r.especialista_id = c.especialista_id
        and r.fecha = p_fecha
        and r.expira_en > now()
        and r.inicio < c.fin and r.fin > c.ini)
  order by c.ini, c.especialista_id;
$function$
