

from tinkoff.invest import Client
import requests
import requests
import zipfile
import os
import io

TOKEN = 't.DoRnMYw4mgCw6RKZb9OtozgIByzl4BACnj24WH2Zz0YhQ1_9OV2_CiLwM4FpyTEFK8UVe5yONaqZJtQbr-TsoA' #токен моего счета только для чтения

with Client(TOKEN) as client:
    print(client.users.get_accounts())
# Ваш токен доступа


# FIGI для валют и биткоина
figis = {
    "USD": "BBG00QX7QPC3",  # Доллар США
    "EUR": "BBG0013HGRY7",  # Евро
    "BTC": "BBG000C9VZQ3"   # Биткоин
}

# URL для получения исторических данных
url = 'https://invest-public-api.tinkoff.ru/history-data'

# FIGI для инструмента
figi = 'BBG00QX7QPC3'  # Замените на нужный вам FIGI
year = 2022  # Год для запроса

# Заголовки для запроса
headers = {
    'Authorization': f'Bearer {TOKEN}'
}

# Параметры запроса
params = {
    'figi': figi,
    'year': year
}

# Выполнение запроса
response = requests.get(url, headers=headers, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    # Путь для сохранения ZIP-архива
    zip_file_path = 'historical_data.zip'
    
    # Сохранение ZIP-архива
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    
    print(f"ZIP-архив успешно загружен: {zip_file_path}")
    
    # Распаковка ZIP-архива
    output_folder = 'historical_data'  # Папка для распаковки
    os.makedirs(output_folder, exist_ok=True)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)

    print(f"ZIP-архив успешно загружен: {os.path.abspath(zip_file_path)}")

    # Вывод списка распакованных файлов
    print("Содержимое папки:")
    for file_name in os.listdir(output_folder):
        print(file_name)
else:
    print(f"Ошибка: {response.status_code}, {response.text}")



# URL для получения информации о котировках
url = 'https://api.tinkoff.ru/v1/market/orderbook'
# Параметры запроса
params = {
    'figi': 'BBG00QKJSX05',  # FIGI для пары USD/RUB
    'depth': 1  # Глубина стакана
}

# Заголовки для запроса
headers = {
    'Authorization': f'Bearer {TOKEN}'
}



response = requests.get(url, headers=headers, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    data = response.json()
    print(data)  # Выводим полный ответ для отладки

    # Проверяем наличие ключа 'payload'
    if 'payload' in data:
        last_price = data['payload']['lastPrice']
        print(f"Текущий курс доллара к рублю: {last_price} RUB")
    else:
        print("Ключ 'payload' отсутствует в ответе.")
else:
    print(f"Ошибка: {response.status_code}, {response.text}")