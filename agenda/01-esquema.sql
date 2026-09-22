-- ============================================================================
--  Agenda CJ Medical · esquema de Postgres
--  Traducción fiel de las reglas que hoy corren en la agenda web.
--
--  Nota sobre horas: todo se guarda como hora de pared de Colombia
--  (date + time, sin zona). Colombia no tiene horario de verano, así que no
--  hay conversiones. No cambiar a timestamptz sin revisar huecos_del_dia().
-- ============================================================================

create extension if not exists btree_gist;

-- ---------------------------------------------------------------- maestros --

create table sedes (
  id            text primary key,
  nombre        text not null,
  codigo        text default '',
  ciudad        text default '',
  bodega        text default '',
  direccion     text default '',
  telefono      text default '',
  hora_inicio   time not null default '09:00',
  hora_fin      time not null default '20:00',
  puestos       int  not null default 1,   -- cuántas personas atienden al tiempo
  capacidad_dia int  not null default 16,  -- citas por puesto al día
  dias_mes      int  not null default 24,
  activo        boolean not null default true
);

-- tipo define el comportamiento, no el nombre. El nombre lo pone CJ Medical.
--   abierto   la cita sigue viva y ocupa cupo   (Pendiente, Confirmado, Llegó)
--   atendido  ya se atendió, ocupa cupo         (Realizado)
--   ausente   no llegó, ocupa cupo              (Incumplido)
--   movido    se pasó a otra hora, LIBERA cupo  (Reprogramado)
--   cancelado se cayó, LIBERA cupo              (Cancelado)
create table estados (
  id           text primary key,
  nombre       text not null,
  color        text not null default '#8A7C75',
  tipo         text not null default 'abierto'
               check (tipo in ('abierto','atendido','ausente','movido','cancelado')),
  transparente boolean not null default false,  -- se pinta sin relleno en la agenda
  inicial      boolean not null default false,  -- estado con el que nace una cita
  orden        int     not null default 0,
  activo       boolean not null default true
);
-- solo puede haber un estado inicial
create unique index estados_un_inicial on estados (inicial) where inicial;

create table servicios (
  id       text primary key,
  nombre   text not null,
  codigo   text default '',
  duracion int  not null default 30,      -- minutos
  precio   numeric(12,2),
  activo   boolean not null default true
);

create table especialistas (
  id           text primary key,
  nombres      text not null,
  apellidos    text not null default '',
  documento    text default '',
  correo       text default '',
  telefono     text default '',
  especialidad text default '',
  color        text default '#8A7C75',
  activo       boolean not null default true
);

-- en qué sedes atiende (se activa/desactiva por sede moviendo estas filas)
create table especialista_sedes (
  especialista_id text references especialistas(id) on delete cascade,
  sede_id         text references sedes(id)         on delete cascade,
  primary key (especialista_id, sede_id)
);

-- qué servicios hace. OJO: sin filas = hace todos los servicios.
-- Es la misma regla de la agenda web (haceServicio); no la cambies sin avisar.
create table especialista_servicios (
  especialista_id text references especialistas(id) on delete cascade,
  servicio_id     text references servicios(id)     on delete cascade,
  primary key (especialista_id, servicio_id)
);

-- horario semanal por sede. dia: 0=domingo … 6=sábado (igual que en la web).
create table horarios (
  id              bigserial primary key,
  especialista_id text not null references especialistas(id) on delete cascade,
  sede_id         text not null references sedes(id)         on delete cascade,
  dia             int  not null check (dia between 0 and 6),
  desde           time not null,
  hasta           time not null,
  alm_desde       time,
  alm_hasta       time,
  check (hasta > desde),
  check ((alm_desde is null) = (alm_hasta is null)),
  check (alm_desde is null or alm_hasta > alm_desde)
);
create index horarios_busqueda on horarios (especialista_id, dia, sede_id);

-- ---------------------------------------------------------------- clientes --

