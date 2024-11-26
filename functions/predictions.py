import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error

# Загрузка данных
# Предполагается, что у вас есть CSV файл с данными, где 'date' - это дата, а 'close' - цена акций
data = pd.read_csv('C:/FinanceBot/FinanceBot/functions/updated_data.csv', parse_dates=['date'], index_col='date')
duplicates = data.index.duplicated()
if duplicates.any():
    print("Дублирующиеся индексы найдены:")
    print(data[data.index.duplicated()])
    # Удаление дубликатов
    data = data[~data.index.duplicated(keep='first')]
    # Или агрегация
    # data = data.groupby(data.index).mean()

# Применение asfreq
data = data.asfreq('4h')  # Убедитесь, что данные имеют частоту 4 часа
data = data.ffill()

print(data)  

  # Заполнение пропущенных значений

# Визуализация данных
plt.figure(figsize=(12, 6))
plt.plot(data['close'])
plt.title('Цены акций TCSG')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.show()

# Проверка стационарности
# Можно использовать тест Дики-Фуллера, чтобы проверить стационарность
from statsmodels.tsa.stattools import adfuller

result = adfuller(data['close'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# Если данные не стационарны, возможно, потребуется дифференцирование
data['close_diff'] = data['close'].diff()
data = data.dropna()

# Визуализация ACF и PACF
plot_acf(data['close_diff'])
plot_pacf(data['close_diff'])
plt.show()

# Определение параметров p, d, q
p = 100  # Порядок авторегрессии
d = 500  # Порядок дифференцирования
q = 10  # Порядок скользящей средней

# Построение модели ARIMA
model = ARIMA(data['close'], order=(p, d, q))
model_fit = model.fit()

# Вывод результатов
print(model_fit.summary())

# Прогнозирование
forecast_steps = 10  # Количество шагов для прогноза
forecast = model_fit.forecast(steps=forecast_steps)
print(forecast)

# Визуализация прогноза
plt.figure(figsize=(12, 6))
plt.plot(data['close'], label='Исторические данные')
plt.plot(pd.date_range(start=data.index[-1], periods=forecast_steps + 1, freq='4H')[1:], forecast, label='Прогноз', color='red')
plt.title('Прогноз цен акций TCSG')
plt.xlabel('Дата')
plt.ylabel('Цена')
plt.legend()
plt.show()

# Оценка модели
# Разделите данные на обучающую и тестовую выборки, чтобы оценить производительность модели
train_size = int(len(data) * 0.8)
train, test = data['close'][:train_size], data['close'][train_size:]

model = ARIMA(train, order=(p, d, q))
model_fit = model.fit()

# Прогнозирование на тестовой выборке
predictions = model_fit.forecast(steps=len(test))
error = mean_squared_error(test, predictions)
print(f'Mean Squared Error: {error}')
