# Generated by Django 4.2.7 on 2024-01-21 10:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0039_purchase_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="purchase",
            name="date",
        ),
    ]
