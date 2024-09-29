import pandas as pd
import re
from decimal import Decimal

class Quotation:
    def __init__(self, units, nano):
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

def main():
    # Чтение CSV файла
    df = pd.read_csv('candles_data.csv')

    # Преобразование значений Quotation в Decimal для столбцов open, close, high, low
    for column in ['open', 'close', 'high', 'low']:
        df[column] = df[column].apply(parse_quotation)

    # Удаление ненужных столбцов
    df = df[['time', 'close']]

    # Удаление части +00:00 из столбца time
    df['time'] = df['time'].str.replace(r'\+00:00$', '', regex=True)

    # Сохранение результата в новый CSV файл
    df.to_csv('candles_data_filtered.csv', index=False)

if __name__ == "__main__":
    main()
