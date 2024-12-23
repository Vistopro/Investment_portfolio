from django import forms
from portfolio.models.financial_instrument import FinancialInstrument


class FinancialInstrumentForm(forms.ModelForm):
    class Meta:
        model = FinancialInstrument
        fields = ['name', 'symbol', 'instrument_type', 'description']


class FinancialInstrumentSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
