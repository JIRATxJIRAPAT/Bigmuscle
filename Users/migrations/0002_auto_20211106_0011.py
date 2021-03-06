# Generated by Django 3.2.8 on 2021-11-05 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0003_alter_course_teach'),
        ('Tracking', '0003_alter_tracks_track_trainer'),
        ('Trainer', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_trainer', to='Trainer.trainer'),
        ),
        migrations.DeleteModel(
            name='Trainer',
        ),
    ]
