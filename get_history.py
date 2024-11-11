from datetime import timedelta
import pandas as pd
from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now
from token_1 import TOKEN

def get_history(FIGI):
    with Client(TOKEN) as client:
        # Создаем пустой список для хранения данных
        data = []

        # Получаем исторические данные
        for candle in client.get_all_candles(
            figi=FIGI,
            from_=now() - timedelta(days=5*365),
            interval=CandleInterval.CANDLE_INTERVAL_4_HOUR,
        ):
            data.append({
                'time': candle.time,
                'open': candle.open,
                'close': candle.close,
                'volume': candle.volume
            })

        # Преобразуем список в DataFrame
        df = pd.DataFrame(data)

        # Сохраняем только необходимые столбцы
        df = df[['time', 'volume', 'open', 'close']]

        # Сохраняем DataFrame в CSV файл
        df.to_csv('C:/FinanceBot/FinanceBot/historical_data/historical_data.csv', index=False)
    
    print("Исторические данные сохранены в файл 'historical_data.csv', приводим к читаемому виду")
    return 0