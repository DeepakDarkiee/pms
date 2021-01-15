# Generated by Django 3.1.2 on 2021-01-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
            ],
            options={
                'db_table': 'contact_details',
            },
        ),
    ]