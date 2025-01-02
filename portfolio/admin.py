from django.contrib import admin
from portfolio.models import FinancialInstrument, Transaction, Quote, Portfolio

admin.site.register(FinancialInstrument)
admin.site.register(Transaction)
admin.site.register(Quote)
admin.site.register(Portfolio)
