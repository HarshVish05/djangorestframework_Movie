# Generated by Django 5.0.7 on 2024-08-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='genre',
            field=models.CharField(default='action', max_length=200),
        ),
    ]
