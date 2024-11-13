import telebot
from bot.main_menu import main_menu
from bot.bot_instance import bot

def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш FinanceBot. Я помогу вам увеличить доходность вашего инвестиционного портфеля. Чтобы узнать обо всех моих функциях нажмите Меню")
    main_menu(message)