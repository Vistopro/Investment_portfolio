import os
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')



def search_instruments(query):
    tickers = []

    try:
        # Crear instancias de las clases de Alpha Vantage
        ts = TimeSeries(key=API_KEY, output_format='json')
        fd = FundamentalData(key=API_KEY, output_format='json')

        # Obtener los datos de precios intradía (puedes ajustar el intervalo según sea necesario)
        data, meta_data = ts.get_intraday(symbol=query, interval='1min', outputsize='compact')

        # Obtener la información fundamental
        overview, _ = fd.get_company_overview(query)

        # Verificar si los datos existen
        if 'Symbol' in overview and 'Name' in overview:
            # Extraer el precio más reciente
            last_close = list(data.values())[0]['4. close'] if data else 'N/A'

            tickers.append({
                'symbol': overview.get('Symbol', 'N/A'),
                'name': overview.get('Name', 'N/A'),
                'sector': overview.get('Sector', 'N/A'),
                'type': overview.get('AssetType', 'N/A'),
                'price': last_close,
                'description': overview.get('Description', 'N/A')
            })

    except Exception as e:
        print(f"Error fetching data for {query}: {e}")

    return tickers
