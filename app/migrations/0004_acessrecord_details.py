# Generated by Django 5.0.3 on 2024-04-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_topic_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='acessrecord',
            name='details',
            field=models.CharField(default='write author details here!', max_length=100),
        ),
    ]
