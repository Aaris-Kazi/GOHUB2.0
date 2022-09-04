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

# import sqlite3
# import pandas as pd

# conn = sqlite3.connect('db.sqlite3')
# cursor = sqlite3.Cursor(conn)
# df = pd.read_csv('auth_user.csv', sep=';')
# df.to_sql('auth_user', conn, if_exists='replace', index=False)
#########################################################################
# df = pd.read_csv('main_resultnotfound.csv', sep=';')
# df = pd.read_csv('main_hotel_details.csv', sep=';')
# df = pd.read_csv('main_hotel_booking.csv', sep=';')

# df.to_sql('main_resultsnotfound', conn, if_exists='replace', index=False)
# df.to_sql('main_hotel_details', conn, if_exists='replace', index=False)

# query = 'INSERT INTO main_resultsnotfound (location) VALUES (?)'
# cursor.executemany(query, contents)
# cursor.executemany(query, df)
# conn.commit()
# conn.close()
##############################

# text = "un was establish on 24-10-1945, India got freedon 15-09-1945."
# # text = "something something something on 24-10-1947, India got freedon 15-09-1945."
# text = input()
# temp = 0
# count = 0
# sp_text = text.split(' ')
# for i in sp_text:
#     i = i.replace(',', '')
#     i = i.replace('.', '')
#     if '-' in i:
#         # print(i)
#         i = i.split('-')
#         # print(i[len(i)-1])
#         if temp == int(i[len(i)-1]):
#             pass
#         else:
#             temp = int(i[len(i)-1])
#             count+=1
# print(count)


# n = int(input())
# e = int(input())
# tab = list(map(int, input()))

# yes = 00100110111111101
# no = 11110111011101


# text = '00100110111111101'

# # text = '11110111011101'

# temp = '2'
# count = 0
# status = ''
# for i in text:
#     # print(type(i))
#     if temp == int(i):
#         count += 1
#         print(i)
#         if count == 7:
#             status = 'YES'
#             break
#     else:
#         temp = i
#         count = 0 
#         status = 'NO'

#     # print(i)

# print(status)

# text = '00100110111111101'

# text = '11110111011101'

input1 = ['0010', '10000000', '001001101111111', '111101111111111', '', '101001', '10100101000000000', '1010101', '0000000001000000000001101011000', '1000010000001101011000', '1000010000110101100', '0', '101010111111111111111111111111', '10011011', '10011010', '11111001', '001101100011100011', '111100010011111100', '100011110010111111', '100000101000000010001100010101000010010010100', '011110111110101111001011000010110010101111100000', '001000001001001011100110010110111011101101100101',
          '101101001100010010111101011100101000100000000001001010101111101111101000', '000111010101011110010110110011011010111111010000101000001110000111001010', '011100001101001101011101001110001011010111010111101101001001111000011101', '111101100110001001111001111011010111111101000101010110111111011101101101', '1001000101011100100010110011101000111000100111101001011000110100010010100010011011110011',
          '1111100100010110100100111111001101100011110000101000110111001111011111011100101011110111100000010', '1111101111000101000001000010101110111010110001110110110110101100101000100001010111110000110100111', '10111101101110101101111110100100101000111110111100000110001100100111101110101101000110101000101110', '00101001111000101101100000111001111101001111100010100001001111111110101111001011010101010010110101',
          '11110101000101001010111011001011011100110000101000100000011111000100111001010100011011110000010110', '01011000110011100011101001111000110101010110000000001101100100101111001011110101111000111011001001', '00011011100111011100000000100111111010011011111000010010101100001100011000000100011110110111100011', '10000100001000001000100001000010000100001000010000100001000010000100001000010000100001000010000100',
          '10000000001000000000100000000010000000001000000000100000000010000000001000000000100000000010000000', '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', '11111111111111111111111111111111111111110111111111111111111111111111111111111111111111111111111111', '101001010', '111101110111', '100000', '000000', '011111', '111111']
for i in input1:
    text = i
    temp = 0
    count = 1
    ans = []
    for i in text:
        if int(i) == temp:
            count += 1
            if count == 7:
                print('YES')
                break
            else:
                pass
        else:
            count = 1
            temp = int(i)

    if count  >= 7:
        print('YES')
    else:
        print('NO')