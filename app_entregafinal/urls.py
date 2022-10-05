from django.contrib import admin
from django.urls import path
from app_entregafinal import views


urlpatterns = [
    path('inicio/', views.inicio, name = "inicio"),
    path('about/', views.about, name= "about"),
    
    path('register/', views.register, name = 'register'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
    path('perfil/', views.ProfileUpdateView.as_view(), name='perfil'),

    path('mis-publicaciones/', views.mis_publicaciones, name= "mis-publicaciones"),
    
    #PELICULAS
    path('peliculas/', views.peliculas, name="peliculas"),
    path('nueva-pelicula/', views.PeliculaCreateView.as_view(), name="nueva-pelicula"),
    path('editar-pelicula/<int:pk>/', views.PeliculaUpdateView.as_view(), name="editar-pelicula"),
    path('eliminar-pelicula/<int:pk>/', views.PeliculaDeleteView.as_view(), name="eliminar-pelicula"),
    path('detalle-pelicula/<int:pk>/', views.PeliculaDetailView.as_view(), name="detalle-pelicula"),

    #VIDEOJUEGOS
    path('videojuegos/', views.videojuegos, name="videojuegos"),
    path('nuevo-videojuego/', views.VideojuegoCreateView.as_view(), name="nuevo-videojuego"),
    path('editar-videojuego/<int:pk>/', views.VideojuegoUpdateView.as_view(), name="editar-videojuego"),
    path('eliminar-videojuego/<int:pk>/', views.VideojuegoDeleteView.as_view(), name="eliminar-videojuego"), 
    path('detalle-videojuego/<int:pk>/', views.VideojuegoDetailView.as_view(), name="detalle-videojuego"),   

    #MUSICA
    path('Musica/', views.discos, name="musica"),
    path('nuevo-disco/', views.DiscoCreateView.as_view(), name="nuevo-disco"),
    path('editar-disco/<int:pk>/', views.DiscoUpdateView.as_view(), name="editar-disco"),
    path('eliminar-disco/<int:pk>/', views.DiscoDeleteView.as_view(), name="eliminar-disco"),  
    path('detalle-disco/<int:pk>/', views.DiscoDetailView.as_view(), name="detalle-disco"),     

    
]