# Generated by Django 3.2.8 on 2021-11-19 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0010_tracks_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='enable_check',
            field=models.BooleanField(default=True),
        ),
    ]
