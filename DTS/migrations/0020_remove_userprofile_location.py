# Generated by Django 3.2 on 2021-06-04 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DTS', '0019_alter_usertype_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='location',
        ),
    ]
