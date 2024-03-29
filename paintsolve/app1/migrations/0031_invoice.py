# Generated by Django 4.2.7 on 2024-01-17 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0030_delete_transaction"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fk",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.customer"
                    ),
                ),
            ],
        ),
    ]
