import sqlite3


def sum_dict(a,b):
    keys1 = a.keys()
    keys2 = b.keys()
    for key in keys2:
        if key in keys1:
            a[key] = a[key]+b[key]
        else:
            a[key] = b[key]
    return a


db_path = r'../BOT4.db'
conn =sqlite3.connect(db_path,check_same_thread=False)
c=conn.cursor()

etehadlist = []
sql = '''SELECT * From etehad'''
recs = c.execute(sql)
for row in recs:
    etehadlist.append(row[0])

for etehad in etehadlist:
    sql = '''SELECT * From etehad'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == etehad:
            ad = 1
            n = row[0]
            memb = eval(row[1])
            eid = row[2]
            an1 = row[8]
            an3 = row[9]
    if ad == 1:
        an1 = eval(an1)
        mnbi = an1[3]
        mnbi = mnbi.split("+")
        manba_list = {}
    
    for m in memb:
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[2]) == m:
                idd = row[1]
                manbae = row[5]   


        manbae = eval(manbae)
        manba_list = sum_dict(manba_list,manbae)

    sum = 0
    for i in mnbi:
        try:
            n = manba_list[i]
            sum = sum+n
        except:
            pass
    try:
        print(etehad)
        print(sum)
    except:
        pass