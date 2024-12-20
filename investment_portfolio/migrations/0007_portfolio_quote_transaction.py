# Generated by Django 5.0.7 on 2024-07-16 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_portfolio', '0006_financialinstrument'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='investment_portfolio.user')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.BigIntegerField()),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment_portfolio.financialinstrument')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=4)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment_portfolio.financialinstrument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investment_portfolio.user')),
            ],
        ),
    ]
