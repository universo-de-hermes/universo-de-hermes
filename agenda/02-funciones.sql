-- ============================================================================
--  Agenda CJ Medical · reglas de negocio
--
--  Todo lo que agenda —la web, el call center y Hermes— pasa por aquí.
--  Si el agente inventa su propia lógica de disponibilidad, tarde o temprano
--  ofrece una hora que la base rechaza. Usa estas funciones.
-- ============================================================================

-- ---------------------------------------------------------------------------
--  huecos_del_dia: los espacios libres de un día.
--
--  Es la traducción exacta de huecosDelDia() de la agenda web:
--    horario de la especialista en ese día (y sede, si se pide)
--    menos el almuerzo
--    menos las citas que ocupan cupo  (canceladas y reprogramadas NO ocupan)
--    menos los cupos apartados que siguen vivos
--    en pasos de p_paso minutos, con la duración del servicio
--
--  Una diferencia a propósito con la web: la ocupación se mira por
--  especialista, no por sede. Una persona no puede estar en Bogotá y en
--  El Tesoro a la misma hora, y la restricción citas_sin_solape tampoco lo
--  permite; si aquí filtráramos por sede ofreceríamos horas que la base
--  después rechaza.
-- ---------------------------------------------------------------------------
create or replace function huecos_del_dia(
  p_fecha        date,
  p_sede         text default null,
  p_especialista text default null,
  p_servicio     text default null,
  p_duracion     int  default null,   -- si es null, la duración del servicio
  p_paso         int  default 15,
  p_margen       int  default 15      -- para hoy: minutos mínimos desde ahora
) returns table (
  fecha date, inicio time, fin time, especialista_id text, sede_id text
) language sql stable as $$
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
    select h.especialista_id, h.sede_id, h.desde, h.hasta,
           h.alm_desde, h.alm_hasta, p.dur, p.paso
    from horarios h
    join parms p on h.dia = p.dow
    join esps   on esps.id = h.especialista_id
    where p_sede is null or h.sede_id = p_sede
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
    -- citas que ocupan cupo
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
$$;

-- Varios días de una, que es como pregunta el agente:
--   «¿cuándo tienes para depilación láser esta semana?»
create or replace function buscar_huecos(
  p_desde        date,
  p_dias         int  default 14,
  p_sede         text default null,
  p_especialista text default null,
  p_servicio     text default null,
  p_duracion     int  default null,
  p_paso         int  default 15,
  p_limite       int  default 60
) returns table (
  fecha date, inicio time, fin time, especialista_id text, sede_id text
) language sql stable as $$
  select h.*
  from generate_series(p_desde, p_desde + (greatest(p_dias,1) - 1), interval '1 day') d
  cross join lateral huecos_del_dia(
    d::date, p_sede, p_especialista, p_servicio, p_duracion, p_paso) h
  order by h.fecha, h.inicio, h.especialista_id
  limit greatest(coalesce(p_limite,60), 1);
$$;

-- ---------------------------------------------------------------------------
--  apartar_cupo: reserva temporal mientras el agente negocia por WhatsApp.
--  Sin esto, dos conversaciones a la vez prometen la misma hora.
--  Vence sola. Devuelve la reserva; si el cupo ya no está, levanta error.
-- ---------------------------------------------------------------------------
create or replace function apartar_cupo(
  p_especialista text,
  p_sede         text,
  p_fecha        date,
  p_inicio       time,
  p_fin          time default null,
  p_servicio     text default null,
  p_minutos      int  default 5,
  p_referencia   text default '',
  p_canal        text default 'WhatsApp'
) returns reservas
language plpgsql as $$
declare
  v_fin time;
  v_res reservas;
