from django.http import JsonResponse
import json
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from portfolio.models import Portfolio
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolio.api import get_name_from_symbol, get_historical_data, get_latest_price, \
    get_market_data_chart, get_all_assets



class AssetSearchView(LoginRequiredMixin, View):
    template_name = 'asset_search.html'

    def get(self, request, pk):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return self.get_dynamic(request)

        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        symbol = request.GET.get('symbol', '').strip().upper()

        asset_name = last_price = data = chart = None
        error = None

        if symbol:
            try:
                asset_name = get_name_from_symbol(symbol)
                last_price = get_latest_price(symbol)
                data = get_historical_data(symbol)
                chart = get_market_data_chart(symbol)

                if not asset_name or not last_price:
                    error = "It was not possible to get the data for the asset"

            except Exception as e:
                error = "An error occurred while trying to get the data for the asset"
        return render(request, self.template_name, {
            'portfolio': portfolio,
            'symbol': symbol,
            'asset_name': asset_name,
            'last_price': last_price,
            'chart': json.dumps(chart),
            'data': data,
            'error': error,
        })

    def get_dynamic(self, request):
        query = request.GET.get('query', '').strip().lower()
        if query:
            assets = get_all_assets()
            exact_matches = []
            contains_matches = []
            for asset in assets:
                symbol_lower = asset.symbol.lower()
                name_lower = asset.name.lower()
                if symbol_lower.startswith(query) or name_lower.startswith(query):
                    exact_matches.append(asset)
                elif query in symbol_lower or query in name_lower:
                    contains_matches.append(asset)
            assets = exact_matches + contains_matches

            assets = assets[:7]
            data = [{'symbol': asset.symbol, 'name': asset.name} for asset in assets]
            return JsonResponse(data, safe=False)
        return JsonResponse([], safe=False)


