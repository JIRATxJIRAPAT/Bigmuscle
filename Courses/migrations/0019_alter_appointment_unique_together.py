# Generated by Django 3.2.8 on 2021-11-12 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_customer_track_customer'),
        ('Courses', '0018_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('date', 'timeslot', 'customer')},
        ),
    ]