create table clientes (
  id              text primary key,        -- cli-<documento> en los importados
  tipo_doc        text default 'CC',
  documento       text not null,
  primer_nombre   text default '',
  segundo_nombre  text default '',
  primer_apellido text default '',
  segundo_apellido text default '',
  telefono        text default '',
  correo          text default '',
  dia_nac         int,
  mes_nac         int,
  genero          text default '',
  ciudad          text default '',
  sede_id         text references sedes(id),
  tipo_cliente    text default '',
  notas           text default '',
  importado       boolean not null default false,
  creado_en       timestamp not null default now(),
  creado_por      text default ''
);
create unique index clientes_documento on clientes (documento) where documento <> '';
-- el agente identifica por teléfono antes de pedir cédula; este índice es el que usa
create index clientes_telefono on clientes (telefono) where telefono <> '';
create index clientes_nombre on clientes
  (lower(primer_nombre || ' ' || primer_apellido));

-- ------------------------------------------------------------------- citas --

create table citas (
  id              text primary key,
  tipo            text not null default 'cita' check (tipo in ('cita','bloqueo')),
  fecha           date not null,
  inicio          time not null,
  fin             time not null,
  especialista_id text not null references especialistas(id),
  sede_id         text not null references sedes(id),
  servicio_id     text references servicios(id),
  cliente_id      text references clientes(id),
  estado_id       text references estados(id),
  canal           text default '',          -- Recepcionista, Call center, WhatsApp…
  asignada_por    text default '',
  notas           text default '',
  motivo          text default '',          -- motivo de cancelación o reprogramación
  reprogramada_de text references citas(id),
  reprogramada_a  text references citas(id),
  importado       boolean not null default false,
  creado_en       timestamp not null default now(),
  creado_por      text default '',
  -- se mantiene por trigger; es lo que decide si el cupo está tomado
  ocupa_cupo      boolean not null default true,
  check (fin > inicio),
  check (tipo = 'bloqueo' or cliente_id is not null)
);
create index citas_dia   on citas (fecha, sede_id);
create index citas_esp   on citas (especialista_id, fecha);
create index citas_cli   on citas (cliente_id, fecha desc);

-- ---- la regla que de verdad impide el doble agendamiento --------------------
-- Con esto, dos citas que se pisan en la misma especialista NO pueden existir,
-- sin importar si las crea la recepcionista, el call center o Hermes, ni si
-- llegan en el mismo milisegundo. Es la única garantía que no se puede saltar.
--
-- «and not importado»: el histórico que viene del sistema actual trae 177
-- citas que se pisan entre sí (ver la vista v_solapes). Son reales: hoy el
-- sistema lo permite, y casi siempre es una cita de 45 minutos agendada en la
-- rejilla de 30. No las tocamos ni las inventamos: entran como están y la
-- restricción cuida solo lo que se agende de aquí en adelante.
-- Cuando el histórico esté depurado, quitar «and not importado» y revalidar.
-- agendar_cita() sí revisa el choque contra TODAS las citas, importadas
-- incluidas, así que por la puerta normal no se cuela ninguna.
alter table citas add constraint citas_sin_solape
  exclude using gist (
    especialista_id with =,
    tsrange(fecha + inicio, fecha + fin) with &&
  ) where (ocupa_cupo and not importado);

-- las citas del histórico que se pisan, para revisarlas con calma
create or replace view v_solapes as
select a.especialista_id, a.fecha,
       a.id as cita_a, a.inicio as inicio_a, a.fin as fin_a, a.estado_id as estado_a,
       b.id as cita_b, b.inicio as inicio_b, b.fin as fin_b, b.estado_id as estado_b
from citas a
join citas b
  on b.especialista_id = a.especialista_id
 and b.fecha = a.fecha
 and b.id > a.id
 and a.ocupa_cupo and b.ocupa_cupo
 and a.inicio < b.fin and a.fin > b.inicio
order by a.fecha, a.especialista_id, a.inicio;

-- ocupa_cupo = el bloqueo siempre tapa; la cita tapa salvo que su estado
-- sea 'movido' o 'cancelado' (esas devuelven el cupo a la agenda).
create or replace function citas_calcular_ocupa() returns trigger
language plpgsql as $$
declare t text;
begin
  if new.tipo = 'bloqueo' then
    new.ocupa_cupo := true;
  else
    select tipo into t from estados where id = new.estado_id;
    new.ocupa_cupo := coalesce(t, 'abierto') not in ('movido','cancelado');
  end if;
  return new;
end $$;

