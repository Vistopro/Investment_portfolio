from django.db import models


class FinancialInstrument(models.Model):
    INSTRUMENT_TYPE_CHOICES = [
        ('stock', 'Stock'),
        ('etf', 'ETF'),
        ('fund', 'Fund'),
    ]
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    instrument_type = models.CharField(max_length=10, choices=INSTRUMENT_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
