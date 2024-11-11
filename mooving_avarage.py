import pandas as pd

df = pd.read_csv("C:/FinanceBot/FinanceBot/historical_data/updated_data.csv")

# Расчет 270-дневной скользящей средней
df['moving_average'] = round(df['close'].rolling(window=270).mean(), 3)
df['e_avarage270'] = round(df['close'].ewm(span=270, adjust=False).mean(), 3)  # EMA за 270
df['e_avarage360'] = round(df['close'].ewm(span=360, adjust=False).mean(), 3)  # EMA за 360

# Расчет MACD Line
df['MACD_Line'] = round(df['e_avarage270'] - df['e_avarage360'], 3)

# Рассчет Signal Line (9-дневная EMA от MACD Line)
df['Signal_Line'] = round(df['MACD_Line'].ewm(span=9, adjust=False).mean(), 3)

# Сохранение результатов в CSV
df.to_csv("C:/FinanceBot/FinanceBot/test.csv", index=False)
