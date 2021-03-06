# Generated by Django 3.2 on 2021-05-31 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0002_rename_location_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='batch',
            old_name='TMDA_verified',
            new_name='TMDA_status',
        ),
        migrations.RenameField(
            model_name='medicine',
            old_name='status',
            new_name='stock_status',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='tmda_verified',
        ),
        migrations.AddField(
            model_name='batch',
            name='manufactured_by',
            field=models.CharField(default='Shelys', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DTS.medicinetype'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.ForeignKey(default='sales', on_delete=django.db.models.deletion.SET_DEFAULT, to='DTS.transactiontype'),
        ),
    ]
