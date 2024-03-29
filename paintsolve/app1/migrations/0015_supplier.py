# Generated by Django 4.2.7 on 2024-01-01 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_remove_category_colorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suppliercode', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('Notes', models.TextField()),
            ],
        ),
    ]
