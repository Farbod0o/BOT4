#__________________******Libraries******____________________
import collections
import heapq
import shutil
import telegram
from telegram.ext import Updater , CommandHandler
from telegram import ParseMode
from telegram.ext import MessageHandler , Filters
from telegram.ext import CallbackQueryHandler
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup 
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from selenium import webdriver
import random as rand
import datetime
import os
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image , ImageOps
import arabic_reshaper
from bidi.algorithm import get_display
import time
import datetime
import sqlite3
import os
import emoji 
import secrets
import threading
from os import remove
import logging
from selenium.webdriver.common.by import By

steps = {}
stats = {}
noelashkar = {}
#__________________________________________________________________________#

keyboardM = [
    ['🏰مرکز شهر','🛖مرکز فرماندهی'],
    ['🕊مرکز ارتباطات',"🔘مشاهده دارایی"],
    ['⚙️تنظیمات']
    ]
#________________________****BOT SETTINGS****________________________#

#_توکن ربات:
updater = Updater("Token")
#_دیتابیس:
db_path =r'BOT4.db'
conn =sqlite3.connect(db_path,check_same_thread=False)
c=conn.cursor()
#_تعریف:
A1  ,  A2 , A3 , A4 , A5 , A6 , A7 , A8 , A9 , A10 , A11 , A12 = range(12)
B1  ,  B2 , B3 , B4 , B5 , B6 , B7 , B8 , B9 , B10 , B11 , B12= range(13,25)
C1  ,  C2 , C3 , C4 , C5 , C6 , C7 , C8 , C9 , C10 , C11 , C12= range(26,38)
G1  , G2  , G3 , G4 , G5 , G6 , G7 , G8 , G9 , G10 , G11 , G12= range(39,51)
H1  , H2  , H3 , H4 , H5 , H6 , H7 , H8 , H9 , H10 , H11 , H12 = range(52,64)
I1  , I2  , I3 , I4 , I5 , I6 , I7 , I8 , I9 , I10 , I11 , I12 = range(65,77)
J1  , J2  , J3 , J4 , J5 , J6 , J7 , J8 , J9 , J10 , J11 , J12 = range(78,90)
K1  , K2  , K3 , K4 , K5 , K6 , K7 , K8 , K9 , K10 , K11 , K12 = range(91,103)
M1  , M2  , M3 , M4 , M5 , M6 , M7 , M8 , M9 , M10 , M11 , M12 = range(104,116)
N1  , N2  , N3 , N4 , N5 , N6 , N7 , N8 , N9 , N10 , N11 , N12 = range(117,129)
O1  , O2  , O3 , O4 , O5 , O6 , O7 , O8 , O9 , O10 , O11 , O12 = range(130,142)
P1  , P2  , P3 , P4 , P5 , P6 , P7 , P8 , P9 , P10 , P11 , P12 = range(143,155)
#_نام ربات:
gamename = "BOT4"
#______________________________________________________________________#

#________________________****Error Log****________________________#
logging.error("Couldn't find %r")
#_________________________________________________________________#

#__________________________**DataBase**__________________________#

