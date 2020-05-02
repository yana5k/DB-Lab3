-- Написати PL/SQL код, що заносить тестові дані в одну з таблиць,
-- що були спроектовані у Лабораторній роботі №2, використавши LOOP.
-- Таблиця повинна містити мінімум два атрибути.

SET SERVEROUTPUT ON

-- визначаємо типи змінних
DECLARE

v_id_avbum albumgenre.id_album%TYPE;
v_genre albumgenre.genre%TYPE;

-- оскільки дані тестові, заповнимо таблицю даними виду 1 - жанр1, 2 - жанр2 і так далі

BEGIN
    FOR i IN 1..10 LOOP
        INSERT INTO albumgenre(id_album, genre)
        VALUES(i, 'genre' || i);
    END LOOP;
END;



