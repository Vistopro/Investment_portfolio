# Generated by Django 5.0.7 on 2024-08-07 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment_portfolio', '0012_remove_user_has_module_perms_user_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='price_per_unit',
            new_name='price',
        ),
    ]
