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



def peliculas(request):
    peliculas = pelicula.objects.all()
    contexto = {'peliculas': peliculas}
#    borrado = request.GET.get('borrado', None)     #Falta agregar que diga "borrado con exito"
#    contexto['borrado'] = borrado
    return render(request, "app_entregafinal/pelicula.html", contexto)

def crear_pelicula(request):
    if request.method == 'POST':
        formulario = formulario_pelicula(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            Pelicula = pelicula(nombre=data['nombre'], genero=data['genero'], estreno=data['estreno'], director=data['director'])
            Pelicula.save()
            url_final = f"{reverse('mis-publicaciones')}?creadopelicula"
            return redirect(url_final)
    else:
        formulario = formulario_pelicula()  # Formulario vacio para construir el html
    return render(request, "app_entregafinal/formulario_pelicula.html", {"formulario": formulario})

def editar_pelicula(request, id):
    pelicula_id = pelicula.objects.get(id = id)
    
    if request.method == 'POST':
        formulario = formulario_pelicula(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            pelicula_id.nombre = data['nombre']
            pelicula_id.genero = data['genero']
            pelicula_id.estreno = data['estreno']
            pelicula_id.director = data['director']

            pelicula_id.save()

            url_final = f"{reverse('mis-publicaciones')}?editadopelicula"
            return redirect(url_final)
    else:  # GET
        inicial = {
            'nombre': pelicula_id.nombre,
            'genero': pelicula_id.genero,
            'estreno': pelicula_id.estreno,
            'director': pelicula_id.director,
        }
        formulario = formulario_pelicula(initial=inicial)
    return render(request, "app_entregafinal/formulario_pelicula.html", {"formulario": formulario})

def eliminar_pelicula(request, id):
    pelicula_id = pelicula.objects.get(id = id)
    borrado_id = pelicula_id.id
    pelicula_id.delete()
    url_final = f"{reverse('mis-publicaciones')}?borradopelicula={borrado_id}"
    return redirect(url_final)



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

