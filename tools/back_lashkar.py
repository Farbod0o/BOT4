#__________________******Libraries******____________________

import datetime
import sqlite3
import os

#__________________________________________________________________________#



#________________________****BOT SETTINGS****________________________#
#_دیتابیس:
db_path = r'../BOT4.db'
conn =sqlite3.connect(db_path,check_same_thread=False)
c=conn.cursor()
#_تعریف:
A1  ,  A2 , A3 , A4 , A5 , A6 , A7 , A8 , A9 , A10 , A11 , A12 = range(12)

def sum_dict(a,b):
    keys1 = a.keys()
    keys2 = b.keys()
    for key in keys2:
        if key in keys1:
            a[key] = a[key]+b[key]
        else:
            a[key] = b[key]
    return a



list = []
sql = '''SELECT * From lashkarkeshi'''
recs = c.execute(sql)
for row in recs:
    code = row[9]
    list.append(code)


for code in list:
    try:
        sql = '''SELECT * From lashkarkeshi'''
        recs = c.execute(sql)
        for row in recs:
            if code == row[9]:
                troops = eval(row[2])
                khandan = row[1]

        print(khandan)
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if row[2] == khandan:
                cid = row[0]
                troops2 = eval(row[9])

        new = sum_dict(troops,troops2)
        c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("troops",new,cid))
        conn.commit() 
    except:
        print(code)

print("end")