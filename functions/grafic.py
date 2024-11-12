import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
from datetime import datetime
import matplotlib.colors as mcolors

def rgb(r, g, b):
    return mcolors.to_hex([r/255, g/255, b/255])


df = pd.read_csv("C:/FinanceBot/FinanceBot/historical_data/updated_data.csv")
df['date'] = pd.to_datetime(df['date'])  # Убедитесь, что столбец 'date' в формате datetime
df.set_index('date', inplace=True)
plt.figure(figsize=(10, 5))
plt.gcf().set_facecolor(rgb(30, 44, 57))  # Цвет фона фигуры
plt.gca().set_facecolor(rgb(30, 44, 57))  # Цвет фона осей
plt.title('5 Лет', color=rgb(179, 199, 219)) 

# Построение графика
plt.plot(df.index, df['close'], linestyle='-', color=rgb(179, 199, 219), linewidth=0.5)  # Убираем маркеры
# Установка пределов по оси X
plt.gca().set_xlim(datetime(2019, 10, 1), df.index[-1].to_pydatetime())  
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  




plt.xticks(rotation=45, color=rgb(179, 199, 219))  # Устанавливаем цвет меток по оси X
plt.yticks(color=rgb(179, 199, 219))                # Устанавливаем цвет меток по оси Y
ax = plt.gca()
ax.spines['top'].set_color(rgb(179, 199, 219))
ax.spines['right'].set_color(rgb(179, 199, 219))
ax.spines['left'].set_color(rgb(179, 199, 219))
ax.spines['bottom'].set_color(rgb(179, 199, 219))
plt.tick_params(axis='x', colors=rgb(179, 199, 219))  # Цвет меток по оси X
plt.tick_params(axis='y', colors=rgb(179, 199, 219))  # Цвет меток по оси Y

# Автоматическая подгонка параметров
plt.tight_layout()

# Сохранение графика в файл
plt.savefig('FinanceBot/source/5Y.png', dpi=300, bbox_inches='tight')  # Сохранение в формате PNG с разрешением 300 dpi

# Закрытие графика
plt.close()
