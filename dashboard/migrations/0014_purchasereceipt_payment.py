# Generated by Django 5.0.6 on 2024-07-26 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_remove_payments_sale_ticketsales_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchasereceipt',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.payments', verbose_name='payment'),
        ),
    ]
