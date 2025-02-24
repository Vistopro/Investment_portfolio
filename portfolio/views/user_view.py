from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View

from ..forms import CreateUserForm, UserUpdateForm


class HomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('portfolio_list')
        return render(request, 'home.html')


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form, 'login': True})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio_list')
            else:
                form.add_error(None, "Invalid username or password")
        return render(request, 'login.html', {'form': form, 'login': True})


class RegisterView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form, 'register': True})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('portfolio_list')
        return render(request, 'register.html', {'form': form, 'register': True})

@method_decorator(login_required, name='dispatch')
class EditView(View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, 'user_update.html', {'form': form, 'update': True})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('portfolio_list')
        return render(request, 'user_update.html', {'form': form, 'update': True})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
