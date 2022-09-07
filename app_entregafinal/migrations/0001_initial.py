# Generated by Django 4.1 on 2022-09-06 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='album_musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('estreno', models.DateField()),
                ('discografica', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('estreno', models.DateField()),
                ('director', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='videojuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('estreno', models.DateField()),
                ('compania', models.CharField(max_length=30)),
            ],
        ),
    ]
