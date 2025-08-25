CREATE DATABASE M5_AE3_ABP;

CREATE TABLE clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    telefono VARCHAR(15)
);

CREATE TABLE pedidos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha DATE,
    total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON DELETE CASCADE
);

-- Inserter 5 CLIENTES 
INSERT INTO clientes (nombre, direccion, telefono) VALUES 
("Elena de Troya", "Calle 123", "1234-5678"), 
("Juaba de Arco", "Blvd. ABC", "2345-6789"), 
("Pablo Picasso", "AV. XYZ", "10203040"), 
("Pedro Paramo", "Comala", "20304050"), 
("Karol Dance", "Vitacura", "09876543");

-- Insertar 10 pedidos
INSERT INTO pedidos (cliente_id, fecha, total) VALUES
(1, '2025-01-01', 15990.00),
(1, '2025-02-01', 10.00),
(1, '2025-02-02', 25000.00),
(2, '2025-03-03', 20000.00),
(3, '2025-03-04', 850000.00),
(3, '2025-03-06', 350000.00),
(3, '2025-03-06', 50000.00),
(3, '2025-03-07', 5000.00),
(4, '2025-01-01', 15000.00),
(5, '2025-01-02', 4500.00);

-- TODOS LOS CLIENTE Y SUS PEDIDOS
SELECT nombre, direccion, telefono, pedidos.id AS pedido_id, fecha, total FROM clientes
JOIN clientes ON clientes.id = pedidos.cliente_id;

-- TODOS LOS PEDIDOS DE UN USUARIO EN BASE A SU ID
SELECT * FROM pedidos WHERE cliente_id = 3;

-- Calcula el total de todos los pedidos para cada cliente
SELECT SUM(total), cliente_id, nombre
FROM clientes
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id
GROUP BY cliente_id;

-- ACTUALIZA DiRECCION DEL CLIENTE
UPDATE clientes SET direccion = "Nueva Calle 10 1234" WHERE clientes.id = 5;

-- ELIMINAR CLIENTE
DELETE FROM pedidos WHERE cliente_id = 5;
DELETE FROM clientes WHERE id = 5;

-- 3 CLIENTES CON MÁS PEDIDOS
SELECT nombre, COUNT(*) AS cantidad_pedidos
FROM clientes
JOIN pedidos ON clientes.id = pedidos.cliente_id
GROUP BY clientes.id
ORDER BY cantidad_pedidos DESC
LIMIT 3;