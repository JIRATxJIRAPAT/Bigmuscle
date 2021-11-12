# Generated by Django 3.2.8 on 2021-11-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_customer_track_customer'),
        ('Courses', '0021_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='Users.customer'),
        ),
    ]
