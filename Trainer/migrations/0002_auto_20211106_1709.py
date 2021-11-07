# Generated by Django 3.2.8 on 2021-11-06 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trainer',
            name='bio',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='trainer',
            name='tel',
            field=models.CharField(max_length=10, null=True),
        ),
    ]