CREATE DATABASE tienda;

USE tienda;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    ciudad VARCHAR(255)
);

INSERT INTO clientes (nombre, email, ciudad)
VALUES
('Juan Pérez', 'juanperez@gmail.com', 'Santiago'),
('María López', 'maria.lopez@yahoo.com', 'Valparaíso'),
('Carlos Díaz', 'carlos.diaz@hotmail.com', 'Concepción'),
('Ana Torres', 'ana.torres@gmail.com', 'Santiago');

SELECT * FROM clientes;

SELECT nombre, ciudad FROM clientes;

SELECT nombre, ciudad FROM clientes;

SELECT * FROM clientes ORDER BY nombre ASC;

SELECT * FROM clientes WHERE nombre LIKE 'M%';

SELECT COUNT(*) AS total_clientes FROM clientes;

SELECT COUNT(*) AS total_clientes
FROM clientes
WHERE ciudad = 'Santiago';

SELECT COUNT(*) AS total_clientes_gmail
FROM clientes
WHERE email LIKE '%gmail%';

SELECT * 
FROM clientes
WHERE nombre LIKE 'M%' OR ciudad LIKE 'S%';

SELECT * 
FROM clientes
WHERE email LIKE '%gmail%' OR email LIKE '%yahoo%';

SELECT * 
FROM clientes
WHERE (ciudad LIKE 'S%' OR ciudad LIKE 'V%')
  AND email LIKE '%gmail%';