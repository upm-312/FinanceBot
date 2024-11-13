
from bot.main_menu import main_menu
from functions.get_names import get_names  # Импортируем функцию из другого файла
from functions.token_1 import TOKEN   

import telebot
from bot.main_menu import main_menu
from bot.bot_instance import bot

def update(message):
    try:
        get_names(TOKEN)  # Вызов функции get_names
        bot.reply_to(message, "Успешно получили данные обо всех новых FIGI и Ticker.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обновлении файла: {str(e)}")
    main_menu(message)