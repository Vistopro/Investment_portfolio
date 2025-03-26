from django import forms
from portfolio.models.transaction import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['symbol','quantity', 'price', 'date', 'commission']
        widgets = {
            'symbol': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'commission': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Commission'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symbol'].widget.attrs['readonly'] = True
