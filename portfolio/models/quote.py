from django.db import models
from portfolio.models.financial_instrument import FinancialInstrument


class Quote(models.Model):
    instrument = models.ForeignKey(FinancialInstrument, on_delete=models.CASCADE)
    date = models.DateField()
    open_price = models.DecimalField(max_digits=10, decimal_places=2)
    close_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.instrument.symbol} on {self.date}"
