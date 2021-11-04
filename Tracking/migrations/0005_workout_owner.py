# Generated by Django 3.2.8 on 2021-11-04 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20211031_1818'),
        ('Tracking', '0004_auto_20211104_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.customer'),
        ),
    ]
