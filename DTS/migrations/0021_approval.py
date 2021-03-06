# Generated by Django 3.2 on 2021-06-06 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0020_remove_userprofile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='DTS.userprofile')),
            ],
        ),
    ]