begin
  perform limpiar_reservas();

  v_fin := coalesce(
    p_fin,
    p_inicio + ((coalesce((select duracion from servicios where id = p_servicio), 30))
                || ' minutes')::interval);

  if exists (select 1 from citas c
             where c.especialista_id = p_especialista and c.fecha = p_fecha
               and c.ocupa_cupo and c.inicio < v_fin and c.fin > p_inicio) then
    raise exception 'CUPO_TOMADO: ya hay una cita en ese horario'
      using errcode = '23P01';
  end if;

  begin
    insert into reservas (especialista_id, sede_id, fecha, inicio, fin,
                          canal, referencia, expira_en)
    values (p_especialista, p_sede, p_fecha, p_inicio, v_fin,
            p_canal, p_referencia,
            now() + (greatest(coalesce(p_minutos,5),1) || ' minutes')::interval)
    returning * into v_res;
  exception when exclusion_violation then
    raise exception 'CUPO_APARTADO: otra conversación está tomando ese horario'
      using errcode = '23P01';
  end;

  return v_res;
end $$;

create or replace function soltar_cupo(p_reserva uuid) returns boolean
language sql as $$
  with ido as (delete from reservas where id = p_reserva returning 1)
  select exists (select 1 from ido);
$$;

-- ---------------------------------------------------------------------------
--  agendar_cita: la única puerta para crear una cita.
--  Valida horario, almuerzo, cupo apartado por otro y choque con otra cita.
--  El choque además lo garantiza la restricción citas_sin_solape, así que ni
--  aunque dos procesos entren en el mismo milisegundo se cuela una doble.
-- ---------------------------------------------------------------------------
create or replace function agendar_cita(
  p_cliente      text,
  p_especialista text,
  p_sede         text,
  p_fecha        date,
  p_inicio       time,
  p_servicio     text default null,
  p_fin          time default null,
  p_canal        text default 'WhatsApp',
  p_por          text default '',
  p_notas        text default '',
  p_reserva      uuid default null,
  p_id           text default null
) returns citas
language plpgsql as $$
declare
  v_fin    time;
  v_estado text;
  v_id     text;
  v_cita   citas;
begin
  perform limpiar_reservas();

  v_fin := coalesce(
    p_fin,
    p_inicio + ((coalesce((select duracion from servicios where id = p_servicio), 30))
                || ' minutes')::interval);

  if v_fin <= p_inicio then
    raise exception 'HORA_INVALIDA: la hora de fin debe ser posterior a la de inicio';
  end if;

  if not exists (select 1 from clientes where id = p_cliente) then
    raise exception 'CLIENTE_NO_EXISTE: %', p_cliente;
  end if;

  if not exists (select 1 from especialistas where id = p_especialista and activo) then
    raise exception 'ESPECIALISTA_NO_DISPONIBLE: %', p_especialista;
  end if;

  -- ¿trabaja ese día en esa sede, y cabe la cita dentro de la franja?
  if not exists (
    select 1 from horarios h
    where h.especialista_id = p_especialista
      and h.sede_id = p_sede
      and h.dia = extract(dow from p_fecha)::int
      and p_inicio >= h.desde and v_fin <= h.hasta) then
    raise exception 'FUERA_DE_HORARIO: % no atiende en % el % a las %',
      p_especialista, p_sede, p_fecha, p_inicio;
  end if;

  if exists (
    select 1 from horarios h
    where h.especialista_id = p_especialista
      and h.sede_id = p_sede
      and h.dia = extract(dow from p_fecha)::int
      and h.alm_desde is not null
      and p_inicio < h.alm_hasta and v_fin > h.alm_desde) then
    raise exception 'ALMUERZO: ese horario cae en el almuerzo';
  end if;

  -- cupo apartado por otra conversación
  if exists (
    select 1 from reservas r
    where r.especialista_id = p_especialista and r.fecha = p_fecha
      and r.expira_en > now()
      and (p_reserva is null or r.id <> p_reserva)
      and r.inicio < v_fin and r.fin > p_inicio) then
    raise exception 'CUPO_APARTADO: otra conversación está tomando ese horario'
      using errcode = '23P01';
  end if;

  -- choque con otra cita. La restricción citas_sin_solape no mira el histórico
  -- importado (ver 01-esquema.sql), así que aquí revisamos TODO.
  if exists (
    select 1 from citas c
    where c.especialista_id = p_especialista and c.fecha = p_fecha
      and c.ocupa_cupo and c.inicio < v_fin and c.fin > p_inicio) then
    raise exception 'CUPO_TOMADO: ya hay una cita en ese horario'
      using errcode = '23P01';
  end if;

  if p_reserva is not null then
    delete from reservas where id = p_reserva;
  end if;

  select id into v_estado from estados where inicial and activo limit 1;
  if v_estado is null then
    select id into v_estado from estados where activo order by orden limit 1;
  end if;

  v_id := coalesce(p_id, 'c_' || replace(gen_random_uuid()::text, '-', ''));

  begin
    insert into citas (id, tipo, fecha, inicio, fin, especialista_id, sede_id,
                       servicio_id, cliente_id, estado_id, canal, asignada_por,
                       notas, creado_por)
    values (v_id, 'cita', p_fecha, p_inicio, v_fin, p_especialista, p_sede,
            p_servicio, p_cliente, v_estado, p_canal, p_por, p_notas, p_por)
    returning * into v_cita;
  exception when exclusion_violation then
    raise exception 'CUPO_TOMADO: ya hay una cita en ese horario'
      using errcode = '23P01';
  end;

  return v_cita;
