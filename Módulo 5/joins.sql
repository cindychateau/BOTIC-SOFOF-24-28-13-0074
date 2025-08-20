SELECT * FROM usuarios;

SELECT * FROM direcciones;

-- Union entre usuarios y direcciones (1:1)
-- JOIN llave primaria de la tabla2 igualo a la llave foranea de la tabla1
SELECT usuarios.*, calle, num, ciudad, cp FROM usuarios
JOIN direcciones ON direcciones.id = direccion_id;

SELECT * FROM usuarios
JOIN direcciones ON direccion_id = direcciones.id;

-- Unión entre pedidos y usuarios (1:n)
-- SELECT columnas FROM <tabla1>
-- JOIN <tabla2> ON <tabla1>.llave_foranea = <tabla2>.llave_primaria
SELECT * FROM pedidos
JOIN usuarios ON pedidos.usuario_id = usuarios.id;

-- Muestra solamente usuarios que hicieron pedido
SELECT * FROM usuarios
JOIN pedidos ON pedidos.usuario_id = usuarios.id;

-- Mostrar TODOS usuarios sin importar si hicieron o no pedido
SELECT * FROM usuarios
LEFT JOIN pedidos ON pedidos.usuario_id = usuarios.id;


-- Union entre usuarios y usuarios_has_hobbies + usuarios_has_hobbies y hobbies (n:m)
-- SELECT columnas FROM <tabla1>
-- JOIN <tabla_intermediaria> ON <tabla1>.llave_primaria = <tabla_intermediaria>.llave_foranea
-- JOIN <tabla2> ON <tabla2>.llave_primaria = <tabla_intermediaria>.llave_foranea
SELECT * FROM usuarios
JOIN usuarios_has_hobbies ON usuarios.id = usuarios_has_hobbies.usuario_id
JOIN hobbies ON hobbies.id = usuarios_has_hobbies.hobbie_id;


SELECT usuarios.id, nombre, actividad FROM usuarios
JOIN usuarios_has_hobbies ON usuarios.id = usuarios_has_hobbies.usuario_id
JOIN hobbies ON hobbies.id = usuarios_has_hobbies.hobbie_id
WHERE actividad LIKE "C%"
ORDER by nombre ASC;


-- SELECT columna1, columna2, columna3, * FROM <tabla>
-- JOINS
-- WHERE <condicional> AND OR <condicional>
-- ORDER BY columna1 ASC/DESC
-- LIMIT inicio, cantidad