from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from investment_portfolio.models import Portfolio
from investment_portfolio.forms import PortfolioForm


class PortfolioEditView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    template_name = 'portfolio_form.html'
    success_url = reverse_lazy('portfolio_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Portfolio, id=self.kwargs['pk'], user=self.request.user)
