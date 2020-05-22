import csv
import cx_Oracle

#------------------------------------------------------------------------------
#з'єднання з БД

username = 'system'
password = 'Qweasd1!2233'
databaseName = 'localhost/xe'

# dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', 'xe')
connection = cx_Oracle.connect('system', 'Qweasd1!2233', 'localhost:1521/XE')
# print (connection.version)

def table_csv_writer(table_name, first_line):
	cursor = connection.cursor()
	csv_file = open(table_name + '.csv','w', newline='')
	query = 'SELECT * FROM ' + table_name
	cursor.execute(query)
	row = cursor.fetchall()

	#запишемо заголовки у файл
	csv_writer = csv.writer(csv_file, delimiter=',')
	csv_writer.writerow(first_line)

	#запишемо тепер рядки із view
	for data in row:
	    csv_writer.writerow(data)

	csv_file.close()
	cursor.close()
	return
#------------------------------------------------------------------------------
genres_headers = ['Genre']
artists_headers = ['Artist']
albuminfo_headers = ['Number', 'Artist', 'Album', 'Year']
albumgenre_headers = ['Number', 'Genre']

table_csv_writer('Genres', genres_headers)
table_csv_writer('Artists', artists_headers)
table_csv_writer('AlbumInfo', albuminfo_headers)
table_csv_writer('AlbumGenre', albumgenre_headers)


#------------------------------------------------------------------------------
#закриваємо все після того, як нашкодили <(￣︶￣)>

connection.close()
