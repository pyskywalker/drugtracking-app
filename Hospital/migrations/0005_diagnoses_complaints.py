# Generated by Django 3.2 on 2021-05-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0004_alter_patient_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnoses',
            name='complaints',
            field=models.TextField(default='Chest Pains'),
            preserve_default=False,
        ),
    ]