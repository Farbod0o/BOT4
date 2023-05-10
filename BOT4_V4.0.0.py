#__________________******Libraries******____________________
from ast import Return
import re
import collections
import heapq
import qrcode
import shutil
from sqlite3.dbapi2 import enable_callback_tracebacks
import requests
import telegram
from telegram.error import RetryAfter
from telegram.ext import Updater , CommandHandler
from telegram import ParseMode
from telegram.ext import MessageHandler , Filters
from telegram.ext import CallbackQueryHandler
from telegram.chataction import ChatAction
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardMarkup 
from telegram import InlineKeyboardButton , InlineKeyboardMarkup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random as rand
import datetime
import os
import string
import textwrap
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image , ImageOps
import arabic_reshaper
from bidi.algorithm import get_display
import textwrap
import time
import datetime
import sqlite3
import os
import emoji 
from os import remove
import logging
from selenium.webdriver.common.by import By

#__________________________________________________________________________#


#________________________****BOT SETTINGS****________________________#

#_توکن ربات:
updater = Updater("5396560558:AAGC6x4NWQ2aZSNpS8V9HvA1D_xvSQH9zUg")
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

def insert_Information(khandan,eghlim,cid,user,manba,buildings,troops,vorodi,khoroji,ghale,buildings2):
    c.execute('''INSERT INTO Information (khandan,eghlim,cid,name,manba,buildings,buildings2,dastresi,troops,vorodi,khoroji,ghale,etehad,sarmaye,vam,tamrin,knight) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(khandan,eghlim,cid,user,manba,buildings,buildings2,"all",troops,"0","0",ghale,"a","[]","[]","{'khali':0,'hojom':0,'defpiyade':0,'defsavare':0}","{'name':0,'lvl':0,'xp':0}"))
    #c.execute('''UPDATE Information SET manba1 = "{}" WHERE keshvar = "{}" '''.format(manba1,keshvar))
    conn.commit() 



#_________________________________________________________________#


def getid (update,context):
    name = update.message.chat.title
    cid = update.message.chat_id
    context.bot.send_message(chat_id = cid , text = f"""
<b>👁‍🗨نام گروه : {name}</b>
➿چت ایدی: <code>{cid}</code>"""
,parse_mode = ParseMode.HTML)





def start (update,context):
    print("hi")
    gid = -1001185952954
    cid = update.message.chat_id
    first_name = update.message.chat.first_name
    ozviat = context.bot.get_chat_member(chat_id=gid,user_id = cid)
    dd = ozviat.status
    last_name = update.message.chat.last_name
    if last_name == "None":
        last_name = ""

    if dd == "left":
            keyboard = [[InlineKeyboardButton("عضو شوید" ,url="https://t.me/TeleeGames")],  
            [InlineKeyboardButton("✅عضو شدم" ,url="https://t.me/BOPGamebot?start")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            photo = open('Pictures/TeleGames Poster 2.jpg','rb')
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
        photo = open('banner.jpg','rb')
        context.bot.send_photo(chat_id = cid , photo = photo , caption = f"""
        👾سلام <b>لرد {first_name}</b> ، به <b> بتل اف ترونز</b> خوش آمدید!
            
▪️از امروز بنده مشاور شما در اداره کشور خواهم بود تا بتوانیم در زمینه های نظامی اقتصادی و آموزشی باعث پیشرفت خاندان خود باشیم هر چند این مسیر طولانی و نیازمند بردباری شماست اما من معتقدم که با کمک یکدیگر میتوانیم موفق شویم
    
🔐*در ابتدا کدی که از ادمین بازی دریافت کرده اید را وارد کنید این کد مجوز ورود شما به مراحل بعد میباشد*

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

    #دریافت عکس پروفایل کاربر
    photo = context.bot.get_user_profile_photos(update.message.from_user.id).photos[0][-1].file_id
    photo_file = context.bot.getFile(photo)
    dl = photo_file.download()
    os.rename(dl,f"{khandan}.png")
    os.rename(f"{khandan}.png",f"prof\{khandan}.png")
    
    manabe = {"👥جمعیت":0,"👥جمعیت بیکار":0,'💰|سکه': 10000, '🔗|آهن': 10000, '⛰|سنگ': 10000, '🌲|چوب': 10000, '🏅|طلا': 10000, '🌾|گندم': 10000, '🐄|گاو': 10000, '🏉|چرم': 10000, '🥩|گوشت': 10000, '🏛|مرمر': 10000, '🍇|انگور': 10000, '🍷|شراب': 10000, '👚|لباس': 10000, }
    b_list = {'🏰قلعه':0 , '🏕|کمپ ویژه':0, '🏟|میدان تمرین':0 ,'🐉|گودال اژدها':0 , '⚓️|بندر':0 , '⛩|ورودی':0 ,
        '⚜️|آکادمی':0 , '👁|برج دیدبانی':0,'⚡️|اقامتگاه شوالیه':0 , '❤️|کمپ مجروحین':0 , '🗡|کمپ پیاده':0 ,
        '🏹|کمپ کماندار':0 , '🐎|کمپ سواره':0, '☄️|کارگاه ادوات':0, '🎋|درخت نیایش':0 ,
        '🏛|تالار بزرگ':0 , '💰|خزانه':0 , '🏦|ایرون بانک':0 , '™️|بازارچه':0,} 

    t_list = {"⚔️|شمشیرزن":0 , "🗡|نیزه دار":0 , "🐎|سوارکار":0,"🏹|کماندار":0,"👀|جاسوس":0,"👣|راهزن":0,"🛡|نگهبان":0,"🛶|کشتی":0,"⛵️|کشتی جنگی":0,"☄️|منجنیق":0,"💈|دژکوب":0,"🎯|بالیستا":0,"⚡️|شوالیه":0}
    b2_list = {'🔗|معدن آهن': 0, '⛰|معدن سنگ': 0, '🌲|چوب بری': 2, '🏅|معدن طلا': 0, '🌾|مزرعه': 2, '🐄|دامداری': 0, '🔪|کشتارگاه': 0, '👝|دباغی': 0, '🏛|معدن مرمر': 0, '🗿|سنگ تراشی': 0, '🍇|تاکستان': 0, '🍷|شراب گیری': 0, '👚|خیاطی': 0}
    insert_Information(khandan,eghlim,cid,namee,manabe,b_list,t_list,"0","0",ghale,b2_list)


    #اضافه کردن اطلاعات به عکس بازی
    shutil.copy('raw.png', f'base/{khandan}.png')
    photo = Image.open(f'base/{khandan}.png')
    myFont = ImageFont.truetype('fonts/Metamorphous.ttf', 24)
    d1 = ImageDraw.Draw(photo)
    d1.text((1675,1250),ghale, font=myFont, fill =(255, 255, 255),anchor="mm")
    d1.text((1675,1279),khandan, font=myFont, fill =(255, 255, 255),anchor="mm")
    d1.text((175,25),eghlim, font=myFont, fill =(255, 255, 255),anchor="mm")

    try:
        mask = Image.open('elements\profile_mask.png').convert('L')
        im = Image.open(f'prof\{khandan}.png')
        output = ImageOps.fit(im, mask.size, centering=(1, 1))
        output.putalpha(mask)
        output = output.resize((115, 115))
        output.save('output.png')
        watermark = Image.open(f'output.png').convert("RGBA")
        try:
            photo.paste(watermark, (1336,1181), watermark)
        except:
            pass
    except:
        pass

    photo.save(f'base/{khandan}.png')
    photo = Image.open(f'base/{khandan}.png').convert("RGBA")
    watermark = Image.open("1.png").convert("RGBA")
    photo.paste(watermark, (1326,1181), watermark)
    photo.save(f'base/{khandan}.png')

    keyboard = [
        ['🔁ادامه']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)

    context.bot.send_message(chat_id = cid , text = f"""
<b> 🔰شما به عنوان لرد {khandan} از قلعه {ghale} واقع در {eghlim} ثبت شدید </b>
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
    return A2



def menu(update,context):
    cid = update.message.chat_id

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]  

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
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        photo = open(f'base\{khandan}.png','rb')
        context.bot.send_photo(chat_id = cid , photo = photo , caption = f"🔻منوی موردنظر را انتخاب کنید",
        reply_markup=reply_markup)
        #context.bot.send_message(chat_id = cid ,
        #text = "⛔️menu",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3




def tasmim(update,context):
    cid = update.message.chat_id
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



    if text == "admin":
        keyboard = [
        ['backup','🔝ساختمان های نظامی'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

        context.bot.send_message(chat_id = cid , text = f"""      
🔻در حال حاضر قصد ورود به کدام بخش را دارید؟     
        """,
        reply_markup=reply_markup)
        return A3

    elif text == "🕊مرکز ارتباطات":
        keyboard = [
        ['🕊توییتر','📄بیانیه'],
        ['🌐ارسال فایل'],
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
        ['🏟|میدان تمرین','❤️|کمپ مجروحین'],
        ['👁|برج دیدبانی','⛩|ورودی'],
        ['🗺لشکرکشی','⚔️|دستور حمله'],
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
        aks = open(f'aks\sakhtniro.png','rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = """<b>🔳قصد تربیت یا ساخت کدام نیرو را دارید?</b>
        """,
        reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return C10


    elif text == '🏕|کمپ نظامی':
        txt = """
🏕کمپ های نظامی:
در این بخش میتوانید ساختمان هایی که به واسطه آن نیروهای نظامی خود را ساخته و تربیت کرده ارتقا دهید

🔻قصد دارید کدام ساختمان زیر را ارتقا دهید؟"""
        keyboard = [
        ['🗡|کمپ پیاده','🏹|کمپ کماندار' , '🐎|کمپ سواره'],['☄️|کارگاه ادوات','🏕|کمپ ویژه',"⚓️|بندر"],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\camp.png','rb')
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
        aks = open(f'aks\❤️کمپ مجروحین.png','rb')
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
        aks = open(f'aks\👁برج دیدبانی.png','rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = txt ,reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4


    elif text == "🏰مرکز شهر":
        keyboard = [
        ['🔝منابع','™️|بازارچه',],
        ['🏛|تالار بزرگ','🎋|درخت نیایش'],
        ["💰|خزانه",'🏦|ایرون بانک'],
        ['🔪|کشتارگاه','🍷|شراب‌ گیری'],
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
            print("a")
            aks = open(f'aks\🍷شراب گیری.png','rb')
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




    elif text == '🎋|درخت نیایش':
        update_information("temp1",'🎋|درخت نیایش',cid)
        keyboard = [
        ['✅ارتقا درخت نیایش',],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\🎋درخت نیایش.png','rb')
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
        aks = open(f'aks\⚜️آکادمی.png','rb')
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
            if key == "💈دژکوب":
                if buildings>1 and lvl<1:
                    list.append(key)
            elif key == "☄️منجنیق" :
                if buildings>2 and lvl<1:
                    list.append(key)
            elif key == "🎯بالیستا" :
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


    elif text == "🗺لشکرکشی":
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
        aks = open(f'aks\🏟میدان تمرین.png','rb')
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
با ارتقا هر سطح میدان تمرین میتوانید یکی از موارد قدرت هجومی،قدرت دفاع در مقابل پیاده نظام یا قدرت دفاع در مقابل سواره نظام را یک درصد بهبود دهید

❗️محدودیت ارتقا این ساختمان ۱۰سطح میباشد
""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4

    elif text == "⛩|ورودی":
        update_information("temp1",text,cid)
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\⛩ورودی.png','rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"""
⛩ورودی شهر میتواند از قلمرو شما حفاظت کند. دیوار ها و ورودی قلعه اولین و یکی از مهمترین خطوط دفاعی شما در مقابل دشمن هستند با ارتقا دیوار ها و ورودی های قلعه نفوذ به قلعه شما سخت تر خواهد شد برای نابود کردن دیوار ها و ورودی های قلعه نیاز به ابزارالات جنگی سنگین میباشد.

🔸هر لول ارتقا دیوار 10 درصد قدرت دفاعی نیروهای شما را افزایش میدهد(نهایتا ۳۰درصد)

❗️شما میتوانید از ویژگی های واقعی قلعه های خود در سناریوهای نبرد خود استفاده کنید. برای استفاده از این ویژگی مستندات خود را از منابع قابل اعتماد دنیای نغمه ارائه کنید

""",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4

    elif text == "🏛|تالار بزرگ":
        keyboard = [
        ['✔️تاسیس اتحاد','🔗دعوت به اتحاد'],['❌خروج از اتحاد','🚫اخراج از اتحاد'],['🏆پروفایل اتحاد','👁‍🗨مشاهده اتحادها'],['🔝ارتقا تالار بزرگ']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\🏛تالار بزرگ.png','rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A3


    elif text == "❌خروج از اتحاد":
        text = f"آیا مطمئن هستید که قصد دارید اتحاد خود را ترک کنید؟"
        keyboard = [['⛔️خروج'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A3

    elif text == "🚫اخراج از اتحاد":
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
        aks = open(f'aks\🏦ایرون بانک.png','rb')
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
        """,parse_mode = ParseMode.HTML)
        return C6


    elif text == "💰|خزانه":
        update_information("temp1",text,cid)
        keyboard = [
        ['💱سرمایه گذاری','🔝ارتقا خرانه'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\💰خزانه.png','rb')
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

""",parse_mode = ParseMode.HTML)
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


    elif text == '⚡️|اقامتگاه شوالیه':
        keyboard = [
        ['✅ارتقا'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\™️بازارچه.png','rb')
        context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"🔻منو مورد نظر را انتخاب کنید",reply_markup=reply_markup,parse_mode = ParseMode.HTML)
        return A4



    elif text == "™️|بازارچه":
        keyboard = [
        ['📦تجارت','🔝ارتقا بازارچه'],
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        aks = open(f'aks\™️بازارچه.png','rb')
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
        new_list = [list[i:i+3] for i in range(0, len(list), 3)]
        keyboard = new_list
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid , text = f"🔻گزینه موردنظر را انتخاب کنید",
        reply_markup=reply_markup)
        return A4
            
    elif text == "🔘مشاهده دارایی":
        keyboard = [
        ['⛲️دارایی اقتصادی','⚔️دارایی نظامی'],
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
            a = f"{key}:{troops[key]}"
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
<code>{buildingslist}</code>

<b>~ ~ ~「 نیرو ها 」~ ~ ~</b>
<code>{troopslist}</code>


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
            elif key == '🗡|کمپ پیاده' or key == '🏹کمپ کماندار' or key =='☄️|کارگاه ادوات':
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
🏰قلعه: {ghalelvl}
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










def co9(update,context):
    cid = update.message.chat_id
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
        print(manba)
        print(key)
        print(hazine)
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

def admini(update,context):
    cid = update.message.chat_id
    text = update.message.text 

    if text == "backup":
        with open("BOT4.db", "rb") as file:
            context.bot.send_document(chat_id=cid, document=file,  
                filename='BOT_backup.db')







def sarmaye_gozari(update,context):
    cid = update.message.chat_id
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
    text = update.message.text 
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
    aks = open(f'aks\{aks}.png','rb')
    print(aks)
    context.bot.send_photo(chat_id=cid ,photo=aks,caption = f"""
🟥هزینه ارتقا: {hazinee}

🟨ذخیره شما: {zakhire}
            
            """ ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
    return A5         


def upgrade2(update,context):
    cid = update.message.chat_id
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

        for key in hazine:
            a1 = hazine[key]*zarib
            a2 = manba[key]
            new = a2-a1
            manba[key] = new
            update_information("manba",manba,cid)


        try:
            pos = pos[a]
            photo = Image.open(f'base/{khandan}.png').convert("RGBA")
            watermark = Image.open(f"buildingspic/{pic}/{a}.png").convert("RGBA")
            photo.paste(watermark, pos, watermark)
            photo.save(f"base/{khandan}.png")
            text = f"🔅ربات در حال بروزرسانی میباشد لطفا چند لحظه صبر کنید"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text)
            time.sleep(1)
        except:
            photo = 1

        try:
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            photo = open(f'base\{khandan}.png','rb')
            context.bot.send_photo(chat_id = cid , photo = photo , caption = f"✅ارتقا ساختمان شما با موفقیت انجام شد",
            reply_markup=reply_markup)
            return A2
        except:
            text = f"✅ارتقا ساختمان شما با موفقیت انجام شد"
            keyboard = [['🔙بازگشت به منوی اصلی'],]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
            return A2
    else:
        text = f"❌"
        keyboard = [['🔙بازگشت به منوی اصلی'],]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id = cid ,text = text ,reply_markup=reply_markup)
        return A2
def manbaersali(update,context):
    cid = update.message.chat_id
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















    keyboard = [["❄North","🦈Riverlands","🦅The Vale"],["🦁Westerlands","🌊Iron Islands","🌼Reach"],["🦌Stormlands","🐲Crownlands","🌞Dorne","🪙Essos"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    context.bot.send_message(chat_id = cid , text = f"""🔻قصد دارید با کدام مورد زیر تجارت کنید؟""",
    reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return A10
def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)

def nezhadtejarat(update,context):
    cid = update.message.chat_id
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
azlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def find_niro(update,context):
    cid = update.message.chat_id
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

    for key in list_harekat:
        a1 = list_harekat[key]
        a2 = temp[key]
        new = a2 - a1
        if new<0:
            keyboard = [["🔙بازگشت به منوی اصلی"]]
            reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=cid ,text = f"❌شما {key} کافی جهت انجام این حرکت را ندارید" ,reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN )
            return A2
        temp[key] = new

    update_information("temp2",temp,cid)
    update_information("temp3",list_harekat,cid)

    keyboard = [["❄North","🦈Riverlands","🦅The Vale"],["🦁Westerlands","🌊Iron Islands","🌼Reach"],["🦌Stormlands","🐲Crownlands","🌞Dorne","🪙Essos"]]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)

    context.bot.send_message(chat_id = cid , text = f"""🔻قلعه ای که قصد لشکرکشی به ان را دارید در قلمرو کدام اقلیم قرار دارد؟""",
    reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN)
    return B2

def co12(update,context):
    cid = update.message.chat_id
    text = update.message.text 

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            etehad = row[19]
            khandan = row[2]
            buildings = eval(row[6])
            tamrin = eval(row[22])
            academy = eval(row[23])
            knight = eval(row[24])

    try:
        sql = '''SELECT * From etehad'''
        recs = c.execute(sql)
        for row in recs:
            if (row[0]) == etehad:
                members = eval(row[1])
    except:
        pass

    ggg = f"""
🗡شمشیرزن: {academy["⚔️|شمشیرزن"]}
🦯نیزه دار:{academy["🗡|نیزه دار"]}
🏹کماندار:{academy["🏹|کماندار"]}
🐎سوارکار:{academy["🐎|سوارکار"]}
❤️|کمپ : {buildings["❤️|کمپ مجروحین"]}
⚔️هجومی: {tamrin["hojom"]}%
🔰دفاع پیاده: {tamrin["defpiyade"]}%
🔰دفاع سواره: {tamrin["defsavare"]}%
🔲شوالیه:{knight["name"]}
🔲لول:{knight["lvl"]}
تجربه:{knight["xp"]}
    """
    fff = f"""🔰فرمانده لشکریان ارتش {cid}>{khandan} دستور حمله به {text} را صادر کرد
    نام اتحاد: {etehad}
    """

    sql = '''SELECT * From lashkarkeshi WHERE vaziat = "{}" AND cid = "{}" '''.format("💢مستقر",cid)
    recs = c.execute(sql)
    for row in recs:
        if (row[4]) == text:
            niro = row[2]

    niro = eval(niro)
    for key in niro:
        num = niro[key]
        if num>0:
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
                ggg = ggg + f"""\n______________{mem}______________ا
🗡شمشیرزن: {academy["⚔️|شمشیرزن"]}
🦯نیزه دار:{academy["🗡|نیزه دار"]}
🏹کماندار:{academy["🏹|کماندار"]}
🐎سوارکار:{academy["🐎|سوارکار"]}
❤️|کمپ : {buildings["❤️|کمپ مجروحین"]}
⚔️هجومی: {tamrin["hojom"]}%
🔰دفاع پیاده: {tamrin["defpiyade"]}%
🔰دفاع سواره: {tamrin["defsavare"]}%
🔲شوالیه:{knight["name"]}
🔲لول:{knight["lvl"]}
تجربه:{knight["xp"]}        
                """
                fff = fff + f"\nا______________{mem}______________ا"
                niro = eval(niro)
                for key in niro:
                    num = niro[key]
                    if num>0:
                        fff = fff + f"\n {key}:{num}"
    except:
        pass

    img = Image.open(f'aks/h1.jpg')
    d1 = ImageDraw.Draw(img)
    reshaped_text = arabic_reshaper.reshape(f"قلعه {text} مورد حمله ارتش {khandan} قرار گرفت")    # correct its shape
    bidi_text = get_display(reshaped_text)
    myFont = ImageFont.truetype('Ordibehesht shablon.TTF', 48)
    d1.text((100,452),bidi_text, font=myFont, fill =(230, 230, 230))
    img.save('hi.jpg')

    photo = open(f"hi.jpg",'rb')
    context.bot.send_photo(chat_id = -1001335810093,photo=photo, caption = f"""<b> 🔰فرمانده لشکریان ارتش <a href="tg://user?id={cid}">{khandan}</a> دستور حمله به {text}  را صادر کرد</b>""",parse_mode = ParseMode.HTML)
    context.bot.send_message(chat_id = -1001559813108 , text = fff ,)
    context.bot.send_message(chat_id = -1001559813108 , text = ggg ,)










def khandan_lashkarkeshi(update,context):
    cid = update.message.chat_id
    text = update.message.text 

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

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            temp = row[10]
            etehad = row[19]
            ghalekhod = row[3]


    sh_masir = shortestPath(edges, temp, text)
    dis = sh_masir[0]
    dis = int(dis)
    dis = dis*60
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
    
    if text == "✅":
        s=0
        newniro = eval(newniro)
        for n in newniro:
            s = s + newniro[n]

        masir = eval(masir)
        mmasir = masir
        maghsad = masir[-1]
        masir.remove(mabda)
        nextmaghsad = masir[0]
        print(nextmaghsad)
        randnum = rand.randint(1,9999)
        randlett = rand.choice(azlist)
        code = f"{randlett}-{randnum}"
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
            if borj>1:
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
            elif borj>0:
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

        sh_masir = shortestPath(edges, mabda, nextmaghsad)
        dis = sh_masir[0]
        dis = int(dis)
        dis = dis*60
        now = datetime.datetime.now()
        time1 = now + datetime.timedelta(seconds=dis)
        nexteta = time1.strftime("%H:%M")
        vaziat = "حرکت"
        c.execute('''INSERT INTO lashkarkeshi (cid,khandan,niro,mabda,maghsad,masir,ETA,nextETA,vaziat,code) values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}");'''.format(cid,khandan,listniro,mabda,maghsad,masir,time,nexteta,vaziat,code))
        conn.commit()
        listniro = eval(listniro)
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
        context.bot.send_photo(chat_id=-1001335810093,photo=photo, caption = f"""<b> 🔰لشکریان ارتش <a href="tg://user?id={cid}">{khandan}</a> از {mabda} حرکت کردند</b>""",parse_mode = ParseMode.HTML)
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
    c.execute('''INSERT INTO etehad (name,members,admin) values("{}","{}","{}");'''.format(text,list,khandan))
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
        os.rename(dl,f"etehad\{etehad}.png")
        time.sleep(1)
    except:
        pass
    chanel_id = -1001335810093
    photo = open(f"etehad\{etehad}.png",'rb')
    context.bot.send_photo(chat_id=chanel_id,photo=photo, caption = f"""
🔰اتحاد <b>{etehad}</b> توسط <a href="tg://user?id={cid}">{firstname}</a> لرد خاندان {khandan} تاسیس شد.
    """,parse_mode = ParseMode.HTML )

    photo = open(f"etehad\{etehad}.png",'rb')
    context.bot.send_photo(chat_id=eid,photo=photo, caption = f"""
🔰اتحاد <b>{etehad}</b> توسط <a href="tg://user?id={cid}">{firstname}</a> لرد خاندان {khandan} تاسیس شد.
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
    
    print(data)
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]
            manbamaghsad = row[5]
            etehadmahsad = row[19]
            vazmaghsad = row[24]
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


    elif data1 == "3":
        sql = '''SELECT * From Information'''
        recs = c.execute(sql)
        for row in recs:
            if int((row[0])) == int(cid):
                khandan = row[2]
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
                etehad_mohajem = row[19]

        
        if ghale != loc :
            text="🚫ارتش مورد نظر از قلعه شما عبور کرده است و شما قادر به بستن راه بر روی آن ها نمیباشید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True) 

        elif etehad == etehad_mohajem and etehad != "a":
            text="🚫شما نمیتوانید راه را بر روی متحد خود ببندید"
            context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True) 

        else:
            c.execute('''UPDATE lashkarkeshi SET vaziat = "{}" WHERE code = "{}" '''.format("💢مستقر",code))
            c.execute('''UPDATE lashkarkeshi SET maghsad = "{}" WHERE code = "{}" '''.format(ghale,code))

            conn.commit() 

            chanelid = -1001335810093
            context.bot.send_message(chat_id=chanelid,text = f"""
<b>⛔️ارتش خاندان {khandan} راه را بر روی ارتش {khandan_mohajem} بست!</b>

<i>⚜️خاندان {khandan_mohajem} در صورت تمایل به ادامه مسیر میبایست ابتدا با ارسال دستور حمله ارتش خاندان {khandan} که راه آن ها را مسدود کرده شکست دهد

🔅خاندان {khandan} در صورت تمایل میبایست طی 2ساعت آینده دستور حمله به ارتش {khandan_mohajem} را صادر کند در غیر این صورت ارتش فوق اجازه حرکت خواهد داشت
</i>
            """,parse_mode = ParseMode.HTML )
            context.bot.edit_message_text(text=f"""
✅ارتش شما با موفقیت راه را بر روی ارتش دشمن بست
        """,chat_id=ciid,message_id=message_id) 
            
            try:
                context.bot.send_message(chat_id=cid_mohajem,text = f"""
<b>⛔️ارتش خاندان {khandan} راه را بر روی ارتش شما بست!</b>

<i>
در صورت تمایل به ادامه مسیر میبایست ابتدا با ارسال دستور حمله ارتش خاندان {khandan} که راه شما  را مسدود کرده شکست دهید

🔅در صورتی که خاندان {khandan} تا دو ساعت آینده دستور حمله ای علیه شما صادر نکند میتوانید بدون درگیری مسیر خود را ادامه دهید
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
        elif num>14:
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
            photo = open(f"etehad\{data2}.png",'rb')
            context.bot.send_photo(chat_id=chanel_id,photo=photo, caption = f"""
🔰خاندان <a href="tg://user?id={cid}">{khandan}</a> به اتحاد <b>{data2}</b> پیوست
            """,parse_mode = ParseMode.HTML )
            photo = open(f"etehad\{data2}.png",'rb')
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
                vazmabda = row[24]

        manbamabda = eval(manbamabda)

        list = eval(list)
        manbaersali = list["manbaersal"]
        meghdarersali = list["meghdarersal"]
        manbadaryafti = list["manbadaryaft"]
        meghdardaryafti = list["meghdardaryaft"]

        meghdarersalie =meghdarersali
        meghdardaryaftie = meghdardaryafti
        if etehadmabda == etehadmahsad:
            meghdarersalie = meghdarersali/2
            meghdardaryaftie = meghdardaryafti/2

        if s == 0:
            context.bot.edit_message_text(text="🚫این تجارت از طرف مبدا لغو شده است",chat_id=ciid,message_id=message_id) 

        elif data3 == "Laghv":
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
            maghsadkhorjiZarfiat = int(khorojimabda) - meghdardaryaftie
            maghsadvorodiiZarfiat = int(vorodimabda) - meghdarersalie

            if mabdakhorojiZarfiat<0 or mabdavorodiZarfiat<0 or maghsadkhorjiZarfiat<0 or maghsadvorodiiZarfiat<0:
                text="🚫ظرفیت کافی جهت تجارت موجود نمیباشد"
                context.bot.answer_callback_query(callback_query_id=query.id, text=text, show_alert=True)
            elif vazmabda == "U" or vazmaghsad == "U":
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
    text = update.message.text
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        print(row[0])
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
    print(buildings)

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
        print("333")
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
    if text == "💈دژکوب":
        hazine = 5000
    elif text == "☄️منجنیق" :
        hazine = 7000
    elif text == "🎯بالیستا" :
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
    keyboard = [['🔙بازگشت به منوی اصلی'],]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id = cid ,text = f"✅{text} با موفقیت تحقیق شد" ,reply_markup=reply_markup)
    return A2 
    


    