end $$;

-- ---------------------------------------------------------------------------
--  cambiar_estado: Pendiente → Confirmado → Llegó → Realizado, o a
--  Incumplido / Cancelado. Queda en la bitácora por el trigger.
-- ---------------------------------------------------------------------------
create or replace function cambiar_estado(
  p_cita   text,
  p_estado text,
  p_por    text default '',
  p_motivo text default ''
) returns citas
language plpgsql as $$
declare v_cita citas;
begin
  if not exists (select 1 from estados where id = p_estado) then
    raise exception 'ESTADO_NO_EXISTE: %', p_estado;
  end if;
  update citas
     set estado_id = p_estado,
         motivo    = case when p_motivo <> '' then p_motivo else motivo end
   where id = p_cita
  returning * into v_cita;
  if v_cita.id is null then
    raise exception 'CITA_NO_EXISTE: %', p_cita;
  end if;
  update cita_bitacora set por = p_por
   where cita_id = p_cita and por = '' and accion = 'estado'
     and ts > now() - interval '5 seconds';
  return v_cita;
end $$;

-- ---------------------------------------------------------------------------
--  reprogramar_cita: NO mueve la cita vieja. Crea una nueva y deja la
--  anterior marcada como Reprogramado, enlazadas en los dos sentidos.
--  Así el historial del cliente muestra lo que de verdad pasó.
-- ---------------------------------------------------------------------------
create or replace function reprogramar_cita(
  p_cita         text,
  p_fecha        date,
  p_inicio       time,
  p_especialista text default null,
  p_sede         text default null,
  p_servicio     text default null,
  p_motivo       text default '',
  p_por          text default '',
  p_canal        text default null,
  p_reserva      uuid default null
) returns citas
language plpgsql as $$
declare
  v_vieja citas;
  v_mov   text;
  v_nueva citas;
begin
  select * into v_vieja from citas where id = p_cita;
  if v_vieja.id is null then
    raise exception 'CITA_NO_EXISTE: %', p_cita;
  end if;

  select id into v_mov from estados where tipo = 'movido' and activo order by orden limit 1;
  if v_mov is null then
    raise exception 'FALTA_ESTADO_MOVIDO: crea un estado de tipo movido (Reprogramado)';
  end if;

  -- primero liberamos el cupo viejo, por si la hora nueva se solapa con la vieja
  update citas set estado_id = v_mov,
                   motivo = case when p_motivo <> '' then p_motivo else motivo end
   where id = p_cita;

  begin
    v_nueva := agendar_cita(
      p_cliente      => v_vieja.cliente_id,
      p_especialista => coalesce(p_especialista, v_vieja.especialista_id),
      p_sede         => coalesce(p_sede, v_vieja.sede_id),
      p_fecha        => p_fecha,
      p_inicio       => p_inicio,
      p_servicio     => coalesce(p_servicio, v_vieja.servicio_id),
      p_canal        => coalesce(p_canal, v_vieja.canal),
      p_por          => p_por,
      p_notas        => v_vieja.notas,
      p_reserva      => p_reserva);
  exception when others then
    -- si la hora nueva no sirve, la cita vieja se queda como estaba
    update citas set estado_id = v_vieja.estado_id, motivo = v_vieja.motivo
     where id = p_cita;
    raise;
  end;

  update citas set reprogramada_de = p_cita   where id = v_nueva.id;
  update citas set reprogramada_a  = v_nueva.id where id = p_cita;

  insert into cita_bitacora (cita_id, por, canal, accion, detalle)
  values (p_cita, p_por, coalesce(p_canal, v_vieja.canal), 'reprogramada',
          jsonb_build_object('nueva', v_nueva.id, 'fecha', p_fecha,
                             'inicio', p_inicio, 'motivo', p_motivo));

  select * into v_nueva from citas where id = v_nueva.id;
  return v_nueva;
