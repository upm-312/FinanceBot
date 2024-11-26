
from bot.bot_instance import bot
from telegram.ext import Updater
from functions.LSTM import LSTM_P

def predictions(message):
    bot.send_message(message.chat.id, "Прогноз займет 30 секунд")
    bot.send_message(message.chat.id,LSTM_P())
    
    with open("C:/FinanceBot/FinanceBot/source/LSTM.png", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    