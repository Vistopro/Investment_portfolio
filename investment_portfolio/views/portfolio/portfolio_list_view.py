from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from investment_portfolio.models import Portfolio


@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio_list.html', {'portfolios':portfolios})
