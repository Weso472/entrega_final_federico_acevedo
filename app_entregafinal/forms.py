from django import forms


class formulario_pelicula(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    estreno = forms.DateField()
    director = forms.CharField(max_length=30)


class formulario_musica(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    artista = forms.CharField(max_length=30)
    lanzamiento = forms.DateField()
    discografica = forms.CharField(max_length=30)


class formulario_videojuego(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    lanzamiento = forms.DateField()
    compañia = forms.CharField(max_length=30)