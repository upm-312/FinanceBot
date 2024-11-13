
from bot.bot_instance import bot

def predictions(message):
    # Логика для обработки прогноза
    bot.send_message(message.chat.id, "Здесь будет ваш прогноз.")