# Generated by Django 3.1.2 on 2021-02-10 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_auto_20210210_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discuss',
            name='user',
        ),
        migrations.AddField(
            model_name='discuss',
            name='reporter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.lead'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discuss',
            name='msg',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='lead',
            name='message',
            field=models.CharField(max_length=1000),
        ),
    ]