import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import matplotlib.pyplot as plt

df = pd.read_csv('C:/FinanceBot/FinanceBot/LKOH_DAY.csv')
df = df[["date", "volume", "open", "close"]]
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

data = df['close'].values
data = data.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

training_data_len = int(np.ceil(len(scaled_data) * .8))
train_data = scaled_data[0:training_data_len, :]

def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 60
X_train, y_train = create_dataset(train_data, time_step)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(50, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(25))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, batch_size=1, epochs=1)

test_data = scaled_data[training_data_len - time_step:, :]
X_test, y_test = create_dataset(test_data, time_step)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

train = df[:training_data_len]
valid = df[training_data_len:].copy()
valid['predictions'] = np.nan

pred_len = len(predictions.flatten())
if pred_len == (len(valid) - time_step):
    valid.iloc[time_step:len(predictions) + time_step, valid.columns.get_loc('predictions')] = predictions.flatten()

last_60_days = scaled_data[-time_step:].reshape(1, time_step, 1)
future_predictions = []

for _ in range(60):
    next_pred = model.predict(last_60_days)
    future_predictions.append(next_pred[0, 0])
    last_60_days = np.append(last_60_days[:, 1:, :], next_pred.reshape(1, 1, 1), axis=1)

future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))
future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=60)
future_df = pd.DataFrame(data=future_predictions, index=future_dates, columns=['predictions'])

plt.figure(figsize=(16, 8))
plt.title('Model Predictions and Future Forecast')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(train['close'], label='Historical Data', color='blue')
plt.plot(valid['close'], label='Validation', color='orange')
plt.plot(valid['predictions'], label='Predictions', color='green')
plt.plot(future_df['predictions'], label='Future Predictions', color='red')
plt.axvline(x=valid.index[0], color='red', linestyle='--', label='Training End')
plt.legend(loc='lower right')
plt.show()
