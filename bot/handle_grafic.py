from bot.bot_instance import bot
from functions.grafic import draw_grafic

def grafic(message):
    draw_grafic()
    bot.send_message(message.chat.id, "Здесь будет ваш график.")
    with open("C:/FinanceBot/FinanceBot/source/5Y.png", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)