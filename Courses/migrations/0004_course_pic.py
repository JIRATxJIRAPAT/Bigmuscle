# Generated by Django 3.2.7 on 2021-11-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_alter_course_teach'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
