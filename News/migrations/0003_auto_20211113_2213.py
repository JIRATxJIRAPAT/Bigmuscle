# Generated by Django 3.2.8 on 2021-11-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pic1',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic2',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic3',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic4',
            field=models.ImageField(blank=True, default='default-image.png', null=True, upload_to=''),
        ),
    ]
