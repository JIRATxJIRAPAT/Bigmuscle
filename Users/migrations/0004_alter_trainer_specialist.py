# Generated by Django 3.2.8 on 2021-10-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20211017_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='specialist',
            field=models.CharField(max_length=100),
        ),
    ]
