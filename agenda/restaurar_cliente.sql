insert into clientes (id,tipo_doc,documento,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,telefono,correo,dia_nac,mes_nac,genero,ciudad,sede_id,tipo_cliente,notas,importado,creado_por) values ('cli-1000084923','Cédula de Ciudadanía','1000084923','ANLLI','','VANESSA','RUIZ','3232045895','anllivanesaruiz23@hotmail.com',null,null,'','','sede-cj-medical-el-tesoro','Cliente Leal','',true,'');
DELETE FROM clientes WHERE id='cli_local_1';
SELECT 'clientes' AS q, count(*)::text FROM clientes UNION ALL SELECT 'ANLLI existe', count(*)::text FROM clientes WHERE id='cli-1000084923';
