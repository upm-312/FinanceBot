
from bot.main_menu import main_menu
from bot.bot_instance import bot

def menu(message):
    commands = (
        "/start - Запустить бота\n"
        "Поиск 🔍 - Найти информацию о компании\n"
        "Курс 📈 - Получить курс акций (пока не реализовано)\n"
        "Инфо ℹ️ - Получить информацию о боте\n"
        "Меню 📱 - Показать все команды\n"
        "Обновить 🔁 - Обновить данные"
    )
    bot.reply_to(message, f"Команды бота:\n{commands}")
    main_menu(message)
