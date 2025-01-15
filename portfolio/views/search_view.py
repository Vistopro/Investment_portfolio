from django.shortcuts import render, redirect
from django.views import View
from portfolio.api import get_data_active


def asset_search_view(request):
    symbol = request.GET.get('symbol')
    data = get_data_active(symbol=symbol)
    return render(request, 'asset_search_result.html', {'data': data})