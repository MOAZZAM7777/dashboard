# Generated by Django 4.2.7 on 2024-01-13 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_remove_transaction_amount_transaction_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
