# Generated by Django 3.1.6 on 2021-03-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20210309_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='lic',
            name='family_dob',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lic',
            name='family_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lic',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lic',
            name='relation_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mutual_fund',
            name='family_dob',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mutual_fund',
            name='family_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mutual_fund',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mutual_fund',
            name='relation_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]