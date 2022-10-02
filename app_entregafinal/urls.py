from django.contrib import admin
from django.urls import path
from app_entregafinal import views


urlpatterns = [
    path('inicio/', views.inicio, name = "inicio"),
    path('about/', views.about, name= "about"),

    path('mis-publicaciones/', views.mis_publicaciones, name= "mis-publicaciones"),
    

    path('pelicula/', views.PeliculaListView.as_view(), name="peliculas"),
    path('nueva-pelicula/', views.PeliculaCreateView.as_view(), name="nueva-pelicula"),
    path('editar-pelicula/<int:pk>/', views.PeliculaUpdateView.as_view(), name="editar-pelicula"),
    path('eliminar-pelicula/<int:pk>/', views.PeliculaDeleteView.as_view(), name="eliminar-pelicula"),
    

    
    path('musica/', views.discos, name = "musica"),
    path('crear-musica/', views.crear_disco, name="crear-musica"),


    path('videojuegos/', views.videojuegos, name = "videojuegos"),
    path('crear-videojuego/', views.crear_videojuego, name="crear-videojuego"),
]

