# Generated by Django 3.2 on 2021-06-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0009_rename_quantity_of_measure_transaction_quantity_measure'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_private',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
