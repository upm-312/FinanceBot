import telebot
import requests

TOKEN = '8185806685:AAEwqjsn_YyjcKjL_iTWdlqwRGO01XBWaLA'
bot = telebot.TeleBot(TOKEN)

API_KEY = 'ef38932d54316f2ed0e81d49'

def get_currency_rates():
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/RUB"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = "Курсы валют:\n"
        
        # Определяем список валют, которые нужно вывести
        target_currencies = ['USD', 'EUR', 'CNY']
        
        # Проходим по всем доступным валютам и добавляем их к строке
        for currency, rate in data['conversion_rates'].items():
            if currency in target_currencies:  # Проверяем только на заданные валюты
                if currency == 'RUB':
                    rates += f"{1} {currency}\n"
                else:
                    exchange_rate = 1 / rate  # Рассчитываем 1/rate
                    formatted_rate = f"{exchange_rate:.4g}"  # Ограничиваем до 4 символов
                    rates += f"{currency}: {formatted_rate} RUB \n"
        return rates
    else:
        return "Ошибка получения данных."