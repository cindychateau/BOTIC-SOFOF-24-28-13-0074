-- JOIN: UNIR dos tablas en base a la relación establecida. Solamente me muestra la información que coincide en ambas tablas
-- SELECT columnas FROM tabla1
-- JOIN tabla2 ON tabla1.clave_foranea = tabla2.clave_primaria


SELECT * FROM usuarios
JOIN direcciones ON usuarios.direccion_id = direcciones.id;

SELECT * FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id;

SELECT * FROM usuarios
JOIN pedidos ON pedidos.usuario_id = usuarios.id;

SELECT * FROM usuarios
LEFT JOIN pedidos ON pedidos.usuario_id = usuarios.id;

SELECT nombre, actividad FROM usuarios
JOIN usuarios_has_hobbies ON usuarios_has_hobbies.usuario_id = usuarios.id
JOIN hobbies ON usuarios_has_hobbies.hobbie_id = hobbies.id
WHERE actividad LIKE "%ar";


