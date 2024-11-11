import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:/FinanceBot/FinanceBot/test.csv")

df['rsi'] = df['close'].reset_index(drop=True) - df ['open'].reset_index(drop=True)

print(df['rsi'])

start = 0
end = 180

for i in range(0, len(df['rsi'])):
    if i < end:
        #ТУТ ПРОДОЛЖИ
# Сохранение DataFrame в новый CSV-файл
df.to_csv("C:/FinanceBot/FinanceBot/test.csv", index=False)