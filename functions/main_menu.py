import telebot
from telebot import types

from functions.token_1 import TOKEN


API_TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(API_TOKEN)

def main_menu(message):# Функция для создания главного меню с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search_button = types.KeyboardButton("Поиск 🔍")
    course_button = types.KeyboardButton("Курс 📈")
    info_button = types.KeyboardButton("Инфо ℹ️")
    menu_button = types.KeyboardButton("Меню 📱")
    refresh_button = types.KeyboardButton("Обновить 🔁")  # Новая кнопка Обновить
    markup.add(search_button, course_button, info_button, menu_button, refresh_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)