end $$;

-- ---------------------------------------------------------------------------
--  Clientes. Por WhatsApp nadie da la cédula de entrada: se identifica por
--  teléfono y solo se pide el documento cuando toca crear la ficha.
-- ---------------------------------------------------------------------------
create or replace function normalizar_telefono(p_tel text) returns text
language sql immutable as $$
  select right(regexp_replace(coalesce(p_tel,''), '\D', '', 'g'), 10);
$$;

create or replace function buscar_cliente(
  p_telefono  text default null,
  p_documento text default null,
  p_nombre    text default null
) returns setof clientes
language sql stable as $$
  select * from clientes c
  where (p_documento is not null
         and regexp_replace(c.documento,'\D','','g') = regexp_replace(p_documento,'\D','','g'))
     or (p_documento is null and p_telefono is not null
         and normalizar_telefono(c.telefono) = normalizar_telefono(p_telefono)
         and normalizar_telefono(p_telefono) <> '')
     or (p_documento is null and p_telefono is null and p_nombre is not null
         and lower(c.primer_nombre || ' ' || c.primer_apellido) like '%' || lower(p_nombre) || '%')
  order by c.creado_en desc
  limit 20;
$$;

create or replace function crear_cliente(
  p_documento       text,
  p_primer_nombre   text,
  p_primer_apellido text,
  p_telefono        text default '',
  p_correo          text default '',
  p_segundo_nombre  text default '',
  p_segundo_apellido text default '',
  p_tipo_doc        text default 'CC',
  p_sede            text default null,
  p_por             text default ''
) returns clientes
language plpgsql as $$
declare v_cli clientes;
begin
  if coalesce(p_documento,'') = '' then
    raise exception 'FALTA_DOCUMENTO: el cliente necesita número de documento';
  end if;

  select * into v_cli from clientes
   where regexp_replace(documento,'\D','','g') = regexp_replace(p_documento,'\D','','g');
  if v_cli.id is not null then
    -- ya existía: completamos teléfono y correo si venían vacíos
    update clientes
       set telefono = case when coalesce(telefono,'') = '' then p_telefono else telefono end,
           correo   = case when coalesce(correo,'')   = '' then p_correo   else correo   end
     where id = v_cli.id
    returning * into v_cli;
    return v_cli;
  end if;

  insert into clientes (id, tipo_doc, documento, primer_nombre, segundo_nombre,
                        primer_apellido, segundo_apellido, telefono, correo,
                        sede_id, creado_por)
  values ('cli-' || regexp_replace(p_documento,'\D','','g'), p_tipo_doc, p_documento,
          p_primer_nombre, p_segundo_nombre, p_primer_apellido, p_segundo_apellido,
          p_telefono, p_correo, p_sede, p_por)
  returning * into v_cli;
  return v_cli;
end $$;

-- ---------------------------------------------------------------------------
--  Nombres presentables. El sistema actual guarda todo en MAYÚSCULA SOSTENIDA
--  y el agente no puede escribirle a un cliente «BUENAS TARDES VALENTINA
--  RIVILLAS BAQUERO». Misma regla que usa la agenda web (titulizar).
-- ---------------------------------------------------------------------------
-- lower()/upper() no tocan las vocales acentuadas si el clúster está en
-- locale C, y MARTÍNEZ saldría «MartÍnez». Lo resolvemos a mano para que dé
-- igual con qué locale hayan creado la base en el VPS.
create or replace function minusculas(p text) returns text
language sql immutable as $$
  select translate(lower(coalesce(p,'')),
                   'ÁÉÍÓÚÜÑÀÈÌÒÙÂÊÎÔÛÄËÏÖÃÕÇ',
                   'áéíóúüñàèìòùâêîôûäëïöãõç');
