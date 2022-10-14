from django.db import models
import uuid
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.

class Libros(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid1, help_text="ID único de este ejemplar")
    titulo=models.CharField(max_length=50)
    genero=models.CharField(max_length=30)
    autor=models.CharField(max_length=50)
    #descripcion=RichTextField(max_length=300)
    idioma=models.CharField(max_length=50)
    portada= models.ImageField(upload_to='portadas') 
    post_date= models.DateField(default=date.today)
    slug=models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.titulo+" "+self.autor

    def save (self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo + "-" + str(self.post_date))
        return super().save(*args, **kwargs)
'''
#FALTA RESOLVER! Me tira error en el admin.
class Portada (models.Model):
    libro=models.ForeignKey(Libros, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='portadas')
'''

class Autores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_n=models.DateField(null=True, blank=True)
    #fecha_d=models.DateField('Fallecido', null=True, blank=True)
    fecha_d=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Genero(models.Model):
    nombre_g=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_g

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_n=models.DateField(null=True, blank=True)
    alias=models.CharField(max_length=50)
    correo=models.EmailField()
    contrasenia=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido


class Avatar(models.Model):
    #Este user apunta a un usuario. Es decir tiene una key de un usuario en particular. Django va a relacionar un usuario con el avatar
    #Relacionar campos de la base de datos
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares')
