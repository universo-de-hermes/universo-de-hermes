-- ============================================================================
--  Horarios por fecha puntual + bloqueos en varios días
--  Se corre una sola vez sobre la base que ya está montada.
--
--  1) horarios_fecha: "este lunes trabaja de 2 a 6, y el otro no"
--     Si una especialista tiene filas en horarios_fecha para una fecha y sede,
--     esas filas MANDAN ese día en esa sede y el horario semanal se ignora.
--     Si no tiene ninguna, sigue rigiendo el horario semanal de siempre.
--
--  2) huecos_del_dia: se reescribe para respetar lo anterior.
--     Todo lo demás (almuerzo, citas que ocupan cupo, cupos apartados,
--     margen de anticipación) queda igual.
--
--  3) bloquear_rango(): bloquea varias fechas de una sola vez
--     (cita médica, incapacidad, vacaciones) escogiendo horas y días.
-- ============================================================================

-- ───────────────────────────── 1. Tabla ─────────────────────────────
create table if not exists horarios_fecha (
  id              bigserial primary key,
  especialista_id text not null references especialistas(id) on delete cascade,
  sede_id         text not null references sedes(id) on delete cascade,
  fecha           date not null,
  desde           time not null,
  hasta           time not null,
  alm_desde       time,
  alm_hasta       time,
  nota            text not null default '',
  creado_en       timestamp not null default now(),
  creado_por      text not null default '',
  constraint horarios_fecha_check  check (hasta > desde),
  constraint horarios_fecha_check1 check ((alm_desde is null) = (alm_hasta is null)),
  constraint horarios_fecha_check2 check (alm_desde is null or alm_hasta > alm_desde),
  constraint horarios_fecha_unica  unique (especialista_id, sede_id, fecha, desde)
);

create index if not exists horarios_fecha_busqueda
  on horarios_fecha (especialista_id, fecha);
create index if not exists horarios_fecha_dia
  on horarios_fecha (fecha);


-- ─────────────────── 2. huecos_del_dia (con fechas puntuales) ───────────────────
create or replace function huecos_del_dia(
  p_fecha date,
  p_sede text default null,
  p_especialista text default null,
  p_servicio text default null,
  p_duracion integer default null,
  p_paso integer default 15,
  p_margen integer default 15)
returns table(fecha date, inicio time without time zone,
              fin time without time zone, especialista_id text, sede_id text)
language sql
stable
as $fn$
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
$fn$;


-- ─────────────── 3. bloquear_rango: varios días de una vez ───────────────
-- p_dias: dias de la semana a incluir (0=domingo .. 6=sabado).
--         null = todos los dias del rango.
-- Devuelve una fila por cada fecha evaluada, diciendo si se creó o por qué no.
create or replace function bloquear_rango(
  p_especialista text,
  p_sede         text,
  p_desde        date,
  p_hasta        date,
  p_inicio       time,
  p_fin          time,
  p_motivo       text default 'Bloqueo',
  p_por          text default '',
  p_dias         int[] default null)
returns table(fecha date, creado boolean, detalle text)
language plpgsql
as $fn$
declare
  d date;
  v_dow int;
  v_id text;
  v_choque text;
