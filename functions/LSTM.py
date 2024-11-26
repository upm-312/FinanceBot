import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import LSTM, Dense, Dropout  # type: ignore
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# Загрузка данных
def LSTM_P():
    df = pd.read_csv('C:/FinanceBot/FinanceBot/historical_data/updated_data.csv')
    df = df[["date", "volume", "open", "close"]]
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    # Подготовка данных
    data = df['close'].values
    data = data.reshape(-1, 1)

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)

    # Определение длины обучающего набора
    training_data_len = int(np.ceil(len(scaled_data) * .8))
    train_data = scaled_data[0:training_data_len, :]

    # Функция для создания набора данных
    def create_dataset(data, time_step=1):
        X, Y = [], []
        for i in range(len(data) - time_step - 1):
            a = data[i:(i + time_step), 0]
            X.append(a)
            Y.append(data[i + time_step, 0])
        return np.array(X), np.array(Y)

    # Параметры
    time_step = 60  # Используем 60 предыдущих дней для прогнозирования
    X_train, y_train = create_dataset(train_data, time_step)

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

    # Создание модели
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(25))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mean_squared_error')

    # Обучение модели
    model.fit(X_train, y_train, batch_size=1, epochs=1)

    # Подготовка тестовых данных
    test_data = scaled_data[training_data_len - time_step:, :]
    X_test, y_test = create_dataset(test_data, time_step)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    # Прогнозирование
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)  # Обратное преобразование

    # Создание DataFrame для предсказаний
    train = df[:training_data_len]
    valid = df[training_data_len:].copy()  # Избегаем предупреждений о копиях

    # Добавление предсказаний в DataFrame valid
    valid['predictions'] = np.nan  # Инициализация столбца

    # Проверка длины предсказаний
    start_index = time_step
    start_index = 1
    # Убедимся, что мы не выходим за границы массива
    print(len(valid))
    print(len(predictions), " ", start_index)
    print(len(train))

    print(len(df))
    if start_index + len(predictions) <= len(valid):
        valid.loc[valid.index[start_index:start_index + len(predictions)], 'predictions'] = predictions.flatten()  # Заполнение предсказаний
    else:
        print("Ошибка: длина предсказаний превышает доступные индексы в valid.")

    # Визуализация
    plt.figure(figsize=(10, 5))
    #plt.figure(figsize=(16, 8))
    plt.title('5 years')
    
    plt.gcf().set_facecolor(rgb(30, 44, 57))  # Цвет фона фигуры
    plt.gca().set_facecolor(rgb(30, 44, 57))  # Цвет фона осей
    ax = plt.gca()
    ax.spines['top'].set_color(rgb(179, 199, 219))
    ax.spines['right'].set_color(rgb(179, 199, 219))
    ax.spines['left'].set_color(rgb(179, 199, 219))
    ax.spines['bottom'].set_color(rgb(179, 199, 219))
    plt.tick_params(axis='x', colors=rgb(179, 199, 219))  # Цвет меток по оси X
    plt.tick_params(axis='y', colors=rgb(179, 199, 219))  # Цвет меток по оси Y
    
    plt.title('5 Лет', color = rgb(179, 199, 219)) 

    plt.plot(train['close'], label ='Train', color = rgb(179, 199, 219), linewidth = 0.5)
    plt.plot(valid['close'], label ='Validation', color =rgb(205, 91, 69), linewidth = 0.5)
    plt.plot(valid['predictions'], label='Predictions', color =rgb(127,255,212), linewidth = 0.5)
    plt.axvline(x=valid.index[0], color='red', linestyle='--', label='Training End')
    plt.legend(loc='lower right')
    plt.savefig('C:/FinanceBot/FinanceBot/source/LSTM.png', dpi=300, bbox_inches='tight')
    plt.tight_layout()

    print(valid['predictions'])
    
    from datetime import datetime
    today = datetime.today()

    # Форматируем дату
    formatted_date = today.strftime("%d.%m.%Y")
    print(round(valid['predictions'].iloc[-1], 2))
    print("Текущая дата в формате дд.мм.гггг:", formatted_date)
    s ="На текущую дату " + str(formatted_date) + " цена составляет " + str(df["close"].iloc[-1]) + ". Модель сделала предсказание " + str(round(valid['predictions'].iloc[-1],2))
    return s


def rgb(r, g, b):
    return mcolors.to_hex([r/255, g/255, b/255])