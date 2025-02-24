from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm



class PortfolioCreateView(View):
    def get(self, request):
        return render(request, 'portfolio_form.html', {'form': PortfolioForm(),'is_edit': False})

    def post(self, request, *args, **kwargs):
        form = PortfolioForm(data=request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio_list')
        return render(request, 'portfolio_form.html', {'form': form,'is_edit': False})


class PortfolioListView(LoginRequiredMixin, View):
    def get(self, request):
        portfolios = Portfolio.objects.filter(user=request.user)
        request.session['last_portfolio_id'] = None
        return render(request, 'portfolio_list.html', {'portfolios': portfolios, 'is_in_portfolio': False})


class PortfolioEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        form = PortfolioForm(instance=portfolio)
        return render(request, 'portfolio_form.html', {'form': form,'is_edit': True})

    def post(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
        return render(request, 'portfolio_form.html', {'form': form,'is_edit': True})


class PortfolioDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        return render(request, 'portfolio_delete.html', {'object': portfolio})

    def post(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        portfolio.delete()
        return redirect('portfolio_list')

class PortfolioView(LoginRequiredMixin, View):
    def get(self, request, pk):
        portfolio = get_object_or_404(Portfolio, id=pk, user=request.user)
        request.session['last_portfolio_id'] = portfolio.pk
        return render(request, 'portfolio_view.html', {'portfolio': portfolio, 'is_in_portfolio': True})
