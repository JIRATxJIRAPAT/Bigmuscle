# Generated by Django 3.2.8 on 2021-11-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_alter_course_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='pic',
            field=models.ImageField(blank=True, default='about.jpg', null=True, upload_to=''),
        ),
    ]