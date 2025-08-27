-- CREATE: Creando tablas, bases de datos, vistas
CREATE DATABASE veterinaria; -- DEFAULT CHARACTER SET utf8;
USE veterinaria;

CREATE TABLE animales(
	nombre VARCHAR(50),
    especie VARCHAR(50),
    edad INT,
    peso DECIMAL(5,2)
);

ALTER TABLE animales
ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;

ALTER TABLE animales
ADD COLUMN color VARCHAR(30);

ALTER TABLE animales
RENAME animalitos;

ALTER TABLE animalitos
ADD COLUMN tiene_pelo BOOLEAN AFTER peso;

ALTER TABLE animalitos
MODIFY COLUMN especie VARCHAR(150) NOT NULL; 

SELECT * FROM animalitos;

ALTER TABLE animalitos
RENAME COLUMN tiene_pelo TO peludito;

-- La manera antigua
ALTER TABLE animalitos
CHANGE COLUMN tiene_pelo peludito BOOLEAN;


CREATE TABLE duenos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

ALTER TABLE animalitos
ADD COLUMN dueno_id INT;

ALTER TABLE animalitos
ADD CONSTRAINT fk_dueno FOREIGN KEY (dueno_id) REFERENCES duenos(id);

TRUNCATE TABLE animalitos; -- Elimina la información y reinicia el ID. NO ELIMINA LA TABLA

-- ALERTA ALERTA
DROP TABLE duenos; -- ERROR ? una llave foránea que conecta con animalitos

DROP TABLE animalitos;
DROP TABLE duenos;

