DELETE FROM AlbumGenre;
DELETE FROM AlbumInfo;
DELETE FROM Genres;
DELETE FROM Artists;


---INSERTING DATA INTO Artists
BEGIN
    FOR i IN 1..10 LOOP
        INSERT INTO Artists(artist)
        VALUES('artist' || i);
    END LOOP;
END;
/

---INSERTING DATA INTO Genres
BEGIN
    FOR i IN 1..10 LOOP
        INSERT INTO Genres(genre)
        VALUES('genre' || i);
    END LOOP;
END;
/

---INSERTING DATA INTO AlbumInfo
BEGIN
   FOR i IN 1..10 LOOP
       INSERT INTO AlbumInfo(id_album, artist, album, year)
       VALUES(i, 'artist' || i, 'album' || i, 1950);
   END LOOP;
END;
/

---INSERTING DATA INTO AlbumGenre
BEGIN
   FOR i IN 1..10 LOOP
       INSERT INTO albumgenre(id_album, genre)
       VALUES(i, 'genre' || i);
   END LOOP;
END;