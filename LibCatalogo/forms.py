#from socket import fromshare
from django import forms
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
