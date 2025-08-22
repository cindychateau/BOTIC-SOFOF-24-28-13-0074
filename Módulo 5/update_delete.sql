SELECT * FROM usuarios;

-- Actualizar
-- UPDATE tabla SET columna1 = valor1 WHERE id = x
UPDATE usuarios SET edad = 33 WHERE id = 12;

UPDATE usuarios SET nombre = "Ele", edad = 31 WHERE id = 8;

-- Eliminar registros
-- DELETE FROM tabla WHERE id = x
DELETE FROM usuarios WHERE id = 11; -- Eliminar el registro

-- Truncate: Elimina los registros de mi tabla, reestablece el id a 1. Conserva tabla y columnas
-- Drop: Elimino por completo todo rastro de mi tabla