# Generated by Django 3.1.6 on 2021-03-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210317_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lic',
            name='family_name',
            field=models.CharField(default='None', max_length=100),
        ),
    ]