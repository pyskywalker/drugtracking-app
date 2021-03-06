# Generated by Django 3.2 on 2021-06-01 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0004_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DTS.transactiontype'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
