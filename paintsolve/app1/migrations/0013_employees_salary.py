# Generated by Django 4.2.7 on 2023-12-30 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='salary',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
