# Generated by Django 2.2.10 on 2020-03-20 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug'),
        ),
    ]