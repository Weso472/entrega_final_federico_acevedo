from typing import Dict

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from app_entregafinal.models import pelicula, videojuego, album_musica
from app_entregafinal.forms import formulario_pelicula, formulario_musica, formulario_videojuego



def inicio(request):

    return render(request, "app_entregafinal/inicio.html")

def about(request):
    
    return render(request, "app_entregafinal/about.html")



def mis_publicaciones(request):
    peliculas = pelicula.objects.all()
    videojuegos = videojuego.objects.all()
    albums = album_musica.objects.all()
    
    return render(request, "app_entregafinal/mis_publicaciones.html", {'peliculas': peliculas,'videojuegos': videojuegos,'albums': albums})





def editar_publicacion(request):
    
    return render(request, "app_entregafinal/editar_publicacion.html")



class PeliculaListView(ListView):
    model = pelicula
    template_name = 'AppCoder/pelicula.html'


class PeliculaCreateView(CreateView):
    model = pelicula
    fields = ['nombre', 'genero', 'estreno', 'director']
    success_url = reverse_lazy('mis-publicaciones')


class PeliculaUpdateView(UpdateView):
    model = pelicula
    fields = ['nombre', 'genero', 'estreno', 'director']
    success_url = reverse_lazy('mis-publicaciones')


class PeliculaDeleteView(DeleteView):
    model = pelicula
    success_url = reverse_lazy('mis-publicaciones')




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

