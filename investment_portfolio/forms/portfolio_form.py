from django import forms
from investment_portfolio.models.portfolio import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "description"]