create trigger citas_ocupa
  before insert or update of tipo, estado_id on citas
  for each row execute function citas_calcular_ocupa();

-- si cambia el tipo de un estado (p. ej. Cancelado deja de liberar cupo),
-- hay que recalcular las citas que lo usan
create or replace function estados_recalcular() returns trigger
language plpgsql as $$
begin
  if new.tipo is distinct from old.tipo then
    update citas set estado_id = estado_id where estado_id = new.id;
  end if;
  return new;
end $$;

create trigger estados_tipo_cambia
  after update of tipo on estados
  for each row execute function estados_recalcular();

-- ---------------------------------------------------------------- bitácora --
-- Quién creó la cita, quién la movió, quién le cambió el estado y cuándo.

create table cita_bitacora (
  id      bigserial primary key,
  cita_id text not null,
  ts      timestamp not null default now(),
  por     text default '',
  canal   text default '',
  accion  text not null,          -- creada, estado, movida, reprogramada, anulada
  detalle jsonb not null default '{}'::jsonb
);
create index bitacora_cita on cita_bitacora (cita_id, ts);

create or replace function citas_registrar() returns trigger
language plpgsql as $$
begin
  if TG_OP = 'INSERT' then
    insert into cita_bitacora (cita_id, por, canal, accion, detalle)
    values (new.id, new.creado_por, new.canal, 'creada',
            jsonb_build_object('fecha', new.fecha, 'inicio', new.inicio,
                               'especialista', new.especialista_id,
                               'sede', new.sede_id, 'estado', new.estado_id));
  else
    if new.estado_id is distinct from old.estado_id then
      insert into cita_bitacora (cita_id, canal, accion, detalle)
      values (new.id, new.canal, 'estado',
              jsonb_build_object('de', old.estado_id, 'a', new.estado_id,
                                 'motivo', new.motivo));
    end if;
    if (new.fecha, new.inicio, new.especialista_id, new.sede_id)
       is distinct from (old.fecha, old.inicio, old.especialista_id, old.sede_id) then
      insert into cita_bitacora (cita_id, canal, accion, detalle)
      values (new.id, new.canal, 'movida',
              jsonb_build_object('de', jsonb_build_object('fecha', old.fecha,
                     'inicio', old.inicio, 'especialista', old.especialista_id,
                     'sede', old.sede_id),
                 'a', jsonb_build_object('fecha', new.fecha,
                     'inicio', new.inicio, 'especialista', new.especialista_id,
                     'sede', new.sede_id)));
    end if;
  end if;
  return new;
end $$;

create trigger citas_bitacora
  after insert or update on citas
  for each row execute function citas_registrar();

-- --------------------------------------------------------------- reservas --
-- Cupo apartado mientras el agente negocia la hora por WhatsApp.
-- Sin esto, dos conversaciones simultáneas se prometen la misma hora y una de
-- las dos se cae al confirmar. Vencen solas; por defecto en 5 minutos.

create table reservas (
  id              uuid primary key default gen_random_uuid(),
  especialista_id text not null references especialistas(id) on delete cascade,
  sede_id         text not null references sedes(id),
  fecha           date not null,
  inicio          time not null,
  fin             time not null,
  canal           text default 'WhatsApp',
  referencia      text default '',        -- id de la conversación / del contacto
  creado_en       timestamp not null default now(),
  expira_en       timestamp not null default now() + interval '5 minutes',
  check (fin > inicio)
);
-- dos reservas vivas tampoco se pueden pisar
alter table reservas add constraint reservas_sin_solape
  exclude using gist (
    especialista_id with =,
    tsrange(fecha + inicio, fecha + fin) with &&
  );
create index reservas_vencen on reservas (expira_en);

create or replace function limpiar_reservas() returns int
language sql as $$
  with ido as (delete from reservas where expira_en < now() returning 1)
  select count(*)::int from ido;
$$;

-- ---------------------------------------------------------------- usuarios --

create table usuarios (
  id      text primary key,
  nombre  text not null default '',
  correo  text default '',
  rol     text not null default 'operador' check (rol in ('admin','operador')),
  canal   text not null default 'Recepcionista',
  activo  boolean not null default true
);

create table config (
  clave text primary key,
  valor jsonb not null
);
