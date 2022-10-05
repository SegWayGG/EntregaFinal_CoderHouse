#from socket import fromshare
from django import forms

from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

import uuid

class LibrosForm(forms.Form):
    titulo = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    autor = forms.CharField(max_length=50)
    sumario = forms.CharField(max_length=250)
    idioma = forms.CharField(max_length=50)

    #def __str__(self):
    #    return self.titulo+" "+self.genero

class AutoresForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_n = forms.DateField(label="FN (YYYY-MM-DD):")
    fecha_d = forms.DateField(label="FD (YYYY-MM-DD):", required=False)
    #fecha_d = forms.DateTimeField()
    #fecha_d = forms.DateField()

class GeneroForm(forms.Form):
    nombre_g = forms.CharField(max_length=50)

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_n = forms.DateField(label="FN (YYYY-MM-DD):")
    alias = forms.CharField(max_length=50)
    correo= forms.EmailField()
    contrasenia = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False, max_length=10)

class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields} 
