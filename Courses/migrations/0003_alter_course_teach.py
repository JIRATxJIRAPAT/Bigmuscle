# Generated by Django 3.2.8 on 2021-11-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0001_initial'),
        ('Courses', '0002_course_teach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teach',
            field=models.ManyToManyField(related_name='teacher', to='Trainer.Trainer'),
        ),
    ]
