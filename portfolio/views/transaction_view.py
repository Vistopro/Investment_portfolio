from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from portfolio.models import Transaction, Portfolio
from portfolio.forms import TransactionForm

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
