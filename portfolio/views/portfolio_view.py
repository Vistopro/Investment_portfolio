from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm
from portfolio.api import listar_activos


class PortfolioCreateView(View):
    def get(self, request):
        return render(request, 'portfolio_form.html', {'form': PortfolioForm()})

    def post(self, request, *args, **kwargs):
        form = PortfolioForm(data=request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio_list')
        return render(request, 'portfolio_form.html', {'form': form})


class PortfolioListView(LoginRequiredMixin, View):
    def get(self, request):
        portfolios = Portfolio.objects.filter(user=request.user)
        resul = listar_activos()
        return render(request, 'portfolio_list.html', {'portfolios': portfolios, 'resultant':resul})


class PortfolioEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        form = PortfolioForm(instance=portfolio)
        return render(request, 'portfolio_form.html', {'form': form})

    def post(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
        return render(request, 'portfolio_form.html', {'form': form})


class PortfolioDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        return render(request, 'portfolio_delete.html', {'object': portfolio})

    def post(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        portfolio.delete()
        return redirect('portfolio_list')
