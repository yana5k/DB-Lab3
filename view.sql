-- у всіх запитах беруть участь таблиці AlbumInfo, AlbumGenre та Genres(?)
-- тому об'єднаємо їх в одне предствалення, яке назвемо
-- rs_view (rs, бо дані про 500 найкращих альбомів за версією Rolling Stones)

CREATE OR REPLACE VIEW rs_view AS
SELECT
albuminfo.id_album
,albuminfo.artist
,albuminfo.album
,albumgenre.genre
,albuminfo.year
FROM albuminfo
JOIN AlbumGenre ON albuminfo.id_album = albumgenre.id_album
-- JOIN genres ON albumgenre.genre = genres.genre
;