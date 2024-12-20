from django import forms
from investment_portfolio.models.transaction import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'quantity', 'price', 'date']
