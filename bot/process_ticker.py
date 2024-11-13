from telebot import types
from functions.main import main
from bot.bot_instance import bot
from bot.main_menu import main_menu
def process_ticker(message):
    
    if len(message.text) != 4:
        bot.reply_to(message, f"Тикера не существует!")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_forecast = types.KeyboardButton("Поиск 🔍")
        btn_back = types.KeyboardButton("Назад ⬅️")
        keyboard.add(btn_forecast, btn_back)
        # Отправляем сообщение с клавиатурой
        bot.send_message(message.chat.id,f"Выберете действие:" ,reply_markup=keyboard)
    else:
        ticker = message.text
        bot.reply_to(message, f"Это займет 15 секунд.")
        main(ticker)
        bot.reply_to(message, f"Создан файл со стоимостью акций за последние 5 лет со свечой 4 часа по тикеру - : {ticker.upper()}.")
        
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_forecast = types.KeyboardButton("Прогноз 📈")
        btn_chart = types.KeyboardButton("График 📊")
        btn_back = types.KeyboardButton("Назад ⬅️")
        keyboard.add(btn_forecast, btn_chart, btn_back)

        # Отправляем сообщение с клавиатурой
        bot.send_message(message.chat.id,f"Выберете действие:" ,reply_markup=keyboard)