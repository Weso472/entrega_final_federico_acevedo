from django.db import models

# Create your models here.
class pelicula(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    genero = models.CharField(max_length=30, null = True)
    estreno = models.DateField()
    director = models.CharField(max_length=30, null = True)

    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.estreno}, {self.director}'


class album_musica(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    genero = models.CharField(max_length=30, null = True)
    artista = models.CharField(max_length=30, null = True)
    lanzamiento = models.DateField()
    discografica = models.CharField(max_length=30, null = True)
    
    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.artista}, {self.lanzamiento}, {self.discografica}'


class videojuego(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    genero = models.CharField(max_length=30, null = True)
    lanzamiento = models.DateField()
    compañia = models.CharField(max_length=30, null = True)

    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.lanzamiento}, {self.compañia}'