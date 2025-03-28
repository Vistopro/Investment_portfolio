from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from portfolio.models import Transaction, Portfolio
from portfolio.forms import TransactionForm

class TransactionCreateView(LoginRequiredMixin, View):
    def get(self, request, pk_portfolio):
        portfolio = get_object_or_404(Portfolio, id=pk_portfolio, user=request.user)
        symbol = request.GET.get('symbol', '')
        form = TransactionForm(initial={'symbol': symbol})
        return render(request, 'transaction_form.html', {'form': form, 'portfolio': portfolio})

    def post(self, request, pk_portfolio):
        portfolio = get_object_or_404(Portfolio, id=pk_portfolio, user=request.user)
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.portfolio = portfolio
            transaction.save()
            return redirect('portfolio', pk=pk_portfolio)
        return render(request, 'transaction_form.html', {'form': form, 'portfolio': portfolio})

class TransactionEditView(LoginRequiredMixin, View):
    def get(self, request, pk_transaction):
        transaction = get_object_or_404(Transaction, id=pk_transaction, user=request.user)
        form = TransactionForm(instance=transaction)
        return render(request, 'transaction_update.html', {'form': form, 'portfolio':  transaction.portfolio})

    def post(self, request, pk_transaction):
        transaction = get_object_or_404(Transaction, id=pk_transaction, user=request.user)
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('portfolio', pk=transaction.portfolio.pk)
        return render(request, 'transaction_update.html', {'form': form, 'portfolio': transaction.portfolio})

class TransactionDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk_transaction):
        transaction = get_object_or_404(Transaction, id=pk_transaction, user=request.user)
        return render(request, 'transaction_delete.html', {'object': transaction, 'portfolio':transaction.portfolio})

    def post(self, request, pk_transaction):
        transaction = get_object_or_404(Transaction, id=pk_transaction, user=request.user)
        transaction.delete()
        return redirect('portfolio',pk=transaction.portfolio.pk)
