#__________________******Libraries******____________________

import datetime
import sqlite3
import os

#__________________________________________________________________________#

def sum_dict(a,b):
    keys1 = a.keys()
    keys2 = b.keys()
    for key in keys2:
        if key in keys1:
            a[key] = a[key]+b[key]
        else:
            a[key] = b[key]
    return a


#________________________****BOT SETTINGS****________________________#
#_دیتابیس:
db_path = r'../BOT4.db'
conn =sqlite3.connect(db_path,check_same_thread=False)
c=conn.cursor()
#_تعریف:
A1  ,  A2 , A3 , A4 , A5 , A6 , A7 , A8 , A9 , A10 , A11 , A12 = range(12)




eghlima = ["🐺North","🦈Riverlands","🦅The Vale","🦁Westerlands","🌊Iron Islands","🌼Reach","🦌Stormlands","🐲Crownlands","🌞Dorne","🪙Essos"]

for egh in eghlima:
    list = []
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if row[4] == egh:
            cid = int(row[0])
            list.append(cid)
    sumn = 0
    num = 0
    sume = 0
    print(egh)
    for key in list:
        num +=1
        cid = key

        try:
            sql = '''SELECT * From Information'''
            recs = c.execute(sql)
            for row in recs:
                if row[0] == key:
                    name = row[1]
                    khandan = row[2]
                    manba = eval(row[5])
                    buildings = eval(row[6])
                    building2 = eval(row[7])
                    dastresi = row[8]
                    troops = eval(row[9])
                    zvorodi = row[12]
                    zkhoroji = row[13]
                    etehad = row[19]
                    sarmaye = row[20]
                    vam = row[21]
            
            for key in building2:
                n = building2[key]
                sume = sume+n

            for key in buildings:
                n = buildings[key]
                sumn = sumn+n


        except:
            pass
    print(sume)
    print(sumn)
    print(num)
