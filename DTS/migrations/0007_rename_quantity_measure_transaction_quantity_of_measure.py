# Generated by Django 3.2 on 2021-06-01 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0006_auto_20210601_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='quantity_measure',
            new_name='quantity_of_measure',
        ),
    ]
