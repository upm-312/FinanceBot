import telebot
from telebot import types
from functions.main import main
from functions.token_1 import TOKEN
from functions.main_menu import main_menu

# Замените 'YOUR_API_TOKEN' на токен, полученный от BotFather
API_TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(API_TOKEN)

def process_ticker(message):
    ticker = message.text
    main(ticker)
    bot.reply_to(message, f"Создан файл со стоимостью акций за последние 3 года со свечой 1 час по тикеру - : {ticker}.")
    main_menu(message)