from bot.send_welcome import send_welcome
from bot.handle_info import info
from bot.handle_search import search
from bot.handle_grafic import grafic
from bot.handle_update import update
from bot.handle_predictions import predictions
from bot.handle_menu import menu 
from bot.handle_course import get_currency_rates
from bot.bot_instance import bot
from bot.handle_back import back

@bot.message_handler(commands=['start'])
def handle_start(message):
    send_welcome(message)

@bot.message_handler(func=lambda message: message.text == "Поиск 🔍")
def handle_search(message):
    search(message)
    
@bot.message_handler(func=lambda message: message.text == "Прогноз 📈")
def handle_predictions(message):
    predictions(message)
    
@bot.message_handler(func=lambda message: message.text == "График 📊")
def handle_grafic(message):
    grafic(message)
    
@bot.message_handler(func=lambda message: message.text == "Курс 📈")
def send_currency_rates(message):
    rates = get_currency_rates()
    bot.reply_to(message, rates)

@bot.message_handler(func=lambda message: message.text == "Инфо ℹ️")
def handle_info(message):
    info(message)
    
@bot.message_handler(func=lambda message: message.text == "Меню 📱")
def handle_menu(message):
    menu(message)
    
#@bot.message_handler(func=lambda message: message.text == "Назад ⬅️")
#def handle_back(message):
    #back(message)
    
@bot.message_handler(func=lambda message: message.text == "Обновить 🔁 НЕ НАЖИМАТЬ, ЛОМАЕТ ПРОГРАММУ, ПОТОМ САМИ FIGI СМОТРЕТЬ БУДЕТЕ")
def handle_update(message):
    update(message)
    
# Запуск бота
if __name__ == '__main__':
    bot.polling()