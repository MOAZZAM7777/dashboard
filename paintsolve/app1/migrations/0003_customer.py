# Generated by Django 4.2.7 on 2023-12-26 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_rename_employess_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('product', models.TextField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
