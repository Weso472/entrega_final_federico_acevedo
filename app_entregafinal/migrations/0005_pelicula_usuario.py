# Generated by Django 4.1 on 2022-10-03 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_entregafinal', '0004_pelicula_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='usuario',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
