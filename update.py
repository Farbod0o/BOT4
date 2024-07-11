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
db_path =r'bot4.db'
conn =sqlite3.connect(db_path,check_same_thread=False)
c=conn.cursor()
#_تعریف:
A1  ,  A2 , A3 , A4 , A5 , A6 , A7 , A8 , A9 , A10 , A11 , A12 = range(12)




list = []
sql = '''SELECT * From Information'''
recs = c.execute(sql)
for row in recs:
    cid = int(row[0])
    if cid == 0:
        pass
    else:
        list.append(cid)

for key in list:
    cid = key
    print(cid)
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
        
        try:
            sar = []
            if sarmaye != "[]":
                sarmaye = eval(sarmaye)
                mande = sarmaye[2]
                newmande = mande - 1
                if newmande<1:
                    hafte = sarmaye[0]
                    lvl = sarmaye[3]
                    meghdar = sarmaye[1]
                    darsadsood = hafte*lvl
                    sood = meghdar*darsadsood/100
                    sood = int(sood)
                    seke = manba["💰|سکه"]
                    newseke = seke + meghdar + sood
                    manba["💰|سکه"] = newseke
                    sar = []
                else:
                    sarmaye[2] = newmande
                    sar = sarmaye
        except Exception as e:
            print("==")
            print(e)

        try:
            ad = 0
            sql = '''SELECT * From etehad'''
            recs = c.execute(sql)
            for row in recs:
                if (row[0]) == etehad:
                    ad = 1
                    n = row[0]
                    memb = row[1]
                    eid = row[2]
                    an1 = row[7]
                    an2 = row[8]
                    an3 = row[9]
                    sum = row[10]
            if ad == 1:
                an1 = eval(an1)
                memb = eval(memb)
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
                    manba_list = sum_dict(manba_list,manba)



                print(sum)
                if an1[1]>0:
                    lvl = an1[1]/20000
                    print(lvl)
                    if an1[1]>=sum:
                        for mnbname in mnbi:
                            try:
                                mnb = manba[mnbname]
                                newmnb = mnb + mnb*lvl/10
                                manba[mnbname] = int(newmnb)
                            except:
                                pass
                    else:
                        print(sum)

        except Exception as e:
            print("==")
            print(e)
            print(khandan)





        try:
            ad = 0
            sql = '''SELECT * From etehad'''
            recs = c.execute(sql)
            for row in recs:
                if (row[0]) == etehad:
                    ad = 1
                    n = row[0]
                    memb = row[1]
                    eid = row[2]
                    an1 = row[8]
                    an3 = row[9]
                    sum = row[11]
            if ad == 1:
                an1 = eval(an1)
                memb = eval(memb)
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
                    manba_list = sum_dict(manba_list,manba)



                print(sum)
                if an1[1]>0:
                    lvl = an1[1]/20000
                    print(lvl)
                    if an1[1]>=sum:
                        for mnbname in mnbi:
                            try:
                                mnb = manba[mnbname]
                                newmnb = mnb + mnb*lvl/10
                                manba[mnbname] = int(newmnb)
                            except:
                                pass
                    else:
                        print(sum)

        except Exception as e:
            print("=====")
            print(e)
            print(khandan)




        try:
            check = buildings["🎋|درخت نیایش"]
            check = check + 1
        except:
            buildings["🎋|درخت نیایش"] = 0
        try:
            check2 = buildings["⛪️|سپت"]
            check2 = check2 + 1

        except:
            building2["⛪️|سپت"] = 0

        try:
            check4 = buildings["🗿|سنگ تراشی"]
            check4 = check4 + 1
        except:
            building2["🗿|سنگ تراشی"] = 0
#_______________تولید منابع_____________________
        masraf = 0
        for key1 in troops:  
            try:
                masrafi = 3
                sql = '''SELECT * From niro'''
                recs = c.execute(sql)
                for row in recs:
                    if row[0] == key1:
                        masrafi = row[3] 
                num = troops[key1] 
                masraf = masraf + num*masrafi
            except Exception as e:
                print(e)

        bikar = manba["👥جمعیت بیکار"]
        masraf = masraf + bikar
        try:
            masraf = masraf/2
            gosht = manba["🥩|گوشت"]
            newgosht = gosht-masraf

            if newgosht<0:
                manba["🥩|گوشت"] = 0
                ghalat = manba["🌾|گندم"]
                masraf = newgosht*2*-1
                newghalat = ghalat - masraf
        except Exception as e:
            print(e)


        for key1 in buildings:
            try:
                if key1 == "☄️|کارگاه ادوات":
                    lvl = buildings["☄️|کارگاه ادوات"]
                    dez = troops['💈|دژکوب']
                    man = troops['☄️|منجنیق']
                    bali = troops['🎯|بالیستا']

                    if lvl == 1:
                        troops['💈|دژکوب'] = dez + 5
                    if lvl == 2:
                        troops['💈|دژکوب'] = dez + 10
                        troops['☄️|منجنیق'] = man + 5
                    if lvl == 3:
                        troops['💈|دژکوب'] = dez + 15
                        troops['☄️|منجنیق'] = man + 10
                        troops['🎯|بالیستا'] =bali +5

                if key1 == "™️|بازارچه":
                    lvl = buildings["™️|بازارچه"]
                    zarf = lvl*250
                    if lvl == 0:
                        zarf = 100

                if key1 == "💰|خزانه":
                    try:
                        lvl = buildings[key1]
                        sql = '''SELECT * From hazine'''
                        recs = c.execute(sql)
                        for row in recs:
                            if row[0] == key1:
                                tolid = int(row[2])  
                                mnbname = row[7] 
                                tolid = tolid*lvl
                        try:
                            mnb = manba[mnbname]
                            newmnb = mnb + tolid
                            manba[mnbname] = newmnb    
                        except:
                            pass
                    except:
                        pass

            except Exception as e:
                print(e)



        for key1 in building2:
            if key1 == "🗿|سنگ تراشی":
                lvl = building2[key1]
                lvl2 = building2["🏛|معدن مرمر"]
                tolid = lvl*lvl2*200
                man = manba["🏛|مرمر"]
                manba["🏛|مرمر"] = man + tolid

            try:
                lvl = building2[key1]
                sql = '''SELECT * From hazine'''
                recs = c.execute(sql)
                for row in recs:
                    if row[0] == key1:
                        tolid = int(row[2])  
                        mnbname = row[7] 
                        tolid = tolid*lvl
                try:
                    mnb = manba[mnbname]
                    newmnb = mnb + tolid
                    manba[mnbname] = newmnb    
                except:
                    pass
            except:
                pass

                    
        try:
            c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("manba",manba,cid))
            c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("troops",troops,cid))
            c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("vorodi",zarf,cid))
            c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("khoroji",zarf,cid))
            c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("sarmaye",sar,cid))

            conn.commit() 
        except Exception as e:
            print(e)
            print("nashod")
            print(khandan)
    except Exception as e:
        print(e)

    #except Exception as e:
        #print(e)
        ##print("++++++++")
        #print(key)
        #print("++++++++")



print("tamom")