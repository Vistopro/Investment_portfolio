import os
from alpaca.data import StockHistoricalDataClient, OptionHistoricalDataClient, TimeFrame
from alpaca.data.requests import StockBarsRequest


from investment_portfolio.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY

stock_client = StockHistoricalDataClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY)
crypto_client = CryptoHistoricalDataClient()
option_client = OptionHistoricalDataClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY

def get_data_stock(symbol):
    try:
        request_params = StockBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=10,
        )

       if bars:
           latest_bar = bars[-1]
           action_info = {
                'symbol': symbol,
                'price': latest_bar.close,  # Último precio de la acción
                'open': latest_bar.open,  # Precio de apertura
                'high': latest_bar.high,  # Precio máximo
                'low': latest_bar.low,   # Precio mínimo
                'volume': latest_bar.volume  # Volumen de transacciones
            }
           return action_info