-- Tabla de Dueños
CREATE TABLE duenos (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE,
    telefono VARCHAR(10),
    biografia TEXT
);

-- Tabla de Mascotas
CREATE TABLE mascotas (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    especie VARCHAR(30),
    fecha_nacimiento DATE,
    peso DECIMAL(5,2) DEFAULT 1.00,
    dueno_id INT,
    FOREIGN KEY (dueno_id) REFERENCES duenos(id)
);

-- Creamos los registros
INSERT INTO duenos (nombre, correo, telefono, biografia) VALUES
('Juana de Arco', 'juana@skillnest.com', '3001234567', 'Amante de los perros, especialmente de razas grandes.'),
('Pedro Páramo', 'pedro@skillnest.com', '3019876543', 'Le encantan los gatos y tiene experiencia cuidando animales rescatados.'),
('Pablo Picasso', 'pablo@skillnest.com', '3025554321', 'Fanático de las aves exóticas, colecciona guacamayas y periquitos.'),
('Elena de Troya', 'elena@skillnest.com', '3032223344', 'Creció rodeada de mascotas en la finca de su familia.');

-- Consultamos los registros
SELECT * FROM duenos;

INSERT INTO mascotas (nombre, especie, fecha_nacimiento, peso, dueno_id) VALUES
('Firulais', 'Perro', '2020-05-10', 25.40, 1),
('Michi', 'Gato', '2021-03-15', 4.20, 2),
('Rocky', 'Perro', '2018-11-20', 28.70, 3),
('Luna', 'Gato', '2022-01-05', 3.80, 4),
('Kiko', 'Ave', '2022-07-12', 0.10, 3),
('Nube', 'Perro', '2019-09-30', 21.50, 1),
('Sol', 'Gato', '2017-02-18', 6.40, 2),
('Toby', 'Perro', '2020-12-25', 2.20, 3),
('Kiwi', 'Ave', '2023-04-01', 0.08, 4),
('Coco', 'Perro', '2021-08-19', 12.70, 1);

SELECT * FROM mascotas;

-- Guardando una consulta dando acceso solo a ciertas columnas. Suele utilizarse cuando sé que voy a estar repitiendo la misma consulta y la quiero tener lista
CREATE VIEW vista_mascotas AS
SELECT nombre, especie FROM mascotas;

SELECT * FROM vista_mascotas;

-- Procedimiento Almacenado: un bloque de instrucciones de SQL que me permite ejecutar cuando lo invoco/llamo. Podemos realizar múltiples acciones en un solo proceso
DELIMITER //
CREATE PROCEDURE actualizar_peso_mascota(
    IN mascotaId INT,
    IN nuevoPeso DECIMAL(5,2)
)
BEGIN
    -- Actualizamos el peso
    UPDATE mascotas
    SET peso = nuevoPeso
    WHERE id = mascotaId;

    -- Mostramos la información de la mascota actualizada
    SELECT id, nombre, especie, fecha_nacimiento, peso
    FROM mascotas
    WHERE id = mascotaId;
END //
DELIMITER ;

CALL actualizar_peso_mascota(3, 20);

-- Función: Similar al procecedimiento almacenado CON LA DIFERENCIA que debe de regresar un valor.
DELIMITER //
CREATE FUNCTION contar_mascotas() RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total FROM mascotas;
    RETURN total;
END //
DELIMITER ;

SELECT contar_mascotas();

SELECT * FROM mascotas WHERE nombre = "Michi";

CREATE INDEX idx_nombre_mascota ON mascotas(nombre);
