from tinkoff.invest import Client
import pandas as pd

# Читаем таблицу из файла, используя табуляцию как разделитель
figis = pd.read_csv('source/name_figi_ticker.txt', sep='\t', encoding='utf-8', on_bad_lines='skip')

# Выводим DataFrame
company = input("Ввести название компании, для которой необходимо найти FIGI, например Сбербанк ")
result = figis.loc[figis.iloc[:, 0] == company, figis.columns[:3]]

# Проверяем, найдены ли строки
if not result.empty:
    print("Найденные строки:")
    print(result)
else:
    print("Компания не найдена.")