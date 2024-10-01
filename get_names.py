from tinkoff.invest.services import MarketDataService, InstrumentsService
from tinkoff.invest import Client, InstrumentStatus
import pandas as pd
from token_1 import TOKEN

def get_names(TOKEN):
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    with Client(TOKEN) as cl:
        instruments: InstrumentsService = cl.instruments
        df = pd.DataFrame(instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments, 
                          columns=["name", 'figi', 'ticker', "class_code", "country_of_risk"])

        
        # Фильтрация акций, где country_of_risk == "RU"
        df_ru = df[df['country_of_risk'] == "RU"]
        # Сохранение отфильтрованных данных в файл
        df_ru.to_csv('./source/name_figi_ticker_ru.txt', sep='\t', index=False)     
    print("Получили актуальные FIGI и Ticker акций российских компаний")
    