import os
import telebot

bot = telebot.TeleBot('7181432878:AAHAo62g1V750grTsc8E2DAlOGg11Bf3Ug0')

from telebot import types

#API_TOKEN = os.environ['TOKEN']='7181432878:AAHAo62g1V750grTsc8E2DAlOGg11Bf3Ug0'
#bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Запустить генератор', url='https://dragon-next.github.io/Hamster-Kombat-Generator/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Нууу", reply_markup = markup)

bot.polling()
