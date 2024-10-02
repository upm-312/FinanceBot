import telebot;
from telebot import types


bot = telebot.TeleBot('8038962051:AAG4BRFC9BNpDKzV8BtdRlbr5Gzof1GrmvE');



@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Поиск")
    btn2 = types.KeyboardButton("Войти")
    markup.row(btn1,btn2)
    btn3 = types.KeyboardButton("Курс")
    btn4 = types.KeyboardButton("Инфо")
    markup.row(btn3,btn4)
    bot.send_message(message.chat.id,"Здравствуйте!Выберете пожалуйста действие",reply_markup=markup)
    bot.register_next_step_handler(message,on_click)

def on_click(message):
    if message.text == "Поиск":
        bot.send_message(message.chat.id,'еще не готово()')
        
    elif message.text == "Войти":
        bot.send_message(message.chat.id,'еще не готово()')
        

    elif message.text == "Курс":
        bot.send_message(message.chat.id,'еще не готово()')
        

    elif message.text == "Инфо":
        bot.send_message(message.chat.id,'FinanceBot поможет вам узнать, сколько будут стоить акции интересующих вас фирм через время. При помощи искусственного интеллекта и машинного обучения бот анализирует и выдает вам предварительную цену акций нужной вам компании. Попробуйте!)')
       


@bot.message_handler(commands=["info"])
def main(message):
    bot.send_message(message.chat.id,"FinanceBot поможет вам узнать, сколько будут стоить акции интересующих вас фирм через время. При помощи искусственного интеллекта и машинного обучения бот анализирует и выдает вам предварительную цену акций нужной вам компании. Попробуйте!")






bot.polling(none_stop=True)