-- ============================================================================
--  Entrada con usuario y contraseña, y sesiones.
--  Se corre una sola vez, sobre la base que ya está montada.
--  No crea ninguna persona: eso lo haces tú con crear_admin.py, para que la
--  primera contraseña la escribas tú y no quede escrita en ningún archivo.
-- ============================================================================

alter table usuarios add column if not exists clave_hash    text;
alter table usuarios add column if not exists sede_id       text references sedes(id);
alter table usuarios add column if not exists nota          text default '';
alter table usuarios add column if not exists creado_en     timestamp not null default now();
alter table usuarios add column if not exists ultimo_acceso timestamp;

-- el correo es con lo que se entra: uno solo por persona
create unique index if not exists usuarios_correo
  on usuarios (lower(correo)) where correo <> '';

-- Las sesiones viven en la base, no en una cookie firmada: así se pueden
-- cerrar de verdad (si a alguien se le queda abierta la agenda en un
-- computador del punto, se le revoca y listo).
create table if not exists sesiones (
  token_hash text primary key,          -- sha256 del token; el token nunca se guarda
  usuario_id text not null references usuarios(id) on delete cascade,
  creado_en  timestamp not null default now(),
  visto_en   timestamp not null default now(),
  expira_en  timestamp not null,
  agente     text default ''
);
create index if not exists sesiones_usuario on sesiones (usuario_id);
create index if not exists sesiones_expiran on sesiones (expira_en);

create or replace function limpiar_sesiones() returns int
language sql as $$
  with ido as (delete from sesiones where expira_en < now() returning 1)
  select count(*)::int from ido;
$$;
