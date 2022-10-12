from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

#from django.urls import reverse_lazy

#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, "LibCatalogo/inicio.html", {"avatar":obtenerAvatar(request)})

def libros(request):
    return render(request, "LibCatalogo/libros.html", {"avatar":obtenerAvatar(request)})

#Vistas para formularios

def libros_f(request):
    if request.method=="POST":
        form_l=LibrosForm(request.POST)
        if form_l.is_valid():
            nuevo_libro_data=form_l.cleaned_data
            titulo=nuevo_libro_data["titulo"]
            genero=nuevo_libro_data["genero"]
            autor=nuevo_libro_data["autor"]
            descripcion=nuevo_libro_data["descripcion"]
            idioma=nuevo_libro_data["idioma"]
            portada=nuevo_libro_data["portada"]
            nuevo_libro=Libros(titulo=titulo, genero=genero, autor=autor, descripcion=descripcion, idioma=idioma, portada=portada)
            nuevo_libro.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Libro creado de forma exitosa!", "avatar":obtenerAvatar(request)})       
    else:
        l_formulario=LibrosForm()
        return render(request, "LibCatalogo/libros_f.html", {"l_formulario":l_formulario, "avatar":obtenerAvatar(request)})

### Biblioteca completa ###
def read_biblioteca(request):
    libros=Libros.objects.all()
    return render (request, "LibCatalogo/full_biblio.html", {"libros":libros, "avatar":obtenerAvatar(request)})

#-----VISTA PARA FORMULARIOS DE BUSQUEDA-----#

### Busqueda de libros ###
def f_busqueda_lib_by_title(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_title.html", {"avatar":obtenerAvatar(request)})

#----------------------------------------------------------------
'''
def filter_set(request):
    ingreso=request.POST["lib_by_title"]
    titulo_libro=Libros.objects.filter(titulo__icontains=ingreso)
    genero_libro=Libros.objects.filter(genero__icontains=ingreso)
    autor_libro=Libros.objects.filter(autor__icontains=ingreso)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_title.html", {"tituloLibro": titulo_libro, "generoLibro": genero_libro, "autorLibro": autor_libro})
'''


### Resultado de titulos ###

def f_resultado_lib_by_title(request):
    lib_by_title_v=request.POST["lib_by_title"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    titulo_libro_v=Libros.objects.filter(titulo__icontains=lib_by_title_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_title.html", {"titulo_libro_k":titulo_libro_v, "avatar":obtenerAvatar(request)})

### Editar usuario ###

@login_required
def editUser(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            ''' 
            No le permito cambiar usuario porque sino me pide que si o si lo cambie cuando quiero guardar.
            usuario.username=info["username"]
            '''
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "LibCatalogo/inicio.html", {"mensaje":"Perfil editado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request,"LibCatalogo/edit_user.html", {"formulario":form, "usuario":usuario, "mensaje":"FORMULARIO INVÁLIDO", "avatar":obtenerAvatar(request)})
    else:
        form= UserEditForm(instance=usuario)
    return render(request,"LibCatalogo/edit_user.html", {"formulario":form, "usuario":usuario, "avatar":obtenerAvatar(request)})

### Loguin Register Logout ###

def loguin_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'LibCatalogo/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "LibCatalogo/register_login_logout/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "LibCatalogo/register_login_logout/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})

    else:
        form=AuthenticationForm()
        return render(request, "LibCatalogo/register_login_logout/login.html", {"formulario":form})

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "LibCatalogo/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "LibCatalogo/register_login_logout/register.html", {"formulario":form, "mensaje":"FORMULARIO INVALIDO"})
    else:
        form=UserRegisterForm()
        return render(request, "LibCatalogo/register_login_logout/register.html", {"formulario":form})

### Avatar ###

@login_required
def agregarAvatar(request):
    if request.method=='POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'LibCatalogo/inicio.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "avatar": avatar.imagen.url})
        else:
            return render(request, 'LibCatalogo/addAvatar.html', {'formulario':formulario, 'mensaje':'FORMULARIO INVALIDO'})
    else:
        formulario=AvatarForm()
        return render(request, "LibCatalogo/addAvatar.html", {"formulario":formulario, "usuario":request.user, "avatar": obtenerAvatar(request)})

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=None
    return imagen