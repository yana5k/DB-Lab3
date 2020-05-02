import cx_Oracle
import chart_studio
##############################################
chart_studio.tools.set_credentials_file(username = 'yanna', api_key = 'vVVLEYx1RCef9YlfOUJU')

import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard
import re

def fileId_from_url(url):
    raw_fileID = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return raw_fileID.replace('/', ':')

username = 'system'
password = 'Qweasd1!2233'
databaseName = 'localhost/xe'


# dsn_tns = cx_Oracle.makedsn('127.0.0.1', '1521', 'xe')
connection = cx_Oracle.connect('system', 'Qweasd1!2233', 'localhost:1521/XE')
# print (connection.version)


cursor = connection.cursor()
# --------------------------------------------------------------
query = '''
SELECT genre, COUNT(id_album) AS albums
FROM rs_view
GROUP BY genre
'''
cursor.execute(query)
# print('')
# print('First task')
# print('|genre               |albums     ')
# print('-'*30)
# row = cursor.fetchone()
# while row:

#     print("|{:20}|{}".format(row[0], row[1]))
#     row = cursor.fetchone()

# print('')

genres = []
albums = []

for record in cursor.fetchall():
    genres.append(record[0])
    albums.append(record[1])

bar = go.Bar(x = genres, y = albums)
bar_scheme = py.plot([bar], filename = 'laboratory3-1')
# --------------------------------------------------------------
"""
second task
"""
query = '''
SELECT artist,
    ROUND(COUNT(album)/(SELECT COUNT(album)
    FROM rs_view
    WHERE genre = 'Rock')*100, 2) AS ratio
FROM rs_view
WHERE genre = 'Rock'
GROUP BY artist
'''
cursor.execute(query)
# print('Second task')
# print('|artist              |ratio     ')
# print('-'*30)

# row = cursor.fetchone()
# while row:

#     print("|{:20}|{}".format(row[0], row[1]))
#     row = cursor.fetchone()

# print('')

# cursor.execute(query)
artists = []
ratios = []

for record in cursor.fetchall():
    artists.append(record[0])
    ratios.append(record[1])

pie = go.Pie(labels = artists, values = ratios)
pie_scheme = py.plot([pie], filename = 'laboratory3-2')

# --------------------------------------------------------------
"""
Third task
"""
query = '''
SELECT year, COUNT(album) AS rock_albums
FROM rs_view
WHERE genre = 'Rock'
GROUP BY year
'''
cursor.execute(query)
# print('Third task')
# print('|year      |rock_albums ')
# print('-'*25)

# row = cursor.fetchone()
# while row:

#     print("|{:10}|{}".format(row[0], row[1]))
#     row = cursor.fetchone()

# print('')


years = []
rock_albums = []

for record in cursor.fetchall():
    years.append(record[0])
    rock_albums.append(record[1])

scatter = go.Scatter(
    x= years,
    y = rock_albums
)

data = [scatter]
plot_scheme = py.plot(data, filename = 'laboratory3-3')

# --------------------------------------------------------------
my_board = dashboard.Dashboard()
bar_scheme_id = fileId_from_url(bar_scheme)
plot_scheme_id = fileId_from_url(plot_scheme)
pie_scheme_id = fileId_from_url(pie_scheme)

box_1 = {
    'type' : 'box',
    'boxType' : 'plot',
    'fileId' : bar_scheme_id,
    'title' : 'Запит 1'
}

box_2 = {
    'type' : 'box',
    'boxType' : 'plot',
    'fileId' : pie_scheme_id,
    'title' : 'Запит 2'
}

box_3 = {
    'type' : 'box',
    'boxType' : 'plot',
    'fileId' : plot_scheme_id,
    'title' : 'Запит 3'
}

my_board.insert(box_3)
my_board.insert(box_1, 'right', 1)
my_board.insert(box_2, 'above', 2)

py.dashboard_ops.upload(my_board, 'RS500')
connection.close()
