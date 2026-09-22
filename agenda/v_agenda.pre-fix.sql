 SELECT c.id,
    c.fecha,
    c.inicio,
    c.fin,
    c.tipo,
    c.canal,
    c.notas,
    c.motivo,
    c.ocupa_cupo,
    s.id AS sede_id,
    s.nombre AS sede,
    e.id AS especialista_id,
    titulizar(TRIM(BOTH FROM ((e.nombres || ' '::text) || e.apellidos))) AS especialista,
    nombre_corto(e.nombres, e.apellidos) AS especialista_corto,
    sv.id AS servicio_id,
    sv.nombre AS servicio,
    sv.duracion,
    cl.id AS cliente_id,
    titulizar(TRIM(BOTH FROM concat_ws(' '::text, cl.primer_nombre, cl.segundo_nombre, cl.primer_apellido, cl.segundo_apellido))) AS cliente,
    nombre_corto(cl.primer_nombre, cl.primer_apellido) AS cliente_corto,
    cl.documento,
    cl.telefono,
    es.id AS estado_id,
    es.nombre AS estado,
    es.tipo AS estado_tipo,
    es.color
   FROM (((((citas c
     JOIN sedes s ON ((s.id = c.sede_id)))
     JOIN especialistas e ON ((e.id = c.especialista_id)))
     LEFT JOIN servicios sv ON ((sv.id = c.servicio_id)))
     LEFT JOIN clientes cl ON ((cl.id = c.cliente_id)))
     LEFT JOIN estados es ON ((es.id = c.estado_id)));