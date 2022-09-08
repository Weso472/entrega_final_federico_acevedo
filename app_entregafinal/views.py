from typing import Dict

from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from app_entregafinal.models import pelicula, videojuego, album_musica
from app_entregafinal.forms import formulario_pelicula, formulario_musica, formulario_videojuego



# Create your views here.


def inicio(request):

      return render(request, "app_entregafinal/inicio.html")



def peliculas(request):
      peliculas = pelicula.objects.all()
      return render(request, "app_entregafinal/pelicula.html", {'peliculas': peliculas})

def crear_pelicula(request):
    if request.method == 'POST':
        formulario = formulario_pelicula(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Pelicula = pelicula(nombre=data['nombre'], genero=data['genero'], estreno=data['estreno'])
            Pelicula.save()
            return render(request, "app_entregafinal/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = formulario_pelicula()  # Formulario vacio para construir el html
    return render(request, "app_entregafinal/formulario_pelicula.html", {"formulario": formulario})



def discos(request):
      discos = album_musica.objects.all()
      return render(request, "app_entregafinal/album_musica.html", {'discos': discos})

def crear_disco(request):
    if request.method == 'POST':
        formulario = formulario_musica(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Disco = album_musica(nombre=data['nombre'], genero=data['genero'], artista=data['artista'], lanzamiento=data['lanzamiento'], discografica=data['discografica'])
            Disco.save()
            return render(request, "app_entregafinal/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = formulario_pelicula()  # Formulario vacio para construir el html
    return render(request, "app_entregafinal/formulario_pelicula.html", {"formulario": formulario})



def videojuegos(request):
      videojuegos = videojuego.objects.all()
      return render(request, "app_entregafinal/videojuego.html", {'videojuegos': videojuegos})

def crear_videojuego(request):
    if request.method == 'POST':
        formulario = formulario_videojuego(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            Videojuego = videojuego(nombre=data['nombre'], genero=data['genero'], lanzamiento=data['lanzamiento'], compañia=data['compañia'])
            Videojuego.save()
            return render(request, "app_entregafinal/inicio.html", {"exitoso": True})
    else:  # GET
        formulario = formulario_videojuego()  # Formulario vacio para construir el html
    return render(request, "app_entregafinal/formulario_videojuego.html", {"formulario": formulario})

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        discos = album_musica.objects.filter(nombre__icontains=nombre)
        peliculas = pelicula.objects.filter(nombre__icontains=nombre)
        videojuegos = videojuego.objects.filter(nombre__icontains=nombre)

        return render(request, "app_entregafinal/busqueda.html", {'discos': discos}, {'peliculas': peliculas}, {'videojuegos': videojuegos})
    else:
        return render(request, "app_entregafinal/busqueda.html", {'discos': []}, {'peliculas': []}, {'videojuegos': []})

