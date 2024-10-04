# Generated by Django 4.2.15 on 2024-10-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='accesos',
        ),
        migrations.AddField(
            model_name='user',
            name='accesos',
            field=models.ManyToManyField(blank=True, related_name='accesos', to='acceso.acceso'),
        ),
    ]
