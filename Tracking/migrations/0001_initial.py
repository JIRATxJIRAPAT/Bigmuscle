# Generated by Django 3.2.8 on 2021-11-05 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=100)),
                ('parts', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveIntegerField()),
                ('sets', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Tracking.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all_program_status', models.BooleanField(default=False)),
                ('day', models.PositiveIntegerField(default=0)),
                ('day_pragram', models.ManyToManyField(blank=True, related_name='daily', to='Tracking.Program')),
            ],
        ),
    ]
