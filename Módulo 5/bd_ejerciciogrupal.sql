-- Crear base de datos
CREATE DATABASE alquiler_autos;
USE alquiler_autos;

-- Tabla Clientes
CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    direccion VARCHAR(150)
);

-- Tabla Vehículos
CREATE TABLE vehiculos (
    id_vehiculo INT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio INT,
    precio_dia DECIMAL(10,2)
);

-- Tabla Alquileres
CREATE TABLE alquileres (
    id_alquiler INT PRIMARY KEY,
    id_cliente INT,
    id_vehiculo INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_vehiculo) REFERENCES vehiculos(id_vehiculo)
);

-- Tabla Pagos
CREATE TABLE pagos (
    id_pago INT PRIMARY KEY,
    id_alquiler INT,
    monto DECIMAL(10,2),
    fecha_pago DATE,
    FOREIGN KEY (id_alquiler) REFERENCES alquileres(id_alquiler)
);

-- Insertar datos en Clientes
INSERT INTO clientes (id_cliente, nombre, telefono, email, direccion) VALUES
(1, 'Juan Pérez', '555-1234', 'juan@mail.com', 'Calle 123'),
(2, 'Laura Gómez', '555-5678', 'laura@mail.com', 'Calle 456'),
(3, 'Carlos Sánchez', '555-9101', 'carlos@mail.com', 'Calle 789');

-- Insertar datos en Vehículos
INSERT INTO vehiculos (id_vehiculo, marca, modelo, anio, precio_dia) VALUES
(1, 'Toyota', 'Corolla', 2020, 30.00),
(2, 'Honda', 'Civic', 2019, 28.00),
(3, 'Ford', 'Focus', 2021, 35.00);

-- Insertar datos en Alquileres
INSERT INTO alquileres (id_alquiler, id_cliente, id_vehiculo, fecha_inicio, fecha_fin) VALUES
(1, 1, 2, '2025-03-10', '2025-03-15'),
(2, 2, 1, '2025-03-12', '2025-03-16'),
(3, 3, 3, '2025-03-20', '2025-03-22');

-- Insertar datos en Pagos
INSERT INTO pagos (id_pago, id_alquiler, monto, fecha_pago) VALUES
(1, 1, 150.00, '2025-03-12'),
(2, 2, 112.00, '2025-03-13'),
(3, 3, 70.00, '2025-03-20');
