from django.shortcuts import render
from django.views import View

from investment_portfolio.API import search_instruments
from investment_portfolio.forms import FinancialInstrumentSearchForm


class SearchFinancialInstrumentView(View):
    def get(self, request):
        form = FinancialInstrumentSearchForm(request.GET)
        instruments = []
        query = request.GET.get('query', '')
        if query:
            if form.is_valid():
                instruments = search_instruments(query)

        return render(request, 'search_financial_instrument.html', {
            'form': form,
            'instruments': instruments,
            'query': query
        })

    def post(self, request, *args, **kwargs):
        form = FinancialInstrumentSearchForm(request.POST)
        instruments = []
        query = ''
        if form.is_valid():
            query = form.cleaned_data['query']
            instruments = search_instruments(query)
        return render(request, 'search_financial_instrument.html', {
            'form': form,
            'instruments': instruments,
            'query': query
        })
