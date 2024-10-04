# Generated by Django 4.2.15 on 2024-10-04 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('video_url', models.CharField(max_length=255)),
                ('imagen_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubTemas',
            fields=[
                ('temas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='temario.temas')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Temas', to='temario.temas')),
            ],
            bases=('temario.temas',),
        ),
    ]
