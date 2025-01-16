import telebot
from telebot import types
"""in this case we learn that how to create telegram bot and write code\
with python in this code we want to get phone number from user and give \
user his/her numerical ID in telegram you know in formal version of telegram\
we can not find numerical ID and we have to install informal version that is\
now good the \nstep of creating new bot : 
1)you must have telegram account
2)type @BotFather in search
3)start the BotFather
4)click on /newbot
5)choose a name for your bot
6)choose a username for your bot that mut end with "bot"
7)you create your telegram bot save the message that have id of your bot\
and telegram bot api that is very important to connect to your bot
8)open your IDE or editor and install telebot
9)write this code 
Remember: you must put your api in line 22 instant of the text that written\
in the method to connect to your bot
"""
# #bot api
bot = telebot.TeleBot("bot api that you get it from botfather")
@bot.message_handler(commands=["start"])
def number(m):
    markup= types.ReplyKeyboardMarkup(resize_keyboard= True,row_width=1)
    button = types.KeyboardButton(text = "send number", request_contact= True)
    markup.add(button)
    bot.send_message(m.chat.id, "welcome!!\nplease verify your number", reply_markup= markup)
@bot.message_handler(content_types=["contact"])
def contact(m):
    bot.send_message(m.chat.id, f"your id number:{m.contact.user_id}")
bot.polling()