def insert_Information(khandan,eghlim,cid,user,manba,buildings,troops,vorodi,khoroji,ghale,buildings2,farsi):
    academy = {'⚔️|شمشیرزن': 0, '🗡|نیزه دار': 0, '🐎|سوارکار': 0, '🏹|کماندار': 0, '☄️|منجنیق': 0, '💈|دژکوب': 0, '🎯|بالیستا': 0,"🔱نیرو ویژه اقلیم":0}
    c.execute('''INSERT INTO Information (khandan,eghlim,cid,name,manba,buildings,buildings2,dastresi,troops,vorodi,khoroji,ghale,etehad,sarmaye,vam,tamrin,knight,win_n,lose_n,zarib,farsi,academy) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(khandan,eghlim,cid,user,manba,buildings,buildings2,"all",troops,"0","0",ghale,"a","[]","[]","{'khali':0,'hojom':0,'defpiyade':0,'defsavare':0}","{'name':0,'lvl':0,'xp':0}",0,0,1,farsi,academy))
    #c.execute('''UPDATE Information SET manba1 = "{}" WHERE keshvar = "{}" '''.format(manba1,keshvar))
    conn.commit() 

def stat_up(cid):
    global stats
    try:
        Y = stats[cid]
    except:
        Y = 0
    stats[cid] = Y+1


def ax2(name1,name2):
    randn = rand.randint(1,7)
    image = Image.open(f'view/sad/{randn}.jpg').convert("RGBA")
    draw = ImageDraw.Draw(image)
    text = f"خاندان *{name1}* دستور توقف ارتش *{name2}* را صادر کرد"
    
    reshaped_text = arabic_reshaper.reshape(text)   
    text = get_display(reshaped_text)
    font_size = 45
    font = ImageFont.truetype("view/fonts/KAGHAZ.ttf", font_size)  # Replace with the actual font path if necessary
    text_position = (120, 620)  # Adjust the coordinates as needed
    hello_color = (220,150,0)  # Red color
    other_words_color = (255, 255, 255)  # White color
    words = text.split("*")

    # Write each word with the appropriate color
    x, y = text_position
    for i, word in enumerate(words):
        word_width, _ = draw.textsize(word, font=font)
        word_color = hello_color if i == 1 or i == 3 else other_words_color
        draw.text((x, y), word, font=font, fill=word_color)
        x += word_width + 5  # Add some spacing between words

    output_path = 'temp/sad.png'
    image.save(output_path)


def ax(name1,name2):
    pos1dict = {"شمال":(575,965),"ریور":(577,949),"ویل":(586,965),"وستر":(574,950),"جزایر":(588,929),"ریچ":(584,965),"استورم":(586,933),"دورن":(586,957),"کرون":(575,953)}
    pos2dict = {"شمال":(383,965),"ریور":(420,958),"ویل":(426,964),"وستر":(412,965),"جزایر":(430,932),"ریچ":(445,965),"استورم":(410,933),"دورن":(408,957),"کرون":(408,954)}
    colordict = {"شمال":(1,190,250),"ریور":(45,140,210),"ویل":(115,115,190),"وستر":(200,170,20),"جزایر":(140,140,140),"ریچ":(110,200,45),"استورم":(220,160,15),"دورن":(220,150,65),"کرون":(200,40,10)}
    pos1 = pos1dict[name1]
    pos2 = pos2dict[name2]

    eghlim = name2
    randn = rand.randint(1,7)
    photo = Image.open(f'dastorhamle/{randn}.jpg').convert("RGBA")
    watermark = Image.open(f"houses/{name1}.png").convert("RGBA")
    photo.paste(watermark, pos1, watermark)
    watermark = Image.open(f"houses/{name2}.png").convert("RGBA")
    photo.paste(watermark, pos2, watermark)
    photo.save(f"new.png")

    image_path = 'temp/new.png'  # Replace with the actual path to your photo
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    text = f"دستور آغاز نبردی در اقلیم *{eghlim}* صادر شد"
    reshaped_text = arabic_reshaper.reshape(text)   
    text = get_display(reshaped_text)
    font_size = 45
    font = ImageFont.truetype("view/fonts/KAGHAZ.ttf", font_size)  # Replace with the actual font path if necessary
    text_position = (270, 620)  # Adjust the coordinates as needed
    hello_color = (200,40,10)  # Red color
    other_words_color = (255, 255, 255)  # White color
    words = text.split("*")

    # Write each word with the appropriate color
    x, y = text_position
    for i, word in enumerate(words):
        word_width, _ = draw.textsize(word, font=font)
        word_color = hello_color if i == 1 else other_words_color
        draw.text((x, y), word, font=font, fill=word_color)
        x += word_width + 5  # Add some spacing between words

    output_path = 'temp/output.png'
    image.save(output_path)
#_________________________________________________________________#

#__________________________**Radar**__________________________#

def radar_func(update, context):
    def thread1(update, context):
        while True:
            try:
                x = datetime.datetime.now()  
                time1 = x.strftime("%H:%M - %d") 
                time2 = x.strftime("%H:%M") 
                min = x.strftime("%M") 
                time2 = f"{time2}"
                print(time2)
                arteshlist = []
                sql = '''SELECT * From lashkarkeshi WHERE vaziat ="{}" AND nextETA = "{}" '''.format('حرکت',time2)
                recs = c.execute(sql)
                for row in recs:
                    codee = row[9]
                    arteshlist.append(codee)
                

                
                for code in arteshlist:
                    sql = '''SELECT * From lashkarkeshi WHERE vaziat ="{}" AND code = "{}" '''.format('حرکت',code)
                    recs = c.execute(sql)
                    for row in recs:
                        namea = row[1]
                        masir = eval(row[5])
                        timee = row[6]
                        code = row[9]
                        noe = row[10]
                        hidden = row[11]
    
                    mande = len(masir)

                    if int(mande)>1:
                        mabda = masir[0]
                        nextmaghsad = masir[1]
                        if int(mande)>1:
                            v = "edame"
                        else:
                            v = "payan"
                        next(context,code,mabda,nextmaghsad,namea,noe,hidden,v)
                    if mande ==1:
                        esteghrar(code)

                time.sleep(20)
            except:
                pass
    t1 = threading.Thread(target=thread1,args=(update,context))
    t1.start()
def next(context,code,mabda,nextmaghsad,namea,noe,hidden,v):

    if v == "edame":
        text_magh = f"⭕️شما مقصد این لشکرکشی نیستید!"
    else:
        text_magh = f"⚠️شما مقصد این لشکرشی هستید!"

    zarib = 1
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[1]) == namea:
            zarib = row[29]

    sql = '''SELECT * From lashkarkeshi WHERE vaziat ="{}" AND code = "{}" '''.format('حرکت',code)
    recs = c.execute(sql)
    for row in recs:
        cid = row[0]
        masir = eval(row[5])
    if noe == "🗺لشکرکشی":
        edges = edges1
    elif noe == "🐉لشکرکشی":
        edges = edges3
        zarib = zarib/2
    else:
        edges = edges2

    sh_masir = shortestPath(edges, mabda, nextmaghsad)
    dis = sh_masir[0]
    masir.remove(masir[0])
    dis = int(dis)
    dis = dis*60*zarib
    now = datetime.datetime.now()
    time1 = now + datetime.timedelta(seconds=dis)
    nexteta = time1.strftime("%H:%M")
    c.execute('''UPDATE lashkarkeshi SET masir = "{}" WHERE code = "{}" '''.format(masir,code))
    c.execute('''UPDATE lashkarkeshi SET mabda = "{}" WHERE code = "{}" '''.format(mabda,code))
    c.execute('''UPDATE lashkarkeshi SET nextETA = "{}" WHERE code = "{}" '''.format(nexteta,code))
    conn.commit() 



    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            eghlim = row[4]
            ghalekhandan = row[3]
            newniro = row[11]
            listniro = row[14]
            time = row[16]
            etehad = row[19]

    data = f"3*{code}*1*1"
    data2 =f"7*{code}*1*1"
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[3]) == nextmaghsad:
            cidnext = row[0]
            khandan_next = row[2]
            buildingnext = row[6]
            etehadnext = row[19]
    d = 0
    if d == 0:
        try:     
            sql = '''SELECT * From etehad'''
            recs = c.execute(sql)
            for row in recs:
                if (row[0]) == etehadnext:
                    eid = row[2]

            buildings = eval(buildingnext)
            borj = buildings["👁|برج دیدبانی"]

            if borj>1 and hidden != "hidden":
                try:
                    keyboard = [[InlineKeyboardButton("⛔️بستن راه" ,callback_data=data)],
                    [InlineKeyboardButton("👁‍🗨مشاهده نیرو" ,callback_data=data2)],
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    context.bot.send_message(chat_id=cidnext ,text = f"""
    <b>🔰با توجه به گزارشی که نیروهای مستقر در برج دیدبانی ارسال کرده اند لشکریان خاندان <a href="tg://user?id={cid}">{khandan}</a> در حال نزدیک شدن به قلعه شما میباشند!</b>

    <i>❗️در صورت تمایل میتوانید راه را بر روی نیروهای فوق ببندید

    {text_magh}

    ‼️توجه داشته باشید بستن  راه بر روی نیروها به معنی اعلام جنگ علیه آن ها میباشد همچنین در صورت بستن راه به روی ارتش نیروهای شما از قلعه خارج شده و شما نمیتوانید از برتری حضور در قلعه استفاده کنید و نبرد در زمین باز صورت خواهد گرفت

    ⚠️در صورتی که قصد بستن مسیر به روی ارتش در حال حرکت را ندارید این پیام را نادیده بگیرید
        </i>""" ,reply_markup=reply_markup,parse_mode = ParseMode.HTML )
                except:
                    pass

                try:
                    if etehad != etehadnext or etehad == "a":
                        context.bot.send_message(chat_id=eid ,text = f"""
        <b>🔰با توجه به گزارشی که دیدبانان {khandan_next} ارسال کرده اند نیروهای ارتش {khandan} در حال حرکت در مرزهای شما میباشد!</b>
        """ ,parse_mode = ParseMode.HTML )
                except Exception as e:
                    print(e)
            elif borj>0 and hidden != "hidden":
                try:
                    keyboard = [[InlineKeyboardButton("⛔️بستن راه" ,callback_data=data)],]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    context.bot.send_message(chat_id=cidnext ,text = f"""
    <b>🔰با توجه به گزارشی که نیروهای مستقر در برج دیدبانی ارسال کرده اند لشکریان خاندان <a href="tg://user?id={cid}">{khandan}</a> در حال نزدیک شدن به قلعه شما میباشند!</b>

    <i>❗️در صورت تمایل میتوانید راه را بر روی نیروهای فوق ببندید

    {text_magh}

    ‼️توجه داشته باشید بستن  راه بر روی نیروها به معنی اعلام جنگ علیه آن ها میباشد همچنین در صورت بستن راه به روی ارتش نیروهای شما از قلعه خارج شده و شما نمیتوانید از برتری حضور در قلعه استفاده کنید و نبرد در زمین باز صورت خواهد گرفت

    ⚠️در صورتی که قصد بستن مسیر به روی ارتش در حال حرکت را ندارید این پیام را نادیده بگیرید
        </i>""" ,reply_markup=reply_markup,parse_mode = ParseMode.HTML )
                except:
                    pass

                try:
                    if etehad != etehadnext or etehad == "a":
                        context.bot.send_message(chat_id=eid ,text = f"""
        <b>🔰با توجه به گزارشی که دیدبانان {khandan_next} ارسال کرده اند نیروهای ارتش {khandan} در حال حرکت در مرزهای شما میباشد!</b>
        """ ,parse_mode = ParseMode.HTML )
                except:
                    pass
        except:
            pass



def esteghrar(code):
    try:
        sql = '''SELECT * From lashkarkeshi WHERE vaziat ="{}" AND code = "{}"'''.format('حرکت',code)
        recs = c.execute(sql)
        for row in recs:
                khandan = row[1]
                niro = row[2]
                masir = eval(row[5])
        maghsad = masir[0]

        s = 0 
        sql = '''SELECT * From lashkarkeshi WHERE vaziat ="{}" AND mabda = "{}"'''.format('💢مستقر',maghsad)
        recs = c.execute(sql)
        for row in recs:
            if row[1] == khandan:
                niros = row[2]
                code2 = row[9]
                s = 1

        sql = '''SELECT * From Information WHERE khandan ="{}"'''.format(khandan)
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == maghsad:
                s = 2
                niros = row[9]
                cid = row[0]

        if s ==1:
            niro = eval(niro)
            niros = eval(niros)

            for key in niro:
                n1 = niro[key]
                n2 = niros[key]
                nf = n1+n2
                niros[key] = nf

            c.execute('''UPDATE lashkarkeshi SET niro = "{}" WHERE code = "{}" AND vaziat = "{}" '''.format(niros,code2,"💢مستقر"))
            c.execute('''DELETE FROM lashkarkeshi WHERE code = "{}" AND vaziat = "{}" ;'''.format(code,"حرکت"))
            conn.commit() 

        if s == 2:
            niro = eval(niro)
            niros = eval(niros)

            for key in niro:
                n1 = niro[key]
                n2 = niros[key]
                nf = n1+n2
                niros[key] = nf

            c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format("troops",niros,cid))
            c.execute('''DELETE FROM lashkarkeshi WHERE code = "{}" AND vaziat = "{}" ;'''.format(code,"حرکت"))
            conn.commit() 

        else:
            c.execute('''UPDATE lashkarkeshi SET vaziat = "{}" WHERE code = "{}" '''.format("💢مستقر",code,))
            c.execute('''UPDATE lashkarkeshi SET mabda = "{}" WHERE code = "{}" '''.format(maghsad,code))
            c.execute('''UPDATE lashkarkeshi SET maghsad = "{}" WHERE code = "{}" '''.format(maghsad,code))
            conn.commit() 
    except:
        c.execute('''DELETE FROM lashkarkeshi WHERE code = "{}" AND vaziat = "{}" ;'''.format(code,"حرکت"))
        conn.commit() 
#_________________________________________________________________#







def getid (update,context):
    name = update.message.chat.title
    cid = update.message.chat_id
    context.bot.send_message(chat_id = cid , text = f"""
<b>👁‍🗨نام گروه : {name}</b>
➿چت ایدی: <code>{cid}</code>"""
,parse_mode = ParseMode.HTML)


def sum_dict(a,b):
    keys1 = a.keys()
    keys2 = b.keys()
    for key in keys2:
        if key in keys1:
            a[key] = a[key]+b[key]
        else:
            a[key] = b[key]
    return a



def start (update,context):
    gid = -1001185952954
    cid = update.message.chat_id
    ciid = update.message.from_user.id
    mid=update.message.message_id
    print(mid)
    stat_up(cid)

    first_name = update.message.chat.first_name
    ozviat = context.bot.get_chat_member(chat_id=gid,user_id = ciid)
    dd = ozviat.status
    last_name = update.message.chat.last_name
    if last_name == "None":
        last_name = ""

    if dd == "left":
            keyboard = [[InlineKeyboardButton("عضو شوید" ,url="https://t.me/TeleeGames")],  
            [InlineKeyboardButton("✅عضو شدم" ,url="https://t.me/battleofthroneBot?start")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            photo = open('temp/poster.jpg', 'rb')
            context.bot.send_photo(chat_id = cid , photo = photo , caption = f"""
👾لطفا جهت حمایت از تیم تله گیمز در کانال ما عضو شده تا از آخرین اخبار بازی های تلگرامی با خبر شوید
@TeleeGames
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)

    s = 0
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            s = 1
            khandan = row[2]

    if s == 0:
        photo = open('temp/banner.jpg', 'rb')
        context.bot.send_photo(chat_id = cid , photo = photo , caption = f"""
        👾سلام <b>لرد {first_name}</b> ، به <b> بتل اف ترونز</b> خوش آمدید!
            
▪️از امروز بنده مشاور شما در اداره خاندانتان خواهم بود تا بتوانیم در زمینه های نظامی اقتصادی و آموزشی باعث پیشرفت خاندان خود باشیم هر چند این مسیر طولانی و نیازمند بردباری شماست اما من معتقدم که با کمک یکدیگر میتوانیم موفق شویم
    
🔐*در ابتدا کدی که از ادمین بازی دریافت کرده اید را وارد کنید این کد مجوز ورود شما به مراحل بعد میباشد*

⚠️توجه: دقت داشته باشید که در مرحله ثبت نام اکانت شما میبایست حتما دارای عکس پروفایل باشد و از عکس پروفایل شما در مراحل مختلفی از بازی استفاده خواهد شد بنابراین توجه لازم را داشته باشید 

در صورت وجود هرگونه سوال و دریافت کد به ایدی : @Farbodo پیام دهید
""",parse_mode = ParseMode.HTML)
        return B5
    else:
        keyboard = [
            ['🔁ادامه']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid , text =  f"شما به عنوان خاندان {khandan} شناسایی شدید",
        reply_markup=reply_markup)
        return A2



def register(update,context):
    user = update.message.chat.username
    cid = update.message.chat_id
    name = update.message.chat.first_name
    code = update.message.text
    namee = f"@{user} - {name}"

        

    sql = '''SELECT * From codes'''
    recs = c.execute(sql)
    for row in recs:
        if row[0] == code:
            khandan = row[1]
            eghlim = row[3]
            ghale = row[2]
            farsi = row[4]

    c.execute('''UPDATE codes SET {} = "{}" WHERE khandan = "{}" '''.format("code","used",khandan))
    conn.commit()
    #دریافت عکس پروفایل کاربر
    try:
        photo = context.bot.get_user_profile_photos(update.message.from_user.id).photos[0][-1].file_id
        photo_file = context.bot.getFile(photo)
        dl = photo_file.download()
        os.rename(dl, f"view/prof\{khandan}.png")
    except:
        pass
    niro = {
            "🐺North":"🐺|دایرولف",
            "🦈Riverlands":"🦈|کمان‌دار رودخانه",
            "🦅The Vale":"🦅|شوالیه شاهین",
            "🦁Westerlands":"🦁|ردا سرخ",
            "🌊Iron Islands":"🌊|تبرزن جزیره",
            "🌼Reach":"🌼|شوالیه رز",
            "🦌Stormlands":"🦌|شوالیه گوزن",
            "🐲Crownlands":"🐲|شوالیه اژدها",
            "🌞Dorne":"🦂|نیزه دار شن‌زار"
                    }
    
    nv = niro[eghlim]
    manabe = {"🪙TGC":0,"👥جمعیت":500,"👥جمعیت بیکار":500,'💰|سکه': 3000, '🔗|آهن': 800, '⛰|سنگ': 800, '🌲|چوب': 800, '🏅|طلا': 800, '🌾|گندم': 1000, '🐄|گاو': 100, '🏉|چرم': 250, '🥩|گوشت': 0, '🏛|مرمر': 500, '🍇|انگور': 500, '🍷|شراب': 0, '👚|لباس': 300, }
    b_list = {'🏰قلعه':0 , '🏕|کمپ ویژه':0, '🏟|میدان تمرین':0 ,'🐉|گودال اژدها':0 , '⚓️|بندر':0 ,
        '⛩|ورودی':0 ,'⚜️|آکادمی':0 , '👁|برج دیدبانی':0,'⚡️|اقامتگاه شوالیه':0 , '❤️|کمپ مجروحین':0 , '🗡|کمپ پیاده':0 ,
        '🏹|کمپ کماندار':0 , '🐎|کمپ سواره':0, '☄️|کارگاه ادوات':0,
        '🏛|تالار بزرگ':0 , '💰|خزانه':0 , '🏦|ایرون بانک':0 , '™️|بازارچه':0,} 

    t_list = {"⚔️|شمشیرزن":50 , "🗡|نیزه دار":50 , "🐎|سوارکار":25,"🏹|کماندار":50,"👀|جاسوس":0,"👣|راهزن":0,"🛡|نگهبان":0,"🛶|کشتی":0,"⛵️|کشتی جنگی":0,"☄️|منجنیق":0,"💈|دژکوب":0,"🎯|بالیستا":0,"⚡️|شوالیه":0}
    b2_list = {'🔗|معدن آهن': 0, '⛰|معدن سنگ': 0, '🌲|چوب بری': 0, '🏅|معدن طلا': 0, '🌾|مزرعه': 0, '🐄|دامداری': 0, '🔪|کشتارگاه': 0, '👝|دباغی': 0, '🏛|معدن مرمر': 0, '🍇|تاکستان': 0, '🍷|شراب گیری': 0, '👚|خیاطی': 0}
    t_list[nv]=0
    insert_Information(khandan,eghlim,cid,namee,manabe,b_list,t_list,"0","0",ghale,b2_list,farsi)

    c.execute('''INSERT INTO hero (khandan,tajrobe,items,hp,def_b,att_b,att_p) values("{}","{}","{}","{}","{}","{}","{}");'''.format(khandan,1,["🔻سپر کوچک","🔻سپر","🔻کیسه کوچک","🔻کلاه خود ساده","🔻کلاه خود جنگی","🔻شمشیر","🔻کمان","🔻نیزه","🔻چکمه","🔻زره چرمی","🔻زره سلامتی",],100,0,0,0))
    conn.commit()

    #اضافه کردن اطلاعات به عکس بازی
    shutil.copy('temp/raw.png', f'pics/base/{khandan}.png')
    photo = Image.open(f'pics/base/{khandan}.png')
    myFont = ImageFont.truetype('view/fonts/Metamorphous.ttf', 24)
    d1 = ImageDraw.Draw(photo)
    d1.text((1675,1250),ghale, font=myFont, fill =(255, 255, 255),anchor="mm")
    d1.text((1675,1279),khandan, font=myFont, fill =(255, 255, 255),anchor="mm")
    d1.text((175,25),eghlim, font=myFont, fill =(255, 255, 255),anchor="mm")

    try:
        mask = Image.open('view/elements\profile_mask.png').convert('L')
        try:
            im = Image.open(f'view/prof\{khandan}.png')
        except:
            im = Image.open(f'telegames.png')

        output = ImageOps.fit(im, mask.size, centering=(1, 1))
        output.putalpha(mask)
        output = output.resize((115, 115))
        output.save('output.png')
        watermark = Image.open(f'temp/output.png').convert("RGBA")
        try:
            photo.paste(watermark, (1336,1181), watermark)
        except:
            pass
    except:
        pass

    photo.save(f'base/{khandan}.png')
    photo = Image.open(f'pics/base/{khandan}.png').convert("RGBA")
    watermark = Image.open("temp/1.png").convert("RGBA")
    photo.paste(watermark, (1326,1181), watermark)
    photo.save(f'base/{khandan}.png')

    keyboard = [
        ['✅قوانین را مطالعه کرده و موافقم']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)

    context.bot.send_message(chat_id = cid , text = f"""
<b> 🔰شما به عنوان لرد {khandan} از قلعه {ghale} واقع در {eghlim} ثبت شدید </b>


⚖️برای ورود به جهان بازی ابتدا میبایست با <a href="http://telegra.ph/شرایط-و-ضوابط-عمومی-08-18">شرایط و ضوابط عمومی</a> موافقت نمایید.


""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
    return A2



def menu(update,context):
    cid = update.message.chat_id
    stat_up(cid)

    user = update.message.chat.username
    cid = update.message.chat_id
    name = update.message.chat.first_name
    namee = f"@{user} - {name}"

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]  
            name1 = row[1]

    if name1 != namee:
        update_information("name",namee,cid)


    sql = ''' SELECT * From Information WHERE khandan ="{}" '''.format(khandan)
    recs = c.execute(sql)
    for row in recs:
        dastresi = '{}'.format(row[8])

    #پلیر به صورت کامل از بازی بن میشود
    if dastresi == "ban":
        context.bot.send_message(chat_id = cid ,
        text = "⛔️دسترسی شما به دلیل نقض قوانین ربات مسدود شده در صورتی که شکایتی در این ارتباط دارید به ادمین بازی اطلاع دهید")
        return A2      

    else:            
        keyboard = [
            ['🏰مرکز شهر','🛖مرکز فرماندهی'],
            ['🕊مرکز ارتباطات',"🔘مشاهده دارایی"],
            ['⚙️تنظیمات']
            ]
        
        if dastresi == "admin":
            keyboard.append(["🔒admin"])

        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        photo = open(f'pics/base\{khandan}.png', 'rb')
        context.bot.send_photo(chat_id = cid , photo = photo , caption = f"🔻منوی موردنظر را انتخاب کنید",
        reply_markup=reply_markup)
        return A3




def tasmim(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2] 
            ghale = row[3]
            manba = row[5]
            eghlim = row[4]
            buildings = row[6]
            buildings2 = row[7]
            rohie = 100
            lord = 100
            troops = row[9]

    manba = eval(manba)
    buildings = eval(buildings)
    buildings2 = eval(buildings2)
    troops = eval(troops)



    if text == "🔒admin":
        keyboard = [
        ['backup','edit','hero'],['by location',"by house","by code"],["sabt","amar","gift"],["payam etehad","payam hamegani"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

        context.bot.send_message(chat_id = cid , text = f"""      
🔻در حال حاضر قصد ورود به کدام بخش را دارید؟     
        """,
        reply_markup=reply_markup)
        return G1

    elif text == "🕊مرکز ارتباطات":
        keyboard = [
        ['🕊توییتر','📄بیانیه'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
بخش های ارتباطی شما مانند ارسال بیانیه، اعلام جنگ و ارسال پیام های عمومی و شخصی در بستر های مختلف مانند توییتر در مرکز ارتباطات امکان پذیر است.

🔻در حال حاضر قصد ورود به کدام بخش را دارید؟     
        """,
        reply_markup=reply_markup)
        return B6

    elif text == "🛖مرکز فرماندهی":
        keyboard = [
        ['🏕|کمپ نظامی','⚔️|تربیت نیرو','⚜️|آکادمی'],
        ['🏟|میدان تمرین','⚡️|شوالیه','⛩|ورودی'],
        ['👁|برج دیدبانی','❤️|کمپ مجروحین'],
        ['🗺لشکرکشی','⛵️لشکرکشی','🐉لشکرکشی'],
        ["🐉|گودال اژدها",'⚔️|دستور حمله'],
        ["🔙بازگشت","🔎استعلام"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

        context.bot.send_message(chat_id = cid , text = f"""
🔸در مرکز نظامی شما به تحقیق و توسعه ارتش و تجهیزات خود می‌پردازید و ‌می‌توانید با تربیت سربازان و به کارگیری دیگر ساختمان های نظامی ارتش و قدرت خود را افزایش دهید.   
        """,
        reply_markup=reply_markup)
        return A3



    if text == "⚔️|تربیت نیرو":
        list = []
        for key in troops:
            list.append(key)
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\sakhtniro.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = """<b>🔳قصد تربیت یا ساخت کدام نیرو را دارید?</b>
        """,
        reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return C10

    elif text == "🐉|گودال اژدها":
        lvl = buildings["🐉|گودال اژدها"]

        if lvl>0:
            x = datetime.datetime.now()  
            time1 = x.strftime("%d%b") 
            time2 = x.strftime("%H:%M")

            sql = '''SELECT * From drag'''
            recs = c.execute(sql)
            for row in recs:
                if (row[0]) == khandan:
                    ghodrat = row[1] 
                    salamati = row[2]
                    bonie = row[3]
                    tozih = row[4]
                    name = row[5]

            txt = f"""
⌛️زمان دریافت گزارش:ا{time1} - {time2}ا

◄◅◄◅◄◅◄◅◄◅ 🐉{name}🐉 ►▻►▻►▻►▻►▻
🔥 قدرت اژدها: {ghodrat}
💊سلامتی: {salamati}
🪫 بنیه اژدها: {bonie}
◾️:{tozih}



        """
            aks = open(f'drag\{name}.jpg','rb')
            context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt ,parse_mode = ParseMode.HTML)
        else:
            update_information("temp1","🐉|گودال اژدها",cid)

            keyboard = [
            ['✅ارتقا'],
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid , text = f"""
🐉ابتدا این ساختمان را تاسیس کنید
    """,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
            return A4
    



    elif text == '🏕|کمپ نظامی':
        txt = """
🏕کمپ های نظامی:
در این بخش میتوانید ساختمان هایی که به واسطه آن نیروهای نظامی خود را ساخته و تربیت کرده ارتقا دهید

🔻قصد دارید کدام ساختمان زیر را ارتقا دهید؟"""
        keyboard = [
        ['🗡|کمپ پیاده','🏹|کمپ کماندار' , '🐎|کمپ سواره'],['☄️|کارگاه ادوات','🏕|کمپ ویژه',"⚓️|بندر"],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\camp.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt ,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4


    elif text == '❤️|کمپ مجروحین':
        update_information("temp1",text,cid)
        txt = """
❤️‍🩹کمپی سیار بوده که متشکل از اساتیدی جوان است که حلقه نقره (پرشکی و درمان) را از سیتادل کسب کرده اند، این کمپ همراه با ارتش شما حرکت می‌کند‌ و حین جنگ کار رسیدگی و درمان مجروحین آسیب دیده در جنگ را بر عهده می‌گیرند.
ظرفیت و فضای بهبود سربازان توسط این استادان در کمپ محدود بوده و فقط مقدار محدودی را ‌می‌توانند درمان کنند که با ارتقا می‌توان تعداد اساتید و تجهیزات را بیشتر کرد تا تعداد سربازان بیشتری درمان شوند
        """
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\❤️کمپ مجروحین.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt ,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4

    elif text == "👁|برج دیدبانی":
        update_information("temp1",text,cid)
        txt = """
🔻با تاسیس این ساختمان در صورتی که خاندانی در حال حرکت به سوی شما  باشد دیدبانان شما پیام اخطاری برای شما ارسال خواهند کرد.

❗️به صورت پیشفرض تمامی لشکرها میتوانند از  تمامی مسیرها عبور کنند با ارتقای این ساختمان در صورتی که ارتشی قصد حرکت از قلعه شما برای رسیدن به مقصد دیگری را داشته باشد دیدبانان شما زودتر از رسیدن ارتش ها به قلعه نیروهای شما را آگاه کرده و این فرصت برای شما ایجاد میشود که راه را بر روی ارتش در حال حرکت ببندید.

👁با ارتقا این ساختمان شما میتوانید نوع سربازانی را که به دهکده شما ارسال میشوند را تشخیص دهید.
        """
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\👁برج دیدبانی.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt ,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4

    elif text == "box":
        context.bot.send_message(chat_id = cid , text = f"""

🔻کد هدیه خود را وارد کنید
        """,)
        return G8


    elif text == "🏰مرکز شهر":
        keyboard = [
        ['🔝منابع','™️|بازارچه',],
        ['🏛|تالار بزرگ','🎋|درخت نیایش'],
        ["💰|خزانه",'🏦|ایرون بانک'],
        ['🔪|کشتارگاه','🍷|شراب‌ گیری'],
        ["🔙بازگشت"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

        context.bot.send_message(chat_id = cid , text = f"""
در این بخش به مدیریت و توسعه ساختمان ها و منابع اقتصادی خود می‌پردازید بخش های اصلی بازی در مرکز شهر قرار دارند.

🔻در حال حاضر قصد ورود به کدام بخش را دارید؟     
        """,
        reply_markup=reply_markup)
        return A3

    elif text == "🍷|شراب‌ گیری":
        lvl = buildings2["🍷|شراب گیری"]
        angor = manba["🍇|انگور"]
        if lvl>0:
            aks = open(f'view/aks\🍷شراب گیری.png', 'rb')
            context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"""          
🔻قصد دارید چه تعداد انگور را به شراب تبدیل کنید؟
🍇|ذخیره انگور: {angor}
""",parse_mode = ParseMode.HTML)
            return C9 
        else:
            text = f"⛔️برای استفاده از این ساختمان ابتدا از بخش منابع آن را ارتقا دهید"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2  

    
    elif text == "🔪|کشتارگاه":
        lvl = buildings2[ "🔪|کشتارگاه"]
        gav = manba["🐄|گاو"]
        if lvl>0:
            aks = open(f'view/aks\🔪کشتارگاه.png', 'rb')
            context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"""          
🔻قصد دارید چه تعداد از گاو های خود را ذبح کنید؟
🐄|گاو {gav}
""",parse_mode = ParseMode.HTML)
            return G4 
        else:
            text = f"⛔️برای استفاده از این ساختمان ابتدا از بخش منابع آن را ارتقا دهید"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2    
    
    


    elif text == '🎋|درخت نیایش':
        update_information("temp1",'🎋|درخت نیایش',cid)
        keyboard = [
        ['✅ارتقا درخت نیایش',],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\🎋درخت نیایش.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3

    elif text == '✅ارتقا درخت نیایش':
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
🧿درختانی کهن، باستانی و مقدس که حتی قبل از آمدن نخستین انسان ها وجود داشتند فرزندان جنگل چهره هایی روی این درختان حک کردند که گفته می‌شود خدای قدیم از طریق آن می‌تواند همه چیز را ببیند و شاهد وقایع مهم باشد 
این درختان که حافظه کهن جهان وستروس می‌باشند قابلیت هایی بی‌نظیر به شما می‌دهد تا از طریق لمس پوسته درخت به گذشته سفر کنید و اطلاعات مورد نیاز خود را از وقایع، اتفاقات و تغییرات در گذشته جست و جو کنید
با ساخت و ارتقای درخت نیایش می‌توانید به امکانات زیر دسترسی پیدا کنید
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4



    elif text == "⚜️|آکادمی":
        update_information("temp1","⚜️|آکادمی",cid)
        keyboard = [
        ['✅ارتقا آکادمی','🔍تحقیق'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\⚜️آکادمی.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3


    elif text == "✅ارتقا آکادمی":
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
⚜️در اکادمی میتوانید نیروهای خود را آموزش و ارتقا دهید. برای ساخت هر نیرو ابتدا باید آن را در اکادمی تحقیق کرده باشید.

🔸با تاسیس اکادمی تمام نیروها در سطح سبک برای تحقیق در دسترس شما خواهند بود 
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4




    elif text == "🔍تحقیق":
        list = []
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[3]
                academy = row[23]
                buildings = row[6]
        buildings = eval(buildings)
        academy = eval(academy)
        buildings = buildings["⚜️|آکادمی"]

        for key in academy:
            lvl = academy[key]
            print(buildings)
            if key == "💈|دژکوب":
                if buildings>1 and lvl<1:
                    list.append(key)
            elif key == '☄️|منجنیق' :
                if buildings>2 and lvl<1:
                    list.append(key)
            elif key == "🎯|بالیستا" :
                if buildings>3 and lvl<1:
                    list.append(key)
            elif key == "🔱نیرو ویژه اقلیم":
                if buildings>4 and lvl<1:
                    list.append(key)
            else:
                if lvl<buildings:
                    list.append(key)
        tsh = ""
        for key in academy:
            tsh = tsh + f"{key}:{academy[key]}\n"
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""<b>🔳قصد دارید از کدام یک از نیروهای زیر را تحقیق کنید؟</b>


🔍نیروهای تحقیق شده:
<code>{tsh}</code>
        """,
        reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return C8

    elif text == '⚔️|دستور حمله':
        list = []
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[3]

        list.append(khandan)
        sql = '''SELECT * From lashkarkeshi WHERE cid ="{}" AND vaziat = "{}"'''.format(cid,"💢مستقر")
        recs = c.execute(sql)
        for row in recs:
            mabda = row[4]
            list.append(mabda)
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = """<b>🔳قصد دارید با کدام یک از ارتش های زیر دستور حمله را صادر کنید؟</b>

_ ⚠️نیروهای شما در حال حاضر در قلعه های زیر مستقر میباشند_

        """,
        reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return C12

    elif text == "🔎استعلام":
        list = []
        sql = '''SELECT * From lashkarkeshi WHERE mabda ="{}" AND vaziat = "{}"'''.format(ghale,"💢مستقر")
        recs = c.execute(sql)
        for row in recs:
            mos = row[1]
            list.append(mos)

        if len(list)<1:
            txt = "🛡در حال حاضر هیچ ارتشی درقلعه شما مستقر نیست"
        else:
            l = ""
            for n in list:
                l = l + f"{n}\n"
            txt = f"⚠️در حال حاضر لشکریانی متعلق به خاندان های {l} در قلعه شما حضور دارند"
        context.bot.send_message(chat_id=cid ,text = txt,parse_mode = ParseMode.HTML)
            
    elif text == "🗺لشکرکشی" or text=="⛵️لشکرکشی" or text == "🐉لشکرکشی":
        global noelashkar
        noelashkar[cid] = text
        list = []
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[3]

        list.append(khandan)
        sql = '''SELECT * From lashkarkeshi WHERE cid ="{}" AND vaziat = "{}"'''.format(cid,"💢مستقر")
        recs = c.execute(sql)
        for row in recs:
            mabda = row[4]
            list.append(mabda)
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = """<b>🔳قصد دارید از کدام یک از قلعه های زیر لشکرکشی خود را آغاز کنید؟</b>

_ ⚠️نیروهای شما در حال حاضر در قلعه های زیر مستقر میباشند_

        """,
        reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A12

    elif text =="🏟|میدان تمرین":
        update_information("temp1","🏟|میدان تمرین",cid)
        keyboard = [
        ['✅ارتقا میدان تمرین','🏟امتیازها'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\🏟میدان تمرین.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3

    elif text == "🏟امتیازها":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                tamrin = row[22]
                buildings = row[6]
        buildings = eval(buildings)
        tamrin = eval(tamrin)
        buildings = buildings["🏟|میدان تمرین"]
        hojom = tamrin["hojom"]
        defpiyade = tamrin["defpiyade"]
        defsavare = tamrin["defsavare"]
        khali  = buildings - hojom - defpiyade -defsavare
        keyboard = [
        ['⚔️امتیاز هجومی'],['🛡دفاع در مقابل پیاده نظام','🐎دفاع در مقابل سواره نظام']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
🔲امتیاز های مصرف نشده: {khali}
⚔️امتیاز هجومی: {hojom}
🛡امتیاز دفاع در مقابل پیاده نظام: {defpiyade}
🐎امتیاز دفاع در مقابل سواره نظام: {defsavare}

🔸دقت داشته باشید که بعد از انتخاب هر بخش کل امتیازات مصرف نشده به آن بخش تعلق خواهد گرفت بنابراین پیشنهاد میشود پس از هر سطح ارتقا امتیاز آن را مصرف کنید
🔻قصد دارید امتیازهای مصرف نشده را به کدام بخش اختصاص دهید؟
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3

    elif text == "⚔️امتیاز هجومی":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                tamrin = row[22]
                buildings = row[6]
        buildings = eval(buildings)
        tamrin = eval(tamrin)
        buildings = buildings["🏟|میدان تمرین"]
        hojom = tamrin["hojom"]
        defpiyade = tamrin["defpiyade"]
        defsavare = tamrin["defsavare"]
        khali  = buildings - hojom - defpiyade - defsavare
        hojom = hojom + khali
        tamrin["hojom"]  = hojom
        update_information("tamrin",tamrin,cid)
        text = f"✅امتیاز هجومی شما به {hojom} درصد افزایش پیدا کرد"
        keyboard = [['🔙بازگشت به منوی اصلی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2  

    elif text == "🛡دفاع در مقابل پیاده نظام":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                tamrin = row[22]
                buildings = row[6]
        buildings = eval(buildings)
        tamrin = eval(tamrin)
        buildings = buildings["🏟|میدان تمرین"]
        hojom = tamrin["hojom"]
        defpiyade = tamrin["defpiyade"]
        defsavare = tamrin["defsavare"]
        khali  = buildings - hojom - defpiyade - defsavare
        defpiyade = defpiyade + khali
        tamrin["defpiyade"]  = defpiyade
        update_information("tamrin",tamrin,cid)
        text = f"✅امتیاز دفاع در مقابل پیاده نظام شما به {defpiyade} درصد افزایش پیدا کرد"
        keyboard = [['🔙بازگشت به منوی اصلی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2 

    elif text == "🐎دفاع در مقابل سواره نظام":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                tamrin = row[22]
                buildings = row[6]
        buildings = eval(buildings)
        tamrin = eval(tamrin)
        buildings = buildings["🏟|میدان تمرین"]
        hojom = tamrin["hojom"]
        defpiyade = tamrin["defpiyade"]
        defsavare = tamrin["defsavare"]
        khali  = buildings - hojom - defpiyade - defsavare
        defsavare = defsavare + khali
        tamrin["defsavare"]  = defsavare
        update_information("tamrin",tamrin,cid)
        text = f"✅امتیاز دفاع در مقابل سواره نظام شما به {defsavare} درصد افزایش پیدا کرد"
        keyboard = [['🔙بازگشت به منوی اصلی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2 

    elif text == "✅ارتقا میدان تمرین":
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
🏟میدان تمرین محلی برای تمرین بیشتر نیروهای شماست در این مکان میتوانید تمرین های متفاوتی انجام داده تا قدرت نیروی های خود را در هر بخش بهبود دهید.
با ارتقا هر سطح میدان تمرین میتوانید یکی از موارد قدرت مبارزه،قدرت دفاع در مقابل پیاده نظام یا قدرت دفاع در مقابل سواره نظام را یک درصد بهبود دهید

❗️محدودیت ارتقا این ساختمان ۱۰سطح میباشد
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4

    elif text == "⛩|ورودی":
        update_information("temp1",text,cid)
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\⛩ورودی.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"""
⛩ورودی شهر میتواند از قلمرو شما حفاظت کند. دیوار ها و ورودی قلعه اولین و یکی از مهمترین خطوط دفاعی شما در مقابل دشمن هستند با ارتقا دیوار ها و ورودی های قلعه نفوذ به قلعه شما سخت تر خواهد شد برای نابود کردن دیوار ها و ورودی های قلعه نیاز به ابزارالات جنگی سنگین میباشد.

🔸هر لول ارتقا دیوار 10 درصد قدرت دفاعی نیروهای شما را افزایش میدهد(نهایتا ۳۰درصد)

❗️شما میتوانید از ویژگی های واقعی قلعه های خود در سناریوهای نبرد خود استفاده کنید. برای استفاده از این ویژگی مستندات خود را از منابع قابل اعتماد دنیای نغمه ارائه کنید

""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4



    elif text == "🏛|تالار بزرگ":
        keyboard = [
        ['✔️تاسیس اتحاد','🔗دعوت به اتحاد'],
        ['❌خروج از اتحاد','🚫اخراج از اتحاد'],
        ['🏆پروفایل اتحاد','📦انبار بزرگ'],
        ['🔝ارتقا تالار بزرگ',"🔙بازگشت"]

        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\🏛تالار بزرگ.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3


    elif text == "📦انبار بزرگ":
        keyboard = [
            ["➕نگهبان(انبار1)","➕نگهبان(انبار2)","➕نگهبان(انبار3)"],
            ['👁‍🗨مشاهده انبارها','🔙بازگشت'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\📦انبار بزرگ.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3
    elif text == "➕نگهبان(انبار2)":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                troops = row[9]      
                etehad = row[19]
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if row[0] == etehad:
                members = row[1]
                leader = row[3]
                an1 = row[8]
        an1 = eval(an1)
        troops =eval(troops)
        moh1 = an1[2]
        mohp = troops["🛡|نگهبان"]
        newmoh1 = moh1+mohp
        troops["🛡|نگهبان"] = 0
        an1[2]=newmoh1
        update_information("troops",troops,cid)
        print(an1)
        c.execute('''UPDATE etehad SET an2 = "{}" WHERE name = "{}" '''.format(an1,etehad))
        conn.commit() 
        keyboard = keyboardM
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = f"✅تعداد {mohp} نگبهان به انبار شماره 2 ارسال شد",reply_markup=reply_markup)    
        
        
        
    elif text == "➕نگهبان(انبار3)":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                troops = row[9]      
                etehad = row[19]
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if row[0] == etehad:
                members = row[1]
                leader = row[3]
                an1 = row[9]
        an1 = eval(an1)
        troops =eval(troops)
        moh1 = an1[2]
        mohp = troops["🛡|نگهبان"]
        newmoh1 = moh1+mohp
        troops["🛡|نگهبان"] = 0
        an1[2]=newmoh1
        update_information("troops",troops,cid)
        print(an1)
        c.execute('''UPDATE etehad SET an3 = "{}" WHERE name = "{}" '''.format(an1,etehad))
        conn.commit() 
        keyboard = keyboardM
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = f"✅تعداد {mohp} نگبهان به انبار شماره 3 ارسال شد",reply_markup=reply_markup)


    elif text == "➕نگهبان(انبار1)":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                troops = row[9]      
                etehad = row[19]
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if row[0] == etehad:
                members = row[1]
                leader = row[3]
                an1 = row[7]
        an1 = eval(an1)
        troops =eval(troops)
        moh1 = an1[2]
        mohp = troops["🛡|نگهبان"]
        newmoh1 = moh1+mohp
        troops["🛡|نگهبان"] = 0
        an1[2]=newmoh1
        update_information("troops",troops,cid)
        print(an1)
        c.execute('''UPDATE etehad SET an1 = "{}" WHERE name = "{}" '''.format(an1,etehad))
        conn.commit() 
        keyboard = keyboardM
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = f"✅تعداد {mohp} نگبهان به انبار شماره 1 ارسال شد",reply_markup=reply_markup)


    elif text == '👁‍🗨مشاهده انبارها':
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                etehad = row[19]

        manba_list = {}
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if row[0] == etehad:
                members = row[1]
                leader = row[3]
                an1 = row[7]
                an2 = row[8]
                an3 = row[9]

        members = eval(members)

        for memb in members:
            sql = '''SELECT * From Information'''
            recs = c.execute(sql)
            for row in recs:
                if (row[2]) == memb:
                    idd = row[1]
                    manba = row[5]      
            manba = eval(manba)
            manba_list = sum_dict(manba_list,manba)


        txt_manba = ""
        for key in manba_list:
            num = manba_list[key]
            if num>0:
                txt_manba = txt_manba + f"{key}:{num}\n"   


            
        an1 = eval(an1)
        an2 = eval(an2)
        an3 = eval(an3)

        zar1 = an1[1]
        moh1 = an1[2]
        toz1 = an1[3]

        zar2 = an2[1]
        moh2 = an2[2]
        toz2 = an2[3]

        zar3 = an3[1]
        moh3 = an3[2]
        toz3 = an3[3]


        a = 0
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == khandan:
                a = 1

        if a ==1:
            loc3 = an3[0]
            loc2 = an2[0]
            loc1 = an1[0]
        else:
            loc3 = "❗️نامشخص"
            loc2 = "❗️نامشخص"
            loc1 = "❗️نامشخص"

        x = datetime.datetime.now()  
        time1 = x.strftime("%d%b") 
        time2 = x.strftime("%H:%M")

        txt = f"""
⌛️زمان دریافت گزارش:ا{time1} - {time2}ا

◄◅◄◅◄◅◄◅◄◅ 📦انبار 1📦 ►▻►▻►▻►▻►▻
🗺مکان:{loc1}
📥ظرفیت:{zar1}
🛡نگهبانان:{moh1}
📜توضیحات:{toz1}
◄◅◄◅◄◅◄◅◄◅ 📦انبار 2📦 ►▻►▻►▻►▻►▻
🗺مکان:{loc2}
📥ظرفیت:{zar2}
🛡نگهبانان:{moh2}
📜توضیحات:{toz2}
◄◅◄◅◄◅◄◅◄◅ 📦انبار 3📦 ►▻►▻►▻►▻►▻
🗺مکان:{loc3}
📥ظرفیت:{zar3}
🛡نگهبانان:{moh3}
📜توضیحات:{toz3}

◄◅◄◅◄◅◄◅ 📦دارایی اتحاد📦 ►▻►▻►▻►▻
{txt_manba}

        """
        aks = open(f'pics/etehad\{etehad}.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt,parse_mode = ParseMode.HTML)
        

    elif text == "🏆پروفایل اتحاد":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                etehad = row[19]


        niro_list = {}
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if row[0] == etehad:
                members = row[1]
                leader = row[3]
                win = row[4]
                lose = row[5]
                achievement = row[6]



        members = eval(members)
        members_list  = ""

        for memb in members:
            sql = '''SELECT * From Information'''
            recs = c.execute(sql)
            for row in recs:
                if (row[2]) == memb:
                    idd = row[1]
                    troops = row[9]      
            troops = eval(troops)
            niro_list = sum_dict(niro_list,troops)
            sql = '''SELECT * From lashkarkeshi'''
            recs = c.execute(sql)
            for row in recs:
                if (row[1]) == memb:
                    troops = eval(row[2])
                    niro_list = sum_dict(niro_list,troops)

            members_list = members_list + f"{memb} |ا| ({idd})\n"

        txt_niro = ""
        for key in niro_list:
            num = niro_list[key]
            if num>0:
                txt_niro = txt_niro + f"{key}:{num}\n"      


        aks = open(f'pics/etehad\{etehad}.png', 'rb')

        try:
            darsad = int(win/(win+lose)*100)
        except:
            darsad = 0

        x = datetime.datetime.now()  
        time1 = x.strftime("%d%b") 
        time2 = x.strftime("%H:%M")
        
        txt = f"""
<b>
🔰نام اتحاد: {etehad}
💂‍♂️رییس اتحاد: {leader} 
📯درصد پیروزی در نبردها: {win}/{win+lose} ({darsad}%)
🏆افتخارات: {achievement}
⌛️زمان دریافت گزارش:ا{time1} - {time2}ا

</b>

◄◅◄◅◄◅◄◅◄◅ لیست نیروها ►▻►▻►▻►▻►▻
{txt_niro}
        """
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt,parse_mode = ParseMode.HTML)

    elif text == "❌خروج از اتحاد":
        text = f"آیا مطمئن هستید که قصد دارید اتحاد خود را ترک کنید؟"
        keyboard = [['⛔️خروج'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A3

    elif text == "🚫اخراج از اتحاد":
        a = 0
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == khandan:
                a = 1

        if a != 1:
            text = f"⛔️تنها موسس یک اتحاد میتواند یک عضو را اخراج کند"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2  

        context.bot.send_message(chat_id = cid , text = f"""
<b>🏆نام خاندانی را که قصد اخراج وی از اتحاد را دارید ارسال کنید</b>
❗️به املای درست نام خاندان دقت کنید(حساس به حرف بزرگ و کوچک)
        """,reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.HTML) 
        return C3

    elif text == "⛔️خروج":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                etehad = row[19]

        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == etehad:
                members = row[1]
                eid = row[2]

        members = eval(members)
        members.remove(khandan)
        c.execute('''UPDATE etehad SET members = "{}" WHERE name = "{}" '''.format(members,etehad))
        conn.commit() 
        update_information("etehad","a",cid)   
        context.bot.send_message(chat_id = eid ,text = f"لرد خاندان {khandan} از اتحاد خارج شد" ,)
        keyboard = [['🔙بازگشت به منوی اصلی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = "✅با موفقیت از اتحاد خارج شدید" ,reply_markup=reply_markup)
        return A2 


        
    elif text == "🔗دعوت به اتحاد":

        a=0

        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == khandan:
                a = 1

        if a != 1:
            text = f"⛔️تنها موسس یک اتحاد میتواند یک عضو را دعوت کند"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2  

        context.bot.send_message(chat_id = cid , text = f"""
<b>🏆نام خاندانی را که قصد دعوت وی به اتحاد را دارید ارسال کنید</b>
❗️به املای درست نام خاندان دقت کنید(حساس به حرف بزرگ و کوچک)
        """,reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.HTML) 
        return C2

        
    elif text == "🔝ارتقا تالار بزرگ":
        update_information("temp1","🏛|تالار بزرگ",cid)
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
🏛تالار بزرگ محلی برای گفت‌ و گو با متحدان شماست در صورت تاسیس این ساختمان شما میتوانید در یکی از اتحاد های موجود در بازی عضو شوید.

🔸️در صورت ارتقا این ساختمان میتونید یک اتحاد تاسیس کنید.
🔸️هر اتحاد میتواند نهایتا ۱۵ عضو داشته باشد.

""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4

    elif text == "✔️تاسیس اتحاد":

        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                buildings = row[6]
        buildings = eval(buildings)
        shora = buildings["🏛|تالار بزرگ"]

        if shora<2:
            text = f"⛔️برای تاسیس اتحاد ابتدا تالار بزرگ خود را ارتقا دهید"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2  

        context.bot.send_message(chat_id = cid , text = f"""
<b>🏆تشکیل یا عضویت در یک اتحاد یکی از مهمترین اقدام شما در طول بازی میباشد.</b>
<code>🔸هر اتحاد میتواند نهایتا 15 عضو داشته باشد تجارت با اعضای اتحاد ظرفیت کمتری از محدودیت تجارت را اشغال میکند همچنین لشکرکشی از قلعه های اعضای اتحاد نیازمند دریافت اجازه نمیباشد و اعضای اتحاد نمیتوانند به شما حمله کنند.
🛡در جنگ های متحد تنها اعضای یک اتحاد میتوانند در یک جبهه بجنگند</code>

<b>⚜️برای تشکیل یک اتحاد ابتدا یک نام برای اتحاد خود مشخص کنید:</b>

<i>❗️در انتخاب نام اتحاد خود دقت داشته باشید زیرا قابل تغییر نیست
‼️در صورت استفاده از نام های بی ربط و توهین آمیز ادمین بازی میتواند اتحاد شما را منحل کند</i>
        """,reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.HTML) 
        return B11

    elif text == "🏦|ایرون بانک":
        update_information("temp1",text,cid)
        keyboard = [
        ['💱دریافت وام','🔝ارتقا ایرون بانک'],['💯پرداخت وام']
        ]    
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\🏦ایرون بانک.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)

    elif text == "🔝ارتقا ایرون بانک":
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
🏦با تاسیس این ساختمان نمایندگان بانک اهنین در مقر خاندان شما حضور خواهند داشت و شما قادر  به دریافت وام از آن ها خواهید بود.

🔹️حداکثر مقدار وام دریافتی برابر با ۱۰درصد ذخیره سکه شما به ازای هر سطح از اسن ساختمان میباشد همچنین باز پرداخت وام به ازای هر سطح ارتقا ۱هفته افزایش خواهد یافت. 

🔸️ شما میباست معادل ۱۲درصد از مبلغ وام خود به بانک آهنین را به عنوان سود به این بانک پرداخت نمایید""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4
    elif text == "💯پرداخت وام":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                manba = row[5]
                buildings = row[6]
                list = row[21]
        manba = eval(manba)
        list = eval(list)
        seke = manba["💰|سکه"]
        bedehi = list[0]
        hafte = list[1]
        context.bot.send_message(chat_id=cid ,text = f"""
〰️شما در حال حاضر {bedehi} سکه به بانک آهنین بدهکار میباشید، موجودی خزانه شما برابر با {seke} سکه میباشد و تا {hafte} هفته دیگر مهلت داشته تا بدهی خود را پرداخت کنید

🔻قصد دارید چه مقدار از بدهی خود را پرداخت کنید
        """,parse_mode = ParseMode.MARKDOWN )
        return C7  

    elif text == "💱دریافت وام":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                manba = row[5]
                buildings = row[6]
                list = row[21]

        if list != "[]":
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"❌برای دریافت وام جدید ابتدا باید بدهی قبلی خود به بانک آهنین را پرداخت کنید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2    
        buildings = eval(buildings)
        manba = eval(manba)
        seke = manba["💰|سکه"]
        buildings = buildings["🏦|ایرون بانک"]
        vam = (seke*buildings/10)
        context.bot.send_message(chat_id = cid , text = f"""
💰ذخیره سکه شما:{seke}
🏦سطح ایرون بانک:{buildings}
💸حداکثر مقدار وام دریافتی: {vam}

🔻قصد دارید چند سکه از بانک آهنین وام دریافت کنید؟
        """,reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN) 
        return C6


    elif text == "💰|خزانه":
        update_information("temp1",text,cid)
        keyboard = [
        ['💱سرمایه گذاری','🔝ارتقا خرانه'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\💰خزانه.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3

    elif text == "💱سرمایه گذاری":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                manba = row[5]
                buildings = row[6]
                list = row[20]
        if list != "[]":
            list = eval(list)
            hafte = list[0]
            meghdar = list[1]
            hafte_mande = list[2]
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"💸شما در حال حاضر {meghdar} سکه را برای مدت {hafte} هفته سرمایه گذاری کرده اید مدت زمان باقی مانده سرمایه گذاری شما {hafte_mande} هفته میباشد!" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2

        buildings = eval(buildings)
        manba = eval(manba)
        seke = manba["💰|سکه"]
        khazane_lvl = buildings["💰|خزانه"]
        context.bot.send_message(chat_id = cid , text = f"""🔻شما میتوانید مقداری از دارایی خود را توسط خزانه خود سرمایه گذاری کنید.
دارایی سرمایه گذاری شده تا پایان مهلت سرمایه گذاری قابل استفاده نمیباشد.
میزان سود سرمایه گذاری برابر با<b> (سطح خزانه × تعداد هفته سرمایه گذاری) درصد سرمایه اولیه</b> شماست سود این سرمایه گذاری در پایان دوره به شما تعلق خواهد گرفت
❗️حداکثر زمان سرمایه گذاری ۴هفته میباشد
<b>
💰ذخیره سکه شما: {seke}
💰سطح خزانه: {khazane_lvl}

💲قصد دارید چه مقدار از سکه های خود را سرمایه گذاری کنید؟
</b>

""",reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.HTML) 
        return C4

    elif text == "🔝ارتقا خرانه":
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
💰خزانه محل نگهداری و ضرب سکه های خاندان شماست با ارتقا خزانه میتوانید درآمد خاندان خود را افزایش دهید.

🔸️سرمایه گذاری:
شما میتوانید مقداری از دارایی خود را توسط خزانه خود سرمایه گذاری کنید.
دارایی سرمایه گذاری شده تا پایان مهلت سرمایه گذاری قابل استفاده نمیباشد.""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4


    elif text == '⚡️|شوالیه':
        keyboard = [
        ['✅ارتقا اقامتگاه','🔰اطلاعات شوالیه'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\⚡️اقامتگاه شوالیه.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3



    elif text == '🔰اطلاعات شوالیه':
        hero_lvl = buildings['⚡️|اقامتگاه شوالیه']
        print(khandan)
        sql = '''SELECT * From hero'''
        recs = c.execute(sql)
        for row in recs:
            print(row[1])
            if row[1] == khandan:
                print("ok")
                name = row[0]
                xp = row[2]
                items = row[3]
                zereh = row[4]
                rast = row[5]
                chap = row[6]
                kolah = row[7]
                kafsh = row[8]
                hp = row[9]
                def_b = row[10]
                att_b = row[11]
                att_p = row[12]

        items = eval(items)
        #now = def_b + att_b + att_p
        keyboard = [[InlineKeyboardButton("➕⚡️" ,callback_data=f"hero*att_p*1*1"),InlineKeyboardButton("➕⚔️" ,callback_data=f"hero*att_b*1*1"),InlineKeyboardButton("➕🛡" ,callback_data=f"hero*def_b*1*1")],
                    [InlineKeyboardButton("🔁تغییر تجهیزات" ,callback_data=f"hero*change*1*1")]
        ]   
        reply_markup = InlineKeyboardMarkup(keyboard)

        it_l = ""
        for item in items:
            it_l = it_l+f"{item}\n"
        txt = f"""
◄◅◄◅◄◅◄◅◄◅اطلاعات کلی►▻►▻►▻►▻►▻
🏷نام: {name}
🗡سطح:{hero_lvl}
💯تجربه: {xp}
💊سلامتی: {hp}
◄◅◄◅◄◅◄◅◄◅آیتم های فعال ►▻►▻►▻►▻►▻
🪖کلاه: {kolah}
🛡زره: {zereh}
👈دست چپ: {chap}
👉دست راست: {rast}
🥾کفش: {kafsh}
◄◅◄◅◄◅◄◅◄◅ امتیازات شوالیه ►▻►▻►▻►▻►▻
⚡️قدرت مبارزه: {att_p}
⚔️امتیاز هجومی: {att_b}
🛡امتیاز دفاعی: {def_b}
◄◅◄◅◄◅◄◅◄◅ آیتم ها ►▻►▻►▻►▻►▻
{it_l}
        """
        try:
            aks = open(f'hero\{name}.png','rb')
            context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        except:
            context.bot.send_message(chat_id = cid , text = txt,reply_markup=reply_markup,parse_mode = ParseMode.HTML)

    elif text == '✅ارتقا اقامتگاه':
        update_information("temp1",'⚡️|اقامتگاه شوالیه',cid)
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
⚡️اقامتگاه شوالیه:
شوالیه مهم ترین نیروی شما در طول بازی میباشد
با تاسیس اقامتگاه شوالیه میتوانید شوالیه خود را کنترل کنید.

🔼 امتیازات: 
شوالیه دارای ۳امتیاز ویژه میباشد(قدت،امتیاز هجومی ، امتیاز دفاعی) در ازای هر سطح جدیدی که شوالیه شما به ان دست پیدا کند میتوانید یکی از این ویژگی ها را ارتقا دهید.

""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4
    


    elif text == "™️|بازارچه":
        keyboard = [
        ['📦تجارت','🔝ارتقا بازارچه'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'view/aks\™️بازارچه.png', 'rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3

    elif text == "🔝ارتقا بازارچه":
        update_information("temp1","™️|بازارچه",cid)
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
™️بازارچه محلی برای انجام تجارت های شماست.
با ارتقا این ساختمان میتوانید ظرفیت تجارت هفتگی خود را افزایش دهید.

🔸️تمام تجارت های بازی باید با ارزش منطقی انجام شوند. در صورت مشاهده هرگونه تجارت غیرمنطقی تجارت لغو و منابع تجارت شده از هر دو طرف کسر خواهد شد.

❗️تجارت با اعضای اتحاد ۵۰درصد ظرفیت کمتری از محدودیت تجارت هفتگی شما را اشغال میکند.""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4
    elif text == "📦تجارت":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                vorodi = row[12] 
                khoroji = row[13]

        list = []
        for key in manba:
            key = f"{key}"
            list.append(key)
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
<b>🔳قصد دارید که کدام منبع را برای متحد خود ارسال کنید؟ </b>

📥ظرفیت ورودی باقی مانده : {vorodi}
📤ظرفیت خروجی باقی مانده: {khoroji}

_ ⚠️توجه داشته باشید حتما اعداد را به صورت لاتین وارد کنید در غیر این صورت تجارت شما تایید نمیگردد _

        """,
        reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A6

    elif text == "🔝منابع":
        list = []
        for key in buildings2:
            key = f"{key}"
            list.append(key)

        list.append("🔙بازگشت")
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        new_list.append(["🏰قلعه"])
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"🔻گزینه موردنظر را انتخاب کنید",
        reply_markup=reply_markup)
        return A4
            
    elif text == "🔘مشاهده دارایی":
        keyboard = [
        ['⛲️دارایی اقتصادی','⚔️دارایی نظامی'],
        ["🔙بازگشت"]
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3

    elif text == "⚔️دارایی نظامی":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                ghale = row[3]
                eghlim = row[4]
                buildings = row[6]
                buildings2 = row[7]
                manba = row[5]
                troops = row[9]
                etehad = row[19]       
        manba = eval(manba)
        buildings = eval(buildings)
        buildings2 = eval(buildings2)
        troops = eval(troops)
        x = datetime.datetime.now()  
        time1 = x.strftime("%d%b") 
        time2 = x.strftime("%H:%M")


        sum = {}
        sql = '''SELECT * From lashkarkeshi'''
        recs = c.execute(sql)
        for row in recs:
            if (row[1]) == khandan:
                troop = eval(row[2])
                sum = sum_dict(sum,troop)

        if etehad == "a":
            etehad = "بدون اتحاد"


        buildingslist = ""
        for key in buildings:
            if key == '🏕|کمپ ویژه' or key == '🏟|میدان تمرین'or key == '🐉|گودال اژدها':
                a = f"{key}:{buildings[key]}"
                buildingslist = buildingslist + f"\n{a}"
            elif key == '⚓️|بندر' or key == '⛩|ورودی' or key =='⚜️|آکادمی' or key == '👁|برج دیدبانی' or key == '⚡️|اقامتگاه شوالیه':
                a = f"{key}:{buildings[key]}"
                buildingslist = buildingslist + f"\n{a}"
            elif key == '🗡|کمپ پیاده' or key == '🏹|کمپ کماندار' or key =='☄️|کارگاه ادوات' or key == "🐎|کمپ سواره":
                a = f"{key}:{buildings[key]}"
                buildingslist = buildingslist + f"\n{a}"
            else:
                pass
        
        troopslist = ""
        for key in troops:
            try:
                n2 = sum[key]
            except:
                n2 = 0
            a = f"{key}:{troops[key]} +「{n2}」"
            troopslist = troopslist + f"\n{a}"

        ghalelvl = buildings["🏰قلعه"]
            
        listi = f"""
<b>💢خاندان: {khandan}
🏰قلعه: {ghale}
🔰اقلیم: {eghlim}
🔰اتحاد: {etehad}
🏰قلعه: {ghalelvl}
ا- - - - - - - - - - - - - - - - - - -ا</b>
⌛️زمان دریافت گزارش:ا{time1} - {time2}ا


<b>~ ~ ~「 ساختمان ها 」~ ~ ~</b>
{buildingslist}

<b>~ ~ ~「 نیرو ها 」~ ~ ~</b>
{troopslist}


        """
        context.bot.send_message(chat_id=cid , text = listi,parse_mode = ParseMode.HTML)

    elif text == "⛲️دارایی اقتصادی":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == cid:
                khandan = row[2]
                ghale = row[3]
                eghlim = row[4]
                manba = row[5]
                buildings = row[6]
                buildings2 = row[7]
                etehad = row[19]
        
        manba = eval(manba)
        buildings = eval(buildings)
        buildings2 = eval(buildings2)

        x = datetime.datetime.now()  
        time1 = x.strftime("%d%b") 
        time2 = x.strftime("%H:%M")

        if etehad == "a":
            etehad = "بدون اتحاد"
        buildingslist2 = ""
        for key in buildings2:
            a = f"{key}:{buildings2[key]}"
            buildingslist2 = buildingslist2 + f"\n{a}"

        buildingslist = ""
        for key in buildings:
            if key == '🏰قلعه' or key == '🏕|کمپ ویژه' or key == '🏟|میدان تمرین'or key == '🐉|گودال اژدها':
                pass
            elif key == '⚓️|بندر' or key == '⛩|ورودی' or key =='⚜️|آکادمی' or key == '👁|برج دیدبانی' or key == '⚡️|اقامتگاه شوالیه':
                pass
            elif key == '🗡|کمپ پیاده' or key == '🏹|کمپ کماندار' or key =='☄️|کارگاه ادوات' or key == '🐎|کمپ سواره':
                pass
            else:
                a = f"{key}:{buildings[key]}"
                buildingslist = buildingslist + f"\n{a}"

        manbalist = ""
        for key in manba:
            a = f"{key}:{manba[key]}"
            manbalist = manbalist + f"\n{a}"

        troopslist = ""
        for key in troops:
            a = f"{key}:{troops[key]}"
            troopslist = troopslist + f"\n{a}"

        ghalelvl = buildings["🏰قلعه"]

        listi = f"""
<b>💢خاندان: {khandan}
🏰قلعه: {ghale}
🔰اقلیم: {eghlim}
🔰اتحاد: {etehad}
ا- - - - - - - - - - - - - - - - - - -ا</b>
⌛️زمان دریافت گزارش:ا{time1} - {time2}ا

~ ~ ~「 ساختمان ها 」~ ~ ~
<code>{buildingslist}</code>

<b>~ ~ ~「 تولیدی‌ ها 」~ ~ ~</b>
<code>{buildingslist2}</code>

<b>~ ~ ~「 لیست منابع 」~ ~ ~</b>
<code>{manbalist}</code>
        """
        context.bot.send_message(chat_id=cid , text = listi,parse_mode = ParseMode.HTML)

    else:
        keyboard = [
            ['🏰مرکز شهر','🛖مرکز فرماندهی'],
            ['🕊مرکز ارتباطات',"🔘مشاهده دارایی"],
            ['⚙️تنظیمات']
            ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        photo = open(f'pics/base\{khandan}.png', 'rb')
        context.bot.send_photo(chat_id = cid , photo = photo , caption = f"🔻منوی موردنظر را انتخاب کنید",
        reply_markup=reply_markup)
        return A3





def go4(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text
    text = int(text) 
    if text<0:
        text = 0
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
            buildings = row[7]
    
    buildings = eval(buildings)
    manba = eval(manba)
    dabaghi = buildings["👝|دباغی"]
    gav = manba["🐄|گاو"]
    gosht = manba["🥩|گوشت"]
    charm = manba['🏉|چرم']
    gav = gav - text
    gosht = gosht + text*20
    if dabaghi>0:
        charm=charm+text*3
    if gosht<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌شما گاو کافی ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    manba["🐄|گاو"] = gav
    manba["🥩|گوشت"] = gosht
    manba['🏉|چرم'] = charm

    update_information("manba",manba,cid)
    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"""
✅تعداد {text} گاو با موفقیت به گوشت و چرم تبدیل شدند
    """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2





def co9(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text
    text = int(text) 
    if text<0:
        text = 0
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
    manba = eval(manba)
    sharab = manba["🍷|شراب"]
    angor = manba['🍇|انگور']
    angor = angor - text
    sharab = sharab + text
    if angor<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌شما انگور کافی ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    manba["🍷|شراب"] = sharab
    manba['🍇|انگور'] = angor
    update_information("manba",manba,cid)
    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"""
✅تعداد {text} انگور با موفقیت به شراب تبدیل شدند
    """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2







def sakhtniro(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
            buildings = row[6]
    buildings = eval(buildings)
    update_information("temp1",text,cid)

    a = 0 
    sql = '''SELECT * From niro'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == text:
            a = 1
    if a == 0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌امکان ساخت این نیرو وجود ندارد" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2  

    context.bot.send_message(chat_id=cid ,text = f"🟨قصد دارید چه تعداد {text} بسازید؟" ,parse_mode = ParseMode.MARKDOWN )
    return C11   

def sakht_niro2(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    text = int(text)
    if text<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2  

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            manba = eval(row[5])
            buildings = eval(row[6])
            temp1 = row[10]
            troops = eval(row[9])
            academy = eval(row[23])

    sql = '''SELECT * From niro'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == temp1:
            hazine = eval(row[1])
            pish = eval(row[2])

    for key in pish:
        e = pish[key]
        ee = buildings[key]
        if e>ee:
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"❌پیشنیاز کافی برای ساخت این نیرو ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2  

    for key in hazine:
        h = hazine[key]
        manbamasrafi = manba[key]
        newmmasrafi = manbamasrafi - h*text
        if newmmasrafi<0:
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"❌منبع {key} کافی برای ساخت این نیرو ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2  
        manba[key] = newmmasrafi

    noniro = troops[temp1]
    newniro = noniro + text
    troops[temp1] = newniro
    update_information("manba",manba,cid)
    update_information("troops",troops,cid)
    text = f"✅ساخت {text} {temp1} با موفقیت انجام شد"
    keyboard = [['🔙بازگشت به منوی اصلی'],]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
    return A2

def go10(update,context):
    cid = update.message.chat_id
    cid = update.message.chat_id
    ciid = update.message.from_user.id
    text = update.message.text 
    stat_up(cid)
    message = update.message

    eidL=[]
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        eidL.append(row[0])
    dastresi = "bayanie"

    for eid in eidL:
        try:
            if dastresi == "bayanie":
                # Concatenate the original caption and the formatted suffix

                if message.text:
                    text = message.text

                    context.bot.send_message(chat_id=eid,text = f'''{text}        ''')              
                    
                else:
                    text = None


                # Send photo
                if message.photo:

                    media_id = message.photo[-1].file_id
                    caption = message.caption
                    new_caption = "{}".format(caption)
                    
                    context.bot.send_photo(chat_id=eid, photo=media_id, caption=new_caption, caption_entities=message.caption_entities)

                # Send video
                elif message.video:
        
                    media_id = message.video.file_id
                    caption = message.caption
                    new_caption = "{}".format(caption)
                            
                    context.bot.send_video(chat_id=eid, video=media_id, caption=new_caption, caption_entities=message.caption_entities)

                # Send audio
                elif message.audio:
                    media_id = message.audio.file_id
                    caption = message.caption
                    new_caption = "{}".format(caption)
                                    
                    context.bot.send_audio(chat_id=eid, audio=media_id, caption=new_caption, caption_entities=message.caption_entities)

                # Send document
                elif message.document:    
                    media_id = message.document.file_id
                    caption = message.caption
                    new_caption = "{}".format(caption)
                                    
                    context.bot.send_document(chat_id=eid, document=media_id, caption=new_caption, caption_entities=message.caption_entities)
        except:
            pass


    keyboard = keyboardM
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = cid,
    text = "✅بیانیه شما ارسال شد",reply_markup=reply_markup)
    return A3



def go9(update,context):
    cid = update.message.chat_id
    cid = update.message.chat_id
    ciid = update.message.from_user.id
    text = update.message.text 
    stat_up(cid)
    message = update.message

    eidL=[]
    sql = '''SELECT * From etehad'''
    recs = c.execute(sql)
    for row in recs:
        eidL.append(row[2])
    dastresi = "bayanie"

    for eid in eidL:
        if dastresi == "bayanie":
            # Concatenate the original caption and the formatted suffix

            if message.text:
                text = message.text

                context.bot.send_message(chat_id=eid,text = f'''{text}        ''')              
                
            else:
                text = None


            # Send photo
            if message.photo:

                media_id = message.photo[-1].file_id
                caption = message.caption
                new_caption = "{}".format(caption)
                
                context.bot.send_photo(chat_id=eid, photo=media_id, caption=new_caption, caption_entities=message.caption_entities)

            # Send video
            elif message.video:
    
                media_id = message.video.file_id
                caption = message.caption
                new_caption = "{}".format(caption)
                        
                context.bot.send_video(chat_id=eid, video=media_id, caption=new_caption, caption_entities=message.caption_entities)

            # Send audio
            elif message.audio:
                media_id = message.audio.file_id
                caption = message.caption
                new_caption = "{}".format(caption)
                                
                context.bot.send_audio(chat_id=eid, audio=media_id, caption=new_caption, caption_entities=message.caption_entities)

            # Send document
            elif message.document:    
                media_id = message.document.file_id
                caption = message.caption
                new_caption = "{}".format(caption)
                                
                context.bot.send_document(chat_id=eid, document=media_id, caption=new_caption, caption_entities=message.caption_entities)



    keyboard = keyboardM
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = cid,
    text = "✅بیانیه شما ارسال شد",reply_markup=reply_markup)
    return A3

            
def admini(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if row[0] == cid:
            dastresi = row[8]

    if dastresi == "admin":
        global steps
        cid = update.message.chat_id
        text = update.message.text 
        stat_up(cid)

        if text == "payam etehad":
            context.bot.send_message(chat_id = cid ,text = "payam ra ersal konid")
            return G9

        if text == "payam hamegani":
            context.bot.send_message(chat_id = cid ,text = "payam ra ersal konid")
            return G10
        

        if text == "backup":
            with open("BOT4.db", "rb") as file:
                context.bot.send_document(chat_id=cid, document=file,  
                    filename='BOT_backup.db')

        elif text == "gift":
            steps[cid]="gift"
            context.bot.send_message(chat_id = cid ,text = """

    1️⃣روش1:
    جعبه اختصاصی
    <code>1*esme jabe*list_khandana</code>
    مثال:
    1*testbox*stark-manderly-lannister-tyrell

    2️⃣روش2:
    جعبه عمومی
    <code>2*esme jabe*tedad code morede niaz</code>
    مثال:
    1*testbox*5

    3️⃣روش3:
    ثابت عمومی
    <code>3*mohtaviat jabe*tedad morde niaz</code>

    4️⃣روش4:
    ثابت اختصاصی
    <code>4*mohtaviat jabe*list_khandan</code>

            """,parse_mode = ParseMode.HTML)


        elif text == "edit":
            list = []
            sql = '''SELECT * From Information'''
            recs = c.execute(sql)
            for row in recs:
                khandan = row[2]
                list.append(khandan)
            new_list = [list[i:i+3] for i in range(0, len(list), 3)]
            keyboard = new_list
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return G2


        elif text == "hero":
            list = []
            sql = '''SELECT * From Information'''
            recs = c.execute(sql)
            for row in recs:
                khandan = row[2]
                list.append(khandan)
            new_list = [list[i:i+3] for i in range(0, len(list), 3)]
            keyboard = new_list
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return G5


        elif text == "amar":
            amar = f"{stats}"
            context.bot.send_message(chat_id = cid ,text = amar)

        elif text =='by location':
            steps[cid]="by location"
            context.bot.send_message(chat_id = cid ,text = "مکانی که قصد دارید ارتش های حاضر در آن را بررسی کنید وارد کنید")
            return G1
        elif text == "by house":
            steps[cid]="by house"
            context.bot.send_message(chat_id = cid ,text = "خاندانی که قصد دارید ارتش های  آن را بررسی کنید وارد کنید")
            return G1
        elif text == "by code":
            steps[cid]="by code"
            context.bot.send_message(chat_id = cid ,text = "کد ارتشی که قصد دارید آن را بررسی کنید وارد کنید")
            return G1
        elif text == "sabt":
            steps[cid]="sabt"
            context.bot.send_message(chat_id = cid ,text = """
    Khandan*ghale*eghlim*اسم فارسی
    برای مثال:
    Stark*Winterfell*🐺North*استارک
    """)
            return G1
        else:
            step = steps[cid]

            if step == "gift":
                text = text.split("*")
                no = int(text[0])
                if no == 1:
                    box_name = text[1]
                    khandanlist = f"{text[2]}"
                    khandanlist = khandanlist.split("-")

                    for khandan in khandanlist:
                        password_length = 9
                        code = secrets.token_urlsafe(password_length)
                        c.execute('''INSERT INTO giftcode (pcode,type,use,content) values("{}","{}","{}","{}");'''.format(code,khandan,"no",box_name))
                        conn.commit()
                        time.sleep(0.3)
                        context.bot.send_message(chat_id = cid ,text = f"""
    👑لرد {khandan}
    🎁غنائمی با عنوان {box_name} برا شما ارسال شده ,لطفا جهت مشاهده و استفاده از  آن ها از
    🔑کد: <code>{code}</code> استفاده کنید.

    ⚠️این کد مخصوص شما و به صورت یکبار مصرف تولید شما و قابل انتقال نمیباشد.

                """,parse_mode = ParseMode.HTML)
                elif no == 2:
                    box_name = text[1]
                    num = int(text[2])
                    while num>0:
                        password_length = 9
                        code = secrets.token_urlsafe(password_length)
                        c.execute('''INSERT INTO giftcode (pcode,type,use,content) values("{}","{}","{}","{}");'''.format(code,"omomi","no",box_name))
                        conn.commit()
                        time.sleep(0.3)
                        context.bot.send_message(chat_id = cid ,text = f"""
    🎁غنائمی با عنوان {box_name} برا شما ارسال شده ,لطفا جهت مشاهده و استفاده از  آن ها از
    🔑کد: <code>{code}</code> استفاده کنید.

    ⚠️این کد مخصوص شما و به صورت یکبار مصرف تولید شما و قابل انتقال نمیباشد.

                """,parse_mode = ParseMode.HTML)
                        num = num-1
                elif no == 3:
                    content = f"{text[1]}"
                    content = eval(content)
                    tt = f"\n"
                    for key in content:
                        tt = tt + f"{key}:{content[key]} + "
                    num = int(text[2])
                    while num>0:
                        password_length = 9
                        code = secrets.token_urlsafe(password_length)
                        c.execute('''INSERT INTO giftcode (pcode,type,use,content) values("{}","{}","{}","{}");'''.format(code,"omomi","no",content))
                        conn.commit()
                        time.sleep(0.3)
                        context.bot.send_message(chat_id = cid ,text = f"""
    🎁غنائمی شامل {tt} برا شما ارسال شده ,لطفا جهت مشاهده و استفاده از  آن ها از
    🔑کد: <code>{code}</code> استفاده کنید.
                """,parse_mode = ParseMode.HTML)
                        num = num-1

                elif no == 4:
                    content = f"{text[1]}"
                    content = eval(content)
                    khandanlist = f"{text[2]}"
                    khandanlist = khandanlist.split("-")  
                    khandanlist = f"{text[2]}"
                    khandanlist = khandanlist.split("-")
                    tt = f"\n"
                    for key in content:
                        tt = tt + f"{key}:{content[key]} + "

                    for khandan in khandanlist:
                        password_length = 9
                        code = secrets.token_urlsafe(password_length)
                        c.execute('''INSERT INTO giftcode (pcode,type,use,content) values("{}","{}","{}","{}");'''.format(code,khandan,"no",content))
                        conn.commit()
                        time.sleep(0.3)
                        context.bot.send_message(chat_id = cid ,text = f"""
    👑لرد {khandan}
    🎁غنائمی شامل {tt} برا شما ارسال شده ,لطفا جهت مشاهده و استفاده از  آن ها از
    🔑کد: <code>{code}</code> استفاده کنید.

    ⚠️این کد مخصوص شما و به صورت یکبار مصرف تولید شما و قابل انتقال نمیباشد.

                """,parse_mode = ParseMode.HTML)


            elif step == "sabt":
                text = text.split("*")
                khandan = text[0]
                ghale = text[1]
                eghlim = text[2]
                farsi = text[3]
                password_length = 8
                code = secrets.token_urlsafe(password_length)
                img = Image.open(f'view/sabt/{eghlim}.jpg')
                d1 = ImageDraw.Draw(img)
                reshaped_text = arabic_reshaper.reshape(f"{farsi}")   
                bidi_text = get_display(reshaped_text)
                myFont = ImageFont.truetype('view/fonts/Kaghaz.TTF', 40)
                d1.text((640,534),bidi_text, font=myFont, fill =(255, 255, 255),anchor="mm")
                img.save('hi.png')
                link = {
                            "🐺North":"https://t.me/+WfeM3NrCTfAwMDRh",
                            "🦈Riverlands":"https://t.me/+XPA1PNJHYwFmMTYx",
                            "🦅The Vale":"https://t.me/+8MVunxfTnR0zNWJh",
                            "🦁Westerlands":"https://t.me/+1U22J7C92HU0Mzhh",
                            "🌊Iron Islands":"https://t.me/+Wc-xO_--CvA5MTM5",
                            "🌼Reach":"https://t.me/+MIgM35XHvSAxZTBh",
                            "🦌Stormlands":"https://t.me/+E7uVOAWtqx9mNTU5",
                            "🐲Crownlands":"https://t.me/+PXnOQNJ5NcY0OTUx",
                            "🌞Dorne":"https://t.me/+dCrrbmIvV8I0NDI5"
                        }


                link = link[eghlim]
                txt = f"""
    🌖 به بازی <b>خاندان اژدها</b> خوش آمدید، شما به عنوان لرد صاحب یکی از خاندان های وستروس برگزیده شده اید.

    🍄 اقلیم شما: {eghlim}
    🐉 خاندان {khandan} از {ghale}

    <a href="{link}">🍃 لینک گروه اقلیم شما </a> | <a href="https://t.me/battleofthroneBot">🍂 ربات بازی</a>

    🔑 رمز ورود شما به بات: <code>{code}</code>

    <u>✨این کد مجوز ورود شما به بازی میباشد لطفا از اشتراک گذاری آن با دیگران جدا خودداری فرمایید.</u>


    <a href="https://t.me/battleofthrone">🔅کانال بازی </a>|<a href="https://t.me/Bot4rules">🔅قوانین</a>|<a href="https://t.me/TeleeGames">🔅تله گیمز</a>
                """
                c.execute('''INSERT INTO codes (code,khandan,ghale,eghlim,farsi) values("{}","{}","{}","{}","{}");'''.format(code,khandan,ghale,eghlim,farsi))
                conn.commit()
                photo = open(f'temp/hi.png', 'rb')
                context.bot.send_photo(chat_id = cid ,photo = photo , caption = txt,parse_mode = ParseMode.HTML)

            elif step == 'by location' or step == "by house" or step == "by code":
                steps[cid] = "A edit"
                list = []
                if step == "by location":
                    sql = '''SELECT * From lashkarkeshi WHERE vaziat = "{}" AND maghsad = "{}" '''.format("💢مستقر",text)
                elif step == "by house":
                    sql = '''SELECT * From lashkarkeshi WHERE khandan = "{}" '''.format(text)
                elif step == "by code":
                    sql = '''SELECT * From lashkarkeshi WHERE code = "{}" '''.format(text)
    

                recs = c.execute(sql)
                for row in recs:
                    khandan = row[1]
                    niro = row[2]
                    mabda = row[3]
                    maghsad = row[4]
                    masir = row[5]
                    ETA = row[6]
                    nextETA = row[7]
                    vaziat = row[8]
                    code = row[9]
                    niro = niro.replace(",",",\n")

                    txt = f"""
    <code>{khandan}*{code}*{vaziat}&    
    {mabda}*{maghsad}&
    {masir}&
    {ETA}*{nextETA}&
    {niro}</code>
                    """
                    context.bot.send_message(chat_id = cid ,text = txt,parse_mode = ParseMode.HTML)
                    time.sleep(0.2)

            elif step == "A edit":
                text=text.replace(f"\n","")
                text = text.split("&")
                l1 = text[0]
                l1 = l1.split("*")
                khandan = l1[0]
                code = l1[1]
                vaziat = l1[2]
                l2 = text[1]
                l2 = l2.split("*")
                mabda = l2[0]
                maghsad = l2[1]
                masir = text[2]
                l4 = text[3]
                l4 = l4.split("*")
                ETA = f"{l4[0]}"
                nextETA = f"{l4[1]}"
                niro = text[4]

                c.execute('''UPDATE lashkarkeshi SET niro = "{}" WHERE code = "{}" '''.format(niro,code))
                c.execute('''UPDATE lashkarkeshi SET nextETA = "{}" WHERE code = "{}" '''.format(nextETA,code))
                c.execute('''UPDATE lashkarkeshi SET ETA = "{}" WHERE code = "{}" '''.format(ETA,code))
                c.execute('''UPDATE lashkarkeshi SET masir = "{}" WHERE code = "{}" '''.format(masir,code))
                c.execute('''UPDATE lashkarkeshi SET maghsad = "{}" WHERE code = "{}" '''.format(maghsad,code))
                c.execute('''UPDATE lashkarkeshi SET mabda = "{}" WHERE code = "{}" '''.format(mabda,code))
                c.execute('''UPDATE lashkarkeshi SET vaziat = "{}" WHERE code = "{}" '''.format(vaziat,code))
                conn.commit() 
                context.bot.send_message(chat_id = cid ,text = "sabt shod baraye khoroj az halat edit artesh /start bezanid",parse_mode = ParseMode.HTML)

    

def go5(update,context):
    ciid = update.message.chat_id
    text = update.message.text
    stat_up(ciid)
    sql = '''SELECT * From hero'''
    recs = c.execute(sql)
    for row in recs:
        print(row[1])
        if row[1] == text:
            name = row[0]
            xp = row[2]
            items = row[3]
            zereh = row[4]
            rast = row[5]
            chap = row[6]
            kolah = row[7]
            kafsh = row[8]
            hp = row[9]
            def_b = row[10]
            att_b = row[11]
            att_p = row[12]

    t = f"""
<code>name*{text}*{name}</code>
    
<code>xp*{text}*{xp}</code>

<code>items*{text}*{items}</code>

<code>zereh*{text}*{zereh}</code>

<code>rast*{text}*{rast}</code>

<code>chap*{text}*{chap}</code>

<code>kolah*{text}*{kolah}</code>

<code>kafsh*{text}*{kafsh}</code>

<code>def_b*{text}*{def_b}</code>

<code>att_b*{text}*{att_b}</code>

<code>att_p*{text}*{att_p}</code>
    """
    context.bot.send_message(chat_id=ciid ,text =t,parse_mode = ParseMode.HTML)
    return G6


def go6(update,context):
    ciid = update.message.chat_id
    stat_up(ciid)
    text = update.message.text 
    text = text.split("*")
    base = text[0]
    khan = text[1]
    megh = text[2]
    c.execute('''UPDATE hero SET {} = "{}" WHERE khandan = "{}" '''.format(base,megh,khan))
    conn.commit()
    keyboard = [
        ['🔁ادامه']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = ciid , text =  f"✅sabt shod",reply_markup=reply_markup)
    return A2 



def edit1(update,context):
    ciid = update.message.chat_id
    stat_up(ciid)
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if row[2] == text:
            cid = row[0]
            name = row[1]
            khandan = row[2]
            ghale = row[3]
            eghlim = row[4]
            manba = row[5]
            buildings = row[6]
            building2 = row[7]
            dastresi = row[8]
            troops = row[9]
            zvorodi = row[12]
            zkhoroji = row[13]
            sarmaye = row[20]
            vam = row[21]
            tamrin = row[22]
            academy = row[23]
            knight = row[24]
            tejaratmode = row[25]
            win_n = row[26]
            lose_n = row[27]
            zarib = row[29]
            vip = row[31]

    manba = manba.replace(",",",\n")
    buildings = buildings.replace(",",",\n")
    building2 = building2.replace(",",",\n")
    troops = troops.replace(",",",\n")
    academy = academy.replace(",",",\n")


    t2 = f"""
<code>manba*{khandan}*
{manba}</code>

<code>buildings*{khandan}*
{buildings}</code>

<code>buildings2*{khandan}*
{building2}</code>

<code>troops*{khandan}*
{troops}</code>

    """
    t1 = f"""
<code>cid*{khandan}*{cid}</code>

<code>name*{khandan}*{name}</code>

<code>khandan*{khandan}*{khandan}</code>

<code>ghale*{khandan}*{ghale}</code>

<code>eghlim*{khandan}*{eghlim}</code>

<code>dastresi*{khandan}*{dastresi}</code>
[ban,admin,all]

<code>zvorodi*{khandan}*{zvorodi}</code>

<code>zkhoroji*{khandan}*{zkhoroji}</code>

<code>sarmaye*{khandan}*{sarmaye}</code>

<code>vam*{khandan}*{vam}</code>

<code>tamrin*{khandan}*{tamrin}</code>

<code>academy*{khandan}*{academy}</code>

<code>tejaratmode*{khandan}*{tejaratmode}</code>
[mohasere,none]

<code>win_n*{khandan}*{win_n}</code>

<code>lose_n*{khandan}*{lose_n}</code>

<code>zarib*{khandan}*{zarib}</code> #sorat_lashkarkeshi

<code>vip*{khandan}*{vip}</code> ✅

    """
    context.bot.send_message(chat_id=ciid ,text =t1,parse_mode = ParseMode.HTML)
    context.bot.send_message(chat_id=ciid ,text =t2,parse_mode = ParseMode.HTML)
    photo = open(f'pics/base\{khandan}.png', 'rb')
    context.bot.send_photo(chat_id = ciid , photo = photo)
    return G3


def edit2(update,context):
    ciid = update.message.chat_id
    stat_up(ciid)
    text = update.message.text 
    text = text.split("*")
    base = text[0]
    khan = text[1]
    megh = text[2]
    c.execute('''UPDATE Information SET {} = "{}" WHERE khandan = "{}" '''.format(base,megh,khan))
    conn.commit()
    keyboard = [
        ['🔁ادامه']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = ciid , text =  f"✅sabt shod",reply_markup=reply_markup)
    return A2  

def sarmaye_gozari(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    text = int(text)
    if text <1:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
            buildings = row[6]
    buildings = eval(buildings)
    manba = eval(manba)
    seke = manba["💰|سکه"]
    khazane_lvl = buildings["💰|خزانه"]
    newseke = seke - text
    if newseke<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌شما سکه کافی جهت این سرمایه گذاری را ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    sood = int(text*khazane_lvl/100)
    update_information("temp1",text,cid)
    context.bot.send_message(chat_id=cid ,text = f"""
💲تعداد سکه سرمایه گذاری: {text}
💸سود شما به ازای هر هفته سرمایه گذاری: {sood}سکه

🔻قصد دارید این تعداد سکه را برای چند هفته سرمایه گذاری کنید؟(حداکثر 4 هفته)
    """,parse_mode = ParseMode.MARKDOWN )
    return C5


def pardakht_vam(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    text = int(text)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
            list = row[21]
    manba = eval(manba)
    list = eval(list)
    seke = manba["💰|سکه"]
    bedehi = list[0]
    hafte = list[1]
    newbedehi = bedehi - text
    newseke = seke - text
    if newseke<0 or text<0 or newbedehi<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    
    if newbedehi == 0:
        list = []
    else:
        list = [newbedehi,hafte]
    update_information("vam",list,cid)
    manba["💰|سکه"] = newseke
    update_information("manba",manba,cid)

    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"""
✅مقدار {text} سکه از {bedehi} سکه بدهی شما به بانک آهنین پرداخت شد
🔸شما {hafte} هفته دیگر مهلت داشته تا باقی بدهی خود را پرداخت کنید
    """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2

def vam(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    text = int(text)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
            buildings = row[6]
    buildings = eval(buildings)
    manba = eval(manba)
    seke = manba["💰|سکه"]
    buildings = buildings["🏦|ایرون بانک"]
    vam = (seke*buildings/10)
    if text<1 or text>vam:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    newseke = seke+text
    manba["💰|سکه"] = newseke
    update_information("manba",manba,cid)
    newtext = text + int(12*text/100)
    list = [newtext,buildings]
    update_information("vam",list,cid)


    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"""
✅مقدار {text} سکه وام از بانک آهنین دریافت شد
💸شما {buildings} هفته مهلت داشته تا {newtext}سکه بدهی خود به بانک آهنین را پرداخت کنید
    """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2

def hafte_sarmayegozari(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    text = int(text)
    if text <1 or text>4:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == cid:
            manba = row[5]
            buildings = row[6]
            temp1 = int(row[10])
    buildings = eval(buildings)
    manba = eval(manba)
    seke = manba["💰|سکه"]
    khazane_lvl = buildings["💰|خزانه"]
    newseke = seke - temp1
    sood = int(temp1*khazane_lvl*text/100)
    #hafte meghdar haftemande lvl
    list = [text,temp1,text,khazane_lvl]
    update_information("sarmaye",list,cid)
    manba["💰|سکه"] = newseke
    update_information("manba",manba,cid)
    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"""
✅تعداد {temp1} سکه برای مدت {text} هفته سرمایه گذاری شد
💸سود شما در پایان مدت سرمایه گذاری: {sood}
    """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2


def upgrade(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 

    if text == "🔙بازگشت":
        keyboard = keyboardM
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = "منو مورد نظر را انتخاب کنید🔻",
        reply_markup=reply_markup)
        return A3


    if text == "✅ارتقا":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                text = row[10]

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            manba = row[5]
            buildings = row[6]
            buildings2 = row[7]



    sql = '''SELECT * From hazine'''
    recs = c.execute(sql)
    for row in recs:
        if row[0] == text:
            hazine = row[1]
            zarib = row[3]
            aks = row[4]
    buildings = eval(buildings)
    buildings2 = eval(buildings2)
    try:
        lvlnow = buildings[text]
    except:
        lvlnow = buildings2[text]
    try:
        a = buildings2[text]
        a +=1
    except:
        a = buildings[text]
        a +=1

    if zarib == "yes":
        zarib = a
    else:
        zarib = 1
      
    manba = eval(manba)
    hazine = eval(hazine)
    hazinee = hazine
    for key in hazine:
        hazinee[key] = hazinee[key]*zarib
    hazine = hazinee
    hazinee = f"{hazine}"
    hazinee = hazinee.replace('}',"")
    hazinee = hazinee.replace('{',"")
    hazinee = hazinee.replace(',',"+")
    hazinee = hazinee.replace("'","")
    zakhire = hazine

    for key in hazine:
        a1 = hazine[key]
        a2 = manba[key]
        zakhire[key] = a2
        new = a2-a1
        if new<0:
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"❌شما {key} کافی برای این ارتقا را ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2
        else:
            pass

    zakhire = f"{zakhire}"
    zakhire = zakhire.replace('}',"")
    zakhire = zakhire.replace('{',"")
    zakhire = zakhire.replace(',',"+")
    zakhire = zakhire.replace("'","")
    keyboard = [["✅","❌"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    update_information("temp1",text,cid)
    aks = open(f'view/aks\{aks}.png', 'rb')
    context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"""
⬛️سطح فعلی: {lvlnow}                     

🟥هزینه ارتقا: {hazinee}

🟨ذخیره شما: {zakhire}
            
            """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A5         


def upgrade2(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 

    if text == "✅":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                manba = row[5]
                text = row[10]
                buildings = row[6]
                buildings2 = row[7]
                khandan = row[2]
                vip = row[31]

        if text == "🗿|سنگ تراشی" or text == "🎋|درخت نیایش":
            if vip != "✅":
                keyboard = [["🔙بازگشت به منوی اصلی"]]
                reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id=cid ,text = f"❌ارتقا این ساختمان تنها برای پلیرهای vip مجاز میباشد!" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
                return A2   


        buildings = eval(buildings)
        buildings2 = eval(buildings2)
        manba = eval(manba)



        sql = '''SELECT * From hazine'''
        recs = c.execute(sql)
        for row in recs:
            if row[0] == text:
                hazine = row[1]
                zarib = row[3]
                pic = row[4]
                pos = row[5]
                mahdodiat = row[6]
        
        mahdodiat = int(mahdodiat) +1
        pos = eval(pos)
        hazine = eval(hazine)

        try:
            a = buildings2[text]
            a +=1
            buildings2[text] = a
            if a<mahdodiat:
                update_information("buildings2",buildings2,cid)
            else:
                text = f"✅این ساختمان به سطح نهایی خود رسیده است"
                keyboard = [['🔙بازگشت به منوی اصلی'],]
                reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
                return A2    
        except:
            a = buildings[text]
            a +=1
            buildings[text] = a
            if a < mahdodiat:
                update_information("buildings",buildings,cid)  
            else:
                text = f"✅این ساختمان به سطح نهایی خود رسیده است"
                keyboard = [['🔙بازگشت به منوی اصلی'],]
                reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
                return A2  

        if zarib == "yes":
            zarib = a
        else:
            zarib = 1

        try:
            for key in hazine:
                a1 = hazine[key]*zarib
                a2 = manba[key]
                new = a2-a1
                manba[key] = new
                update_information("manba",manba,cid)


            try:
                pos = pos[a]
                photo = Image.open(f'pics/base/{khandan}.png').convert("RGBA")
                watermark = Image.open(f"buildingspic/{pic}/{a}.png").convert("RGBA")
                photo.paste(watermark, pos, watermark)
                photo.save(f"base/{khandan}.png")
                text = f"🔅ربات در حال بروزرسانی میباشد لطفا چند لحظه صبر کنید"
                keyboard = keyboardM
                reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id = cid ,text = text)
                time.sleep(1)
            except:
                photo = 1

            try:
                keyboard = [
                    ['🏰مرکز شهر','🛖مرکز فرماندهی'],
                    ['🕊مرکز ارتباطات',"🔘مشاهده دارایی"],
                    ['⚙️تنظیمات']
                    ]
                photo = open(f'pics/base\{khandan}.png', 'rb')
                context.bot.send_photo(chat_id = cid , photo = photo , caption = f"✅ارتقا ساختمان شما با موفقیت انجام شد",
                reply_markup=reply_markup)
                return A3
            except:
                keyboard = [
                    ['🏰مرکز شهر','🛖مرکز فرماندهی'],
                    ['🕊مرکز ارتباطات',"🔘مشاهده دارایی"],
                    ['⚙️تنظیمات']
                    ]
                text = f"✅ارتقا ساختمان شما با موفقیت انجام شد"
                reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
                return A3
        except:
            pass
    else:
        text = f"❌"
        keyboard = [['🔙بازگشت به منوی اصلی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2
def manbaersali(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            manba = row[5]

    manba = eval(manba)

    list = {"manbaersal":text , "meghdarersal":0 , "manbadaryaft":0 , "meghdardaryaft":0 ,}
    update_information("temp1",list,cid)
    manba = manba[text]
    context.bot.send_message(chat_id = cid , text = f"""
*🚛قصد دارید چه مقدار {text} را برای متحد خود ارسال کنید؟ *
🔻تعداد {text} شما: {manba}
        """,reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN) 
    return A7

def meghdarersali(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text
    text = int(text)

    if text<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            manba = row[5]
            temp = row[10]
    manba = eval(manba)
    temp = eval(temp)
    manbaname = temp["manbaersal"]
    manbazakhire = manba[manbaname]
    new = manbazakhire - text
    if new<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌شما منبع کافی برای این تجارت را ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    temp["meghdarersal"] = text
    update_information("temp1",temp,cid)
    list = []
    for key in manba:
        key = f"{key}"
        list.append(key)
    new_list = [list[i:i+3] for i in range(0, len(list), 3)]
    keyboard = new_list
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    context.bot.send_message(chat_id = cid , text = f"""🚚قصد دارید کدام منبع را در ازای {text} {manbaname} دریافت کنید؟""",
    reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return A8


def manbadaryafti(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            temp = row[10]
            manba = row[5]

    temp = eval(temp)
    manba = eval(manba)
    manba = manba[text]
    temp["manbadaryaft"] = text
    update_information("temp1",temp,cid)
    context.bot.send_message(chat_id = cid , text = f"""
*🚛قصد دارید چه مقدار {text} را از متحد خود دریافت کنید؟ *
🔻تعداد {text} شما: {manba}
        """,reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN) 
    return A9


def meghdardaryafti(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text
    text = int(text)

    if text<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            temp = row[10]
    temp = eval(temp)
    temp["meghdardaryaft"] = text
    update_information("temp1",temp,cid)















    keyboard = [["🐺North","🦈Riverlands","🦅The Vale"],["🦁Westerlands","🌊Iron Islands","🌼Reach"],["🦌Stormlands","🐲Crownlands","🌞Dorne","🪙Essos"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    context.bot.send_message(chat_id = cid , text = f"""🔻قصد دارید با کدام مورد زیر تجارت کنید؟""",
    reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return A10
def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)

def nezhadtejarat(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 

    khandans_list = []
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[4]) == text:
            khandans_list.append(row[2])
    

    keyboard = [khandans_list[i:i+3] for i in range(0, len(khandans_list), 3)]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)               
    context.bot.send_message(chat_id = cid , text = f"""🔻قصد دارید با کدام یک تجارت کنید؟""",
    reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return A11

def tejaratfinal(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            temp = row[10]
            khandan = row[2]
    list = eval(temp)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[2]) == text:
            cidmaghsad = row[0]

    randnum = rand.randint(1,9999)
    randlett = rand.choice(azlist)
    Tradecode = f"1*{randlett}-{randnum}*1*1"
    laghvdata = f"1*{Tradecode}*Laghv*1"

    c.execute('''INSERT INTO TejaratCode (list,code,mabda,cid) values("{}","{}","{}","{}");'''.format(list,Tradecode,khandan,cid))
    conn.commit()
    manbaersali = list["manbaersal"]
    meghdarersali = list["meghdarersal"]
    manbadaryafti = list["manbadaryaft"]
    meghdardaryafti = list["meghdardaryaft"]

    if manbaersali == manbadaryafti:
        text = f"🚫شما نمی توانید یک منبع را با همان منبع تجارت کنید"
        keyboard = [
                    ['🔙بازگشت به منوی اصلی'],
                    ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2


    keyboard = [[InlineKeyboardButton("✅تایید تجارت" ,callback_data=Tradecode)],
    [InlineKeyboardButton("❌لغو تجارت" ,callback_data=laghvdata)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        context.bot.send_message(chat_id=cidmaghsad, text=f"""
📦 یک درخواست تجارت از سوی {khandan} به شما ارسال شده است:
◼️کالای ارسال شده برای شما: 
{meghdarersali} {manbaersali}
◽️کالای درخواست شده از شما: 
{meghdardaryafti} {manbadaryafti}    
        """,parse_mode=ParseMode.HTML,reply_markup=reply_markup)

        text = f"✅درخواست شما با موفقیت به {text} ارسال شد"
        keyboard = [
                    ['🔙بازگشت به منوی اصلی'],
                    ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)

        return A2
    except:
        text = f"🚫متاسفانه خاندان مقصد شما در حال حاضر فعال نمیباشد"
        keyboard = [
                    ['🔙بازگشت به منوی اصلی'],
                    ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2


def khoroj(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    context.bot.ban_chat_member(chat_id = -1001767002742 , user_id = cid, timeout=None, until_date=None, api_kwargs=None, revoke_messages=None)

def update_information(motaghayer,meghdar,cid):
    c.execute('''UPDATE Information SET {} = "{}" WHERE cid = "{}" '''.format(motaghayer,meghdar,cid))
    conn.commit() 

def update_etehad(motaghayer,meghdar,name):
    c.execute('''UPDATE etehad SET {} = "{}" WHERE name = "{}" '''.format(motaghayer,meghdar,name))
    conn.commit() 
azlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def find_niro(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    update_information("temp1",text,cid)
    vaziat = "💢مستقر"

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[3]
            niro = row[9]

    if text == khandan:
        pass
    else:
        sql = '''SELECT * From lashkarkeshi WHERE vaziat = "{}" AND cid = "{}" '''.format("💢مستقر",cid)
        recs = c.execute(sql)
        for row in recs:
            if (row[4]) == text:
                niro = row[2]
                vaziat = row[8]
                code = row[9]
                typ = row[10]

        minutes = 61  
        try:    
            now = datetime.datetime.now()
            print(now)
            now2 = typ
            # strptime(input_string, input_format)
            date_time = datetime.datetime.strptime(now2, '%Y-%m-%d %H:%M:%S.%f')

            d = now - date_time
            minutes = d.total_seconds() / 60
            minutes = int(minutes)
        except:
            pass

        if minutes<60:
            text = f"🚫متاسفانه شما تا {60-minutes} دقیقه دیگر مجاز به حرکت دادن این ارتش نمیباشید"
            keyboard = [
                        ['🔙بازگشت به منوی اصلی'],
                        ]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2
    

    niro = eval(niro)
    update_information("temp2",niro,cid)

    troopslist = ""
    for key in niro:
        a = f"▪️{key}:{niro[key]}"
        troopslist = troopslist + f"\n{a}"
    context.bot.send_message(chat_id=cid , text =f"""<b>🔅لیست نیروهایی که قصد جا به جایی آن ها را دارید ارسال کنید

🔰وضعیت: {vaziat}
〰️لیست نیروها:</b>
<code>{troopslist}</code>

‼️با یک بار لمس کردن لیست فوق لیست کپی شده و تغییرات مدنظر خود را اعمال کنید
⚠️گزینه هایی که قصد تغییر آن را ندارید را بدون تغییر رها کنید(هیچ موردی را حذف نکنید)""",parse_mode = ParseMode.HTML)
    return B1


def new_artesh(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            temp = row[11]

    temp = eval(temp)
    txt = update.message.text
    txt = txt.replace("▪️","'")
    txt = txt.replace(":","':")
    txt = txt.replace("\n",",")
    text = "{" + f"{txt}" + "}"
    list_harekat = eval(text)

    kol = 0
    for key in list_harekat:
        a1 = list_harekat[key]
        kol = kol + a1
        a2 = temp[key]
        new = a2 - a1
        if new<0:
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"❌شما {key} کافی جهت انجام این حرکت را ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2
        temp[key] = new

    if kol<1:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"❌شما نیرو کافی جهت انجام این حرکت را ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    
    update_information("temp2",temp,cid)
    update_information("temp3",list_harekat,cid)

    keyboard = [["🐺North","🦈Riverlands","🦅The Vale"],["🦁Westerlands","🌊Iron Islands","🌼Reach"],["🦌Stormlands","🐲Crownlands","🌞Dorne","🪙Essos"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    context.bot.send_message(chat_id = cid , text = f"""🔻قلعه ای که قصد لشکرکشی به ان را دارید در قلمرو کدام اقلیم قرار دارد؟""",
    reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return B2

def co12(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            name = row[1]
            etehad = row[19]
            khandan = row[2]
            eghlim = row[4]
            buildings = eval(row[6])
            tamrin = eval(row[22])
            academy = eval(row[23])
            knight = eval(row[24])

    eghlim_dict = {"🐺North":"شمال","🦈Riverlands":"ریور","🦅The Vale":"ویل","🦁Westerlands":"وستر","🌊Iron Islands":"جزایر","🌼Reach":"ریچ","🦌Stormlands":"استورم","🐲Crownlands":"کرون","🌞Dorne":"دورن","🪙Essos":"دورن"}
    eghlimM = eghlim_dict[eghlim]

    sql = '''SELECT * From hero'''
    recs = c.execute(sql)
    for row in recs:
        if row[1] == khandan:
            name = row[0]
            xp = row[2]
            zereh = row[4]
            rast = row[5]
            chap = row[6]
            kolah = row[7]
            kafsh = row[8]
            hp = row[9]
            def_b = row[10]
            att_b = row[11]
            att_p = row[12]

    fff = ""
    ffff = ""
    ggg = ""
    gggg = ""
    try:
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == etehad:
                members = eval(row[1])
    except:
        pass

    ggg = f"""
❤️|کمپ : {buildings["❤️|کمپ مجروحین"]}
⚔️هجومی: {tamrin["hojom"]}%
🔰دفاع پیاده: {tamrin["defpiyade"]}%
🔰دفاع سواره: {tamrin["defsavare"]}%   
    """
    fff = f"""🔰فرمانده لشکریان ارتش {name}>{khandan} دستور حمله به {text} را صادر کرد
🔰نام اتحاد: {etehad}

<b>آمار تفکیکی مهاجم</b>:

••••••••••••••{khandan}••••••••••••••
    """

    sql = '''SELECT * From lashkarkeshi WHERE vaziat = "{}" AND cid = "{}" '''.format("💢مستقر",cid)
    recs = c.execute(sql)
    for row in recs:
        if (row[4]) == text:
            niro = row[2]

    print(niro)
    niro = eval(niro)
    for key in niro:
        num = niro[key]
        if num>0:
            if key == "⚔️|شمشیرزن" or key =="🗡|نیزه دار" or key == "🐎|سوارکار" or key == "🏹|کماندار":
                fff = fff + f"\n {key}:{num} ({academy[key]})"
            else:
                fff = fff + f"\n {key}:{num}"

    try:
        for mem in members:
            a = 0
            sql = '''SELECT * From lashkarkeshi WHERE vaziat = "{}" AND khandan = "{}" '''.format("💢مستقر",mem)
            recs = c.execute(sql)
            for row in recs:
                if (row[4]) == text:
                    a = 1
                    niro = row[2]

            if a == 1 and mem != khandan:
                sql = '''SELECT * From Information'''
                recs = c.execute(sql)
                for row in recs:
                    if (row[2]) == mem:
                        buildings = eval(row[6])
                        tamrin = eval(row[22])
                        academy = eval(row[23])
                        knight = eval(row[24])



                ggg = ggg + f"""\n••••••••••••••{mem}••••••••••••••
❤️: {buildings["❤️|کمپ مجروحین"]} - ⚔️ {tamrin["hojom"]}% - 🛡🚶‍♂️: {tamrin["defpiyade"]}% - 🛡🐎{tamrin["defsavare"]}%  
                """
                fff = fff + f"\n••••••••••••••{mem}••••••••••••••"
                niro = eval(niro)
                for key in niro:
                    num = niro[key]
                    if num>0:
                        if key == "⚔️|شمشیرزن" or key =="🗡|نیزه دار" or key == "🐎|سوارکار" or key == "🏹|کماندار":
                            fff = fff + f"\n {key}:{num} ({academy[key]})"
                        else:
                            fff = fff + f"\n {key}:{num}"
    except:
        pass

    try:
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == text:
                cid_d = row[0]
                name_d = row[1]
                eghlim_d = row[4]
                etehad_d = row[19]
                khandan_d = row[2]
                troops_d = eval(row[9])
                buildings_d = eval(row[6])
                tamrin_d = eval(row[22])
                academy_d = eval(row[23])
                knight_d = eval(row[24])
        eghlimD = eghlim_dict[eghlim_d]

        sql = '''SELECT * From hero'''
        recs = c.execute(sql)
        for row in recs:
            if row[1] == text:
                name = row[0]
                xp = row[2]
                zereh = row[4]
                rast = row[5]
                chap = row[6]
                kolah = row[7]
                kafsh = row[8]
                hp = row[9]
                def_b = row[10]
                att_b = row[11]
                att_p = row[12]
        try:
            sql = '''SELECT * From etehad'''
            recs = c.execute(sql)
            for row in recs:
                if (row[0]) == etehad_d:
                    members_d = eval(row[1])
                    eid_d = row[2]
        except:
            pass
        

        gggg = f"""
    ❤️|کمپ : {buildings_d["❤️|کمپ مجروحین"]}
    ⚔️هجومی: {tamrin_d["hojom"]}%
    🔰دفاع پیاده: {tamrin_d["defpiyade"]}%
    🔰دفاع سواره: {tamrin_d["defsavare"]}%
        """
        ffff = f"""🔰فرمانده لشکریان ارتش {name}>{khandan} دستور حمله به {text} را صادر کرد
🔰نام اتحاد: {etehad_d}
🔰مدافع:{name_d}

<b> آمار تفکیکی مدافع </b>:

••••••••••••••{khandan_d}••••••••••••••
        """


        for key in troops_d:
            num = troops_d[key]
            if num>0:
                if key == "⚔️|شمشیرزن" or key =="🗡|نیزه دار" or key == "🐎|سوارکار" or key == "🏹|کماندار":
                    ffff = ffff + f"\n {key}:{num} ({academy_d[key]})"
                else:
                    ffff = ffff + f"\n {key}:{num}"
        try:
            for mem in members_d:
                a = 0
                sql = '''SELECT * From lashkarkeshi WHERE vaziat = "{}" AND khandan = "{}" '''.format("💢مستقر",mem)
                recs = c.execute(sql)
                for row in recs:
                    if (row[4]) == text:
                        a = 1
                        niro = row[2]
                if a == 1 and mem != khandan:
                    sql = '''SELECT * From Information'''
                    recs = c.execute(sql)
                    for row in recs:
                        if (row[2]) == mem:
                            buildings = eval(row[6])
                            tamrin = eval(row[22])
                            academy = eval(row[23])

                    gggg = gggg + f"""\n••••••••••••••{mem}••••••••••••••
❤️: {buildings["❤️|کمپ مجروحین"]} - ⚔️ {tamrin["hojom"]}% - 🛡🚶‍♂️: {tamrin["defpiyade"]}% - 🛡🐎{tamrin["defsavare"]}%   
                    """
                    ffff = ffff + f"\n••••••••••••••{mem}••••••••••••••"
                    niro = eval(niro)
                    for key in niro:
                        num = niro[key]
                        if num>0:
                            if key == "⚔️|شمشیرزن" or key =="🗡|نیزه دار" or key == "🐎|سوارکار" or key == "🏹|کماندار":
                                ffff = ffff + f"\n {key}:{num} ({academy_d[key]})"
                            else:
                                ffff = ffff + f"\n {key}:{num}"
        except:
            pass
    except:
        pass

    ax(eghlimM,eghlimD)
    if etehad == etehad_d:
        if etehad_d != "a":
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"""💢شما نمیتوانید به متحد خود حمله کنید""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2

    photo = open(f"temp/output.png", 'rb')
    context.bot.send_photo(chat_id = -1001335810093,photo=photo, caption = f"""<b> 🔰فرمانده لشکریان ارتش <a href="tg://user?id={cid}">{khandan}</a> دستور حمله به {text}  را صادر کرد</b>""",parse_mode = ParseMode.HTML)
    #context.bot.send_photo(chat_id = -1001559813108,photo=photo, caption = f"""<b> 🔰فرمانده لشکریان ارتش <a href="tg://user?id={cid}">{khandan}</a> دستور حمله به {text}  را صادر کرد</b>""",parse_mode = ParseMode.HTML)
    time.sleep(0.2)
    context.bot.send_message(chat_id = -1001559813108 , text = fff ,parse_mode = ParseMode.HTML)
    context.bot.send_message(chat_id = -1001559813108 , text = ggg ,parse_mode = ParseMode.HTML)
    context.bot.send_message(chat_id = -1001559813108 , text = ffff ,parse_mode = ParseMode.HTML)
    context.bot.send_message(chat_id = -1001559813108 , text = gggg ,parse_mode = ParseMode.HTML)
    time.sleep(0.2)

    keyboard = [[InlineKeyboardButton("✅پیروزی مدافع" ,callback_data=f"nabard2*{khandan_d}*{khandan}*{cid}")],
    [InlineKeyboardButton("✅پیروزی مهاجم" ,callback_data=f"nabard*{khandan}*{khandan_d}*{cid}")],
]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id = -1001559813108 , text = "💢نتیجه نبرد را مشخص کنید" ,reply_markup=reply_markup,parse_mode = ParseMode.HTML)

    try:
        photo = open(f"temp/output.png", 'rb')
        context.bot.send_photo(chat_id = eid_d,photo=photo, caption = f"""<b> 🔰فرمانده لشکریان ارتش {khandan}({name}) دستور حمله به {text}({name_d})  را صادر کرد</b>""",parse_mode = ParseMode.HTML)
    except:
        pass
    try:
        update_information("tejaratmode","mohasere",cid_d)
        photo = open(f"temp/output.png", 'rb')
        context.bot.send_photo(chat_id = cid_d,photo=photo, caption = f"""
<b>🔰فرمانده لشکریان ارتش {khandan}({name}) دستور حمله به شما را صادر کرد</b>
            
⚠️از این لحظه قلعه شما محاصره شده و قوانین محاصره بر آن اعمال خواهد شد.
                               """,parse_mode = ParseMode.HTML)
    except:
        pass

    print("______________________________________")
    keyboard = [["🔙پایان سناریو"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id = cid , text = """
💢سناریو نبرد خود را وارد کنید
(در این مرحله میتوانید چندین پیام ارسال کنید بعد از اتمام سناریو خود دکمه پایان سناریو را ارسال کنید)                             
                            """ ,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
    return G7

def go8(update,context):
    cid = update.message.chat_id
    text = update.message.text

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            manba = row[5]
            troops = row[9]

    sql = '''SELECT * From giftcode'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == text:
            type = row[1]
            use = row[2]
            content = row[3]

    sql = '''SELECT * From box'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == content:
            mohtavi = row[1]

    mohtavi = eval(mohtavi)
    manba = eval(manba)
    troops = eval(troops)


    if use != "no":
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""💢این کد قبلا مورد استفاده قرار گرفته""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2    
    
    if type == "omomi" or type == khandan:
        c.execute('''UPDATE giftcode SET use = "{}" WHERE pcode = "{}" '''.format("used",text))
        conn.commit() 
        keys = mohtavi.keys()

        for key in keys:
            try:
                n1 = manba[key]
                n2 = mohtavi[key]
                new = n1+n2
                manba[key] = new
            except:
                pass
            try:
                n1 = troops[key]
                n2 = mohtavi[key]
                new = n1+n2
                troops[key] = new
            except:
                pass

        list = ""
        for key in mohtavi:
            list = list + f'{key}:{mohtavi[key]}\n'

        update_information("troops",troops,cid)
        update_information("manba",manba,cid)

        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""جعبه {content} شامل \n {list} بر دارایی شما اعمال شد""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2 
        


def go7(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    mid=update.message.message_id
    if text == "🔙پایان سناریو":
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""💢سناریو شما به تیم ادمینی ارسال شد نتیجه نبرد به زودی اعلام خواهد شد""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    else:
        context.bot.forward_message(chat_id = -1001559813108,from_chat_id=cid , message_id = mid )


def khandan_lashkarkeshi(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    stat_up(cid)
    khandans_list = []
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[4]) == text:
            khandans_list.append(row[3])
    

    keyboard = [khandans_list[i:i+3] for i in range(0, len(khandans_list), 3)]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)               
    context.bot.send_message(chat_id = cid , text = f"""🔻قصد دارید به کدام قلعه لشکرکشی کنید؟
<i>❗️لیست زیر شامل خاندان هایی میباشد که دارای پلیر میباشند برای لشکرکشی به دیگر قلعه های موجود در بازی که فاقد پلیر میباشند نام آن ها را دقیق تایپ کنید</i>
    """,
    reply_markup=reply_markup,parse_mode = ParseMode.HTML)
    return B3

def masirlashkarkeshi(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            temp = row[10]
            etehad = row[19]
            ghalekhod = row[3]
            zarib = row[29]

    no = noelashkar[cid]
    if no =="🗺لشکرکشی":
        edges = edges1
    elif no == "🐉لشکرکشی":
        edges = edges3
        zarib = zarib/2
    else:
        edges = edges2

    sh_masir = shortestPath(edges, temp, text)
    dis = sh_masir[0]
    dis = int(dis)
    dis = dis*60*zarib
    now = datetime.datetime.now()
    time1 = now + datetime.timedelta(seconds=dis)
    time = time1.strftime("%H:%M")
    masir = sh_masir[1]

    doshman = []
    for key in masir:
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == key:
                etehaddosh = row[19]
                if etehaddosh != etehad or etehaddosh == "a":
                    doshman.append(key)

    try:
        doshman.remove(ghalekhod)
    except:
        pass

    list_doshman = ""
    for key in doshman:
        list_doshman = list_doshman + "\n" + f"◾️{key}"

    mmasir = f"{masir}"
    mmasir = mmasir.replace(']',"")
    mmasir = mmasir.replace('[',"")
    mmasir = mmasir.replace("'","")
    mmasir = mmasir.replace(','," 🔜 ")
    keyboard = [["✅","❌"]]
    update_information("temp4",masir,cid)
    update_information("temp5",time,cid)

    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    text = f"""
🗺مبدا : {temp}
🗺مقصد : {text}
💢مسیر : 
{mmasir}
🕰زمان رسیدن:{time}

🔰در مسیر فوق قلعه های زیر جزو متحدین شما نمیباشند و میتوانند راه را بر روی ارتش شما ببندد بنابراین دقت کافی داشته باشید:
{list_doshman}
    """
    context.bot.send_message(chat_id = cid , text = text, reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return B4


def final_lashkarkeshi(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            eghlim = row[4]
            ghalekhandan = row[3]
            mabda = row[10]
            newniro = row[11]
            listniro = row[14]
            masir = row[15]
            time = row[16]
            etehad = row[19]
            zarib = row[29]
    
    if text == "✅":
        listniro = eval(listniro)
        check = 0
        hidden = 0
        for key in listniro:
            if key == "👀|جاسوس":
                if listniro[key]>0:
                    hidden = "hidden"
            elif key == "👣|راهزن":
                if listniro[key]>0:
                    hidden = "hidden"
            else:
                m = listniro[key]
                check = check + m

        if check>0:
            hidden = 0
            
        s=0
        newniro = eval(newniro)
        for n in newniro:
            s = s + newniro[n]

        masir = eval(masir)
        mmasir = masir
        maghsad = masir[-1]
        masir.remove(mabda)
        nextmaghsad = masir[0]
        randnum = rand.randint(1,9999)
        randlett = rand.choice(azlist)
        randlett1 = rand.choice(azlist)

        code = f"{randlett1}{randlett}-{randnum}"
        data = f"3*{code}*1*1"
        data2 =f"7*{code}*1*1"

        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if (row[3]) == nextmaghsad:
                cidnext = row[0]
                khandan_next = row[2]
                buildingnext = row[6]
                etehadnext = row[19]
        try:           
            sql = '''SELECT * From etehad'''
            recs = c.execute(sql)
            for row in recs:
                if (row[0]) == etehadnext:
                    eid = row[2]

            buildings = eval(buildingnext)
            borj = buildings["👁|برج دیدبانی"]
            if borj>1 and hidden != "hidden":
                try:
                    keyboard = [[InlineKeyboardButton("⛔️بستن راه" ,callback_data=data)],
                    [InlineKeyboardButton("👁‍🗨مشاهده نیرو" ,callback_data=data2)],
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    context.bot.send_message(chat_id=cidnext ,text = f"""
    <b>🔰با توجه به گزارشی که نیروهای مستقر در برج دیدبانی ارسال کرده اند لشکریان خاندان <a href="tg://user?id={cid}">{khandan}</a> در حال نزدیک شدن به قلعه شما میباشند!</b>

    <i>❗️در صورت تمایل میتوانید راه را بر روی نیروهای فوق ببندید

    ‼️توجه داشته باشید بستن  راه بر روی نیروها به معنی اعلام جنگ علیه آن ها میباشد همچنین در صورت بستن راه به روی ارتش نیروهای شما از قلعه خارج شده و شما نمیتوانید از برتری حضور در قلعه استفاده کنید و نبرد در زمین باز صورت خواهد گرفت

    ⚠️در صورتی که قصد بستن مسیر به روی ارتش در حال حرکت را ندارید این پیام را نادیده بگیرید
        </i>""" ,reply_markup=reply_markup,parse_mode = ParseMode.HTML )
                except:
                    pass

                try:
                    if etehad != etehadnext or etehad == "a":
                        context.bot.send_message(chat_id=eid ,text = f"""
        <b>🔰با توجه به گزارشی که دیدبانان {khandan_next} ارسال کرده اند نیروهای ارتش {khandan} در حال حرکت در مرزهای شما میباشد!</b>
        """ ,parse_mode = ParseMode.HTML )
                except:
                    pass
            elif borj>0 and hidden!="hidden":
                try:
                    keyboard = [[InlineKeyboardButton("⛔️بستن راه" ,callback_data=data)],]
                    reply_markup = InlineKeyboardMarkup(keyboard)
                    context.bot.send_message(chat_id=cidnext ,text = f"""
    <b>🔰با توجه به گزارشی که نیروهای مستقر در برج دیدبانی ارسال کرده اند لشکریان خاندان <a href="tg://user?id={cid}">{khandan}</a> در حال نزدیک شدن به قلعه شما میباشند!</b>

    <i>❗️در صورت تمایل میتوانید راه را بر روی نیروهای فوق ببندید

    ‼️توجه داشته باشید بستن  راه بر روی نیروها به معنی اعلام جنگ علیه آن ها میباشد همچنین در صورت بستن راه به روی ارتش نیروهای شما از قلعه خارج شده و شما نمیتوانید از برتری حضور در قلعه استفاده کنید و نبرد در زمین باز صورت خواهد گرفت

    ⚠️در صورتی که قصد بستن مسیر به روی ارتش در حال حرکت را ندارید این پیام را نادیده بگیرید
        </i>""" ,reply_markup=reply_markup,parse_mode = ParseMode.HTML )
                except:
                    pass

                try:
                    if etehad != etehadnext or etehad == "a":
                        context.bot.send_message(chat_id=eid ,text = f"""
        <b>🔰با توجه به گزارشی که دیدبانان {khandan_next} ارسال کرده اند نیروهای ارتش {khandan} در حال حرکت در مرزهای شما میباشد!</b>
        """ ,parse_mode = ParseMode.HTML )
                except:
                    pass
        except:
            pass
        no = noelashkar[cid]
        if no =="🗺لشکرکشی":
            emoj = "🗺"
            edges = edges1
        elif no == "🐉لشکرکشی":
            edges = edges3
            emoj = "🐉"
        else:
            edges = edges2
            emoj = "⛵️"

        sh_masir = shortestPath(edges, mabda, nextmaghsad)
        dis = sh_masir[0]
        dis = int(dis)
        dis = dis*60*zarib
        now = datetime.datetime.now()
        time1 = now + datetime.timedelta(seconds=dis)
        nexteta = time1.strftime("%H:%M")
        vaziat = "حرکت"
        c.execute('''INSERT INTO lashkarkeshi (cid,khandan,niro,mabda,maghsad,masir,ETA,nextETA,vaziat,code,noe,hidden) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(cid,khandan,listniro,mabda,maghsad,masir,time,nexteta,vaziat,code,no,hidden))
        conn.commit()

        troopslist = ""
        for key in listniro:
            a = f"▪️{key}:{listniro[key]}"
            troopslist = troopslist + f"\n{a}"



        

            
        if mabda == ghalekhandan:
            update_information("troops",newniro,cid)
        else:
            m = "💢مستقر"
            c.execute('''UPDATE lashkarkeshi SET niro = "{}" WHERE cid = "{}" AND maghsad = "{}" AND vaziat = "{}"'''.format(newniro,cid,mabda,m))
            conn.commit() 
            if s==0:
                c.execute('''DELETE FROM lashkarkeshi WHERE niro = "{}" AND cid = "{}";'''.format(newniro,cid))
                conn.commit() 
        text = f"""
🔰خاندان : {khandan}
🗺مبدا : {mabda}
🗺مقصد : {maghsad}
کد لشکرکشی: {code}

💢مسیر : 
{mmasir}

🕰زمان رسیدن:{time}
⚔️لیست نیروها: {troopslist}
        """
        context.bot.send_message(chat_id = -1001640007420 , text = text,parse_mode = ParseMode.MARKDOWN)

        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        photo = open(f"lashkar\{eghlim}.jpg",'rb')
        if check>0:
            code = f"9*{code}*1*1"
            keyboard = [[InlineKeyboardButton("🔍بررسی بیشتر" ,callback_data=code)],]
            reply_markup = InlineKeyboardMarkup(keyboard)
            context.bot.send_photo(chat_id=-1001335810093,photo=photo, caption = f"""<b> {emoj}لشکریان ارتش <a href="tg://user?id={cid}">{khandan}</a> از {mabda} حرکت کردند</b>""",parse_mode = ParseMode.HTML,reply_markup=reply_markup)
        else:
            #context.bot.send_photo(chat_id=-1001559813108,photo=photo, caption = f"""<b> 🔰لشکریان ارتش <a href="tg://user?id={cid}">{khandan}</a> از {mabda} حرکت کردند</b>""",parse_mode = ParseMode.HTML)
            pass

        context.bot.send_message(chat_id=cid ,text = f"✅نیروهای شما با موفقیت ارسال شدند" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    else:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"💢لشکرکشی شما تایید نشد" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2



#___________________________ etehad ____________________________#

def davat_etehad(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    firstname = update.message.chat.first_name
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            etehad1 = row[19]
            khandan = row[2]

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[2]) == (text):
            cidd = row[0]
            etehad = row[19]
    if etehad != "a":
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""💢خاندان مورد نظر در حال حاضر در اتحاد دیگری عضو میباشد""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2


    try:
        code = f"2*{etehad1}*1*1"
        keyboard = [[InlineKeyboardButton("✅عضویت در اتحاد" ,callback_data=code)],]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=cidd ,text = f"""
🔰یک دعوتنامه جهت پیوستن به اتحاد <b>{etehad1}</b> توسط <a href="tg://user?id={cid}">{firstname}</a> لرد خاندان {khandan} برای شما ارسال شده است.

❗️در صورت عدم تمایل به عضویت این پیام را نادیده بگیرید

    """ ,reply_markup=reply_markup,parse_mode = ParseMode.HTML )
    except:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""💢هیچ پلیر فعالی برای خاندان مورد نظر یافت نشد!
❗️از وجود خاندان مورد نظر اطمینان حاصل کنید در صورت رفع نشدن مشکل به ادمین بازی مراجعه کنید""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"""✅دعوت نامه با موفقیت ارسال شد""" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2
def etehad_ban(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if (row[2]) == text:
            cid_ban = row[0]
            etehad = row[19]

    sql = '''SELECT * From etehad'''
    recs = c.execute(sql)
    for row in recs:
        if (row[0]) == etehad:
            members = row[1]
            eid = row[2]

    members = eval(members)
    members.remove(text)
    c.execute('''UPDATE etehad SET members = "{}" WHERE name = "{}" '''.format(members,etehad))
    conn.commit() 
    update_information("etehad","a",cid_ban)   

    context.bot.send_message(chat_id = eid ,text = f"لرد خاندان {text} از اتحاد اخراج شد" ,)
    keyboard = [['🔙بازگشت به منوی اصلی'],]
    try:
        context.bot.send_message(chat_id = cid_ban ,text = f"💢شما از اتحاد {etehad} اخراج شدید" ,)
    except:
        pass
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id = cid ,text = f"✅خاندان {text} با موفقیت از اتحاد اخراج شد" ,reply_markup=reply_markup)

    return A2 

def creat_etehad(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            etehad = row[19]
            khandan = row[2]

    sql = '''SELECT * From etehad'''
    recs = c.execute(sql)
    for row in recs:
        if (row[3]) == khandan:
            etehadname = row[0]
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"💢شما موسس اتحاد {etehadname} میباشید بنابراین نمیتوانید اتحاد جدید تاسیس کنید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2


    if etehad != "a":
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"💢شما در حال حاضر عضو یک اتحاد میباشید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2
    list = []
    list.append(khandan)
    c.execute('''INSERT INTO etehad (name,members,admin,win,lose,an1,an2,an3) values("{}","{}","{}","{}","{}","{}","{}","{}");'''.format(text,list,khandan,0,0,["None",0,0,"None"],["None",0,0,"None"],["None",0,0,"None"]))
    c.execute('''UPDATE Information SET {} = "{}" WHERE khandan = "{}" '''.format("etehad",text,khandan))
    conn.commit() 

    context.bot.send_message(chat_id=cid ,text = f"""
✅اتحاد شما با نام {text} تشکیل شد!

<b>❗️موارد زیر را به دقت مطالعه کنید در صورت مشکل داشتن در هر بخش قبل از رفتن به مرحله بعد به ادمین بازی مراجعه کنید:</b>
<code>💢ابتدا یک گروه با نام اتحاد خود تشکیل داده و ربات بازی را در آن عضو کنید
🔻سپس ربات بازی را ادمین کرده و تمام دسترسی های مدیریتی را به ربات بازی برای آن فعال نمایید(حتما دسترسی add new admins را برای ربات فعال کنید)
🔻دستور /getid را در گروه خود ارسال کنید پس از ارسال این دستور ربات چت ایدی گروه را برای شما ارسال خواهد کرد چت ایدی گروه را کپی کنید
</code>

🔰اکنون چت ایدی ای را که از ربات دریافت کرده اید ارسال کنید
    """ ,parse_mode = ParseMode.HTML )
    return B12


def eid_etehad(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]

    c.execute('''UPDATE etehad SET eid = "{}" WHERE admin = "{}" '''.format(text,khandan))
    conn.commit() 



    context.bot.send_message(chat_id=cid ,text = f"""
✅گروه شما با موفقیت ثبت شد

<b>🔰اکنون یک عکس به عنوان نماد و پرچم اتحاد خود ارسال کنید</b>
<i>❗️این عکس قابل تغییر نمیباشد در انتخاب آن دقت کنید</i>
""" ,parse_mode = ParseMode.HTML )
    return C1

def etehad_pic(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    firstname = update.message.chat.first_name
    stat_up(cid)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            etehad = row[19]

    sql = '''SELECT * From etehad'''
    recs = c.execute(sql)
    for row in recs:
        if (row[3]) == khandan:
            eid = row[2]


    try:
        file_id = update.message.photo[-1]
        photo_file = context.bot.getFile(file_id)
        dl = photo_file.download()
        os.rename(dl, f"pics/etehad\{etehad}.png")
        time.sleep(1)
    except:
        pass
    chanel_id = -1001335810093
    photo = open(f"pics/etehad\{etehad}.png", 'rb')
    context.bot.send_photo(chat_id=chanel_id,photo=photo, caption = f"""
🌖 خبر ها حکایت از تشکیل و گردهمایی اتحاد جدیدی با نام <b>{etehad}</b> توسط لرد خاندان <a href="tg://user?id={cid}">{firstname}</a> در سطح وستروس می دهد. ✨

🧩 برای عضویت در این اتحاد لازم است که دعوتنامه ای از سوی رییس آن دریافت کنید.

🐉 @BattleOfthrone
    """,parse_mode = ParseMode.HTML )

    photo = open(f"pics/etehad\{etehad}.png", 'rb')
    context.bot.send_photo(chat_id=eid,photo=photo, caption = f"""
🌖 خبر ها حکایت از تشکیل و گردهمایی اتحاد جدیدی با نام <b>{etehad}</b> توسط لرد خاندان <a href="tg://user?id={cid}">{firstname}</a> در سطح وستروس می دهد. ✨

🧩 برای عضویت در این اتحاد لازم است که دعوتنامه ای از سوی رییس آن دریافت کنید.

🐉 @BattleOfthrone
""",parse_mode = ParseMode.HTML )

    keyboard = [["🔙بازگشت به منوی اصلی"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=cid ,text = f"✅مراحل تاسیس اتحاد با موفقیت به پایان رسید جهت مدیریت اتحاد خود به تالار بزرگ مراجعه کنید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A2







def shortestPath(edges, source, sink):


    a = [1000000,"مسیری یافت نشد"]
    # create a weighted DAG - {node:[(cost,neighbour), ...]}
    graph = collections.defaultdict(list)
    for l, r, c in edges:
        graph[l].append((c,r))
    # create a priority queue and hash set to store visited nodes
    queue, visited = [(0, source, [])], set()
    heapq.heapify(queue)
    # traverse graph with BFS
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        # visit the node if it was not visited before
        if node not in visited:
            visited.add(node)
            path = path + [node]
            # hit the sink
            if node == sink:
                return (cost, path)
            # visit neighbours
            for c, neighbour in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(queue, (cost+c, neighbour, path))
    return a

#___________________________________________#
def Button (update,context):
    query = update.callback_query
    message_id = query.message.message_id
    cid = query.from_user.id
    ciid = query.message.chat_id
    stat_up(ciid)
    data = f"{query.data}"
    dataa = 0
    try:
        dataaa = data.split("*")
        data1 = f"{dataaa[0]}"
        data2 = f"{dataaa[1]}"
        data3 = f"{dataaa[2]}"
        data4 = f"{dataaa[3]}"
    except:
        data1 = 0 
    
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            manbamaghsad = row[5]
            vorodimaghsad = int(row[12])
            khorojimaghsad = int(row[13])
            etehadmahsad = row[19]
            vazmaghsad = row[25]
            cidaslimaghsad = row[28]
    manbamaghsad = eval(manbamaghsad)

    if data1 == "7":
        code = data2
        sql = '''SELECT * From lashkarkeshi WHERE code = "{}"'''.format(code)
        recs = c.execute(sql)
        for row in recs:
            cid_mohajem = row[0]
            khandan_mohajem = row[1]
            niro = row[2]

        niro = eval(niro)
        list = ""
        for key in niro:
            num = niro[key]
            if num>0:
                list = list + f"\n{key}"
        context.bot.answer_callback_query(callback_query_id=query.id, text=list, show_alert=True)


    elif data1 == "9":
        code = data2
        sql = '''SELECT * From lashkarkeshi WHERE code = "{}"'''.format(code)
        recs = c.execute(sql)
        for row in recs:
            masir = eval(row[5])
            vaz = row[8]


        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                buildings = row[6]
        buildings = eval(buildings)
        borj = buildings["👁|برج دیدبانی"]

        if borj>2:
            if vaz == "💢مستقر":
                text=f"💢مستقر در {masir[0]}"
            else:
                text=f"👣در حال حرکت به {masir[0]}"

            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
        else:
            text=f"🚫ابتدا برج دیدبانی خود را ارتقا دهید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)


    elif data1 == "nabard" or data1 == "nabard2":
        print("ok")
        winner = data2
        looser = data3

        sql = '''SELECT * From Information WHERE khandan = "{}"'''.format(looser)
        recs = c.execute(sql)
        for row in recs:
            cid_l = int(row[0])
            lose_num = row[27]
            etehad_l = row[19]


        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == etehad_l:
                eid_l = row[2]
                lose_l = row[5]

        sql = '''SELECT * From Information WHERE khandan = "{}"'''.format(winner)
        recs = c.execute(sql)
        for row in recs:
            cid_w = int(row[0])
            win_num = row[26]
            etehad_w = row[19]
        
        if data1=="nabard2":
            update_information("tejaratmode","None",cid_w)

        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == etehad_w:
                eid_w = row[2]
                win_w = row[4]

        bf = 0 
        if bf == 0:
            print("!")
            try:
                win_num +=1
                update_information("win_n",win_num,cid_w)
                context.bot.send_message(chat_id=cid_w,text = f"""<b>⚔️نیروهای شما در نبرد با نیروهای {looser}پیروز شدند </b>""",parse_mode = ParseMode.HTML )
            except:
                print("error1")

            try:
                win_w += 1
                update_etehad("win",win_w,etehad_w)
                context.bot.send_message(chat_id=eid_w,text = f"""<b>⚔️نیروهای {winner} در نبرد با نیروهای {looser}پیروز شدند </b>""",parse_mode = ParseMode.HTML )

            except:
                print("error2")

            try:
                lose_l +=1
                update_etehad("lose",lose_l,etehad_l)
                context.bot.send_message(chat_id=eid_l,text = f"""<b>⚔️نیروهای {looser} در نبرد با نیروهای {winner} شکست خوردند.</b>""",parse_mode = ParseMode.HTML )

            except:
                print("error3")

            try:
                lose_num += 1
                update_information("lose_n",lose_num,cid_l)
                context.bot.send_message(chat_id=cid_l,text = f"""<b>⚔️نیروهای شما در نبرد با نیروهای {winner} شکست خوردند </b>""",parse_mode = ParseMode.HTML )
            except:
                print("error4")
                
            context.bot.edit_message_text(text=f"""
✅نتیجه نبرد ثبت شد!
پیروز: {winner}
شکست خورده:{looser}
""",chat_id=ciid,message_id=message_id,parse_mode = ParseMode.HTML )


    elif data1 == "hero":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                buildings = row[6]
        buildings = eval(buildings)

        hero_lvl = buildings['⚡️|اقامتگاه شوالیه']
        print(khandan)
        sql = '''SELECT * From hero'''
        recs = c.execute(sql)
        for row in recs:
            print(row[1])
            if row[1] == khandan:
                print("ok")
                name = row[0]
                xp = row[2]
                items = row[3]
                zereh = row[4]
                rast = row[5]
                chap = row[6]
                kolah = row[7]
                kafsh = row[8]
                hp = row[9]
                def_b = row[10]
                att_b = row[11]
                att_p = row[12]
        items = eval(items)
        now = def_b + def_b + att_p
        dif = hero_lvl - now


        if data2 == "change":
            list = []
            for key in items:
                key = f"{key}"
                list.append(key)
            keyboard = []
            for kk in list:
                keyboard.append(InlineKeyboardButton(kk, callback_data=f'hero*change2*{kk}*1'))
            out = [keyboard[i: i+2] for i in range(0, len(keyboard), 2)]
            reply_markup = InlineKeyboardMarkup(out)
            context.bot.edit_message_text(text="قصد استفاده از کدام مورد را دارید؟",chat_id=ciid,message_id=message_id,reply_markup=reply_markup) 

        elif data2 == "change2":
            sql = '''SELECT * From heroE WHERE name = "{}"'''.format(data3)
            recs = c.execute(sql)
            for row in recs:
                no = row[1]
            c.execute('''UPDATE hero SET "{}" = "{}" WHERE khandan = "{}" '''.format(no,data3,khandan))
            conn.commit() 
            context.bot.edit_message_text(text="✅شوالیه شما با موفقیت ارتقا یافت",chat_id=cid,message_id=message_id) 

        elif data2 == "att_p":
            if dif<1:
                text="🚫ابتدا اقامتگاه را ارتقا دهید"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
            else:
                n = att_p+1
                c.execute('''UPDATE hero SET att_p = "{}" WHERE khandan = "{}" '''.format(n,khandan))
                conn.commit() 
                context.bot.edit_message_text(text="✅شوالیه شما با موفقیت ارتقا یافت",chat_id=cid,message_id=message_id) 

        elif data2 == "def_b":
            if dif<1:
                text="🚫ابتدا اقامتگاه را ارتقا دهید"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
            else:
                n = def_b+1
                c.execute('''UPDATE hero SET def_b = "{}" WHERE khandan = "{}" '''.format(n,khandan))
                conn.commit() 
                context.bot.edit_message_text(text="✅شوالیه شما با موفقیت ارتقا یافت",chat_id=cid,message_id=message_id) 

        elif data2 == "att_b":
            if dif<1:
                text="🚫ابتدا اقامتگاه را ارتقا دهید"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)

            else:
                n = att_b+1
                c.execute('''UPDATE hero SET att_b = "{}" WHERE khandan = "{}" '''.format(n,khandan))
                conn.commit() 
                context.bot.edit_message_text(text="✅شوالیه شما با موفقیت ارتقا یافت",chat_id=cid,message_id=message_id) 


    elif data1 == "3":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                khandan = row[2]
                khandanf = row[30]
                ghale = row[3]
                etehad = row[19]

        code = data2
        sql = '''SELECT * From lashkarkeshi WHERE code = "{}"'''.format(code)
        recs = c.execute(sql)
        for row in recs:
            cid_mohajem = row[0]
            khandan_mohajem = row[1]
            masir = row[5]
        masir = eval(masir)
        loc = masir[0]

        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid_mohajem):
                khandan_m = row[2]
                khandan_mf = row[30]

                etehad_mohajem = row[19]

        
        if ghale != loc :
            text="🚫ارتش مورد نظر از قلعه شما عبور کرده است و شما قادر به بستن راه بر روی آن ها نمیباشید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True) 

        elif etehad == etehad_mohajem and etehad != "a":
            text="🚫شما نمیتوانید راه را بر روی متحد خود ببندید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True) 

        else:
            esteghrar(code)
            now = datetime.datetime.now()
            c.execute('''UPDATE lashkarkeshi SET noe = "{}" WHERE code = "{}" '''.format(f"{now}",code))
            conn.commit() 
            chanelid = -1001335810093
            ax2(khandanf,khandan_mf)
            photo = open(f"temp/sad.png", 'rb')


            context.bot.send_photo(chat_id=chanelid,photo=photo,caption = f"""
<b>⛔️ارتش خاندان {khandan} راه را بر روی ارتش {khandan_mohajem} بست!</b>

<i>⚜️خاندان {khandan_mohajem} در صورت تمایل به ادامه مسیر میبایست ابتدا با ارسال دستور حمله ارتش خاندان {khandan} که راه آن ها را مسدود کرده شکست دهد

🔅خاندان {khandan} در صورت تمایل میبایست طی 1 ساعت آینده دستور حمله به ارتش {khandan_mohajem} را صادر کند در غیر این صورت ارتش فوق اجازه حرکت خواهد داشت
</i>
            """,parse_mode = ParseMode.HTML )
            context.bot.edit_message_text(text=f"""
✅ارتش شما با موفقیت راه را بر روی ارتش دشمن بست
        """,chat_id=ciid,message_id=message_id) 
            
            try:
                photo = open(f"temp/sad.png", 'rb')
                context.bot.send_photo(chat_id=cid_mohajem,photo=photo,caption = f"""
<b>⛔️ارتش خاندان {khandan} راه را بر روی ارتش شما بست!</b>

<i>
در صورت تمایل به ادامه مسیر میبایست ابتدا با ارسال دستور حمله ارتش خاندان {khandan} که راه شما  را مسدود کرده شکست دهید

🔅در صورتی که خاندان {khandan} تا یک ساعت آینده دستور حمله ای علیه شما صادر نکند میتوانید بدون درگیری مسیر خود را ادامه دهید
</i>""",parse_mode = ParseMode.HTML )
            except:
                pass



    if data1 == "2":
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == data2:
                eid = row[2]
                members = row[1]

        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                etehad = row[19]
                khandan = row[2]
                buildings = row[6]
        buildings = eval(buildings)
        shora = buildings["🏛|تالار بزرگ"]


        members = eval(members)
        num = len(members)
        if shora <1:
            text="🚫برای عضویت در اتحاد میبایست ابتدا تالار بزرگ را تاسیس کنید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)           
        elif num>150:
            text="🚫متاسفانه ظرفیت اتحاد در حال حاضر تکمیل است لطفا بعدا مجددا تلاش کنید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
        elif etehad != "a":
            text="🚫شما در حال حاضر در اتحاد دیگری عضو هستید ابتدا از اتحاد فعلی خارج شوید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
        else:
            members.append(khandan)
            c.execute('''UPDATE etehad SET members = "{}" WHERE name = "{}" '''.format(members,data2))
            conn.commit() 
            update_information("etehad",data2,cid)
            link = context.bot.create_chat_invite_link(chat_id=eid, member_limit=1,)
            link = link.invite_link

            context.bot.edit_message_text(text=f"""
✅َشما با موفقیت در اتحاد {data2} عضو شدید:

<b>🔗لینک گروه اتحاد: {link}</b>
""",chat_id=cid,message_id=message_id,parse_mode = ParseMode.HTML )

            chanel_id = -1001335810093
            photo = open(f"pics/etehad\{data2}.png", 'rb')
            context.bot.send_photo(chat_id=chanel_id,photo=photo, caption = f"""
🔰خاندان <a href="tg://user?id={cid}">{khandan}</a> به اتحاد <b>{data2}</b> پیوست
            """,parse_mode = ParseMode.HTML )
            photo = open(f"pics/etehad\{data2}.png", 'rb')
            context.bot.send_photo(chat_id=eid,photo=photo, caption = f"""
🔰خاندان <a href="tg://user?id={cid}">{khandan}</a> به اتحاد <b>{data2}</b> پیوست
            """,parse_mode = ParseMode.HTML )





    if data1 == "1":
        sql = '''SELECT * From TejaratCode'''
        recs = c.execute(sql)
        for row in recs:
            if row[1] == data:
                s = 1
                list = row[0]
                mabda = row[2]
                cidmabda = row[3]


        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cidmabda):
                khandanmabda = row[2]
                manbamabda = row[5]
                vorodimabda = int(row[12])
                khorojimabda = int(row[13])
                etehadmabda = row[19]
                vazmabda = row[25]
                cidaslimabda = row[28]

        manbamabda = eval(manbamabda)

        list = eval(list)
        manbaersali = list["manbaersal"]
        meghdarersali = list["meghdarersal"]
        manbadaryafti = list["manbadaryaft"]
        meghdardaryafti = list["meghdardaryaft"]

        meghdarersalie =meghdarersali
        meghdardaryaftie = meghdardaryafti

        if etehadmabda == etehadmahsad:
            if etehadmabda != "a":
                meghdarersalie = meghdarersali/2
                meghdardaryaftie = meghdardaryafti/2

        if cidaslimabda == cidaslimaghsad:
            if cidaslimaghsad != 1:
                meghdarersalie = 0
                meghdardaryaftie = 0

        if cidaslimabda==0 or cidaslimaghsad==0:
            meghdarersalie = 0
            meghdardaryaftie = 0

        if s == 0:
            context.bot.edit_message_text(text="🚫این تجارت از طرف مبدا لغو شده است",chat_id=ciid,message_id=message_id) 

        if data3 == "Laghv":
            context.bot.edit_message_text(text="🚫تجارت با موفقیت لغو شد",chat_id=cid,message_id=message_id) 
            try:
                context.bot.send_message(chat_id = cidmabda , text = f"🚫درخواست تجارت شما توسط {khandan} رد شد!")
            except:
                pass 


        else:
            mabdavorodi = manbamabda[manbadaryafti] + meghdardaryafti
            mabdakhoroji = manbamabda[manbaersali] - meghdarersali
            mabdakhorojiZarfiat = int(khorojimabda) - meghdarersalie
            mabdavorodiZarfiat = int(vorodimabda) - meghdardaryaftie

            maghsadvorodi = manbamaghsad[manbaersali] + meghdarersali
            maghsadkhoroji = manbamaghsad[manbadaryafti] - meghdardaryafti
            maghsadkhorjiZarfiat = int(khorojimaghsad) - meghdardaryaftie
            maghsadvorodiiZarfiat = int(vorodimaghsad) - meghdarersalie

            if mabdakhorojiZarfiat<0 or mabdavorodiZarfiat<0 or maghsadkhorjiZarfiat<0 or maghsadvorodiiZarfiat<0:
                text="🚫ظرفیت کافی جهت تجارت موجود نمیباشد"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
            elif vazmabda == "mohasere" or vazmaghsad == "mohasere":
                text="🚫خاندان مبدا یا مقصد تحت محاصره میباشد"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)            
            elif cidmabda == cid:
                text="🚫شما نمیتوانید با خاندان خود تجارت کنید"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
            elif maghsadkhoroji<0:
                text="🚫شما منبع کافی برای انجام این تجارت را ندارید"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)           
            else:    
                if mabdakhoroji < 0 or maghsadkhoroji<0:
                    if ciid == cid:
                        context.bot.edit_message_text(text="🚫منابع مورد نیاز برای این تجارت موجود نمیباشد",chat_id=cid,message_id=message_id) 
                        try:
                            context.bot.send_message(chat_id = cidmabda , text = f"🚫تجارت  با {khandan} به دلیل کمبود منابع لغو شد")
                        except:
                            pass
                    else:
                        context.bot.send_message(chat_id=cid,text="🚫منابع مورد نیاز برای این تجارت موجود نمیباشد")

                else:
                    manbamabda[manbaersali] = mabdakhoroji
                    manbamabda[manbadaryafti] = mabdavorodi
                    update_information("manba",manbamabda,cidmabda)
                    manbamaghsad[manbadaryafti] = maghsadkhoroji
                    manbamaghsad[manbaersali] = maghsadvorodi
                    update_information("manba",manbamaghsad,cid)

                    update_information("vorodi",mabdavorodiZarfiat,cidmabda)
                    update_information("khoroji",mabdakhorojiZarfiat,cidmabda)

                    update_information("vorodi",maghsadvorodiiZarfiat,cid)
                    update_information("khoroji",maghsadkhorjiZarfiat,cid)
                    
                              
                    context.bot.edit_message_text(text=f"""✅تجارت {khandanmabda} به {khandan}:
        📤ارسال: {meghdarersali} {manbaersali}
        📥دریافت:{meghdardaryafti} {manbadaryafti}
        """,chat_id=ciid,message_id=message_id) 
                    cidlog = -1001602894203

                    context.bot.send_message(chat_id = cidlog ,text = f""" 
        ✅تجارت {khandanmabda} به {khandan}:
        📤ارسال: {meghdarersali} {manbaersali}
        📥دریافت:{meghdardaryafti} {manbadaryafti}
        """)

                    try:
                        context.bot.send_message(chat_id = cidmabda , text = f"""
        ✅تجارت {khandanmabda} به {khandan}:
        📤ارسال: {meghdarersali} {manbaersali}
        📥دریافت:{meghdardaryafti} {manbadaryafti}
                        """)
                    except:
                        pass



