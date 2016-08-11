# -*- coding: utf-8 -*-
import telebot
import random
from telebot import types
from telebot import util
from random import randint
import json
import redis
import logging
import urllib
import time
import logging
import subprocess
import requests
import os
token = "199356209:AAHMUXxTeFXnsqwWjZxJD2Zc" #token
sudo = 122774063 #admin
bot = telebot.TeleBot(token)
db = "https://api.telegram.org/bot{}/getMe?".format(token)
res = urllib.request.urlopen(db)
res_body = res.read()
parsed_json = json.loads(res_body.decode("utf-8"))
botid = parsed_json['result']['id']
botuser = parsed_json['result']['username']
R = redis.StrictRedis(host='localhost', port=6379, db=0)
bhash = "banned:users:{}".format(botuser)
mhash = "pmresan:users:{}".format(botuser)
if R.get("logchat:{}".format(botuser)) :
    logchat = int(R.get("logchat:{}".format(botuser)))
else:
    logchat = sudo
@bot.message_handler(commands=['setstart'])
def shstart(m):
    try:
        if m.chat.id == logchat :
            text = m.text.replace('/setstart ','')
            R.set("welcome:{}".format(str(botid)),text)
            bot.send_message(m.chat.id,"*Welcome TexT Changed To :*\n{}".format(text),parse_mode='Markdown')
    except :
        print("Error")
