from django.contrib import admin
from django.urls import path
from app_entregafinal import views


urlpatterns = [
    path('', views.inicio, name = "inicio"), #esta era nuestra primer view
    path('peliculas/', views.peliculas, name = "peliculas"),
    path('musica/', views.album_musica, name = "musica"),
    path('videojuegos/', views.videojuego, name = "videojuegos"),
]

