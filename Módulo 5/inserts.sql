-- CRUD : CREATE
-- INSERT INTO tabla (columna1, columna2, columna3) VALUES (valor1, valor2, valor3);
SELECT * FROM usuarios;


INSERT INTO usuarios (nombre, edad, direccion_id)
VALUES ("Elena", 30, 2);

INSERT INTO usuarios (nombre, edad, direccion_id) VALUES
("Juana", 28, 3),
("Pablo", 55, 5),
("Pedro", 32, 7);