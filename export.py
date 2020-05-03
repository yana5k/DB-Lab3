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

cursor = connection.cursor()
#------------------------------------------------------------------------------
#відкриття файлу

csv_file = open('rs500.csv', 'w', newline='')

#використаємо нашу вьюшку, яка містить всі необхідні дані(так склались обставини)
cursor.execute("SELECT * FROM rs_view")
row = cursor.fetchall()

#запишемо заголовки у файл
csv_writer = csv.writer(csv_file, delimiter=',')
csv_writer.writerow(['Number', 'Artist', 'Album', 'Genre', 'Year'])

#запишемо тепер рядки із view
for data in row:
    csv_writer.writerow(data)

#------------------------------------------------------------------------------
#закриваємо все після того, як нашкодили <(￣︶￣)>
cursor.close()
connection.close()
csv_file.close()

