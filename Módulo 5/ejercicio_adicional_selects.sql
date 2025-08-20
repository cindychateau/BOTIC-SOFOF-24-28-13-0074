-- 1. Crear la base de datos
CREATE DATABASE skilltify;
USE skilltify;

-- 2. Crear tablas
CREATE TABLE artistas (
    artista_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    pais VARCHAR(50)
);

CREATE TABLE canciones (
    cancion_id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(100),
    artista_id INT,
    genero VARCHAR(30),
    duracion INT, -- duración en segundos
    FOREIGN KEY (artista_id) REFERENCES artistas(artista_id)
);

CREATE TABLE playlists (
    playlist_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    creador VARCHAR(50)
);

CREATE TABLE playlist_cancion (
    id INT PRIMARY KEY AUTO_INCREMENT,
    playlist_id INT,
    cancion_id INT,
    FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id),
    FOREIGN KEY (cancion_id) REFERENCES canciones(cancion_id)
);

-- 3. Poblar tablas
INSERT INTO artistas (nombre, pais) VALUES
('Bad Bunny', 'Puerto Rico'),
('Taylor Swift', 'USA'),
('Shakira', 'Colombia'),
('BTS', 'Corea del Sur'),
('Dua Lipa', 'Reino Unido'),
('The Beatles', 'Reino Unido'),
('Queen', 'Reino Unido'),
('Coldplay', 'Reino Unido'),
('Linkin Park', 'USA'),
('Foo Fighters', 'USA'),
('Maná', 'México'),
('Caifanes', 'México');

INSERT INTO canciones (titulo, artista_id, genero, duracion) VALUES
('Tití Me Preguntó', 1, 'Reggaeton', 240),
('Gato de Noche', 1, 'Reggaeton', 250),
('Anti-Hero', 2, 'Pop', 200),
('Blank Space', 2, 'Pop', 210),
('Hips Don’t Lie', 3, 'Pop', 215),
('Dynamite', 4, 'K-pop', 230),
('Levitating', 5, 'Pop', 205),
('Let It Be', 6, 'Rock', 243),
('Hey Jude', 6, 'Rock', 431),
('Bohemian Rhapsody', 7, 'Rock', 354),
('We Will Rock You', 7, 'Rock', 122),
('Yellow', 8, 'Rock', 269),
('Fix You', 8, 'Rock', 294),
('In The End', 9, 'Rock', 216),
('Numb', 9, 'Rock', 185),
('Everlong', 10, 'Rock', 250),
('Best of You', 10, 'Rock', 255),
('Rayando el Sol', 11, 'Rock Latino', 260),
('Clavado en un Bar', 11, 'Rock Latino', 280),
('Afuera', 12, 'Rock Latino', 270);

-- Playlists
INSERT INTO playlists (nombre, creador) VALUES
('Fiesta Latina', 'Ana'),
('Pop Hits', 'Luis'),
('Workout', 'Caro'),
('Rock Classics', 'Pedro'),
('Rock Latino', 'Sofi');

-- PlaylistCancion
INSERT INTO playlist_cancion (playlist_id, cancion_id) VALUES
-- Fiesta Latina
(1, 1), -- Tití Me Preguntó
(1, 5), -- Hips Don’t Lie
(1, 2), -- Gato de Noche
(2, 3), -- Anti-Hero
(2, 4), -- Blank Space
(2, 7), -- Levitating
(3, 6), -- Dynamite
(3, 7), -- Levitating
(3, 14), -- Numb
(4, 8),  -- Let It Be
(4, 9),  -- Hey Jude
(4, 10), -- Bohemian Rhapsody
(4, 11), -- We Will Rock You
(4, 12), -- Yellow
(4, 13), -- Fix You
(4, 15), -- In The End
(4, 16), -- Everlong
(5, 18), -- Rayando el Sol
(5, 19), -- Clavado en un Bar
(5, 20); -- Afuera

-- Consulta 1: Muestra el titulo y duracion de todas las canciones ordenadas por duración.

-- Consulta 2: Muestra todas las canciones de Rock ordenadas por titulo de la canción.

-- Consulta 3: Muestra todas las canciones que duran más de 5 minutos

-- Consulta 4: Muestra el titulo y duracion de las 5 canciones más cortas.

-- Consulta 5: Muestra la canción, artista y el género de todas las canciones. Ordénalas de manera descendiente por nombre de artista

-- Consulta 6: Muestra la promedio de duración de todas las canciones

-- Consulta 7: Muestra la promedio de todas las canciones del género pop

-- Consulta 8: Muestra las canciones en cada playlist, incluye el nombre del playlist, titulo de la canción y nombre del artista. Ordénalas en base al nombre de la playlist

-- Consulta 9: Muestra la cantidadad de canciones por género. Muestra primero los géneros que tienen más canciones

-- Consulta 10: Muestra al artista con más canciones en la DB
