from django import forms
from investment_portfolio.models.transaction import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        fields = ['instrument', 'transaction_type', 'quantity', 'price_per_unit']
