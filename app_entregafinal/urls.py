from django.contrib import admin
from django.urls import path
from app_entregafinal import views


urlpatterns = [
    path('', views.inicio, name = "inicio"), #esta era nuestra primer view
    path('busqueda', views.buscar, name= "busqueda"),
    
    path('peliculas/', views.peliculas, name = "peliculas"),
    path('crear-pelicula/', views.crear_pelicula, name="crear-pelicula"),
    
    
    path('musica/', views.discos, name = "musica"),
    path('crear-musica/', views.crear_pelicula, name="crear-musica"),


    path('videojuegos/', views.videojuegos, name = "videojuegos"),
    path('crear-videojuego/', views.crear_videojuego, name="crear-videojuego"),
]

