# Generated by Django 4.2.7 on 2024-01-22 07:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0043_remove_purchase_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchase",
            name="date_purchased",
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]