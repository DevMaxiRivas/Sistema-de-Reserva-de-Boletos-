# Generated by Django 5.0.6 on 2024-08-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_payments_status_alter_payments_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seatcategory',
            name='type',
            field=models.CharField(blank=True, choices=[('standar', 'Standar'), ('vip', 'VIP'), ('ejecutive', 'Ejecutive')], default='cash', help_text='Seat Type', max_length=50, verbose_name='type'),
        ),
    ]