#________________________****ertebatat****________________________#
def ertebatat(update,context):
    cid = update.message.chat_id
    text = update.message.text
    

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

*متن بیانیه خود را وارد کنید:* 
        """,
        reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN)
        return B10

    elif text == "🌐ارسال فایل":
        context.bot.send_message(chat_id = cid , text = f"""
در بخش*🌐ارسال فایل* میتوانید هرگونه فایلی را (متنی،عکس،فیلم،گیف، آهنگ و .... ) را برای نمایش در کانال ارسال کنید . 

_ ⚠️توجه داشته باشید که پیام های این بخش پس از تایید ادمین در کانال نمایش داده خواهد شد_

*✳️فایل خود را ارسال کنید:* 
""",reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN)
        return B9





def file_send(update,context):
    chanelid = -1001559813108
    cid = update.message.chat_id
    mid = update.message.message_id
    midd = f"file*{mid}*news*{cid}"
    middd = f"file*{mid}*asli*{cid}"
    keyboard = [[InlineKeyboardButton("✅تایید به توییتر" ,callback_data=midd)],
    [InlineKeyboardButton("✅تایید به کانال اصلی" ,callback_data=middd)],
    [InlineKeyboardButton("❌لغو" ,callback_data="file*laghv*laghv*{cid}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.forward_message(chat_id=chanelid,from_chat_id=cid,message_id=mid)
    context.bot.send_message(chat_id = chanelid, text = "آیا ارسال فایل بالا به کانال بازی را تایید میکنید؟",reply_markup=reply_markup)
    
    keyboard1 = [['🔙بازگشت به منوی اصلی']]
    reply_markup1 = ReplyKeyboardMarkup(keyboard1,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = cid,
    text = "✅فایل شما جهت بررسی و تایید به ادمین بازی ارسال شد",reply_markup=reply_markup1)
    return A2

def twitter_pic(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2] 

    try:
        remove(f"TweetPhoto\{khandan}.jpg")
    except:
        pass

    if text == "➡️مرحله بعدی":
        pass
    else:
        file_id = update.message.photo[-1]
        photo_file = context.bot.getFile(file_id)
        dl = photo_file.download()
        os.rename(dl,f"TweetPhoto\{khandan}.jpg")

    context.bot.send_message(chat_id = cid , text = f"""
