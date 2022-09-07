
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse


from app_entregafinal.models import pelicula, videojuego, album_musica



# Create your views here.


def inicio(request):

      return render(request, "app_entregafinal/inicio.html")

def peliculas(request):
      peliculas = pelicula.objects.all()
      return render(request, "app_entregafinal/pelicula.html", {'peliculas': peliculas})

def album_musica(request):
      albums = album_musica.objects.all()
      return render(request, "app_entregafinal/album_musica.html")

def videojuego(request):
  
      return render(request, "app_entregafinal/videojuego.html")
