from django.contrib import admin
from django.urls import path
from app_entregafinal import views


urlpatterns = [
    path('inicio/', views.inicio, name = "inicio"),
    path('about/', views.about, name= "about"),

    path('mis-publicaciones/', views.mis_publicaciones, name= "mis-publicaciones"),
    path('eliminar-publicación/', views.eliminar_publicacion, name= "eliminar-publicacion"),
    path('editar-publicación/', views.editar_publicacion, name= "editar-publicacion"),
    
    path('nueva-pelicula/', views.crear_pelicula, name = "nueva-pelicula"),

    path('peliculas/', views.peliculas, name = "peliculas"),
    path('crear-pelicula/', views.crear_pelicula, name="crear-pelicula"),
    
    
    path('musica/', views.discos, name = "musica"),
    path('crear-musica/', views.crear_pelicula, name="crear-musica"),


    path('videojuegos/', views.videojuegos, name = "videojuegos"),
    path('crear-videojuego/', views.crear_videojuego, name="crear-videojuego"),
]

