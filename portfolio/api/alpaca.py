from alpaca.data import StockHistoricalDataClient, OptionHistoricalDataClient, CryptoHistoricalDataClient, TimeFrame
from alpaca.data.requests import StockBarsRequest, CryptoBarsRequest, OptionBarsRequest


from investment_portfolio.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY

stock_client = StockHistoricalDataClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY)
crypto_client = CryptoHistoricalDataClient()
option_client = OptionHistoricalDataClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY)

def get_data_stock(symbol):
    try:
        request_params = StockBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=10,
        )

        bars = stock_client.get_stock_bars(request_params)
        if bars:
            latest_bar = bars[symbol][-1]
            action_info = {
                'symbol': symbol,
                'price': latest_bar.close,
                'open': latest_bar.open,
                'high': latest_bar.high,
                'low': latest_bar.low,
                'volume': latest_bar.volume
            }
            return action_info
        else:
            return {"error": "No data found"}
    except Exception as e:
        return {"error": str(e)}

def get_data_crypto(symbol):
    try:
        request_params = CryptoBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=10,
        )

        bars = crypto_client.get_crypto_bars(request_params)
        if bars:
            latest_bar = bars[symbol][-1]
            action_info = {
                'symbol': symbol,
                'price': latest_bar.close,
                'open': latest_bar.open,
                'high': latest_bar.high,
                'low': latest_bar.low,
                'volume': latest_bar.volume
            }
            return action_info
        else:
            return {"error": "No data found"}
    except Exception as e:
        return {"error": str(e)}


def get_data_option(symbol):
    try:
        request_params = OptionBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=10,
        )

        bars = (option_client.get_option_bars(request_params))
        if bars:
            latest_bar = bars[symbol][-1]
            action_info = {
                'symbol': symbol,
                'price': latest_bar.close,
                'open': latest_bar.open,
                'high': latest_bar.high,
                'low': latest_bar.low,
                'volume': latest_bar.volume
            }
            return action_info
        else:
            return {"error": "No data found"}
    except Exception as e:
        return {"error": str(e)}


def get_data_active(symbol):
    crypto_suffixes = ('-USD', '-USDT', '-USDC')
    symbol = symbol.upper()

    if symbol.endswith(crypto_suffixes):
        return 'crypto'
    return 'stock'