from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class pelicula(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    genero = models.CharField(max_length=30, null = True)
    estreno = models.DateField()
    director = models.CharField(max_length=30, null = True)
    portada = models.ImageField(upload_to='portadas', null = True, blank = True)
    descripcion = models.CharField(max_length=300, null = True)
    usuarioid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.estreno}, {self.director}, {self.portada}, {self.usuarioid}'


class album_musica(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    genero = models.CharField(max_length=30, null = True)
    artista = models.CharField(max_length=30, null = True)
    lanzamiento = models.DateField()
    discografica = models.CharField(max_length=30, null = True)
    descripcion = models.CharField(max_length=300, null = True)
    portada = models.ImageField(upload_to='portadas', null = True, blank = True)
    usuarioid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.artista}, {self.lanzamiento}, {self.discografica}, {self.portada}, {self.usuarioid}'


class videojuego(models.Model):
    nombre = models.CharField(max_length=30, null = True)
    genero = models.CharField(max_length=30, null = True)
    lanzamiento = models.DateField()
    compañia = models.CharField(max_length=30, null = True)
    portada = models.ImageField(upload_to='portadas', null = True, blank = True)
    descripcion = models.CharField(max_length=300, null = True)
    usuarioid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.lanzamiento}, {self.compañia}, {self.portada}, {self.usuarioid}'

