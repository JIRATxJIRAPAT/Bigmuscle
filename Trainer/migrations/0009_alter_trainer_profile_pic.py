# Generated by Django 3.2.8 on 2021-11-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0008_alter_trainer_videocall_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='trainer_default_pic.jpg', null=True, upload_to=''),
        ),
    ]
