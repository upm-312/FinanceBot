import os
from datetime import datetime

# Путь к папке с вашими файлами
folder_path = './data_cost'
output_file = 'data_cost_file'

with open(output_file, 'w') as outfile:
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):  # Убедитесь, что обрабатываются только текстовые файлы
            with open(os.path.join(folder_path, filename), 'r') as infile:
                for line in infile:
                    parts = line.strip().split(';')
                    if len(parts) >= 5:  # Убедитесь, что строка содержит достаточное количество частей
                        timestamp = parts[1]
                        value = parts[3]
                        
                        # Преобразуем timestamp в нужный формат
                        dt = datetime.fromisoformat(timestamp[:-1])  # Удаляем 'Z' и преобразуем
                        formatted_line = f"{dt.strftime('%Y-%m-%d')} {dt.strftime('%H:%M:%S')} {value}\n"
                        
                        # Записываем в выходной файл
                        outfile.write(formatted_line)

print("Обработка завершена. Результат записан в", output_file)
