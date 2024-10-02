import os
import pandas as pd
from tinkoff.invest import Client, InstrumentStatus
from tinkoff.invest.services import InstrumentsService
from token_1 import TOKEN

def get_names(TOKEN):
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    #TOKEN = 't.DoRnMYw4mgCw6RKZb9OtozgIByzl4BACnj24WH2Zz0YhQ1_9OV2_CiLwM4FpyTEFK8UVe5yONaqZJtQbr-TsoA'
    with Client(TOKEN) as cl:
        instruments: InstrumentsService = cl.instruments
        df = pd.DataFrame(instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments, 
                          columns=["name", 'figi', 'ticker', "class_code", "country_of_risk"])

        # Фильтрация акций, где country_of_risk == "RU"
        df_ru = df[df['country_of_risk'] == "RU"]
        
        # Указываем абсолютный путь к директории
        directory = 'C:/FinanceBot/FinanceBot/source'

        # Проверяем, существует ли директория, и создаем её, если нет
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Сохранение отфильтрованных данных в файл
        df_ru.to_csv(os.path.join(directory, 'name_figi_ticker_ru.txt'), sep='\t', index=False)     
        
        
        return "Получили актуальные FIGI и Ticker акций российских компаний"

