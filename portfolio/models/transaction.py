from django.db import models
from django.contrib.auth.models import User
from portfolio.models.portfolio import Portfolio


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE,related_name="transactions")
    asset_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.asset_name} ({self.symbol}) on {self.date}"