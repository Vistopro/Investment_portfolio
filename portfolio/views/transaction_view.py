from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from portfolio.api import search_instruments
from portfolio.forms import TransactionForm, FinancialInstrumentSearchForm
from portfolio.models import Transaction, FinancialInstrument

from django.shortcuts import get_object_or_404


class TransactionCreateView(View):
    def get(self, request):
        search_form = FinancialInstrumentSearchForm()
        transaction_form = TransactionForm()
        selected_instrument = request.session.get('selected_instrument', None)
        return render(request, 'transaction_form.html', {
            'search_form': search_form,
            'transaction_form': transaction_form,
            'instruments': [],
            'selected_instrument': selected_instrument
        })
    def post(self, request):
        if 'select_instrument' in request.POST:
            symbol = request.POST.get('selected_instrument')
            request.session['selected_instrument'] = symbol

            # Intenta obtener el FinancialInstrument desde la base de datos
            instrument, created = FinancialInstrument.objects.get_or_create(
                symbol=symbol,
                defaults={'name': 'Unknown', 'type': 'Unknown'}
            )

            search_form = FinancialInstrumentSearchForm()
            transaction_form = TransactionForm(initial={'financial_instrument': instrument.id})
            return render(request, 'transaction_form.html', {
                'search_form': search_form,
                'transaction_form': transaction_form,
                'instruments': [],
                'selected_instrument': instrument.symbol
            })

        elif 'create_transaction' in request.POST:
            transaction_form = TransactionForm(request.POST)
            if transaction_form.is_valid():
                transaction = transaction_form.save(commit=False)

                # Asocia el instrumento seleccionado a la transacción
                symbol = request.session.get('selected_instrument')
                instrument = get_object_or_404(FinancialInstrument, symbol=symbol)
                transaction.instrument = instrument
                transaction.user = request.user
                transaction.save()

                request.session.pop('selected_instrument', None)
                return redirect('transaction_list')

        return render(request, 'transaction_form.html', {
            'search_form': FinancialInstrumentSearchForm(),
            'transaction_form': TransactionForm(),
            'instruments': [],
            'selected_instrument': request.session.get('selected_instrument', None)
        })


class TransactionListView(LoginRequiredMixin, View):
    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        return render(request, 'transaction_list.html', {'transactions': transactions})


class TransactionEditView(LoginRequiredMixin, View):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, id=pk, user=request.user)
        form = TransactionForm(instance=transaction)
        return render(request, 'transaction_form.html', {'form': form})

    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, id=pk, user=request.user)
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
        return render(request, 'transaction_form.html', {'form': form})


class TransactionDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, id=pk, user=request.user)
        return render(request, 'transaction_confirm_delete.html', {'object': transaction})

    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, id=pk, user=request.user)
        transaction.delete()
        return redirect('transaction_list')
