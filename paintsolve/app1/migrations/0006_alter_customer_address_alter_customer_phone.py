# Generated by Django 4.2.7 on 2023-12-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_customer_amount_alter_customer_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]