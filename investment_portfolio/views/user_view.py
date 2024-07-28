from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from ..forms import CreateUserForm


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio_list')  # Redirige después de iniciar sesión
            else:
                form.add_error(None, "Invalid username or password")
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'login': True})


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('portfolio_list')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form, 'register':True})
