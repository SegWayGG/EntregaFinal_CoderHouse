from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

#from django.urls import reverse_lazy

#from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

#from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    #return HttpResponse("Inicio")
    return render(request, "LibCatalogo/inicio.html")

def libros(request):
    return render(request, "LibCatalogo/libros.html")

def autores(request):
    return render(request, "LibCatalogo/autores.html")

def generos(request):
    return render(request, "LibCatalogo/generos.html")

def usuario(request):
    return render(request, "LibCatalogo/usuarios.html")

#Vistas para formularios

def libros_f(request):
    if request.method=="POST":
        form_l=LibrosForm(request.POST)
        #print(form_l)
        if form_l.is_valid():
            nuevo_libro_data=form_l.cleaned_data
            #print(nuevo_libro_data)
            titulo=nuevo_libro_data["titulo"]
            genero=nuevo_libro_data["genero"]
            autor=nuevo_libro_data["autor"]
            sumario=nuevo_libro_data["sumario"]
            idioma=nuevo_libro_data["idioma"]
            nuevo_libro=Libros(titulo=titulo, genero=genero, autor=autor, sumario=sumario, idioma=idioma)
            nuevo_libro.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Libro creado de forma exitosa!"})       
    else:
        l_formulario=LibrosForm()
        return render(request, "LibCatalogo/libros_f.html", {"l_formulario":l_formulario})

def autores_f(request):
    if request.method=="POST":
        form_a=AutoresForm(request.POST)
        if form_a.is_valid():
            nuevo_autor_data=form_a.cleaned_data
            nombre=nuevo_autor_data["nombre"]
            apellido=nuevo_autor_data["apellido"]
            fecha_n=nuevo_autor_data["fecha_n"]
            fecha_d=nuevo_autor_data["fecha_d"]
            nuevo_autor=Autores(nombre=nombre, apellido=apellido, fecha_n=fecha_n, fecha_d=fecha_d)
            nuevo_autor.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Autor creado de forma exitosa!"})       
    else:
        a_formulario=AutoresForm()
        return render(request, "LibCatalogo/autores_f.html", {"a_formulario":a_formulario})

def generos_f(request):
    if request.method=="POST":
        form_g=GeneroForm(request.POST)
        if form_g.is_valid():
            nuevo_genero_data=form_g.cleaned_data
            nombre_g=nuevo_genero_data["nombre_g"]
            nuevo_genero=Genero(nombre_g=nombre_g)
            nuevo_genero.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Genero creado de forma exitosa!"})       
    else:
        g_formulario=GeneroForm()
        return render(request, "LibCatalogo/generos_f.html", {"g_formulario":g_formulario})

#Vista para carga de usuarios
def usuarios_f(request):
    if request.method=="POST":
        form_u=UsuariosForm(request.POST)
        if form_u.is_valid():
            nuevo_usuario_data=form_u.cleaned_data
            nombre_u=nuevo_usuario_data["nombre"]
            apellido_u=nuevo_usuario_data["apellido"]
            fecha_n_u=nuevo_usuario_data["fecha_n"]
            alias_u=nuevo_usuario_data["alias"]
            correo_u=nuevo_usuario_data["correo"]
            clave_u=nuevo_usuario_data["contrasenia"]
            nuevo_usuario=Usuarios(nombre=nombre_u, apellido=apellido_u, fecha_n=fecha_n_u, alias=alias_u, correo=correo_u, contrasenia=clave_u)
            nuevo_usuario.save()
            return render(request, "LibCatalogo/cargaexito.html", {"mensaje":"Usuario creado de forma exitosa!"})       
    else:
        u_formulario=UsuariosForm()
        return render(request, "LibCatalogo/usuarios_f.html", {"u_formulario":u_formulario})

#-----VISTA PARA FORMULARIOS DE BUSQUEDA-----

