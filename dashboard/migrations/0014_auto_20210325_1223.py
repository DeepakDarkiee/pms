# Generated by Django 3.1.6 on 2021-03-25 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20210325_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mutual_fund',
            name='family_dob',
        ),
        migrations.RemoveField(
            model_name='mutual_fund',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='mutual_fund',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='mutual_fund',
            name='relation_type',
        ),
    ]
