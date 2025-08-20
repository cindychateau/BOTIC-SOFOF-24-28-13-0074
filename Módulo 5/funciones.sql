-- Funciones de Texto
SELECT CONCAT(nombre," " ,edad) AS username FROM usuarios; -- CONCAT pega texto. JOIN pega tablas
SELECT CONCAT(nombre,edad) AS username FROM usuarios;
SELECT LENGTH(nombre) AS tamanio, nombre FROM usuarios;
SELECT UPPER(nombre) as NOMBRE FROM usuarios;

-- Funciones numéricas
SELECT * FROM pedidos;
SELECT SUM(total) FROM pedidos;
SELECT AVG(envio) FROM pedidos;
SELECT id, ROUND(total) FROM pedidos;
SELECT ROUND(AVG(envio)) FROM pedidos;
SELECT MAX(total) FROM pedidos;
SELECT MIN(total) FROM pedidos;

-- Funciones de Fechas
SELECT NOW(); --  Fecha y hora ->INSERT UPDATE
SELECT CURDATE(); -- CURRENT DATE
SELECT DATE_FORMAT(created_at, "%a %D, %c %y"), created_at FROM pedidos;

SELECT COUNT(*) FROM pedidos;
SELECT COUNT(*) FROM usuarios;
SELECT COUNT(*) FROM hobbies;

-- Agrupaciones
SELECT * FROM pedidos ORDER BY usuario_id;
SELECT AVG(total), usuario_id 
FROM pedidos
GROUP BY usuario_id;

SELECT COUNT(*), usuario_id
FROM pedidos
GROUP BY usuario_id;

SELECT usuario_id, COUNT(*) as cantidad_pedidos, AVG(total), SUM(total)
FROM pedidos
GROUP BY usuario_id;

SELECT usuario_id, COUNT(*) as cantidad_pedidos, AVG(total), SUM(total)
FROM pedidos
GROUP BY usuario_id
HAVING cantidad_pedidos > 1;

-- SELECT columna1, columna2, columna3, * FROM <tabla>
-- JOINS
-- WHERE <condicional> AND OR <condicional>
-- GROUP BY
-- HAVING
-- ORDER BY columna1 ASC/DESC
-- LIMIT inicio, cantidad