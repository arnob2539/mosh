# Generated by Django 4.1.5 on 2023-01-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_name', 'first_name'], name='store_custo_last_na_a2c5ee_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customes',
        ),
    ]