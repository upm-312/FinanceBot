import os
from datetime import timedelta
from tinkoff.invest import CandleInterval, Client
from tinkoff.invest.utils import now
from token_1 import TOKEN
import pandas as pd

def main():
    # Создаем пустой DataFrame для хранения данных
    candles_data = pd.DataFrame(columns=["time", "open", "close", "high", "low", "volume"])
    
    with Client(TOKEN) as client:
        # Создаем список для хранения данных свечей
        candles_list = []
        
        for candle in client.get_all_candles(
            figi="BBG004730N88",
            from_=now() - timedelta(days=1095),  # За 3 года
            interval=CandleInterval.CANDLE_INTERVAL_HOUR,
        ):
            # Добавляем данные свечи в список
            candles_list.append({
                "time": candle.time,
                "open": candle.open,
                "close": candle.close,
                "high": candle.high,
                "low": candle.low,
                "volume": candle.volume
            })
        
        # Конвертируем список в DataFrame
        candles_data = pd.DataFrame(candles_list)
    
    # Сохраняем данные в CSV файл
    candles_data.to_csv("candles_data.csv", index=False)
    print("Данные успешно сохранены в файл: candles_data.csv")

    return 0

if __name__ == "__main__":
    main()