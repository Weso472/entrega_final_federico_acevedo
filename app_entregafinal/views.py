from typing import Dict

from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from app_entregafinal.models import pelicula, videojuego, album_musica
from app_entregafinal.forms import formulario_pelicula, formulario_musica, formulario_videojuego, UserRegisterForm, UserUpdateForm#, AvatarFormulario



def inicio(request):

    return render(request, "app_entregafinal/inicio.html")

def about(request):
    
    return render(request, "app_entregafinal/about.html")


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "app_entregafinal/inicio.html", {"mensaje": "Usuario Creado Exitosamente"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "app_entregafinal/registro.html", context=context)

def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "app_entregafinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"app_entregafinal/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"app_entregafinal/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"app_entregafinal/login.html", {'form':form} )

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'app_entregafinal/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user

class CustomLogoutView(LogoutView):
    template_name = 'app_entregafinal/logout.html'
    next_page = reverse_lazy('inicio')

@login_required
def mis_publicaciones(request):
    peliculas = pelicula.objects.all()
    videojuegos = videojuego.objects.all()
    albums = album_musica.objects.all()
    
    return render(request, "app_entregafinal/mis_publicaciones.html", {'peliculas': peliculas,'videojuegos': videojuegos,'albums': albums})

def peliculas(request):
    peliculas = pelicula.objects.all()

    return render(request, "app_entregafinal/pelicula.html", {'peliculas': peliculas})

class PeliculaListView(LoginRequiredMixin, ListView):
    model = pelicula
    template_name = 'app_entregafinal/pelicula.html'


class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = pelicula
    fields = ['nombre', 'genero', 'estreno', 'director', 'portada', 'usuario']
    success_url = reverse_lazy('mis-publicaciones')


class PeliculaUpdateView(LoginRequiredMixin, UpdateView):
    model = pelicula
    fields = ['nombre', 'genero', 'estreno', 'director']
    success_url = reverse_lazy('mis-publicaciones')


class PeliculaDeleteView(LoginRequiredMixin, DeleteView):
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

