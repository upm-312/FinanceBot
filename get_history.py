from tinkoff.invest import Client
from token_1 import TOKEN
import requests
import requests
import zipfile
import os

# URL для получения исторических данных
url = 'https://invest-public-api.tinkoff.ru/history-data'

# FIGI для инструмента
figi = "ISSUANCEMOEX"  # Замените на нужный вам FIGI BBG01LR40593. BBG00QX7QPC3. BBG00KDWPPW2
year = int(input("За какой год показать историю ")) # Год для запроса

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
    zip_file_path = 'data_cost.zip'
    # Сохранение ZIP-архива
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)
    # Папка для распаковки
    output_folder = 'data_cost'  # Измените на папку для распаковки
    os.makedirs(output_folder, exist_ok=True)
    # Распаковка ZIP-архива
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)
    # Удаление ZIP-архива
    os.remove(zip_file_path)
    print("Готово!")
else:
    print(f"Ошибка: {response.status_code}, {response.text}")