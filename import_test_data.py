# Написати python код, що робить insert тестовими даними у вибрані раніше таблиці для імпорту.
# Під час insert  заповнювати тільки ті атрибути, що будуть імпортуватися з kaggle.
# Для решти продумати значення за default

import cx_Oracle


username = 'system'
password = 'Qweasd1!2233'
databaseName = 'localhost/xe'


# dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', 'xe')
connection = cx_Oracle.connect('system', 'Qweasd1!2233', 'localhost:1521/XE')
print (connection.version)
cursor = connection.cursor()
#------------------------------------------------------------------------------
tables = ['AlbumGenre', 'AlbumInfo', 'Genres', 'Artists']

# очистимо дані з таблиць, якщо в таблицях щось міститься
for table in tables:
    cursor.execute("DELETE FROM " +table)
    print("Data in " + table + " is deleted")

#______________________________________________________________________________
#код для перевірки наявності даних(при необхідності)

cursor.execute("SELECT * FROM AlbumGenre")
print("all from table:")
print("________________________________________________________")
print(cursor.fetchall())
print('')
#______________________________________________________________________________



#почнемо заповнення із батьківських таблиць, щоби не трапилося збою
#------------------------------------------------------------------------------
#заповнимо таблицю Artists

artist_base = [
    'AC/DC'
    ,'Arctic Monkeys'
    ,'B.B. King'
    ,'Black Sabbath'
    ,'Bob Dylan'
    ,'Bob Marley & Wailers'
    ,'Pink Floyd'
    ,'Pixies'
    ,'The Beatles'
    ,'The Doors'
]

for musician in artist_base:
    cursor.execute("INSERT INTO Artists(artist) VALUES(:mus_name)", mus_name=musician)
#------------------------------------------------------------------------------
#заповнимо таблицю Genres
genres_base = [
	'Blues'
	,'Electronic'
	,'Folk'
	,'Funk / Soul'
	,'Hip Hop'
	,'Jazz'
	,'Latin'
	,'Pop'
	,'Reggae'
	,'Rock'
]

for gen in genres_base:
	cursor.execute("INSERT INTO Genres(genre) VALUES(:gen_name)", gen_name=gen)

#------------------------------------------------------------------------------
#заповнимо таблицю AlbumInfo(id_album, artist, album, year)
artist_list = [
	'Black Sabbath'
	,'Pink Floyd'
	,'The Doors'
	,'AC/DC'
	,'Bob Marley & Wailers'
	,'B.B. King'
	,'B.B. King'
	,'Black Sabbath'
	,'Pixies'
	,'Bob Dylan'
]

album_list = [
	'Paranoid'
	,'The Dark Side of the Moon'
	,'The Doors'
	,'Highway to Hell'
	,'Legend: The Best of Bob Marley and The Wailers'
	,'Live in Cook County Jail'
	,'Live at the Regal'
	,'Black Sabbath'
	,'Doolittle'
	,'Blonde on Blonde'
]

year_list = [
	1970
	,1973
	,1967
	,1979
	,1984
	,1971
	,1965
	,1970
	,1989
	,1966
]

for i in range(len(artist_list)):
	cursor.execute("INSERT INTO AlbumInfo(id_album, artist, album, year) VALUES(:id, :mus_name, :alb, :no_year)",
		id = i+1, mus_name = artist_list[i], alb = album_list[i], no_year = year_list[i])

#------------------------------------------------------------------------------
#заповнимо таблицю AlbumGenre(id_album, genre)
genres_list = [
	'Rock'
	,'Rock'
	,'Rock'
	,'Rock'
	,'Reggae'
	,'Blues'
	,'Blues'
	,'Rock'
	,'Rock'
	,'Blues'
]

for i in range(len(genres_list)):
	cursor.execute("INSERT INTO AlbumGenre(id_album, genre) VALUES(:id, :gen)",
		id = i+1, gen = genres_list[i])
cursor.execute("INSERT INTO AlbumGenre(id_album, genre) VALUES(10, 'Rock')")

#______________________________________________________________________________
#код для перевірки наявності даних(при необхідності)
cursor.execute("SELECT * FROM AlbumGenre")
print("all from table:")
print("________________________________________________________")
print(cursor.fetchall())
print('')
#______________________________________________________________________________