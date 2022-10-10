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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    ''' 
    No le permito cambiar usuario porque sino me pide que si o si lo cambie cuando quiero guardar.
    username = forms.CharField(label='Nombre de usuario')
    '''
    email = forms.EmailField(label='Direccion de correo')
    password1= forms.CharField(label='Ingrese su contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(label='Nombre real')
    last_name=forms.CharField(label='Apellido real')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields} 
