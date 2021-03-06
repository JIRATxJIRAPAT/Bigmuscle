# Generated by Django 3.2.8 on 2021-11-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0005_delete_book'),
        ('Users', '0003_alter_customer_track_customer'),
        ('Courses', '0013_auto_20211112_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '04:00 – 06:00'), (1, '06:00 – 08:00'), (2, '11:00 – 11:30'), (3, '12:00 – 12:30'), (4, '13:00 – 13:30'), (5, '14:00 – 14:30'), (6, '15:00 – 15:30'), (7, '16:00 – 16:30'), (8, '17:00 – 17:30')]),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('trainer', 'date', 'timeslot', 'customer')},
        ),
    ]
