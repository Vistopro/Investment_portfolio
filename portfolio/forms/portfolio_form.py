from django import forms
from portfolio.models.portfolio import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ["name", "description"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Name"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"}),
        }
