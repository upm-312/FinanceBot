from tinkoff.invest.services import MarketDataService, InstrumentsService
from tinkoff.invest import Client, InstrumentStatus
import pandas as pd
from token_1 import TOKEN
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def run():
    with Client(TOKEN) as cl:
        instruments : InstrumentsService = cl.instruments
        market_data: MarketDataService = cl.market_data
        #r =instruments.share_by(id_type = InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id = "BBG007N0Z367")
        df = pd.DataFrame(instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments, 
                         columns = ["name", 'figi', 'ticker', 'class_code'])
        df.to_csv('name_figi_ticker.txt', sep='\t', index=False)
        
if __name__ == '__main__':
    run()