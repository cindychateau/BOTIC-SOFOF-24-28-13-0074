-- Query = Consulta (Instrucción que se manda al servidor para hacer algo en específico: Seleccionar, Guardar, Actualizar, Borrar)
-- CRUD: Create, Read, Update, Delete
-- Crear, Leer, Actualizar, Borrar
-- SELECT: Seleccionar información de una tabla -> READ

-- SELECT * FROM <tabla>; -> Seleccionando todas las columnas de una tabla específica
SELECT * FROM usuarios;

-- SELECT columna1, columna2, columna3 FROM <tabla>; Mostrando columnas específicas
SELECT nombre, edad FROM usuarios;

-- SELECT columna1, columna2, columna3 FROM <tabla> WHERE <condicional>; "Filtrando" los registros que quiero mostrar
SELECT nombre, edad FROM usuarios WHERE id = 2; 

SELECT * FROM usuarios WHERE edad > 20;

SELECT * FROM usuarios WHERE nombre LIKE "aurelianO"; -- Indistinto a Mayúsculas/Minúsculas

SELECT nombre FROM usuarios WHERE nombre LIKE "Al%"; -- % comodin. Puede tener cualquier caracter

SELECT nombre FROM usuarios WHERE nombre LIKE "%o";

SELECT nombre FROM usuarios WHERE nombre LIKE "%e%";

-- AND: Ambas condicionales se cumplan
SELECT * FROM usuarios WHERE nombre LIKE "%o" AND edad > 23;

-- OR: Una u otra condicional se cumpla
SELECT * FROM usuarios WHERE nombre LIKE "%o" OR edad > 23; 

SELECT * FROM usuarios WHERE edad > 25 ORDER BY nombre ASC; -- Defecto:ASC (A-Z), DESC (Z-A)
SELECT * FROM usuarios WHERE edad > 25 ORDER BY nombre DESC;

SELECT * FROM usuarios WHERE edad > 25 ORDER BY edad DESC; -- ASC: menor a mayor. DESC: mayor a menor

SELECT * FROM usuarios;
SELECT * FROM usuarios LIMIT 3, 3; -- LIMIT inicio, cantidad

-- SELECT columna1, columna2, columna3, * FROM <tabla>
-- WHERE <condicional> AND OR <condicional>
-- ORDER BY columna1 ASC/DESC
-- LIMIT inicio, cantidad
