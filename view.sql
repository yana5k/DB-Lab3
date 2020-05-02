CREATE OR REPLACE VIEW rs_view AS
SELECT albuminfo.artist, albuminfo.album, albumgenre.genre,albuminfo.year
FROM albuminfo
JOIN AlbumGenre ON albuminfo.id_album = albumgenre.id_album
JOIN genres ON albumgenre.genre = genres.genre;