begin
  if p_hasta < p_desde then
    raise exception 'FECHA_INVALIDA: la fecha final es anterior a la inicial';
  end if;
  if p_fin <= p_inicio then
    raise exception 'HORA_INVALIDA: la hora de fin debe ser mayor a la de inicio';
  end if;
  if not exists (select 1 from especialistas where id = p_especialista) then
    raise exception 'ESPECIALISTA_NO_EXISTE: %', p_especialista;
  end if;
  if not exists (select 1 from sedes where id = p_sede) then
    raise exception 'SEDE_NO_EXISTE: %', p_sede;
  end if;

  d := p_desde;
  while d <= p_hasta loop
    v_dow := extract(dow from d)::int;
    if p_dias is null or v_dow = any(p_dias) then
      -- ¿choca con una cita o bloqueo que ya ocupa ese cupo?
      select ct.id into v_choque
        from citas ct
       where ct.especialista_id = p_especialista
         and ct.fecha = d
         and ct.ocupa_cupo
         and ct.inicio < p_fin and ct.fin > p_inicio
       limit 1;

      if v_choque is not null then
        fecha := d; creado := false;
        detalle := 'Ya hay una cita o bloqueo en ese rango (' || v_choque || ')';
        return next;
      else
        v_id := 'b_' || replace(gen_random_uuid()::text, '-', '');
        insert into citas(id, tipo, fecha, inicio, fin, especialista_id, sede_id,
                          estado_id, canal, motivo, notas, creado_por)
        values (v_id, 'bloqueo', d, p_inicio, p_fin, p_especialista, p_sede,
                (select id from estados where inicial and activo limit 1),
                'manual', p_motivo, p_motivo, p_por);
        fecha := d; creado := true; detalle := 'Bloqueado';
        return next;
      end if;
    end if;
    d := d + 1;
  end loop;
end;
$fn$;


-- ─────────────── 4. horario puntual en varios días de una vez ───────────────
-- Crea la misma franja de horario en varias fechas escogidas.
create or replace function horario_fecha_rango(
  p_especialista text,
  p_sede         text,
  p_desde        date,
  p_hasta        date,
  p_inicio       time,
  p_fin          time,
  p_alm_desde    time default null,
  p_alm_hasta    time default null,
  p_nota         text default '',
  p_por          text default '',
  p_dias         int[] default null,
  p_reemplazar   boolean default true)
returns table(fecha date, creado boolean, detalle text)
language plpgsql
as $fn$
declare
  d date;
  v_dow int;
begin
  if p_hasta < p_desde then
    raise exception 'FECHA_INVALIDA: la fecha final es anterior a la inicial';
  end if;
  if p_fin <= p_inicio then
    raise exception 'HORA_INVALIDA: la hora de fin debe ser mayor a la de inicio';
  end if;
  if (p_alm_desde is null) <> (p_alm_hasta is null) then
    raise exception 'ALMUERZO_INCOMPLETO: hay que dar las dos horas del almuerzo o ninguna';
  end if;

  d := p_desde;
  while d <= p_hasta loop
    v_dow := extract(dow from d)::int;
    if p_dias is null or v_dow = any(p_dias) then
      if p_reemplazar then
        delete from horarios_fecha hf
         where hf.especialista_id = p_especialista
           and hf.sede_id = p_sede
           and hf.fecha = d;
      end if;
      insert into horarios_fecha(especialista_id, sede_id, fecha, desde, hasta,
                                 alm_desde, alm_hasta, nota, creado_por)
      values (p_especialista, p_sede, d, p_inicio, p_fin,
              p_alm_desde, p_alm_hasta, p_nota, p_por)
      on conflict on constraint horarios_fecha_unica do update
        set hasta = excluded.hasta,
            alm_desde = excluded.alm_desde,
            alm_hasta = excluded.alm_hasta,
            nota = excluded.nota;
      fecha := d; creado := true; detalle := 'Horario puesto';
      return next;
    end if;
    d := d + 1;
  end loop;
end;
$fn$;


-- ─────────────── 5. Verificación ───────────────
select 'tabla horarios_fecha' as que,
       case when exists (select 1 from information_schema.tables
                         where table_name='horarios_fecha')
            then 'OK' else 'FALTA' end as estado
union all
select 'huecos_del_dia reescrita',
       case when (select prosrc from pg_proc where proname='huecos_del_dia')
                 like '%horarios_fecha%' then 'OK' else 'FALTA' end
union all
select 'bloquear_rango', case when exists (select 1 from pg_proc where proname='bloquear_rango')
       then 'OK' else 'FALTA' end
union all
select 'horario_fecha_rango', case when exists (select 1 from pg_proc where proname='horario_fecha_rango')
       then 'OK' else 'FALTA' end;