*متن توییت خود را وارد کنید:*
""",reply_markup=telegram.ReplyKeyboardRemove(),parse_mode = ParseMode.MARKDOWN)
    return B8

def bayanie(update,context):
    cid = update.message.chat_id
    text = update.message.text
    first_name = update.message.chat.first_name

    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2]

    matn = f"""🕊 <b>بیانیه لرد {khandan}</b>:
《_ {text} _》
    
*امضا: <a href="tg://user?id={cid}">{first_name}</a>  """

    chanelid = -1001322789383
    context.bot.send_message(chat_id = chanelid , text = matn ,parse_mode = ParseMode.HTML )
    keyboard = [['🔙بازگشت به منوی اصلی']]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
    context.bot.send_message(chat_id = cid,
    text = "✅بیانیه شما ارسال شد",reply_markup=reply_markup)
    return A2



def send_twitt(update,context):
    cid = update.message.chat_id


    sql = '''SELECT * From Information'''
    recs = c.execute(sql)
    for row in recs:
        if int((row[0])) == int(cid):
            khandan = row[2] 

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
        os.rename(f"TweetPhoto\{khandan}.jpg",f"img.jpg")
    except:
        pass
    try:
        driver = webdriver.Chrome()
        print("hi")
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
        driver.find_element(by=By.XPATH, value='//*[@id="clientInput"]').send_keys(client)
        driver.find_element(by=By.XPATH, value='//*[@id="pfpInput"]').send_keys(os.getcwd()+f"\prof.jpg")
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="imgInput"]').send_keys(os.getcwd()+f"\img.jpg")
        except:
            print("nashod")
        driver.find_element(by=By.XPATH, value='//*[@id="downloadButton"]').click()
        try:
            driver.find_element(by=By.XPATH, value='/html/body/div/div/div[1]/form/div[1]').click()
        except:
            pass
        with open("TweetPhoto/photo.png", "wb") as photo:
            photo.write(driver.find_element(by=By.XPATH, value='//*[@id="tweetInnerContainer"]').screenshot_as_png)
        photo = open('TweetPhoto/photo.png','rb')

        try:
            remove("img.jpg")
        except:
            pass

        photo = open('TweetPhoto/photo.png','rb')
        chanelid = -1001322789383

        context.bot.send_photo(chat_id = chanelid , photo = photo )

        keyboard = [
            ['🔙بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = "✅توییت شما ارسال شد",
        reply_markup=reply_markup)
        return A2
    except Exception as e:
        print(e)
        try:
            remove("img.jpg")
        except:
            pass
        
        keyboard = [
            ['🔙بازگشت به منوی اصلی']
        ]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=False)
        context.bot.send_message(chat_id = cid,
        text = "مشکلی در روند ارسال توییت شما ایجاد شد",
        reply_markup=reply_markup)
        return A2


#_______________________________________________________________#
edges = [
("Mole's Town" , 'Castle Black' , 10) , ('Castle Black' , "Mole's Town" , 10) ,
("Mole's Town" , 'Queenscrown' , 20) , ('Queenscrown' , "Mole's Town" , 20) ,
('North Dot 1' , 'Queenscrown' , 60) , ('Queenscrown' , 'North Dot 1' , 60) ,
('North Dot 1' , 'Last Hearth' , 15) , ('Last Hearth' , 'North Dot 1' , 15) ,
('Karhold' , 'Last Hearth' , 150) , ('Last Hearth' , 'Karhold' , 150) ,
('North Dot 1' , 'North Dot 2' , 135) , ('North Dot 2' , 'North Dot 1' , 135) ,
('North Dot 2' , 'Winterfell' , 35) , ('Winterfell' , 'North Dot 2' , 35) ,
('North Dot 2' , 'Deepwood Motte' , 180) , ('Deepwood Motte' , 'North Dot 2' , 180) ,
('Winterfell' , 'North Dot 3' , 80) ,('North Dot 3' , 'Winterfell' , 80) ,
('North Dot 3' , 'North Dot 4' , 50) ,('North Dot 4' , 'North Dot 3' , 50) ,
('North Dot 4' , 'Torrhen"s Square' , 40) ,('Torrhen"s Square' , 'North Dot 4' , 40) ,
('North Dot 4' , 'Barrowton' , 90) ,('Barrowton' , 'North Dot 4' , 90) ,
('Barrowton' , 'Moat Cailin' , 140) ,('Moat Cailin' , 'Barrowton' , 140) ,
('North Dot 3' , 'Moat Cailin' , 100) ,('Moat Cailin' , 'North Dot 3' , 100) ,
('White Harbor' , 'Moat Cailin' , 45) ,('Moat Cailin' , 'White Harbor' , 45) ,
('North Dot 5' , 'Moat Cailin' , 65) ,('Moat Cailin' , 'North Dot 5' , 65) ,
('North Dot 5' , 'Greywater Watch' , 20) ,('Greywater Watch' , 'North Dot 5' , 20) ,
("Flint's Finger" , 'Greywater Watch' , 225) ,('Greywater Watch' , "Flint's Finger" , 225) ,
('White Harbor' , 'Oldcastle' , 75) ,('Oldcastle' , 'White Harbor' , 75) ,
('White Harbor' , 'Ramsgate' , 60) ,('Ramsgate' , 'White Harbor' , 60) ,
('White Harbor' , 'North Dot 6' , 80) ,('North Dot 6' , 'White Harbor' , 80) ,
('Widow"s Watch' , 'North Dot 6' , 165) ,('North Dot 6' , 'Widow"s Watch' , 165) ,
('Dreadfort' , 'North Dot 6' , 135) ,('North Dot 6' , 'Dreadfort' , 135) ,
("Mole's Town", 'East Watch by the Sea' , 35) ,('East Watch by the Sea' , "Mole's Town" , 35) ,
('The Shadow Tower' , 'Castle Black' , 75) ,('Castle Black' , 'The Shadow Tower' , 75),
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
        B9 : [MessageHandler(Filters.all & ~Filters.command, file_send)],
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
updater.dispatcher.add_handler(CallbackQueryHandler(Button))

updater.start_polling()
updater.idle()