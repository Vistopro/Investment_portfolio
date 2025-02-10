from django import forms
from portfolio.models.transaction import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['symbol','quantity', 'price', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symbol'].widget.attrs['readonly'] = True
        self.fields['price'].widget.attrs['readonly'] = True
