# Generated by Django 4.2.7 on 2023-12-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_customer_address_alter_customer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
