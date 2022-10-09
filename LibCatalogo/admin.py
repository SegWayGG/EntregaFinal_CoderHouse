from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Libros)
admin.site.register(Autores)
admin.site.register(Genero)
admin.site.register(Usuarios)
#admin.site.register(Portada)