from django.views import View
from django.shortcuts import render
from portfolio.api import get_data_stock, get_data_crypto, get_data_option, get_data_active

class AssetSearchView(View):
    template_name = 'asset_search.html'

    def get(self, request):

        symbol = request.GET.get('symbol', '').strip()
        data = None
        error = None

        if symbol:
            asset_type = get_data_active(symbol)

            if asset_type == 'crypto':
                data = get_data_crypto(symbol)
            elif asset_type == 'stock':
                data = get_data_stock(symbol)
            else:
                try:
                    data = get_data_option(symbol)
                except Exception as e:
                    error = str(e)

        context = {
            'symbol': symbol,
            'data': data,
            'error': error,
        }
        return render(request, self.template_name, context)