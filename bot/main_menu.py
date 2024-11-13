from telebot import types
from bot.bot_instance import bot

def main_menu(message):# Функция для создания главного меню с кнопками
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search_button = types.KeyboardButton("Поиск 🔍")
    course_button = types.KeyboardButton("Курс 📈")
    info_button = types.KeyboardButton("Инфо ℹ️")
    menu_button = types.KeyboardButton("Меню 📱")
    #refresh_button = types.KeyboardButton("Обновить 🔁")  # Новая кнопка Обновить
    keyboard.add(search_button, course_button, info_button, menu_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)
    return keyboard