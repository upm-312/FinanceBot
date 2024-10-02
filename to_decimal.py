import pandas as pd
import re
from decimal import Decimal

class Quotation:
    def __init__(self, units, nano):  # Исправлено на __init__
        self.units = units
        self.nano = nano

    def to_big_decimal(self):
        return Decimal(self.units) + Decimal(self.nano) / Decimal(1_000_000_000)

def parse_quotation(quotation_str):
    # Используем регулярное выражение для извлечения units и nano
    match = re.match(r'Quotation\(units=(\d+), nano=(\d+)\)', quotation_str)
    if match:
        units = int(match.group(1))
        nano = int(match.group(2))
        return Quotation(units, nano).to_big_decimal()
    else:
        raise ValueError(f"Неверный формат: {quotation_str}")

def process_quotation_data():
    # Чтение CSV файла
    df = pd.read_csv('C:/FinanceBot/FinanceBot/historical_data/historical_data.csv')

    # Преобразование значений Quotation в Decimal для столбцов open, close
    for column in ['open', 'close']:
        df[column] = df[column].apply(parse_quotation)

    # Удаление ненужных столбцов
    df = df[['time', 'volume', 'open', 'close']]

    # Удаление части +00:00 из столбца time
    df['time'] = df['time'].str.replace(r'\+00:00$', '', regex=True)

    # Сохранение результата в новый CSV файл
    df.to_csv('C:/FinanceBot/FinanceBot/historical_data/historical_data_filtered.csv', index=False)
    print("Файл приведен к читаемому виду и сохранен в historical_data_filtered.csv")
if __name__ == "__main__":  # Исправлено на __name__
    process_quotation_data()
