# Generated by Django 3.2 on 2021-06-04 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0017_batch_concentration'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manufacturer', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='batch',
            name='manufactured_by',
        ),
        migrations.AddField(
            model_name='batch',
            name='medicine_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='DTS.medicinedetails'),
            preserve_default=False,
        ),
    ]