$$;

create or replace function mayusculas(p text) returns text
language sql immutable as $$
  select translate(upper(coalesce(p,'')),
                   'áéíóúüñàèìòùâêîôûäëïöãõç',
                   'ÁÉÍÓÚÜÑÀÈÌÒÙÂÊÎÔÛÄËÏÖÃÕÇ');
$$;

create or replace function titulizar(p text) returns text
language sql immutable as $$
  select case
    when coalesce(trim(p), '') = '' then ''
    -- si ya viene con minúsculas, la persona la escribió bien: no tocar
    when p <> mayusculas(p) then trim(p)
    else (
      select string_agg(
        case when t.i > 1 and t.w = any (array['de','del','la','las','los','y',
                                               'da','do','van','von'])
             then t.w
             else mayusculas(left(t.w, 1)) || substr(t.w, 2) end,
        ' ' order by t.i)
      from unnest(string_to_array(
             regexp_replace(minusculas(trim(p)), '\s+', ' ', 'g'), ' '))
           with ordinality as t(w, i))
  end;
$$;

-- «Valentina Baquero»: primer nombre + primer apellido, que es como se
-- presenta a un cliente por WhatsApp.
create or replace function nombre_corto(p_nombres text, p_apellidos text)
returns text language sql immutable as $$
  select trim(coalesce(titulizar(split_part(trim(p_nombres), ' ', 1)), '') || ' ' ||
              coalesce(titulizar((
                select w from unnest(string_to_array(regexp_replace(trim(p_apellidos),
                                                     '\s+', ' ', 'g'), ' ')) w
                 where lower(w) <> all (array['de','del','la','las','los','y',
                                              'da','do','van','von'])
                 limit 1)), ''));
$$;

-- ---------------------------------------------------------------------------
--  Vistas de lectura, para que el agente no arme JOINs a mano.
-- ---------------------------------------------------------------------------
create or replace view v_agenda as
select c.id, c.fecha, c.inicio, c.fin, c.tipo, c.canal, c.notas, c.motivo,
       c.ocupa_cupo,
       s.id as sede_id, s.nombre as sede,
       e.id as especialista_id,
       titulizar(trim(e.nombres || ' ' || e.apellidos)) as especialista,
       nombre_corto(e.nombres, e.apellidos) as especialista_corto,
       sv.id as servicio_id, sv.nombre as servicio, sv.duracion,
       cl.id as cliente_id,
       titulizar(trim(concat_ws(' ', cl.primer_nombre, cl.segundo_nombre,
                                     cl.primer_apellido, cl.segundo_apellido))) as cliente,
       nombre_corto(cl.primer_nombre, cl.primer_apellido) as cliente_corto,
       cl.documento, cl.telefono,
       es.id as estado_id, es.nombre as estado, es.tipo as estado_tipo, es.color
from citas c
join sedes s          on s.id  = c.sede_id
join especialistas e  on e.id  = c.especialista_id
left join servicios sv on sv.id = c.servicio_id
left join clientes cl  on cl.id = c.cliente_id
left join estados es   on es.id = c.estado_id;

create or replace view v_historial_cliente as
select cliente_id, id as cita_id, fecha, inicio, sede, especialista_corto as especialista,
       servicio, estado, estado_tipo, color, canal
from v_agenda
where cliente_id is not null
order by fecha desc, inicio desc;

-- lo que el agente necesita para ofrecer una hora en una frase:
-- «el martes 22 a las 10:00 con Valentina Baquero en El Tesoro»
create or replace view v_especialistas as
select e.id, titulizar(trim(e.nombres || ' ' || e.apellidos)) as nombre,
       nombre_corto(e.nombres, e.apellidos) as nombre_corto,
       e.especialidad, e.color, e.activo,
       (select array_agg(s.sede_id order by s.sede_id)
          from especialista_sedes s where s.especialista_id = e.id) as sedes,
       (select array_agg(x.servicio_id order by x.servicio_id)
          from especialista_servicios x where x.especialista_id = e.id) as servicios
from especialistas e;
