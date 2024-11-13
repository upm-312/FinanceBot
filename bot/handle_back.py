from telebot import types
from bot.bot_instance import bot
from bot.main_menu import main_menu

@bot.message_handler(func=lambda message: message.text == "Назад ⬅️")
def back(message):
    # Логика для обработки кнопки "Назад"
    bot.send_message(message.chat.id, "Вы вернулись назад. Какую команду вы хотите выполнить?", reply_markup=main_menu(message))
    
