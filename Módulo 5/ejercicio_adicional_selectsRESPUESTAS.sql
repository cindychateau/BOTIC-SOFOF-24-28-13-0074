-- Consulta 1: Muestra el titulo y duracion de todas las canciones ordenadas por duración.
SELECT titulo, duracion FROM canciones ORDER BY duracion; -- ASC

-- Consulta 2: Muestra todas las canciones de Rock ordenadas por titulo de la canción.
SELECT * FROM canciones WHERE genero = "Rock" ORDER BY titulo ASC;

-- Consulta 3: Muestra todas las canciones que duran más de 5 minutos ordenarlas la que dura más a la que dura menos
SELECT * FROM canciones WHERE duracion > 300;

-- Consulta 4: Muestra el titulo y duracion de las 5 canciones más cortas.
SELECT titulo, duracion FROM canciones ORDER BY duracion ASC LIMIT 5; -- 1: cantidad   2: posicion, cantidad

-- Consulta 5: Muestra la canción, artista y el género de todas las canciones. Ordénalas de manera descendiente por nombre de artista
SELECT titulo AS cancion, nombre AS artista, genero FROM canciones
JOIN artistas ON canciones.artista_id = artistas.artista_id
ORDER BY artista DESC;

-- Consulta 6: Muestra el promedio de duración de todas las canciones
SELECT AVG(duracion) AS promedio_segundos FROM canciones;

-- Consulta 7: Muestra el promedio de todas las canciones del género pop
SELECT AVG(duracion) AS promedio_segundos FROM canciones WHERE genero = "pop";

-- Consulta 8: Muestra las canciones en cada playlist, incluye el nombre del playlist, titulo de la canción y nombre del artista. Ordénalas en base al nombre de la playlist
SELECT playlists.nombre AS nombre_playlist, titulo, artistas.nombre AS nombre_artista FROM playlists
JOIN playlist_cancion ON playlists.playlist_id = playlist_cancion.playlist_id
JOIN canciones ON playlist_cancion.cancion_id = canciones.cancion_id
JOIN artistas ON canciones.artista_id = artistas.artista_id
ORDER BY nombre_playlist;

-- Consulta 9: Muestra la cantidadad de canciones por género. Muestra primero los géneros que tienen más canciones
SELECT genero, COUNT(*) AS cantidad
FROM canciones
GROUP BY genero
ORDER BY cantidad DESC;

-- Consulta 10: Muestra al artista con más canciones en la DB
SELECT artistas.artista_id, nombre, COUNT(*) AS cantidad
FROM canciones
JOIN artistas ON canciones.artista_id = artistas.artista_id
GROUP BY artistas.artista_id
ORDER BY cantidad DESC
LIMIT 1;
