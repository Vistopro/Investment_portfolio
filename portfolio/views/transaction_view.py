from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from portfolio.forms import TransactionForm, FinancialInstrumentSearchForm
from portfolio.models import Transaction, FinancialInstrument

from django.shortcuts import get_object_or_404


