# Generated by Django 3.2.8 on 2021-11-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0011_alter_tracks_maxday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracks',
            name='maxday',
            field=models.PositiveIntegerField(),
        ),
    ]