#Vistas de formularios de busqueda de libros
def f_busqueda_lib_by_title(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_title.html")

def f_busqueda_lib_by_gen(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_genero.html")

def f_busqueda_lib_by_autor(request):
    return render(request, "LibCatalogo/busquedas/busq_lib_by_autor.html")

#Esta es la que me muestra los resultados de titulos buscando por titulo
def f_resultado_lib_by_title(request):
    lib_by_title_v=request.POST["lib_by_title"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    titulo_libro_v=Libros.objects.filter(titulo__icontains=lib_by_title_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_title.html", {"titulo_libro_k":titulo_libro_v})

#Esta es la que me muestra los resultados de titulos buscando por genero
def f_resultado_lib_by_gen(request):
    lib_by_gen_v=request.POST["lib_by_genero"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    gen_libro_v=Libros.objects.filter(genero__icontains=lib_by_gen_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_gen.html", {"gen_libro_k":gen_libro_v})

#Esta es la que me muestra los resultados de titulos buscando por autor
def f_resultado_lib_by_autor(request):
    lib_by_autor_v=request.POST["lib_by_autor"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    autor_libro_v=Libros.objects.filter(autor__icontains=lib_by_autor_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_lib_by_autor.html", {"autor_libro_k":autor_libro_v})

#Vista para ver biblioteca completa
def read_biblioteca(request):
    libros=Libros.objects.all()
    return render (request, "LibCatalogo/full_biblio.html", {"libros":libros})

#--------------------------------------------------------------------
#Vistas de formularios de busqueda de autores
def f_busqueda_autor_by_nombre(request):
    return render(request, "LibCatalogo/busquedas/busq_autor_by_name.html")

def f_busqueda_autor_by_apellido(request):
    return render(request, "LibCatalogo/busquedas/busq_autor_by_apellido.html")

def f_busqueda_autor_by_fecha_n(request):
    return render(request, "LibCatalogo/busquedas/busq_autor_by_fechan.html")

#Vistas de resultados de busquedas de autores
def f_resultado_autor_by_nombre(request):
    autor_by_name_v=request.POST["autor_by_name"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    autor_name_v=Autores.objects.filter(nombre__icontains=autor_by_name_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_autor_by_name.html", {"autor_name_k":autor_name_v})

def f_resultado_autor_by_apellido(request):
    autor_by_apellido_v=request.POST["autor_by_apellido"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    autor_apellido_v=Autores.objects.filter(apellido__icontains=autor_by_apellido_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_autor_by_apellido.html", {"autor_apellido_k":autor_apellido_v})

def f_resultado_autor_by_fecha_n(request):
    autor_by_fn_v=request.POST["autor_by_fn"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    autor_fn_v=Autores.objects.filter(fecha_n__icontains=autor_by_fn_v)
    return render(request, "LibCatalogo/busquedas/resultado_busq_autor_by_fechan.html", {"autor_fn_k":autor_fn_v})

#--------------------------------------------------------------------
#Vistas para busqueda de generos
def f_busqueda_generos(request):
    return render(request, "LibCatalogo/busquedas/busq_generos.html")

def f_resultado_generos(request):
    #b_generos_v=request.POST['']
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    generos_v=Genero.objects.all()
    return render(request, "LibCatalogo/busquedas/resultado_busq_generos.html", {"generos_k":generos_v})

#--------------------------------------------------------------------

#Vistas para busqueda de usuarios
def f_busqueda_usuario_byname(request):
    return render(request, "LibCatalogo/busquedas/busq_usuario_byname.html")

def f_busqueda_usuario_bysurename(request):
    return render(request, "LibCatalogo/busquedas/busq_usuario_bysurename.html")

def f_busqueda_usuario_byalias(request):
    return render(request, "LibCatalogo/busquedas/busq_usuario_byalias.html")

def f_resultado_usuario_byname(request):
    usuario_byname_v=request.POST["usuario_byname"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    usuario_v=Usuarios.objects.filter(nombre__icontains=usuario_byname_v)
    return render(request, "LibCatalogo/busquedas/resultado_usuario_byname.html", {"usuario_k":usuario_v})

def f_resultado_usuario_bysurename(request):
    usuario_bysurename_v=request.POST["usuario_bysurename"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    usuario_a_v=Usuarios.objects.filter(apellido__icontains=usuario_bysurename_v)
    return render(request, "LibCatalogo/busquedas/resultado_usuario_bysurename.html", {"usuario_a_k":usuario_a_v})

def f_resultado_usuario_byalias(request):
    usuario_byalias_v=request.POST["usuario_byalias"]
    #Traer de la base todas las ocurrencias que coincidan con la busqueda 
    #__icontains es para busquedas aproximadas
    usuario_alias_v=Usuarios.objects.filter(alias__icontains=usuario_byalias_v)
    return render(request, "LibCatalogo/busquedas/resultado_usuario_byalias.html", {"usuario_alias_k":usuario_alias_v})

#--------------------------------------------------------------------
#Vistas para editar usuario

@login_required
def editarUser(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Perfil editado correctamente"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request,"LibCatalogo/edit_user.html", {"formulario":form, "usuario":usuario})

    



