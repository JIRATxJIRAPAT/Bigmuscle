# Generated by Django 3.2.8 on 2021-11-11 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_customer_track_customer'),
        ('Trainer', '0005_delete_book'),
        ('Courses', '0011_alter_course_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='YYYY-MM-DD')),
                ('timeslot', models.IntegerField(choices=[(0, '09:00 – 09:30'), (1, '10:00 – 10:30'), (2, '11:00 – 11:30'), (3, '12:00 – 12:30'), (4, '13:00 – 13:30'), (5, '14:00 – 14:30'), (6, '15:00 – 15:30'), (7, '16:00 – 16:30'), (8, '17:00 – 17:30')])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.customer')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Trainer.trainer')),
            ],
            options={
                'unique_together': {('trainer', 'date', 'timeslot')},
            },
        ),
    ]