@bot.message_handler(commands=['setwait'])
def show_alert(m):
    try:
        if m.chat.id == logchat :
            text = m.text.replace('/setwait ','')
            R.set("wait:{}".format(str(botid)),text)
            bot.send_message(m.chat.id,"*Wait TexT Changed To :*\n{}".format(text),parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(commands=['setflood'])
def sflood(m):
    try:
        if m.chat.id == logchat :
            text = m.text.replace('/setflood ','')
            R.set("maxmsgs:{}".format(botuser),int(text))
            bot.send_message(m.chat.id,"*Flood Messages Changed To {}*".format(text),parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(commands=['setfloodtime'])
def sft(m):
    try:
        if m.chat.id == logchat :
            text = m.text.replace('/setfloodtime ','')
            R.set("maxflood:{}".format(botuser),int(text))
            bot.send_message(m.chat.id,"*Flood Time Changed To {}*".format(text),parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(commands=['enableads'])
def sads(m):
    try:
        if m.chat.id == logchat :
            R.set("ads:{}".format(botuser),True)
            bot.send_message(m.chat.id,"تبلیغات آی تیم در ربات شما فعال شد\nممنون که مارو حمایت میکنید")
    except Exception as e:
        print(e)
@bot.message_handler(commands=['disableads'])
def sadsd(m):
    try:
        if m.chat.id == logchat :
            R.delete("ads:{}".format(botuser))
            bot.send_message(m.chat.id,"تبلیغات و حمایت شما از ما قطع شد :(")
    except Exception as e:
        print(e)
@bot.message_handler(commands=['setlog'])
def setlog(m):
    try:
        if m.from_user.id == sudo :
            R.set("logchat:{}".format(botuser),m.chat.id)
            bot.send_message(m.chat.id,"*New Log Chat Set*\n`ID` : _{}_".format(m.chat.id),parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(commands=['dellog'])
def remlog(m):
    try:
        if m.from_user.id == sudo :
            R.set("logchat:{}".format(botuser),sudo)
            bot.send_message(m.chat.id,"*Old Log Chat Deleted*",parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(commands=['start','help'])
def start(m):
    try :
        if m.chat.id == logchat :
            text = 'سلام رئیس 👋\nدستورات از این قراره:\n\n/setstart <text>\nتنظیم متن شروع با قابلیت مارکداون\n/setwait <text>\nتنظیم متن ارسالی به کاربر بعد از پیام های وی با قابلیت مارکدون\n/ban <on reply/id>\nبن کردن یک نفر از پیام رسان\n/unban <on reply/id>\nآن بن کردن یک نفر از پیام رسان\n/users\nتعداد کاربران\n/bans\nتعداد افراد بن شده\n/showstart\nنمایش متن استارت فعلی\n/showwait\nدریافت متن انتظار فعلی\n/setlog <in group or private>\nتنظیم یک گروه به عنوان گروه ادمین\n/dellog\nحذف گروه ادمین\n/sendtoall <text>\nارسال یک متن به تمامی کاربران\n/fwdtoall <on reply>\nفوروارد یک پیام به تمامی اعضا\n/setflood <num>\nتنظیم تعداد پیام های ارسالی برای تشخیص اسپم (پیشفرض : ۵ در ۴ ثانیه)\n/setfloodtime <num>\nتنظیم زمان محدودیت ارسال پیام(پیشفرض : ۴)\n/msg <id> <text>\nفرستادن یک پیام به یک شخص از طریق آیدی\n/enableads\nحمایت از ما با تبلیغ سورس ربات :)\n/disableads\nقطع حمایت از ما :(\n\nنکته :‌برای جواب دادن به اشخاص روی پیام آنها ریپلای کنید\nنکته : پیشنهاد میشه تنظیمات فلود رو دستکاری نکنید \n\nبا آروزی خوشحالی برای شما\nمنتظر سورپرایز ها در ورژن بعدی باشید\n[iTeam](https://telegram.me/iTeam_ir)'
            bot.send_message(logchat,text,parse_mode='Markdown')
        elif not m.chat.id == logchat :
            markup =  types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton('ربات خود را بسازید!', url='https://telegram.me/iTeam_ir/39'))
            if R.get("welcome:{}".format(str(botid))) :
                tex3 = R.get("welcome:{}".format(str(botid)))
            else :
                tex3 = "*Welcome Dude ,*\n_I'll Forward Your Message To Bot Owner_"                
            if R.get("ads:{}".format(botuser)):
                bot.send_message(m.chat.id,tex3,parse_mode='Markdown',reply_markup=markup)
            else:
                bot.send_message(m.chat.id,tex3,parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(commands=['sendall'])
def sendall(m):
    if m.chat.id == logchat :
        text = m.text.replace('/sendall ','')
        ids = R.smembers(mhash)
        for id in ids:
            try:
                bot.send_message(id,text)
            except:
                R.srem(mhash,id)
@bot.message_handler(commands=['fwdtoall'])
def fwdall(m):
    if m.chat.id == logchat :
        if m.reply_to_message:
            mid = m.reply_to_message.message_id
            ids = R.smembers(mhash)
            for id in ids:
                try:
                    bot.forward_message(id,m.chat.id,mid)
                except:
                    R.srem(mhash,id)
@bot.message_handler(commands=['unban'])
def unban(m):
    if not m.reply_to_message :
        if m.chat.id == logchat :
            try :
                if m.reply_to_message:
                    if m.reply_to_message.forward_from :
                        user = m.reply_to_message.forward_from
                        R.srem(bhash,user)
                        bot.send_message(logchat,"Unbanned")
                else:
                    id = m.text.replace("/unban ","")
                    R.srem(bhash,int(id))
                    bot.send_message(logchat,"Unbanned")
            except Exception as e:
                print(e)
@bot.message_handler(commands=['ban'])
def unban(m):
    if not m.reply_to_message :
        if m.chat.id == logchat :
            try :
                if m.reply_to_message:
                    if m.reply_to_message.forward_from :
                        user = m.reply_to_message.forward_from
                        R.srem(bhash,user)
                        bot.send_message(logchat,"Unbanned")
                else:
                    id = m.text.replace("/ban ","")
                    R.sadd(bhash,int(id))
                    bot.send_message(logchat,"Banned")
            except Exception as e:
                print(e)
@bot.message_handler(commands=['msg'])
def smsg(m):
    if not m.reply_to_message :
        if m.chat.id == logchat :
            try :
                id = m.text.split()[1]
                text = m.text.split()[2]
                receiver = int(id)
                bot.send_message(logchat,"Message Sent To *{}*".format(id),parse_mode='Markdown')
                bot.send_message(receiver,text)
            except :
                bot.send_message(logchat,"Message Not Sent\niThink User Blocked Me")
@bot.message_handler(content_types=['video','photo','sticker','document','audio','voice','text'])
def mfwdr(m):
    try:
        if m.text :
            if m.chat.id == logchat :
                if m.reply_to_message :
                    text = m.text
                    user = m.reply_to_message.forward_from.id
                    if m.text == '/ban' :
                        return None
                    elif m.text == '/unban' :
                        return None
                    else:
                        bot.send_message(user,text)
                        bot.send_message(m.chat.id,"Message Sent")
                elif not m.reply_to_message :
                    if m.text == '/bans' :
                        res = R.scard(bhash)
                        tex = "Banned Users : {}".format(str(res))
                        bot.send_message(logchat,tex)
                    elif m.text == '/users' :
                        res2 = R.scard(mhash)
                        tex2 = "Bot Users : {}".format(str(res2))
                        bot.send_message(logchat,tex2)
                    elif m.text == '/showstart' :
                        if R.get("welcome:{}".format(str(botid))) :
                            tex3 = R.get("welcome:{}".format(str(botid)))
                        else :
                            tex3 = "*Welcome Dude ,*\n_I'll Forward Your Message To Bot Owner_"
                            bot.send_message(m.chat.id,tex3,parse_mode='Markdown')
                    elif m.text == '/showwait' :
                        if R.get("wait:{}".format(str(botid))) :
                            tex3 = R.get("wait:{}".format(str(botid)))
                        else :
                            tex3 = "*Message Sent*"
                            bot.send_message(m.chat.id,tex3,parse_mode='Markdown')
            elif not m.chat.id == logchat :
                _hash = "anti_flood:{}:{}".format(botuser,m.from_user.id)
                msgs = 0
                max_time = 5
                if R.get(_hash):
                    msgs = int(R.get(_hash))
                    max_time = R.ttl(_hash)
                else:
                    if R.get("maxflood:{}".format(botuser)) :
                        max_time = R.get("maxflood:{}".format(botuser))
                R.setex(_hash, max_time, int(msgs) + 1)
                if m.chat.type == 'private' :
                    if R.sismember(bhash,m.chat.id) :
                        bot.send_message(m.chat.id,"You're Banned")
                    elif not R.sismember(bhash,m.chat.id) :
                        if not m.text == '/start' or not m.text == '/help' :
                            if not R.sismember(mhash,m.from_user.id):
                                if R.get("wait:{}".format(str(botid))) :
                                    tex3 = R.get("wait:{}".format(str(botid)))
                                else :
                                    tex3 = "*Message Sent*"
                                R.sadd(mhash,m.from_user.id)
                                bot.forward_message(logchat,m.chat.id,m.message_id)
                                bot.send_message(m.chat.id,tex3,parse_mode='Markdown')
                            elif R.sismember(mhash,m.from_user.id):
                                if R.get("wait:{}".format(str(botid))) :
                                    tex3 = R.get("wait:{}".format(str(botid)))
                                else :
                                    tex3 = "*Message Sent*"
                                bot.forward_message(logchat,m.chat.id,m.message_id)
                                bot.send_message(m.chat.id,tex3,parse_mode='Markdown')
        else:
            if m.chat.id == logchat:
                if m.reply_to_message:
                    user = m.reply_to_message.forward_from.id
                    if m.photo:
                        file_id = m.photo[1].file_id
                        bot.send_photo(user,file_id)
                    elif m.video:
                        file_id = m.video.file_id
                        bot.send_video(user,file_id)
                    elif m.sticker:
                        file_id = m.sticker.file_id
                        bot.send_sticker(user,file_id)
                    elif m.document:
                        file_id = m.document.file_id
                        bot.send_document(user,file_id)
                    elif m.audio:
                        file_id = m.audio.file_id
                        bot.send_audio(user,file_id)
                    elif m.voice:
                        file_id = m.voice.file_id
                        bot.send_voice(user,file_id)
                    bot.send_message(m.chat.id,"Message Sent")
            elif not m.chat.id == logchat :
                bot.forward_message(logchat,m.chat.id,m.message_id)
                if R.get("wait:{}".format(str(botid))) :
                    tex3 = R.get("wait:{}".format(str(botid)))
                else :
                    tex3 = "*Message Sent*"
                bot.send_message(logchat,"Message Sent by {} - @{}".format(m.from_user.first_name,m.from_user.username))
                bot.send_message(m.chat.id,tex3,parse_mode='Markdown')
    except Exception as e:
        print(e)
@bot.message_handler(func=lambda message: True)
def fwdr(m):
    try:
        _hash = "anti_flood:{}:{}".format(botuser,m.from_user.id)
        msgs = 0
        if R.get(_hash):
            msgs = int(R.get(_hash))
        max_msgs = 5
        if R.get("maxmsgs:{}".format(botuser)) :
            max_msgs = R.get("maxmsgs:{}".format(botuser))
        if msgs > max_msgs:
            R.sadd(bhash,m.from_user.id)
            text = "User {} - @{} is Flooding".format(m.from_user.first_name,m.from_user.username)
            text2 = "Flood Is Not Allowed !\nYou're Banned"
            bot.send_message(logchat,text)
            bot.send_message(m.from_user.id,text2)
    except Exception as e:
        print(e)
bot.polling(True)
