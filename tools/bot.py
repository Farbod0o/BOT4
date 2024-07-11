#__________________******Libraries******____________________
import re
import collections
import heapq
import qrcode
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
#__________________________________________________________________________#


#________________________****BOT SETTINGS****________________________#

#_توکن ربات:
updater = Updater("956982928:AAFrRxZFkqH43P4vyOUWxzJ6r4Nx-XiuXGY")
#_دیتابیس:
db_path = r'../BOT4.db'
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
def start (update,context):
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
        if int((row[2])) == int(cid):
            s = 1
            khandan = row[0]

    if s == 0:
        print(f"New Memmber:{first_name}")
        photo = open('../temp/banner.jpg', 'rb')
        context.bot.send_photo(chat_id = cid , photo = photo , caption = f"""
        👾سلام <b>لرد {first_name}</b> ، به <b> بتل اف ترونز</b> خوش آمدید!
            
▪️از امروز بنده مشاور شما در اداره کشور خواهم بود تا بتوانیم در زمینه های نظامی اقتصادی و آموزشی باعث پیشرفت خاندان خود باشیم هر چند این مسیر طولانی و نیازمند بردباری شماست اما من معتقدم که با کمک یکدیگر میتوانیم موفق شویم
    
🔐*در ابتدا کدی که از ادمین بازی دریافت کرده اید را وارد کنید این کد مجوز ورود شما به مراحل بعد میباشد*

در صورت وجود هرگونه سوال و دریافت کد به ایدی : @TG_SupportA پیام دهید
""",parse_mode = ParseMode.HTML)
        return A1


        
def khoroj(update,context):
    cid = update.message.chat_id
    text = update.message.text 
    context.bot.ban_chat_member(chat_id = -1001767002742 , user_id = cid, timeout=None, until_date=None, api_kwargs=None, revoke_messages=None)

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
    },

	fallbacks=[CommandHandler('start' , start)
    ,CommandHandler('cancel' , cancel)]

	)
#______________________________________________________________#





#________________________****DISPATCHERS****________________________#

updater.dispatcher.add_handler(conv_handler)
updater.dispatcher.add_handler(CommandHandler('start' , start))
updater.dispatcher.add_handler(CommandHandler('cancel' , cancel))
updater.dispatcher.add_handler(CommandHandler('khoroj' , khoroj))

updater.start_polling()
updater.idle()