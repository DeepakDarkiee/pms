# Generated by Django 3.1.6 on 2021-03-13 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20210313_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lic',
            name='relation_type',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Wife', 'Wife'), ('Children', 'Children')], max_length=100, null=True),
        ),
    ]
