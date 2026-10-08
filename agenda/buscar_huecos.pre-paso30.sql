CREATE OR REPLACE FUNCTION public.buscar_huecos(p_desde date, p_dias integer DEFAULT 14, p_sede text DEFAULT NULL::text, p_especialista text DEFAULT NULL::text, p_servicio text DEFAULT NULL::text, p_duracion integer DEFAULT NULL::integer, p_paso integer DEFAULT 15, p_limite integer DEFAULT 60)
 RETURNS TABLE(fecha date, inicio time without time zone, fin time without time zone, especialista_id text, sede_id text)
 LANGUAGE sql
 STABLE
AS $function$
  select h.*
  from generate_series(p_desde, p_desde + (greatest(p_dias,1) - 1), interval '1 day') d
  cross join lateral huecos_del_dia(
    d::date, p_sede, p_especialista, p_servicio, p_duracion, p_paso) h
  order by h.fecha, h.inicio, h.especialista_id
  limit greatest(coalesce(p_limite,60), 1);
$function$
