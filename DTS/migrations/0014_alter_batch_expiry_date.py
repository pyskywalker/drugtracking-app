# Generated by Django 3.2 on 2021-06-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0013_alter_medicine_on_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
