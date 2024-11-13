#import telebot
#from telebot import types

#from main_menu import main_menu
from bot.process_ticker import process_ticker

import telebot
from bot.main_menu import main_menu
from bot.bot_instance import bot

#API_TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
#bot = telebot.TeleBot(API_TOKEN)

def search(message):
    msg = bot.reply_to(message, "Пожалуйста, напишите тикер интересующей вас компании, например тикер Росбанка - ROSB:")
    bot.register_next_step_handler(msg, process_ticker)
    