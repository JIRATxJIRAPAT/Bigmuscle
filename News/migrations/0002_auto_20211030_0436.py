# Generated by Django 3.2.8 on 2021-10-29 21:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='ps',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