#_________________________markaz tahghighat________________________#
def tahghigh_academy(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[3]
            academy = row[23]
            manba = row[5]
            buildings = row[6]
    manba = eval(manba)
    buildings = eval(buildings)
    academy = eval(academy)
    sh = buildings["🗡|کمپ پیاده"]
    sh2 = buildings["🏹|کمپ کماندار"]
    sh3 = buildings["🐎|کمپ سواره"]
    buildings = buildings["⚜️|آکادمی"]
    lvl = academy[text]

    b = 0
    if text == "⚔️|شمشیرزن" or text == "🗡|نیزه دار":
        if lvl>buildings or lvl>3 or lvl+1>sh:
            b = 1
    elif text == "🏹|کماندار":
        if lvl>buildings or lvl>3 or lvl+1>sh2:
            b = 1
    elif text == "🐎|سوارکار":
        if lvl>buildings or lvl>3 or lvl+1>sh3:
            b = 1
    elif text == "💈|دژکوب":
        if buildings<2 or lvl>0:
            b = 1
    elif text == "☄️|منجنیق" :
        if buildings<3 or lvl>0:
            b = 1
    elif text == "🎯|بالیستا" :
        if buildings<4 or lvl>0:
            b = 1
    elif text == "🔱|نیرو ویژه اقلیم":
        if buildings<5 or lvl>0:
            b = 1
    else:
        if lvl>buildings or lvl>3:
            b = 1

    if b == 1:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""⛔️این تحقیق امکان پذیر نیست

⚠️این خطا ممکن است به دلایل زیر رخ داده باشد:
🔻سطح آکادمی شما برای این تحقیق کافی نیست
🔻پیشنیاز این تحقیق برای شما کامل نیست
🔻این نیرو قبلا تحقیق شده است
            
            """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2

    newlvl = lvl+1
    if text == "💈|دژکوب":
        hazine = 5000
    elif text == "☄️|منجنیق" :
        hazine = 7000
    elif text == "🎯|بالیستا" :
        hazine = 8000
    elif text == "🔱نیرو ویژه اقلیم":
        hazine = 10000
    else:
        if newlvl == 1:
            hazine = 3000
        elif newlvl ==2:
            hazine = 5000
        else:
            hazine = 10000

    seke = manba["💰|سکه"]
    newseke = seke - hazine
    if newseke<0:
        keyboard = [["🔙بازگشت به منوی اصلی"]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=cid ,text = f"""⛔️سکه کافی برای این تحقیق را در اختیار ندارید      
            """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
        return A2   
    manba["💰|سکه"] = newseke
    academy[text] = newlvl
    update_information("manba",manba,cid)
    update_information("academy",academy,cid)
    keyboard = keyboardM
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id = cid ,text = f"✅{text} با موفقیت تحقیق شد" ,reply_markup=reply_markup)
    return A3
    


    
#________________________****ertebatat****________________________#
def ertebatat(update,context):
    cid = update.message.chat_id
    text = update.message.text
    stat_up(cid)   

    if text == "🕊توییتر":
        keyboard = [['➡️مرحله بعدی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"""
در *🕊توییتر* با ارسال توییت های خود میتوانید نظرات خود را  با دیگران به اشتراک بگذارید 
⚠️_ استفاده از لحن رسمی در توییتر اجباری است _

* عکس توییت خود را وارد کنید(در صورتی که قصد ارسال عکس ندارید کیبورد مرحله بعد را فشار دهید) * 
        """,
        reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
        return B7
        
    elif text == "📄بیانیه":
        context.bot.send_message(chat_id = cid , text = f"""
*📄بیانیه ها* مانند توییت ها میمانند اما محدودیت کلمه برای آن ها تعریف نشده و میتوانید انتقادات ، جهت گیری ها و ... را از طریق بیانیه ها اعلام کنید  
⚠️_ استفاده از لحن رسمی در بیانیه ها اجباری است _

* بیانیه خود را ارسال کنید:* 
        """,
        reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN)
        return B10



def twitter_pic(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2] 

    try:
        remove(f"temp/TweetPhoto\{khandan}.jpg")
    except:
        pass

    if text == "➡️مرحله بعدی":
        pass
    else:
        file_id = update.message.photo[-1]
        photo_file = context.bot.getFile(file_id)
        dl = photo_file.download()
        os.rename(dl, f"temp/TweetPhoto\{khandan}.jpg")

    context.bot.send_message(chat_id = cid , text = f"""
*متن توییت خود را وارد کنید:*
""",reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN)
    return B8

def bayanie(update,context):
    cid = update.message.chat_id
    stat_up(cid)
    dastresi = "bayanie"
    if dastresi == "bayanie":
        cid = update.message.chat_id
        ciid = update.message.from_user.id
        text = update.message.text 
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                keshvar = row[2] 
        username = update.message.from_user.username
        message = update.message

        # Concatenate the original caption and the formatted suffix

        if message.text:
            text = message.text

            context.bot.send_message(chat_id=-1001322789383,text = f'''
    🗽New Tweet of  {keshvar}

    🗨️ {text}

    ID: @{username}
    ''')              
            
        else:
            text = None


        # Send photo
        if message.photo:
            suffix = "New Tweet Of {}"
            suffix_formatted = suffix.format(keshvar)
            suffix1 = "ID @{}"
            suffix_formatted1 = suffix1.format(username)
            
            media_id = message.photo[-1].file_id
            caption = message.caption
            new_caption = "🗽{}\n🗨️ {}\n{}".format(suffix_formatted, caption,suffix_formatted1)
            
            context.bot.send_photo(chat_id=-1001322789383, photo=media_id, caption=new_caption, caption_entities=message.caption_entities)

        # Send video
        elif message.video:
            suffix = "New Tweet Of {}"
            suffix_formatted = suffix.format(keshvar)
            suffix1 = "ID @{}"
            suffix_formatted1 = suffix1.format(username)
                    
            media_id = message.video.file_id
            caption = message.caption
            new_caption = "🗽{}\n🗨️ {}\n{}".format(suffix_formatted, caption,suffix_formatted1)
                    
            context.bot.send_video(chat_id=-1001322789383, video=media_id, caption=new_caption, caption_entities=message.caption_entities)

        # Send audio
        elif message.audio:
            suffix = "New Tweet Of {}"
            suffix_formatted = suffix.format(keshvar)
            suffix1 = "ID @{}"
            suffix_formatted1 = suffix1.format(username)
                    
            media_id = message.audio.file_id
            caption = message.caption
            new_caption = "🗽{}\n🗨️ {}\n{}".format(suffix_formatted, caption,suffix_formatted1)
                            
            context.bot.send_audio(chat_id=-1001322789383, audio=media_id, caption=new_caption, caption_entities=message.caption_entities)

        # Send document
        elif message.document:
            suffix = "New Tweet Of {}"
            suffix_formatted = suffix.format(keshvar)
            suffix1 = "ID @{}"
            suffix_formatted1 = suffix1.format(username)
                    
            media_id = message.document.file_id
            caption = message.caption
            new_caption = "🗽{}\n🗨️ {}\n{}".format(suffix_formatted, caption,suffix_formatted1)
                            
            context.bot.send_document(chat_id=-1001322789383, document=media_id, caption=new_caption, caption_entities=message.caption_entities)

        # Send animation
        elif message.animation:
            suffix = "New Tweet Of {}"
            suffix_formatted = suffix.format(keshvar)
            suffix1 = "ID @{}"
            suffix_formatted1 = suffix1.format(username)
                    
            media_id = message.animation.file_id
            caption = message.caption
            new_caption = "🗽{}\n🗨️ {}\n{}".format(suffix_formatted, caption,suffix_formatted1)
                            
            context.bot.send_animation(chat_id=-1001322789383, animation=media_id, caption=new_caption, caption_entities=message.caption_entities)


    keyboard = keyboardM
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = cid,
    text = "✅بیانیه شما ارسال شد",reply_markup=reply_markup)
    return A3



def send_twitt(update,context):
    cid = update.message.chat_id
    stat_up(cid)

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2] 
            vip = row[31]

    try:
        remove("prof.jpg")
    except:
        pass

    cid = update.message.chat_id
    photo = context.bot.get_user_profile_photos(update.message.from_user.id).photos[0][-1].file_id
    photo_file = context.bot.getFile(photo)
    dl = photo_file.download()
    os.rename(dl,"prof.jpg")

    twitt = update.message.text
    username = update.message.chat.username
    username = f"{username}"
    firstname = update.message.chat.first_name

    name = f"{firstname}"

    now = datetime.datetime.today()
    mnth = str(now.strftime("%b")) 
    day = str(now.day)
    year = str(now.year)
    hour = str(now.strftime("%I"))
    am = str(now.strftime("%p"))
    min = str(now.minute)
    saat = hour+":"+min+am

    retweets = rand.randint(20,200)
    qut = rand.randint(20,200)
    likes = rand.randint(25,200)

    context.bot.send_message(chat_id=cid,
    text = "⚠️لطفا صبرکنید ، توییت شما تا لحظاتی دیگر ارسال خواهد شد",
    reply_markup=telegram.ReplyKeyboardRemove())
    client = "BOT Twitter"

    try:
        os.rename(f"temp/TweetPhoto\{khandan}.jpg", f"img.jpg")
    except:
        pass
    try:
        driver = webdriver.Chrome()
        driver.get('https://www.tweetgen.com/create/tweet-classic.html')
        driver.maximize_window()
        driver.find_element(by=By.XPATH, value='//*[@id="nameInput"]').send_keys(name)
        driver.find_element(by=By.XPATH, value='//*[@id="usernameInput"]').send_keys(username)
        driver.find_element(by=By.XPATH, value='//*[@id="dayInput"]').send_keys(day)
        driver.find_element(by=By.XPATH, value='//*[@id="monthInput"]').send_keys(mnth)
        driver.find_element(by=By.XPATH, value='//*[@id="yearInput"]').send_keys(year)
        driver.find_element(by=By.XPATH, value='//*[@id="clientInput"]').send_keys(client)
        driver.find_element(by=By.XPATH, value='//*[@id="retweetInput"]').send_keys(retweets)
        driver.find_element(by=By.XPATH, value='//*[@id="quotesInput"]').send_keys(qut)
        driver.find_element(by=By.XPATH, value='//*[@id="likeInput"]').send_keys(likes)
        driver.find_element(by=By.XPATH, value='//*[@id="timeInput"]').send_keys(saat)
        driver.find_element(by=By.XPATH, value='//*[@id="tweetTextInput"]').send_keys(twitt)
        #driver.find_element(by=By.XPATH, value='//*[@id="debunkInput"]').send_keys("توجه داشته باشید صحبت های تسجیس فاقد ارزش میباشد")
        driver.find_element(by=By.XPATH, value='//*[@id="pfpInput"]').send_keys(os.getcwd()+f"\prof.jpg")

        try:
            if vip == "✅":
                driver.find_element(by=By.XPATH, value='//*[@id="verifiedInput"]').click()
        except:
            pass

        try:
            driver.find_element(by=By.XPATH, value='//*[@id="imgInput"]').send_keys(os.getcwd()+f"\img.jpg")
        except:
            print("nashod")
        driver.find_element(by=By.XPATH, value='//*[@id="downloadButton"]').click()
        try:
            driver.find_element(by=By.XPATH, value='/html/body/div/div/div[1]/form/div[1]').click()
        except:
            pass
        with open("temp/TweetPhoto/photo.png", "wb") as photo:
            photo.write(driver.find_element(by=By.XPATH, value='//*[@id="tweetInnerContainer"]').screenshot_as_png)
        photo = open('temp/TweetPhoto/photo.png', 'rb')

        try:
            remove("img.jpg")
        except:
            pass

        photo = open('temp/TweetPhoto/photo.png', 'rb')
        chanelid = -1001322789383

        context.bot.send_photo(chat_id = chanelid , photo = photo )

        keyboard = keyboardM
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = "✅توییت شما ارسال شد",
        reply_markup=reply_markup)
        return A3
    except Exception as e:
        print(e)
        try:
            remove("img.jpg")
        except:
            pass
        
        keyboard = keyboardM
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = "مشکلی در روند ارسال توییت شما ایجاد شد",
        reply_markup=reply_markup)
        return A3


#_______________________________________________________________#

edges1 = [
["Moat Cailin","White Harbor",60],
["White Harbor","Moat Cailin",60],
["Riverrun","Golden Tooth",30],
["Golden Tooth","Riverrun",30],
["Sarsfield","Golden Tooth",15],
["Golden Tooth","Sarsfield",15],
["Qarkash","Qarth",30],
["Qarth","Qarkash",30],
["Qarkash","Port Yhos",60],
["Port Yhos","Qarkash",60],
["Port Yhos","Old Ghis",90],
["Old Ghis","Port Yhos",90],
["Old Ghis","Astapor",60],
["Astapor","Old Ghis",60],
["Yunkai","Astapor",60],
["Astapor","Yunkai",60],
["Yunkai","Meereen",45],
["Meereen","Yunkai",45],
["Port Yhos","Lhazosh",90],
["Lhazosh","Port Yhos",90],
["Lhazosh","Kosrak",30],
["Kosrak","Lhazosh",30],
["Kosrak","Meereen",90],
["Meereen","Kosrak",90],
["Meereen","Tolos",90],
["Tolos","Meereen",90],
["Tolos","E1",90],
["E1","Tolos",90],
["Oros","DE1",90],
["E1","Oros",90],
["Meereen","Vaes Mejhah",45],
["Vaes Mejhah","Meereen",45],
["Vaes Mejhah","Efe",30],
["Efe","Vaes Mejhah",30],
["Vaes Efe","Vaes Dothrak",90],
["Vaes Dothraki","Vaes Efe",90],
["Vaes Lesoe","Vaes Dothrak",60],
["Vaes Dothraki","Vaes Lesoe",60],
["Vaes Mejhah","Vaes Diaf",60],
["Vaes Diaf","Vaes Mejhah",60],
["Vaes Diaf","E1",90],
["Vaes E1","Vaes Diaf",90],
["Vaes Diaf","Vaes Qamayi",60],
["Vaes Qamayi","Vaes Diaf",60],
["Vaes Qamayi","Vaes Khewo",45],
["Vaes Khewo","Vaes Qamayi",45],
["Vaes Kheeo","Qohor",90],
["Vaes Qohor","Vaes Khewo",90],
["Qohor","Ar Noy",15],
["Ar Noy","Qohor",15],
["Qohor","E2",60],
["E2","Qohor",60],
["Ny Sar","E2",15],
["E2","Ny Sar",15],
["Pentos","E2",90],
["E2","Pentos",90],
["Pentos","E3",90],
["E3","Pentos",90],
["Braavos","E3",45],
["E3","Braavos",45],
["Norvos","E3",90],
["E3","Norvos",90],
["Volantis","E1",90],
["E1","Volantis",90],
["Volantis","Sarmell",20],
["Sarmell","Volantis",20],
["Volantis","E4",60],
["E4","Volantis",60],
["The Sorrow","E4",45],
["E4","The Sorrow",45],
["Myr","E4",45],
["E4","Myr",45],
["Pentos","E4",60],
["E4","Pentos",60],
["Shadow Tower","Queenscrown",30],
["Queenscrown","Shadow Tower",30],
["Queenscrown","Castle Black",15],
["Castle Black","Queenscrown",15],
["Eastwatch","Catle Black",30],
["Castle Black","Eastwatch",30],
["Castle Black","W1",90],
["W1","Castle Black",90],
["Last Hearth","W1",90],
["W1","Last Hearth",90],
["Last Hearth","Karhold",90],
["Karhold","Last Hearth",90],
["W2","W1",15],
["W1","W2",15],
["W2","The Dreadfort",90],
["The Dreadfort","W2",90],
["The Dreadfort","Hornwood",90],
["Hornwood","The Dreadfort",90],
["White Harbor","Hornwood",120],
["Hornwood","White Harbor",120],
["Ramsgate","Hornwood",90],
["Hornwood","Ramsgate",90],
["Widows Watch","Ramsgate",60],
["Ramsgate","Widows Watch",60],
["W2","W3",45],
["W3","W2",45],
["W3","W4",45],
["W4","W3",45],
["W4","Hornwood",60],
["Hornwood","W4",60],
["Winterfell","W4",15],
["W4","Winterfell",15],
["Castle Cerwyn","W4",15],
["W4","Castle Cerwyn",15],
["Barrowton","Torrhens Square",90],
["Torrhens Square","Barrowton",90],
["Castle Cerwyn","Torrhens Square",90],
["Torrhens Square","Castle Cerwyn",90],
["W3","Deepwood Motte",120],
["Deepwood Motte","W3",120],
["Castle Cerwyn","Moat Cailin",45],
["Moat Cailin","Castle Cerwyn",45],
["Moat Cailin","Barrowton",90],
["Barrowton","Moat Cailin",90],
["Moat Cailin","W5",45],
["W5","Moat Cailin",45],
["Greywater Watch","W5",45],
["W5","Greywater Watch",45],
["W6","W5",45],
["W5","W6",45],
["W6","The Twins",30],
["The Twins","W6",30],
["Greywater Watch","The Twins",120],
["The Twins","Greywater Watch",120],
["W6","The Twins",45],
["The Twins","W6",45],
["Flints Finger","The Twins",180],
["The Twins","Flints Finger",180],
["Seagard","The Twins",30],
["The Twins","Seagard",30],
["W6","W7",90],
["W7","W6",90],
["Coldwater","W7",30],
["W7","Coldwater",30],
["Hearts Home","W7",30],
["W7","Hearts Home",30],
["Snakewood","W7",30],
["W7","Snakewood",30],
["W6","W8",30],
["W8","W6",30],
["Strongsong","W8",90],
["W8","Strongsong",90],
["Inn At Crossroads","W8",30],
["W8","Inn At Crossroads",30],
["Inn At Crossroads","W10",30],
["W10","Inn At Crossroads",30],
["The Bloody Gate","W10",30],
["W10","The Bloody Gate",30],
["The Bloody Gate","The Eyrie",30],
["The Eyrie","The Bloody Gate",30],
["Redfort","W10",90],
["W10","Redfort",90],
["Redfort","Gulltown",45],
["Gulltown","Redfort",45],
["Runestone","Gulltown",30],
["Gulltown","Runestone",30],
["Redfort","Ironoaks",30],
["Ironoaks","Redfort",30],
["Redfort","Ironoaks",30],
["Ironoaks","Redfort",30],
["Longbow Hall","Ironoaks",90],
["Ironoaks","Longbow Hall",90],
["Longbow Hall","The Eyrie",90],
["The Eyrie","Longbow Hall",90],
["Old Anchor","Ironoaks",45],
["Ironoaks","Old Anchor",45],
["Inn At Crossroads","Harrenhall",30],
["Harrenhall","Inn At Crossroads",30],
["Inn At Crossroads","Wickenden",90],
["Wickenden","Inn At Crossroads",90],
["Inn At Crossroads","Antlers",45],
["Antlers","Inn At Crossroads",45],
["Inn At Crossroads","W11",45],
["W11","Inn At Crossroads",45],
["Rosby","W11",45],
["W11","Rosby",45],
["Rosby","Hayford",15],
["Hayford","Rosby",15],
["Rosby","Duskendale",15],
["Duskendale","Rosby",15],
["Rosby","Antlers",30],
["Antlers","Rosby",30],
["Dyre Den","Maidenpool",30],
["Maidenpool","Dyre Den",30],
["Antlers","Maidenpool",30],
["Maidenpool","Antlers",30],
["Rosby","Kings Landing",30],
["Kings Landing","Rosby",30],
["The Whispers","Kings Landing",60],
["Kings Landing","The Whispers",60],
["Deep Den","W11",60],
["W11","Deep Den",60],
["Cornfield","Silverhill",45],
["Silverhill","Cornfield",45],
["Highgarden","Red Lake",60],
["Red Lake","Highgarden",60],
["Silverhill","Red Lake",60],
["Red Lake","Silverhill",60],
["Silverhill","Bitterbridge",60],
["Bitterbridge","Silverhill",60],
["Silverhill","Bitterbridge",60],
["Bitterbridge","Silverhill",60],
["Silverhill","Goldengrove",60],
["Goldengrove","Silverhill",60],
["Bitterbridge","Tumbleton",60],
["Tumbleton","Bitterbridge",60],
["Deep Den","Silverhill",45],
["Silverhill","Deep Den",45],
["Deep Den","Pinkmaiden",45],
["Pinkmaiden","Deep Den",45],
["Deep Den","Casterly Rock",30],
["Casterly Rock","Deep Den",30],
["Lannisport","Casterly Rock",30],
["Casterly Rock","Lannisport",30],
["Feastfires","Casterly Rock",30],
["Casterly Rock","Feastfires",30],
["Sarsfield","Casterly Rock",30],
["Casterly Rock","Sarsfield",30],
["Sarsfield","Ashemark",10],
["Ashemark","Sarsfield",10],
["Sarsfield","Pinkmaiden",30],
["Pinkmaiden","Sarsfield",30],
["Castamere","Ashemark",30],
["Ashemark","Castamere",30],
["Castamere","The Crag",30],
["The Crag","Castamere",30],
["Banefort","The Crag",45],
["The Crag","Banefort",45],
["Banefort","W12",60],
["W12","Banefort",60],
["Wendish Town","W12",30],
["W12","Wendish Town",30],
["Wendish Town","Oldstones",15],
["Oldstones","Wendish Town",15],
["Wendish Town","Seagard",45],
["Seagard","Wendish Town",45],
["Raventree Hall","Riverrun",30],
["Riverrun","Raventree Hall",30],
["Raventree Hall","W12",30],
["W12","Raventree Hall",30],
["W14","Riverrun",30],
["Riverrun","W14",30],
["W14","Harrenhall",30],
["Harrenhall","W14",30],
["W11","Harrenhall",30],
["Harrenhall","W11",30],
["W14","Stone Hedge",30],
["Stone Hedge","W14",30],
["High Heart","Stone Hedge",30],
["Stone Hedge","High Heart",30],
["High Heart","Acorn Hall",30],
["Acorn Hall","High Heart",30],
["Hornvale","Acorn Hall",30],
["Acorn Hall","Hornvale",30],
["Hornvale","Pinkmaiden",30],
["Pinkmaiden","Hornvale",30],
["Crakehall","Lannisport",30],
["Lannisport","Crakehall",30],
["Crakehall","Cornfield",45],
["Cornfield","Crakehall",45],
["Crakehall","Old Oak",30],
["Old Oak","Crakehall",30],
["Crakehall","Old Oak",30],
["Old Oak","Crakehall",30],
["Red Lake","Old Oak",45],
["Old Oak","Red Lake",45],
["Red Lake","Old Oak",45],
["Old Oak","Red Lake",45],
["Highgarden","Old Oak",45],
["Old Oak","Highgarden",45],
["Highgarden","Goldengrove",45],
["Goldengrove","Highgarden",45],
["Highgarden","Horn Hill",30],
["Horn Hill","Highgarden",30],
["Highgarden","Brightwater Keep",60],
["Brightwater Keep","Highgarden",60],
["Highgarden","Oldtown",45],
["Oldtown","Honeyholt",30],
["Honeyholt","Oldtown",30],
["Brightwater Keep","Honeyholt",30],
["Honeyholt","Brightwater Keep",30],
["Oldtown","Highgarden",45],
["Bandallon","Oldtown",45],
["Oldtown","Bandallon",45],
["Blackcrown","Oldtown",30],
["Oldtown","Blackcrown",30],
["Three Towers","Oldtown",30],
["Oldtown","Three Towers",30],
["Uplands","Oldtown",45],
["Oldtown","Uplands",45],
["Highgarden","Cider Hall",45],
["Cider Hall","Highgarden",45],
["Cider Hall","Longtable",30],
["Longtable","Cider Hall",30],
["Cider Hall","Ashford",30],
["Ashford","Cider Hall",30],
["Highgarden","Bitterbridge",45],
["Bitterbridge","Highgarden",45],
["Longtable","Bitterbridge",30],
["Bitterbridge","Longtable",30],
["Grassy Vale","Bitterbridge",120],
["Bitterbridge","Grassy Vale",120],
["Grassy Vale","Summerhall",60],
["Summerhall","Grassy Vale",60],
["Storms End","Summerhall",45],
["Summerhall","Storms End",45],
["Storms End","Griffins Roost",30],
["Griffins Roost","Storms End",30],
["Storms End","Bronzegate",30],
["Bronzegate","Storms End",30],
["W16","Bronzegate",60],
["Bronzegate","W16",60],
["Storms End","Felwood",45],
["Felwood","Storms End",45],
["Haystack Hall","Bronzegate",30],
["Bronzegate","Haystack Hall",30],
["Haystack Hall","Stonedance",120],
["Stonedance","Haystack Hall",120],
["Sharp Point","Stonedance",30],
["Stonedance","Sharp Point",30],
["Stonehelm","Griffins Roost",60],
["Griffins Roost","Stonehelm",60],
["Stonehelm","Mistwood",60],
["Mistwood","Stonehelm",60],
["Rain House","Mistwood",90],
["Mistwood","Rain House",90],
["Rain House","Mistwood",90],
["Mistwood","Rain House",90],
["Weeoing Town","Mistwood",45],
["Mistwood","Weeoing Town",45],
["W15","Bitterbridge",45],
["Bitterbridge","W15",45],
["W15","Tumbleton",30],
["Tumbleton","W15",30],
["Felwood","Tumbleton",45],
["Tumbleton","Felwood",45],
["W15","W16",30],
["W16","W15",30],
["Kings Landing","W16",30],
["W16","Kings Landing",30],
["Blackhaven","Ashford",120],
["Ashford","Blackhaven",120],
["Blackhaven","Summerhall",45],
["Summerhall","Blackhaven",45],
["Nightsong","Blackhaven",120],
["Blackhaven","Nightsong",120],
["Blackhaven","W17",30],
["W17","Blackhaven",30],
["Three Towers","Sunhouse",90],
["Sunhouse","Three Towers",90],
["Starfall","Sunhouse",90],
["Sunhouse","Starfall",90],
["Starfall","Uplands",60],
["Uplands","Starfall",60],
["Starfall","Blackmont",45],
["Blackmont","Starfall",45],
["Starfall","Sandstone",60],
["Sandstone","Starfall",60],
["Hellholt","Sandstone",45],
["Sandstone","Hellholt",45],
["Hellholt","Skyreach",60],
["Skyreach","Hellholt",60],
["Yronwood","Skyreach",45],
["Skyreach","Yronwood",45],
["Blackmont","Skyreach",45],
["Skyreach","Blackmont",45],
["Vaith","Skyreach",120],
["Skyreach","Vaith",120],
["W19","Skyreach",30],
["Skyreach","W19",30],
["W19","Kingsgrave",30],
["Kingsgrave","W19",30],
["W19","Vultures Roost",30],
["Vultures Roost","W19",30],
["W19","W18",30],
["W18","W19",30],
["W17","W18",30],
["W18","W17",30],
["W18","Wyl",30],
["Wyl","W18",30],
["Yronwood","W18",30],
["W18","Yronwood",30],
["Yronwood","Vaith",90],
["Vaith","Yronwood",90],
["Salt Shore","Vaith",45],
["Vaith","Salt Shore",45],
["Salt Shore","Lemonwood",90],
["Lemonwood","Salt Shore",90],
["Yronwood","The Tor",90],
["The Tor","Yronwood",90],
["Godsgrace","The Tor",45],
["The Tor","Godsgrace",45],
["Godsgrace","W20",45],
["W20","Godsgrace",45],
["Ghost Hill","W20",45],
["W20","Ghost Hill",45],
["Ghost Hill","Sunspear",45],
["Sunspear","Ghost Hill",45],
["Valyria","Tyria",15],
["Tyria","Valyria",15],
["Meereen","Vaes Mejhah",45],
["Vaes Mejhah","Meereen",45],
["Vaes Mejhah","Vaes Efe",30],
["Vaes Efe","Vaes Mejhah",30],
["Vaes Efe","Vaes Dothrak",90],
["Vaes Dothrak","Vaes Efe",90],
["Vaes Leqse","Vaes Dothrak",60],
["Vaes Dothrak","Vaes Leqse",60],
["Vaes Mejhah","Vaes Diaf",60],
["Vaes Diaf","Vaes Mejhah",60],
["Vaes Diaf","E1",90],
["Vaes E1","Vaes Diaf",90],
["Vaes Diaf","Vaes Qamayi",60],
["Vaes Qamayi","Vaes Diaf",60],
["Vaes Qamayi","Vaes Khewo",45],
["Vaes Khewo","Vaes Qamayi",45],
["Vaes Khewo","Qohor",90],
["Qohor","Vaes Khewo",90],
["Qohor","Ar Noy",15],
]





edges2 =[
["Pentos","Tyrosh",90],
["Tyrosh","Pentos",90],
["Braavos","Pentos",120],
["Pentos","Braavos",120],
["Valyria","Tyria",15],
["Tyria","Valyria",15],
["Karhold","D1",60],
["D1","Karhold",60],
["Eastwatch","D1",120],
["D1","Eastwatch",120],
["D1","Widows Watch",120],
["Widows Watch","D1",120],
["Widows Watch","Sisterton",120],
["Sisterton","Widows Watch",120],
["Sisterton","White Harbor",60],
["White Harbor","Sisterton",60],
["Widows Watch","D2",120],
["D2","Widows Watch",120],
["D2","Snakewood",60],
["Snakewood","D2",60],
["Strongsong","Snakewood",60],
["Snakewood","Strongsong",60],
["D2","Runestone",60],
["Runestone","D2",60],
["Braavos","Runestone",120],
["Runestone","Braavos",120],
["Braavos","Lorath",60],
["Lorath","Braavos",60],
["The Whispers","Runestone",60],
["Runestone","The Whispers",60],
["Old Anchor","Runestone",30],
["Runestone","Old Anchor",30],
["The Whispers","Wickenden",60],
["Wickenden","The Whispers",60],
["Wickenden","Maidenpool",30],
["Maidenpool","Wickenden",30],
["The Whispers","Dragonstone",30],
["Dragonstone","The Whispers",30],
["The Whispers","Driftmark",30],
["Driftmark","The Whispers",30],
["Sharp Point","Driftmark",30],
["Driftmark","Sharp Point",30],
["Kings Landing","Driftmark",60],
["Driftmark","Kings Landing",60],
["Sharp Point","Stonedance",30],
["Stonedance","Sharp Point",30],
["Sharp Point","Pentos",120],
["Pentos","Sharp Point",120],
["Stonedance","D3",120],
["D3","Stonedance",120],
["Storms End","D3",60],
["D3","Storms End",60],
["Rain House","D3",60],
["D3","Rain House",60],
["Rain House","D4",60],
["D4","Rain House",60],
["D4","Weeoing Town",60],
["Weeoing Town","D4",60],
["Weeoing Town","Stonehelm",60],
["Stonehelm","Weeoing Town",60],
["Stonehelm","Wyl",60],
["Wyl","Stonehelm",60],
["Ghost Hill","D4",60],
["D4","Ghost Hill",60],
["Ghost Hill","D5",60],
["D5","Ghost Hill",60],
["The Stepstones","D5",60],
["D5","The Stepstones",60],
["Sunspear","D5",60],
["D5","Sunspear",60],
["Sunspear","Lemonwood",60],
["Lemonwood","Sunspear",60],
["Lemonwood","Salt Shore",60],
["Salt Shore","Lemonwood",60],
["Salt Shore","Sunhouse",180],
["Sunhouse","Salt Shore",180],
["Sunhouse","The Arbor",60],
["The Arbor","Sunhouse",60],
["The Arbor","Three Towers",60],
["Three Towers","The Arbor",60],
["Three Towers","Blackcrown",30],
["Blackcrown","Three Towers",30],
["Blackcrown","Bandallon",60],
["Bandallon","Blackcrown",60],
["Bandallon","Crakehall",60],
["Crakehall","Bandallon",60],
["Crakehall","Lannisport",60],
["Lannisport","Crakehall",60],
["Lannisport","Feastfires",30],
["Feastfires","Lannisport",30],
["Feastfires","Faircastle",30],
["Faircastle","Feastfires",30],
["Faircastle","Castamere",30],
["Castamere","Faircastle",30],
["Faircastle","Banefort",60],
["Banefort","Faircastle",60],
["Banefort","Pyke",30],
["Pyke","Banefort",30],
["Harlaw","Lordsport",15],
["Lordsport","Harlaw",15],
["Harlaw","Ten Towers",15],
["Ten Towers","Harlaw",15],
["Pyke","Lordsport",15],
["Lordsport","Pyke",15],
["Lonely Light","Saltcliffe",15],
["Saltcliffe","Lonely Light",15],
["Pyke","Saltcliffe",15],
["Saltcliffe","Pyke",15],
["Lonely Light","Flints Finger",60],
["Flints Finger","Lonely Light",60],
["Lonely Light","Pyke",30],
["Pyke","Lonely Light",30],
["Lonely Light","Saltcliffe",15],
["Saltcliffe","Lonely Light",15],
["Lonely Light","Great Wyk",15],
["Great Wyk","Lonely Light",15],
["Blacktyde","Great Wyk",15],
["Great Wyk","Blacktyde",15],
["Old Wyk","Great Wyk",15],
["Great Wyk","Old Wyk",15],
["Old Wyk","Orkmont",15],
["Orkmont","Old Wyk",15],
["Flints Finger","Bear Island",180],
["Bear Island","Flints Finger",180],
["Bear Island","Deepwood Motte",60],
["Deepwood Motte","Bear Island",60],
["Rain House","Tyrosh",60],
["Tyrosh","Rain House",60],
["Tyrosh","Myr",60],
["Myr","Tyrosh",60],
["Tyrosh","The Stepstones",60],
["The Stepstones","Tyrosh",60],
["The Stepstones","Lys",60],
["Lys","The Stepstones",60],
["Lys","Volantis",120],
["Volantis","Lys",120],
["Volantis","Oros",120],
["Oros","Volantis",120],
["Oros","Tyria",60],
["Tyria","Oros",60],
["Oros","Velos",60],
["Velos","Oros",60],
["Velos","Ghozai",30],
["Ghozai","Velos",30],
["Ghozai","Elyria",60],
["Elyria","Ghozai",60],
["Elyria","Tolos",30],
["Tolos","Elyria",30],
["Tolos","Astapor",120],
["Astapor","Tolos",120],
["Astapor","Yunkai",60],
["Yunkai","Astapor",60],
["Yunkai","Meereen",60],
["Meereen","Yunkai",60],
["Velos","Old Ghis",120],
["Old Ghis","Velos",120],
["Old Ghis","New Ghis",60],
["New Ghis","Old Ghis",60],
["New Ghis","Port Yhos",120],
["Port Yhos","New Ghis",120],
["Port Yhos","Qarkash",60],
["Qarkash","Port Yhos",60],
["Qarkash","Qarth",60],
["Qarth","Qarkash",60],
["Oldtown","Three Towers",15],
["Three Towers","Oldtown",15],
["The Whispers","Gulltown",30],
["Gulltown","The Whispers",30],
["The Whispers","Dyre Den",30],
["Dyre Den","The Whispers",30],
["Pyke","Great Pyke",15],
["Great Pyke","Pyke",15],
["Pyke","Pebbleton",15],
["Pebbleton","Pyke",15],
["Banefort","Wendish Town",30],
["Wendish Town","Banefort",30],
["Seagard","Wendish Town",15],
["Wendish Town","Seagard",15],
["Seagard","Ten Towers",60],
["Ten Towers","Seagard",60],
["Blacktyde","Seagard",30],
["Seagard","Blacktyde",30],
]


edges3 =[
["Pentos","Tyrosh",90],
["Tyrosh","Pentos",90],
["Braavos","Pentos",120],
["Pentos","Braavos",120],
["Valyria","Tyria",15],
["Tyria","Valyria",15],
["Karhold","D1",60],
["D1","Karhold",60],
["Eastwatch","D1",120],
["D1","Eastwatch",120],
["D1","Widows Watch",120],
["Widows Watch","D1",120],
["Widows Watch","Sisterton",120],
["Sisterton","Widows Watch",120],
["Sisterton","White Harbor",60],
["White Harbor","Sisterton",60],
["Widows Watch","D2",120],
["D2","Widows Watch",120],
["D2","Snakewood",60],
["Snakewood","D2",60],
["Strongsong","Snakewood",60],
["Snakewood","Strongsong",60],
["D2","Runestone",60],
["Runestone","D2",60],
["Braavos","Runestone",120],
["Runestone","Braavos",120],
["Braavos","Lorath",60],
["Lorath","Braavos",60],
["The Whispers","Runestone",60],
["Runestone","The Whispers",60],
["Old Anchor","Runestone",30],
["Runestone","Old Anchor",30],
["The Whispers","Wickenden",60],
["Wickenden","The Whispers",60],
["Wickenden","Maidenpool",30],
["Maidenpool","Wickenden",30],
["The Whispers","Dragonstone",30],
["Dragonstone","The Whispers",30],
["The Whispers","Driftmark",30],
["Driftmark","The Whispers",30],
["Sharp Point","Driftmark",30],
["Driftmark","Sharp Point",30],
["Kings Landing","Driftmark",60],
["Driftmark","Kings Landing",60],
["Sharp Point","Stonedance",30],
["Stonedance","Sharp Point",30],
["Sharp Point","Pentos",120],
["Pentos","Sharp Point",120],
["Stonedance","D3",120],
["D3","Stonedance",120],
["Storms End","D3",60],
["D3","Storms End",60],
["Rain House","D3",60],
["D3","Rain House",60],
["Rain House","D4",60],
["D4","Rain House",60],
["D4","Weeoing Town",60],
["Weeoing Town","D4",60],
["Weeoing Town","Stonehelm",60],
["Stonehelm","Weeoing Town",60],
["Stonehelm","Wyl",60],
["Wyl","Stonehelm",60],
["Ghost Hill","D4",60],
["D4","Ghost Hill",60],
["Ghost Hill","D5",60],
["D5","Ghost Hill",60],
["The Stepstones","D5",60],
["D5","The Stepstones",60],
["Sunspear","D5",60],
["D5","Sunspear",60],
["Sunspear","Lemonwood",60],
["Lemonwood","Sunspear",60],
["Lemonwood","Salt Shore",60],
["Salt Shore","Lemonwood",60],
["Salt Shore","Sunhouse",180],
["Sunhouse","Salt Shore",180],
["Sunhouse","The Arbor",60],
["The Arbor","Sunhouse",60],
["The Arbor","Three Towers",60],
["Three Towers","The Arbor",60],
["Three Towers","Blackcrown",30],
["Blackcrown","Three Towers",30],
["Blackcrown","Bandallon",60],
["Bandallon","Blackcrown",60],
["Bandallon","Crakehall",60],
["Crakehall","Bandallon",60],
["Crakehall","Lannisport",60],
["Lannisport","Crakehall",60],
["Lannisport","Feastfires",30],
["Feastfires","Lannisport",30],
["Feastfires","Faircastle",30],
["Faircastle","Feastfires",30],
["Faircastle","Castamere",30],
["Castamere","Faircastle",30],
["Faircastle","Banefort",60],
["Banefort","Faircastle",60],
["Banefort","Pyke",30],
["Pyke","Banefort",30],
["Harlaw","Lordsport",15],
["Lordsport","Harlaw",15],
["Harlaw","Ten Towers",15],
["Ten Towers","Harlaw",15],
["Pyke","Lordsport",15],
["Lordsport","Pyke",15],
["Lonely Light","Saltcliffe",15],
["Saltcliffe","Lonely Light",15],
["Pyke","Saltcliffe",15],
["Saltcliffe","Pyke",15],
["Lonely Light","Flints Finger",60],
["Flints Finger","Lonely Light",60],
["Lonely Light","Pyke",30],
["Pyke","Lonely Light",30],
["Lonely Light","Saltcliffe",15],
["Saltcliffe","Lonely Light",15],
["Lonely Light","Great Wyk",15],
["Great Wyk","Lonely Light",15],
["Blacktyde","Great Wyk",15],
["Great Wyk","Blacktyde",15],
["Old Wyk","Great Wyk",15],
["Great Wyk","Old Wyk",15],
["Old Wyk","Orkmont",15],
["Orkmont","Old Wyk",15],
["Flints Finger","Bear Island",180],
["Bear Island","Flints Finger",180],
["Bear Island","Deepwood Motte",60],
["Deepwood Motte","Bear Island",60],
["Rain House","Tyrosh",60],
["Tyrosh","Rain House",60],
["Tyrosh","Myr",60],
["Myr","Tyrosh",60],
["Tyrosh","The Stepstones",60],
["The Stepstones","Tyrosh",60],
["The Stepstones","Lys",60],
["Lys","The Stepstones",60],
["Lys","Volantis",120],
["Volantis","Lys",120],
["Volantis","Oros",120],
["Oros","Volantis",120],
["Oros","Tyria",60],
["Tyria","Oros",60],
["Oros","Velos",60],
["Velos","Oros",60],
["Velos","Ghozai",30],
["Ghozai","Velos",30],
["Ghozai","Elyria",60],
["Elyria","Ghozai",60],
["Elyria","Tolos",30],
["Tolos","Elyria",30],
["Tolos","Astapor",120],
["Astapor","Tolos",120],
["Astapor","Yunkai",60],
["Yunkai","Astapor",60],
["Yunkai","Meereen",60],
["Meereen","Yunkai",60],
["Velos","Old Ghis",120],
["Old Ghis","Velos",120],
["Old Ghis","New Ghis",60],
["New Ghis","Old Ghis",60],
["New Ghis","Port Yhos",120],
["Port Yhos","New Ghis",120],
["Port Yhos","Qarkash",60],
["Qarkash","Port Yhos",60],
["Qarkash","Qarth",60],
["Qarth","Qarkash",60],
["Oldtown","Three Towers",15],
["Three Towers","Oldtown",15],
["The Whispers","Gulltown",30],
["Gulltown","The Whispers",30],
["The Whispers","Dyre Den",30],
["Dyre Den","The Whispers",30],
["Pyke","Great Pyke",15],
["Great Pyke","Pyke",15],
["Pyke","Pebbleton",15],
["Pebbleton","Pyke",15],
["Banefort","Wendish Town",30],
["Wendish Town","Banefort",30],
["Seagard","Wendish Town",15],
["Wendish Town","Seagard",15],
["Seagard","Ten Towers",60],
["Ten Towers","Seagard",60],
["Blacktyde","Seagard",30],
["Seagard","Blacktyde",30],
["Moat Cailin","White Harbor",60],
["White Harbor","Moat Cailin",60],
["Riverrun","Golden Tooth",30],
["Golden Tooth","Riverrun",30],
["Sarsfield","Golden Tooth",15],
["Golden Tooth","Sarsfield",15],
["Qarkash","Qarth",30],
["Qarth","Qarkash",30],
["Qarkash","Port Yhos",60],
["Port Yhos","Qarkash",60],
["Port Yhos","Old Ghis",90],
["Old Ghis","Port Yhos",90],
["Old Ghis","Astapor",60],
["Astapor","Old Ghis",60],
["Yunkai","Astapor",60],
["Astapor","Yunkai",60],
["Yunkai","Meereen",45],
["Meereen","Yunkai",45],
["Port Yhos","Lhazosh",90],
["Lhazosh","Port Yhos",90],
["Lhazosh","Kosrak",30],
["Kosrak","Lhazosh",30],
["Kosrak","Meereen",90],
["Meereen","Kosrak",90],
["Meereen","Tolos",90],
["Tolos","Meereen",90],
["Tolos","E1",90],
["E1","Tolos",90],
["Oros","DE1",90],
["E1","Oros",90],
["Meereen","Vaes Mejhah",45],
["Vaes Mejhah","Meereen",45],
["Vaes Mejhah","Efe",30],
["Efe","Vaes Mejhah",30],
["Vaes Efe","Vaes Dothrak",90],
["Vaes Dothraki","Vaes Efe",90],
["Vaes Lesoe","Vaes Dothrak",60],
["Vaes Dothraki","Vaes Lesoe",60],
["Vaes Mejhah","Vaes Diaf",60],
["Vaes Diaf","Vaes Mejhah",60],
["Vaes Diaf","E1",90],
["Vaes E1","Vaes Diaf",90],
["Vaes Diaf","Vaes Qamayi",60],
["Vaes Qamayi","Vaes Diaf",60],
["Vaes Qamayi","Vaes Khewo",45],
["Vaes Khewo","Vaes Qamayi",45],
["Vaes Kheeo","Qohor",90],
["Vaes Qohor","Vaes Khewo",90],
["Qohor","Ar Noy",15],
["Ar Noy","Qohor",15],
["Qohor","E2",60],
["E2","Qohor",60],
["Ny Sar","E2",15],
["E2","Ny Sar",15],
["Pentos","E2",90],
["E2","Pentos",90],
["Pentos","E3",90],
["E3","Pentos",90],
["Braavos","E3",45],
["E3","Braavos",45],
["Norvos","E3",90],
["E3","Norvos",90],
["Volantis","E1",90],
["E1","Volantis",90],
["Volantis","Sarmell",20],
["Sarmell","Volantis",20],
["Volantis","E4",60],
["E4","Volantis",60],
["The Sorrow","E4",45],
["E4","The Sorrow",45],
["Myr","E4",45],
["E4","Myr",45],
["Pentos","E4",60],
["E4","Pentos",60],
["Shadow Tower","Queenscrown",30],
["Queenscrown","Shadow Tower",30],
["Queenscrown","Castle Black",15],
["Castle Black","Queenscrown",15],
["Eastwatch","Catle Black",30],
["Castle Black","Eastwatch",30],
["Castle Black","W1",90],
["W1","Castle Black",90],
["Last Hearth","W1",90],
["W1","Last Hearth",90],
["Last Hearth","Karhold",90],
["Karhold","Last Hearth",90],
["W2","W1",15],
["W1","W2",15],
["W2","The Dreadfort",90],
["The Dreadfort","W2",90],
["The Dreadfort","Hornwood",90],
["Hornwood","The Dreadfort",90],
["White Harbor","Hornwood",120],
["Hornwood","White Harbor",120],
["Ramsgate","Hornwood",90],
["Hornwood","Ramsgate",90],
["Widows Watch","Ramsgate",60],
["Ramsgate","Widows Watch",60],
["W2","W3",45],
["W3","W2",45],
["W3","W4",45],
["W4","W3",45],
["W4","Hornwood",60],
["Hornwood","W4",60],
["Winterfell","W4",15],
["W4","Winterfell",15],
["Castle Cerwyn","W4",15],
["W4","Castle Cerwyn",15],
["Barrowton","Torrhens Square",90],
["Torrhens Square","Barrowton",90],
["Castle Cerwyn","Torrhens Square",90],
["Torrhens Square","Castle Cerwyn",90],
["W3","Deepwood Motte",120],
["Deepwood Motte","W3",120],
["Castle Cerwyn","Moat Cailin",45],
["Moat Cailin","Castle Cerwyn",45],
["Moat Cailin","Barrowton",90],
["Barrowton","Moat Cailin",90],
["Moat Cailin","W5",45],
["W5","Moat Cailin",45],
["Greywater Watch","W5",45],
["W5","Greywater Watch",45],
["W6","W5",45],
["W5","W6",45],
["W6","The Twins",30],
["The Twins","W6",30],
["Greywater Watch","The Twins",120],
["The Twins","Greywater Watch",120],
["W6","The Twins",45],
["The Twins","W6",45],
["Flints Finger","The Twins",180],
["The Twins","Flints Finger",180],
["Seagard","The Twins",30],
["The Twins","Seagard",30],
["W6","W7",90],
["W7","W6",90],
["Coldwater","W7",30],
["W7","Coldwater",30],
["Hearts Home","W7",30],
["W7","Hearts Home",30],
["Snakewood","W7",30],
["W7","Snakewood",30],
["W6","W8",30],
["W8","W6",30],
["Strongsong","W8",90],
["W8","Strongsong",90],
["Inn At Crossroads","W8",30],
["W8","Inn At Crossroads",30],
["Inn At Crossroads","W10",30],
["W10","Inn At Crossroads",30],
["The Bloody Gate","W10",30],
["W10","The Bloody Gate",30],
["The Bloody Gate","The Eyrie",30],
["The Eyrie","The Bloody Gate",30],
["Redfort","W10",90],
["W10","Redfort",90],
["Redfort","Gulltown",45],
["Gulltown","Redfort",45],
["Runestone","Gulltown",30],
["Gulltown","Runestone",30],
["Redfort","Ironoaks",30],
["Ironoaks","Redfort",30],
["Redfort","Ironoaks",30],
["Ironoaks","Redfort",30],
["Longbow Hall","Ironoaks",90],
["Ironoaks","Longbow Hall",90],
["Longbow Hall","The Eyrie",90],
["The Eyrie","Longbow Hall",90],
["Old Anchor","Ironoaks",45],
["Ironoaks","Old Anchor",45],
["Inn At Crossroads","Harrenhall",30],
["Harrenhall","Inn At Crossroads",30],
["Inn At Crossroads","Wickenden",90],
["Wickenden","Inn At Crossroads",90],
["Inn At Crossroads","Antlers",45],
["Antlers","Inn At Crossroads",45],
["Inn At Crossroads","W11",45],
["W11","Inn At Crossroads",45],
["Rosby","W11",45],
["W11","Rosby",45],
["Rosby","Hayford",15],
["Hayford","Rosby",15],
["Rosby","Duskendale",15],
["Duskendale","Rosby",15],
["Rosby","Antlers",30],
["Antlers","Rosby",30],
["Dyre Den","Maidenpool",30],
["Maidenpool","Dyre Den",30],
["Antlers","Maidenpool",30],
["Maidenpool","Antlers",30],
["Rosby","Kings Landing",30],
["Kings Landing","Rosby",30],
["The Whispers","Kings Landing",60],
["Kings Landing","The Whispers",60],
["Deep Den","W11",60],
["W11","Deep Den",60],
["Cornfield","Silverhill",45],
["Silverhill","Cornfield",45],
["Highgarden","Red Lake",60],
["Red Lake","Highgarden",60],
["Silverhill","Red Lake",60],
["Red Lake","Silverhill",60],
["Silverhill","Bitterbridge",60],
["Bitterbridge","Silverhill",60],
["Silverhill","Bitterbridge",60],
["Bitterbridge","Silverhill",60],
["Silverhill","Goldengrove",60],
["Goldengrove","Silverhill",60],
["Bitterbridge","Tumbleton",60],
["Tumbleton","Bitterbridge",60],
["Deep Den","Silverhill",45],
["Silverhill","Deep Den",45],
["Deep Den","Pinkmaiden",45],
["Pinkmaiden","Deep Den",45],
["Deep Den","Casterly Rock",30],
["Casterly Rock","Deep Den",30],
["Lannisport","Casterly Rock",30],
["Casterly Rock","Lannisport",30],
["Feastfires","Casterly Rock",30],
["Casterly Rock","Feastfires",30],
["Sarsfield","Casterly Rock",30],
["Casterly Rock","Sarsfield",30],
["Sarsfield","Ashemark",10],
["Ashemark","Sarsfield",10],
["Sarsfield","Pinkmaiden",30],
["Pinkmaiden","Sarsfield",30],
["Castamere","Ashemark",30],
["Ashemark","Castamere",30],
["Castamere","The Crag",30],
["The Crag","Castamere",30],
["Banefort","The Crag",45],
["The Crag","Banefort",45],
["Banefort","W12",60],
["W12","Banefort",60],
["Wendish Town","W12",30],
["W12","Wendish Town",30],
["Wendish Town","Oldstones",15],
["Oldstones","Wendish Town",15],
["Wendish Town","Seagard",45],
["Seagard","Wendish Town",45],
["Raventree Hall","Riverrun",30],
["Riverrun","Raventree Hall",30],
["Raventree Hall","W12",30],
["W12","Raventree Hall",30],
["W14","Riverrun",30],
["Riverrun","W14",30],
["W14","Harrenhall",30],
["Harrenhall","W14",30],
["W11","Harrenhall",30],
["Harrenhall","W11",30],
["W14","Stone Hedge",30],
["Stone Hedge","W14",30],
["High Heart","Stone Hedge",30],
["Stone Hedge","High Heart",30],
["High Heart","Acorn Hall",30],
["Acorn Hall","High Heart",30],
["Hornvale","Acorn Hall",30],
["Acorn Hall","Hornvale",30],
["Hornvale","Pinkmaiden",30],
["Pinkmaiden","Hornvale",30],
["Crakehall","Lannisport",30],
["Lannisport","Crakehall",30],
["Crakehall","Cornfield",45],
["Cornfield","Crakehall",45],
["Crakehall","Old Oak",30],
["Old Oak","Crakehall",30],
["Crakehall","Old Oak",30],
["Old Oak","Crakehall",30],
["Red Lake","Old Oak",45],
["Old Oak","Red Lake",45],
["Red Lake","Old Oak",45],
["Old Oak","Red Lake",45],
["Highgarden","Old Oak",45],
["Old Oak","Highgarden",45],
["Highgarden","Goldengrove",45],
["Goldengrove","Highgarden",45],
["Highgarden","Horn Hill",30],
["Horn Hill","Highgarden",30],
["Highgarden","Brightwater Keep",60],
["Brightwater Keep","Highgarden",60],
["Highgarden","Oldtown",45],
["Oldtown","Honeyholt",30],
["Honeyholt","Oldtown",30],
["Brightwater Keep","Honeyholt",30],
["Honeyholt","Brightwater Keep",30],
["Oldtown","Highgarden",45],
["Bandallon","Oldtown",45],
["Oldtown","Bandallon",45],
["Blackcrown","Oldtown",30],
["Oldtown","Blackcrown",30],
["Three Towers","Oldtown",30],
["Oldtown","Three Towers",30],
["Uplands","Oldtown",45],
["Oldtown","Uplands",45],
["Highgarden","Cider Hall",45],
["Cider Hall","Highgarden",45],
["Cider Hall","Longtable",30],
["Longtable","Cider Hall",30],
["Cider Hall","Ashford",30],
["Ashford","Cider Hall",30],
["Highgarden","Bitterbridge",45],
["Bitterbridge","Highgarden",45],
["Longtable","Bitterbridge",30],
["Bitterbridge","Longtable",30],
["Grassy Vale","Bitterbridge",120],
["Bitterbridge","Grassy Vale",120],
["Grassy Vale","Summerhall",60],
["Summerhall","Grassy Vale",60],
["Storms End","Summerhall",45],
["Summerhall","Storms End",45],
["Storms End","Griffins Roost",30],
["Griffins Roost","Storms End",30],
["Storms End","Bronzegate",30],
["Bronzegate","Storms End",30],
["W16","Bronzegate",60],
["Bronzegate","W16",60],
["Storms End","Felwood",45],
["Felwood","Storms End",45],
["Haystack Hall","Bronzegate",30],
["Bronzegate","Haystack Hall",30],
["Haystack Hall","Stonedance",120],
["Stonedance","Haystack Hall",120],
["Sharp Point","Stonedance",30],
["Stonedance","Sharp Point",30],
["Stonehelm","Griffins Roost",60],





["Griffins Roost","Stonehelm",60],
["Stonehelm","Mistwood",60],
["Mistwood","Stonehelm",60],
["Rain House","Mistwood",90],
["Mistwood","Rain House",90],
["Rain House","Mistwood",90],
["Mistwood","Rain House",90],
["Weeoing Town","Mistwood",45],
["Mistwood","Weeoing Town",45],
["W15","Bitterbridge",45],
["Bitterbridge","W15",45],
["W15","Tumbleton",30],
["Tumbleton","W15",30],
["Felwood","Tumbleton",45],
["Tumbleton","Felwood",45],
["W15","W16",30],
["W16","W15",30],
["Kings Landing","W16",30],
["W16","Kings Landing",30],
["Blackhaven","Ashford",120],
["Ashford","Blackhaven",120],
["Blackhaven","Summerhall",45],
["Summerhall","Blackhaven",45],
["Nightsong","Blackhaven",120],
["Blackhaven","Nightsong",120],
["Blackhaven","W17",30],
["W17","Blackhaven",30],
["Three Towers","Sunhouse",90],
["Sunhouse","Three Towers",90],
["Starfall","Sunhouse",90],
["Sunhouse","Starfall",90],
["Starfall","Uplands",60],
["Uplands","Starfall",60],
["Starfall","Blackmont",45],
["Blackmont","Starfall",45],
["Starfall","Sandstone",60],
["Sandstone","Starfall",60],
["Hellholt","Sandstone",45],
["Sandstone","Hellholt",45],
["Hellholt","Skyreach",60],
["Skyreach","Hellholt",60],
["Yronwood","Skyreach",45],
["Skyreach","Yronwood",45],
["Blackmont","Skyreach",45],
["Skyreach","Blackmont",45],
["Vaith","Skyreach",120],
["Skyreach","Vaith",120],
["W19","Skyreach",30],
["Skyreach","W19",30],
["W19","Kingsgrave",30],
["Kingsgrave","W19",30],
["W19","Vultures Roost",30],
["Vultures Roost","W19",30],
["W19","W18",30],
["W18","W19",30],
["W17","W18",30],
["W18","W17",30],
["W18","Wyl",30],
["Wyl","W18",30],
["Yronwood","W18",30],
["W18","Yronwood",30],
["Yronwood","Vaith",90],
["Vaith","Yronwood",90],
["Salt Shore","Vaith",45],
["Vaith","Salt Shore",45],
["Salt Shore","Lemonwood",90],
["Lemonwood","Salt Shore",90],
["Yronwood","The Tor",90],
["The Tor","Yronwood",90],
["Godsgrace","The Tor",45],
["The Tor","Godsgrace",45],
["Godsgrace","W20",45],
["W20","Godsgrace",45],
["Ghost Hill","W20",45],
["W20","Ghost Hill",45],
["Ghost Hill","Sunspear",45],
["Sunspear","Ghost Hill",45],
["Valyria","Tyria",15],
["Tyria","Valyria",15],
["Meereen","Vaes Mejhah",45],
["Vaes Mejhah","Meereen",45],
["Vaes Mejhah","Vaes Efe",30],
["Vaes Efe","Vaes Mejhah",30],
["Vaes Efe","Vaes Dothrak",90],
["Vaes Dothrak","Vaes Efe",90],
["Vaes Leqse","Vaes Dothrak",60],
["Vaes Dothrak","Vaes Leqse",60],
["Vaes Mejhah","Vaes Diaf",60],
["Vaes Diaf","Vaes Mejhah",60],
["Vaes Diaf","E1",90],
["Vaes E1","Vaes Diaf",90],
["Vaes Diaf","Vaes Qamayi",60],
["Vaes Qamayi","Vaes Diaf",60],
["Vaes Qamayi","Vaes Khewo",45],
["Vaes Khewo","Vaes Qamayi",45],
["Vaes Khewo","Qohor",90],
["Qohor","Vaes Khewo",90],
["Qohor","Ar Noy",15],

]
#________________________****Cancel****________________________#

def cancel(update,context):
    cid = update.message.chat_id
    context.bot.send_message(chat_id=cid , text = 'Bye! I hope we can talk again some day.')

  
    return ConversationHandler.END
#______________________________________________________________#

#__________________**CONVERSATIONHANDLER**____________________#
conv_handler = ConversationHandler(

	entry_points=[CommandHandler('start' , start),
    ],
    
    

	states={

        A1 : [MessageHandler(Filters.text & ~Filters.command, start)],
        A2 : [MessageHandler(Filters.text & ~Filters.command, menu)],
        A3 : [MessageHandler(Filters.text & ~Filters.command, tasmim)],
        A4 : [MessageHandler(Filters.text & ~Filters.command, upgrade)],
        A5 : [MessageHandler(Filters.text & ~Filters.command, upgrade2)],
        A6 : [MessageHandler(Filters.text & ~Filters.command, manbaersali)],
        A7 : [MessageHandler(Filters.text & ~Filters.command, meghdarersali)],
        A8 : [MessageHandler(Filters.text & ~Filters.command, manbadaryafti)],
        A9 : [MessageHandler(Filters.text & ~Filters.command, meghdardaryafti)],
        A10 : [MessageHandler(Filters.text & ~Filters.command, nezhadtejarat)],
        A11 : [MessageHandler(Filters.text & ~Filters.command, tejaratfinal)],
        A12 : [MessageHandler(Filters.text & ~Filters.command, find_niro)],
        B1 : [MessageHandler(Filters.text & ~Filters.command, new_artesh)],
        B2 : [MessageHandler(Filters.text & ~Filters.command, khandan_lashkarkeshi)],
        B3 : [MessageHandler(Filters.text & ~Filters.command, masirlashkarkeshi)],
        B4 : [MessageHandler(Filters.text & ~Filters.command, final_lashkarkeshi)],
        B5 : [MessageHandler(Filters.text & ~Filters.command, register)],
        B6 : [MessageHandler(Filters.text & ~Filters.command, ertebatat)],
        B7 : [MessageHandler(Filters.all & ~Filters.command, twitter_pic)],
        B8 : [MessageHandler(Filters.text & ~Filters.command, send_twitt)],
        B10 : [MessageHandler(Filters.all & ~Filters.command, bayanie)],
        B11 : [MessageHandler(Filters.all & ~Filters.command, creat_etehad)],
        B12 : [MessageHandler(Filters.all & ~Filters.command, eid_etehad)],
        C1 : [MessageHandler(Filters.all & ~Filters.command, etehad_pic)],
        C2 : [MessageHandler(Filters.all & ~Filters.command, davat_etehad)],
        C3 : [MessageHandler(Filters.all & ~Filters.command, etehad_ban)],
        C4 : [MessageHandler(Filters.all & ~Filters.command, sarmaye_gozari)],
        C5 : [MessageHandler(Filters.all & ~Filters.command, hafte_sarmayegozari)],
        C6 : [MessageHandler(Filters.all & ~Filters.command, vam)],
        C7 : [MessageHandler(Filters.all & ~Filters.command, pardakht_vam)],
        C8 : [MessageHandler(Filters.all & ~Filters.command, tahghigh_academy)],
        C9 : [MessageHandler(Filters.all & ~Filters.command, co9)],
        C10 : [MessageHandler(Filters.all & ~Filters.command, sakhtniro)],
        C11 : [MessageHandler(Filters.all & ~Filters.command, sakht_niro2)],
        C12 : [MessageHandler(Filters.all & ~Filters.command, co12)],
        G1 : [MessageHandler(Filters.all & ~Filters.command, admini)],
        G2 : [MessageHandler(Filters.all & ~Filters.command, edit1)],
        G3 : [MessageHandler(Filters.all & ~Filters.command, edit2)],
        G4 : [MessageHandler(Filters.all & ~Filters.command, go4)],
        G5 : [MessageHandler(Filters.all & ~Filters.command, go5)],
        G6 : [MessageHandler(Filters.all & ~Filters.command, go6)],
        G7 : [MessageHandler(Filters.all & ~Filters.command, go7)],
        G8 : [MessageHandler(Filters.all & ~Filters.command, go8)],
        G9 : [MessageHandler(Filters.all & ~Filters.command, go9)],
        G10 : [MessageHandler(Filters.all & ~Filters.command, go10)],



    },

	fallbacks=[CommandHandler('start' , start)
    ,CommandHandler('cancel' , cancel)]

	)
#______________________________________________________________#








#________________________****DISPATCHERS****________________________#

updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(CommandHandler('getid' , getid))
updater.dispatcher.add_handler(CommandHandler('cancel' , cancel))
updater.dispatcher.add_handler(CommandHandler('khoroj' , khoroj))
updater.dispatcher.add_handler(CommandHandler('radar_func' , radar_func))
updater.dispatcher.add_handler(CallbackQueryHandler(Button))

updater.start_polling()
updater.idle()


