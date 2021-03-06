# Generated by Django 3.2.8 on 2021-11-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('context', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('pic1', models.ImageField(blank=True, default='default-image.png', null=True, upload_to='')),
            ],
        ),
    ]
