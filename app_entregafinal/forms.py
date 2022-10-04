from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formulario_pelicula(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    estreno = forms.DateField()
    director = forms.CharField(max_length=30)
    portada = forms.ImageField()
    usuario = forms.CharField(max_length=30)

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


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput,)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput,)

    class Meta:
        model = User
        help_texts = {'username': None}
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email']