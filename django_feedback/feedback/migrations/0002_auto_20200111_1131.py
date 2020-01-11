# Generated by Django 3.0.2 on 2020-01-11 06:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='time_created',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]