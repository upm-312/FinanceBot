import pandas as pd
import numpy as np

# Загрузка данных из CSV файла
df_csv = pd.read_csv('C:/FinanceBot/FinanceBot/historical_data/data.csv')

# Преобразование столбца 'date' в datetime с обработкой ошибок
df_csv['date'] = pd.to_datetime(df_csv['date'], errors='coerce')

# Создание столбцов
df_csv['rate'] = np.nan  
df_csv['infl'] = np.nan
df_csv['vvp'] = np.nan

# Загрузка данных 
df_rates = pd.read_csv("C:/FinanceBot/FinanceBot/fundament/cb_rates.csv", sep = ";")
df_infl = pd.read_csv("C:/FinanceBot/FinanceBot/fundament/infl.csv", sep = ",")
df_vvp = pd.read_csv("C:/FinanceBot/FinanceBot/fundament/vvp.csv", sep = ",")

# Преобразование столбца 'time' в datetime с обработкой ошибок
if 'date' in df_rates.columns:
    df_rates['date'] = pd.to_datetime(df_rates['date'], errors='coerce', dayfirst=True)
else:
    raise KeyError("Столбец 'time' не найден в Excel файле.")

if 'date' in df_infl.columns:
    df_infl['date'] = pd.to_datetime(df_infl['date'], errors='coerce', dayfirst=True)
else:
    raise KeyError("Столбец 'time' не найден в Excel файле.")

if 'date' in df_vvp.columns:
    df_vvp['date'] = pd.to_datetime(df_vvp['date'], errors='coerce', dayfirst=True)
else:
    raise KeyError("Столбец 'time' не найден в Excel файле.")

# Переменная для отслеживания текущего индекса 'time' в df_excel
current_date_rates = 0
current_date_infl = 0
current_date_vvp = 0

# Итерация по строкам df_csv
for i in range(len(df_csv)):
    current_date = df_csv.loc[i, 'date']
    # Перебираем строки df_excel, пока не найдем соответствие по дате
    while (current_date_rates < len(df_rates) and current_date >= df_rates.loc[current_date_rates, 'date']):
        current_date_rates += 1  # Переходим к следующему 'time'
        
    while (current_date_infl < len(df_infl) and current_date >= df_infl.loc[current_date_infl, 'date']):
        current_date_infl += 1  # Переходим к следующему 'time'
        
    while (current_date_vvp < len(df_vvp) and current_date >= df_vvp.loc[current_date_vvp, 'date']):
        current_date_vvp += 1  # Переходим к следующему 'time'
          
    # Если current_time_index больше 0, значит мы нашли соответствующую дату
    if current_date_rates > 0:
        df_csv.loc[i, 'rate'] = df_rates.loc[current_date_rates - 1, 'rate']  # Используем предыдущий индекс
    if current_date_infl > 0:
        df_csv.loc[i, 'infl'] = df_infl.loc[current_date_infl - 1, 'infl']  # Используем предыдущий индекс 
    if current_date_vvp > 0:
        df_csv.loc[i, 'vvp'] = df_vvp.loc[current_date_vvp - 1, 'vvp']  # Используем предыдущий индекс     
# Сохранение обновленного CSV файла
df_csv.to_csv('C:/FinanceBot/FinanceBot/historical_data/updated_data.csv', index=False)

# Вывод результата
print(df_csv)
