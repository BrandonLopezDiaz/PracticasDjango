# Generated by Django 5.1.1 on 2024-09-19 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='archivo',
        ),
    ]
