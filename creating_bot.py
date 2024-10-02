import telebot 
from telebot import types
from get_names import get_names  # Импортируем функцию из другого файла
from main import main
from token_1 import TOKEN

# Замените 'YOUR_API_TOKEN' на токен, полученный от BotFather
API_TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(API_TOKEN)

# Функция для создания главного меню с кнопками
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    search_button = types.KeyboardButton("Поиск 🔍")
    course_button = types.KeyboardButton("Курс 📈")
    info_button = types.KeyboardButton("Инфо ℹ️")
    menu_button = types.KeyboardButton("Меню 📱")
    refresh_button = types.KeyboardButton("Обновить 🔁")  # Новая кнопка Обновить
    markup.add(search_button, course_button, info_button, menu_button, refresh_button)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш FinanceBot. Я помогу вам увеличить доходность вашего инвестиционного портфеля. Чтобы узнать обо всех моих функциях нажмите Меню")
    main_menu(message)

# Обработка нажатия кнопки "Поиск"
@bot.message_handler(func=lambda message: message.text == "Поиск 🔍")
def handle_search(message):
    msg = bot.reply_to(message, "Пожалуйста, напишите тикер интересующей вас компании, например тикер Росбанка - ROSB:")
    bot.register_next_step_handler(msg, process_ticker)

# Обработка тикера
def process_ticker(message):
    ticker = message.text
    main(ticker)
    bot.reply_to(message, f"Создан файл со стоимостью акций за последние 3 года со свечой 1 час по тикеру - : {ticker}.")
    main_menu(message)

# Обработка нажатия кнопки "Курс"
@bot.message_handler(func=lambda message: message.text == "Курс 📈")
def handle_course(message):
    bot.reply_to(message, "Эта кнопка пока ничего не делает. Тут будет транслироваться курс USD, EUR, BTC")
    main_menu(message)

# Обработка нажатия кнопки "Инфо"
@bot.message_handler(func=lambda message: message.text == "Инфо ℹ️")
def handle_info(message):
    bot.reply_to(message, "FinanceBot создается как студенческий проект, целью которго является практика в коде на Python, работа с ML-моделями, знакомство с Git, и работа с TinkoffInvest API и TelegramBot API. Принцип работы: введите тикер компании например ROSB или TCSG, далее по тикеру выгружаются архивные данные по цене акций за последние 3 года со свечой 1 час, после чего создаётся таблица где будет стоимость акций по времени, макроэкономические параметры, показатели компании, и при помощи ML мы угадываем стоимость через 3, 6, 9, 12 месяцев ")
    
    main_menu(message)

# Обработка нажатия кнопки "Меню"
@bot.message_handler(func=lambda message: message.text == "Меню 📱")
def handle_menu(message):
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

# Обработка нажатия кнопки "Обновить"
@bot.message_handler(func=lambda message: message.text == "Обновить 🔁")
def handle_refresh(message):
    try:
        get_names(TOKEN)  # Вызов функции get_names
        bot.reply_to(message, "Успешно получили данные обо всех новых FIGI и Ticker.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обновлении файла: {str(e)}")
    main_menu(message)


# Запуск бота
if __name__ == '__main__':
    bot.polling()

