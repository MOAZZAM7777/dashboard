# Generated by Django 4.2.7 on 2024-01-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0033_customer_invoicedate_customer_invoicenumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="invoiceDate",
            field=models.CharField(max_length=10),
        ),
    ]
