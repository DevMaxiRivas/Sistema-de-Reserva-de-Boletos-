# Generated by Django 5.0.6 on 2024-07-20 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_category_alter_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Categories',
        ),
    ]
