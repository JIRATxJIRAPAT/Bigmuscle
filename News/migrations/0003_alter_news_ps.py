# Generated by Django 3.2.8 on 2021-10-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_auto_20211030_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='ps',
            field=models.TextField(blank=True, null=True),
        ),
    ]
