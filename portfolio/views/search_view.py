from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from portfolio.models import Portfolio
from django.contrib.auth.mixins import LoginRequiredMixin
from portfolio.models import Transaction
from portfolio.api import get_data_stock, get_data_crypto, get_data_option, get_data_active


class AssetSearchView(LoginRequiredMixin,View):
    template_name = 'asset_search.html'

    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
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
            'portfolio': portfolio,
            'symbol': symbol,
            'data': data,
            'error': error,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        symbol = request.POST.get('symbol')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        date = request.POST.get('date')
        if symbol and quantity and price:
            Transaction.objects.create(
                user=request.user,
                portfolio=portfolio,
                asset_name=symbol,
                symbol=symbol,
                transaction_type='buy',
                quantity=quantity,
                price=price,
                date=date
            )

        return redirect('portfolio', pk=portfolio.id)