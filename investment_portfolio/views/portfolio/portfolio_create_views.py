from django.shortcuts import render, redirect
from django.views import View
from investment_portfolio.forms import PortfolioForm


class PortfolioCreateView(View):
    def get(self, request):
        form = PortfolioForm()
        return render(request, 'portfolio_form.html', {'form': form})

    def post(self, request):
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio_list')
        return render(request, 'portfolio_form.html', {'form': form})

