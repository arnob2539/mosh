# Generated by Django 4.1.5 on 2023-01-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
