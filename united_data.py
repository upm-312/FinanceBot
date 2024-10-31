import pandas as pd
import numpy as np

# Загрузка данных из CSV файла
csv_file_path = r'C:\FinanceBot\FinanceBot\historical_data\data.csv'
df_csv = pd.read_csv(csv_file_path)

# Преобразование столбца 'date' в datetime с обработкой ошибок
df_csv['date'] = pd.to_datetime(df_csv['date'], errors='coerce')

# Создание столбца 'rate' и заполнение его значениями NaN
df_csv['rate'] = np.nan  # Инициализация столбца 'rate' с NaN

# Загрузка данных из Excel файла
excel_file_path = r'C:\FinanceBot\FinanceBot\source\cb_rates.xlsx'
df_excel = pd.read_excel(excel_file_path)

# Удаление лишних пробелов в именах столбцов
df_excel.columns = df_excel.columns.str.strip()

# Преобразование столбца 'time' в datetime с обработкой ошибок
if 'time' in df_excel.columns:
    df_excel['time'] = pd.to_datetime(df_excel['time'], errors='coerce')
else:
    raise KeyError("Столбец 'time' не найден в Excel файле.")

# Переменная для отслеживания текущего индекса 'time' в df_excel
current_time_index = 0

# Итерация по строкам df_csv
for i in range(len(df_csv)):
    current_date = df_csv.loc[i, 'date']
    
    # Перебираем строки df_excel, пока не найдем соответствие по дате
    while (current_time_index < len(df_excel) and current_date >= df_excel.loc[current_time_index, 'time']):
        current_time_index += 1  # Переходим к следующему 'time'

    # Если current_time_index больше 0, значит мы нашли соответствующую дату
    if current_time_index > 0:
        # Заполняем столбец 'rate' в df_csv значением из df_excel
        df_csv.loc[i, 'rate'] = df_excel.loc[current_time_index - 1, 'rate']  # Используем предыдущий индекс

# Сохранение обновленного CSV файла
output_csv_file_path = r'C:\FinanceBot\FinanceBot\sourse\updated_data.csv'
df_csv.to_csv(output_csv_file_path, index=False)

# Вывод результата
print(df_csv)
