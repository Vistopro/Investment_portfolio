from django import forms
from django.contrib.auth.forms import UserCreationForm
from investment_portfolio.models.user import User


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
