# a = [
#     {'id': 1, 'name': 'A'},
#     {'id': 2, 'name': 'B'},
#     {'id': 3, 'name': 'C'},
# ]
# b = []
# c = []
# i = 0
# while i < len(a):
#     temp = a[i]
#     id = temp['id']
#     b.append(id)
#     name = temp['name']
#     c.append(name)
#     i+=1
# print(b)
# print(tuple(c))

# print(len('https://imgcy.trivago.com/c_lfill,d_dummy.jpeg,e_sharpen:60,f_auto,h_225,q_auto,w_225/itemimages/17/21/1721801_v2.jpeg'))

# a ='₹13,560'
# print(a.replace('₹', ''))
# import pandas as pd

# df = pd.read_csv('lonavalatest.csv')
# price = []
# for i in df['price']:
#     i = i.replace(",", "")
#     i = i.strip("₹")
#     price.append()

import sqlite3
import pandas as pd

conn = sqlite3.connect('db.sqlite3')
cursor = sqlite3.Cursor(conn)

# df = pd.read_csv('main_resultnotfound.csv', sep=';')
# df = pd.read_csv('main_hotel_details.csv', sep=';')
# df = pd.read_csv('main_hotel_booking.csv', sep=';')
df = pd.read_csv('auth_user.csv', sep=';')

# df.to_sql('main_resultsnotfound', conn, if_exists='replace', index=False)
# df.to_sql('main_hotel_details', conn, if_exists='replace', index=False)
df.to_sql('auth_user', conn, if_exists='replace', index=False)

# query = 'INSERT INTO main_resultsnotfound (location) VALUES (?)'
# cursor.executemany(query, contents)
# cursor.executemany(query, df)
# conn.commit()
# conn.close()