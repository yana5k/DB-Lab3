import csv
from re import split as re_split 
import cx_Oracle

#------------------------------------------------------------------------------
#з'єднання з БД

username = 'system'
password = 'Qweasd1!2233'
databaseName = 'localhost/xe'

# dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', 'xe')
connection = cx_Oracle.connect('system', 'Qweasd1!2233', 'localhost:1521/XE')
# print (connection.version)

cursor = connection.cursor()

#------------------------------------------------------------------------------
#підготуємо таблиці до запису даних, видаливши їх можливий вміст
tables = ['AlbumGenre', 'AlbumInfo', 'Genres', 'Artists']
for table in tables:
    cursor.execute("DELETE FROM " +table)
    print("Data in " + table + " is deleted")


#------------------------------------------------------------------------------
#відкриття файлу

csv_file = open('albumlist.csv', encoding='utf-8', errors='ignore')
data = csv.reader(csv_file, delimiter=',')

#таблиці Artists та Genres повинні містити унікальні значення, тому "відловимо" їх за допомогою масивів
artist_un = []
genre_un = []

#------------------------------------------------------------------------------
#власне робота із файлом

i = 1 #змінна для створення id_album
next(data)
for row in data:
    year = int(row[1].strip())
    album = row[2].strip()
    artist = row[3].strip()
    # genre = row[4].strip()

    #деяким альбомам відповідає кілька жанрів, тому потрібно виконати розділення
    genre = re_split(r',', row[4])

    #приберемо пробіли по боках
    genre = [gen.strip() for gen in genre]

    #заповнення таблиці Artists унікальними значеннями
    if artist not in artist_un:
        artist_un.append(artist)
        cursor.execute("INSERT INTO Artists(artist) VALUES(:artist)", artist=artist) #...too many artists... (o_O)

    #заповнення таблиці Genres унікальними значеннями
    for gen in genre:
        if gen not in genre_un:
            genre_un.append(gen)
            cursor.execute("INSERT INTO Genres(genre) VALUES(:genre)", genre=gen) #and genres too 

    #заповнення таблиці AlbumInfo з використанням попередньо оголошеної змінної i
    cursor.execute("INSERT INTO AlbumInfo(id_album, artist, album, year) VALUES(:id, :artist, :album, :year)",
		id = i, artist = artist, album = album, year = year)

    #заповнення таблиці AlbumGenre
    for gen in genre:
        cursor.execute("INSERT INTO AlbumGenre(id_album, genre) VALUES(:id, :genre)",
            id = i, genre = gen)

    i += 1 #збільшуємо наш ітератор для наступних записів

#------------------------------------------------------------------------------
#закриваємо все після того, як нашкодили <(￣︶￣)>
connection.commit()
cursor.close()
connection.close()
csv_file.close()
