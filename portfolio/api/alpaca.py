from alpaca.data import (StockHistoricalDataClient,
                         OptionHistoricalDataClient,
                         CryptoHistoricalDataClient,
                         TimeFrame,)
from alpaca.data.requests import (StockBarsRequest,
                                  CryptoBarsRequest,
                                  OptionBarsRequest,
                                  CryptoLatestQuoteRequest,
                                  StockLatestQuoteRequest)
from datetime import datetime, timedelta

from alpaca.trading import TradingClient

from investment_portfolio.settings import ALPACA_API_KEY, ALPACA_SECRET_KEY

stock_client = StockHistoricalDataClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY)
crypto_client = CryptoHistoricalDataClient()
option_client = OptionHistoricalDataClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY)
trading_client = TradingClient(api_key=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, paper = True)

start_date = (datetime.now() - timedelta(days=365)).isoformat()
end_date = datetime.now().isoformat()

def get_latest_price(symbol):
    """Get the latest price of a stock, crypto, or option
    If the symbol ends with /USD, /USDT, or /USDC, it is a crypto
    Otherwise, it is a stock
    input: symbol
    format: string
    output: latest price of the asset
    format: float"""

    crypto_suffixes = ('/USD', '/USDT', '/USDC')
    symbol = symbol.upper()

    if symbol.endswith(crypto_suffixes):
        request_params = CryptoLatestQuoteRequest(symbol_or_symbols=[symbol])
        latest_quote = crypto_client.get_crypto_latest_quote(request_params)
        return latest_quote[symbol].ask_price

    else:
        request_params = StockLatestQuoteRequest(symbol_or_symbols=[symbol])
        latest_quote = stock_client.get_stock_latest_quote(request_params)
        return latest_quote[symbol].ask_price

def get_name_from_symbol(symbol):
    asset = trading_client.get_asset(symbol)
    return asset.name

def get_historical_data(symbol):
    """Get the historical data of a stock, crypto, or option
    If the symbol ends with /USD, /USDT, or /USDC, it is a crypto
    Otherwise, it is a stock
    input: symbol
    format: string
    output: historical data of the asset
    format: dictionary"""

    crypto_suffixes = ('/USD', '/USDT', '/USDC')
    symbol = symbol.upper()

    if symbol.endswith(crypto_suffixes):
        request_params = CryptoBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=10,
            start=start_date,
            end=end_date,
        )
        bars = crypto_client.get_crypto_bars(request_params)
    else:
        request_params = StockBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=10,
            start=start_date,
            end=end_date,
            feed='iex'
        )
        bars = stock_client.get_stock_bars(request_params)
    if bars:
            latest_bar = bars[symbol][-1]
            action_info = {
                'symbol': symbol,
                'price': latest_bar.close,
                'open': latest_bar.open,
                'close': latest_bar.close,
                'high': latest_bar.high,
                'low': latest_bar.low,
                'volume': latest_bar.volume
            }
            return action_info
    else:
        return {"error": "No data found"}

def get_market_data_chart(symbol):
    """Get the historical data of a stock, crypto, or option
    If the symbol ends with /USD, /USDT, or /USDC, it is a crypto
    Otherwise, it is a stock
    input: symbol
    format: string
    output: historical data of the asset
    format: list of dictionaries
    time: string
    open: float
    high: float
    low: float
    close: float
    """

    crypto_suffixes = ('/USD', '/USDT', '/USDC')
    symbol = symbol.upper()

    if symbol.endswith(crypto_suffixes):
        request_params = CryptoBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=365,
            start=start_date,
            end=end_date,
        )
        bars = crypto_client.get_crypto_bars(request_params)
    else:
        request_params = StockBarsRequest(
            symbol_or_symbols=[symbol],
            timeframe=TimeFrame.Day,
            limit=365,
            start=start_date,
            end=end_date,
            feed='iex'
        )
        bars = stock_client.get_stock_bars(request_params)

    if not bars:
        return {"error": "No data found"}

    data = bars[symbol]
    formatted_data = [
        {
            "time": bar.timestamp.strftime('%Y-%m-%d'),
            "open": bar.open,
            "high": bar.high,
            "low": bar.low,
            "close": bar.close
        }
        for bar in data
    ]

    return formatted_data

def get_all_assets():
    #obtain all assets
    assets = trading_client.get_all_assets()
    return assets

def get_data_option(symbol):
    #not implemented yet
    symbol = symbol.upper()
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
                'close': latest_bar.close,
                'high': latest_bar.high,
                'low': latest_bar.low,
                'volume': latest_bar.volume
            }
            return action_info
        else:
            return {"error": "No data found"}
    except Exception as e:
        return {"error": str(e)}

