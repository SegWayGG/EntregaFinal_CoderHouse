"""Libreria_v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from LibCatalogo.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('libros/', libros, name='libros'),
    path('autores/', autores, name='autores'),
    path('generos/', generos, name='generos'),
    path('usuarios/', usuario, name='usuarios'),
    path('', inicio, name='inicio'),
    #path('inicio/', inicio, name='inicio'),
    path('librosf/', libros_f, name='librosf'),
    path('autoresf/', autores_f, name='autoresf'),
    path('generosf/', generos_f, name='generosf'),
    #Urls de busquedas de libros
    path('buscar_l_by_t/', f_busqueda_lib_by_title, name='buscar_l_by_t'),
    path('buscar_l_by_g/', f_busqueda_lib_by_gen, name='buscar_l_by_g'),
    path('buscar_l_by_a/', f_busqueda_lib_by_autor, name='buscar_l_by_a'),
    path('result_l_by_t/', f_resultado_lib_by_title, name='result_l_by_t'),
    path('result_l_by_g/', f_resultado_lib_by_gen, name='result_l_by_g'),
    path('result_l_by_a/', f_resultado_lib_by_autor, name='result_l_by_a'),
    path('full_biblio/', read_biblioteca, name='full_biblio'),

    #Urls de busqueda de autores
    path('buscar_a_by_n/', f_busqueda_autor_by_nombre, name='buscar_a_by_n'),
    path('buscar_a_by_a/', f_busqueda_autor_by_apellido, name='buscar_a_by_a'),
    path('buscar_a_by_fn/', f_busqueda_autor_by_fecha_n, name='buscar_a_by_fn'),
    path('result_a_by_n/', f_resultado_autor_by_nombre, name='result_a_by_n'),
    path('result_a_by_a/', f_resultado_autor_by_apellido, name='result_a_by_a'),
    path('result_a_by_fn/', f_resultado_autor_by_fecha_n, name='result_a_by_fn'),

    #Urls de busqueda de generos
    path('buscar_g/', f_busqueda_generos, name='buscar_g'),
    path('result_g/', f_resultado_generos, name='result_g'),



    path('usuarios_f/', usuarios_f, name='usuariosf'),
    #Urls de busqueda de usuarios
    path('buscar_u_by_n/', f_busqueda_usuario_byname, name='buscar_u_by_n'),
    path('buscar_u_by_s/', f_busqueda_usuario_bysurename, name='buscar_u_by_s'),
    path('buscar_u_by_a/', f_busqueda_usuario_byalias, name='buscar_u_by_a'),

    path('result_u_by_n/', f_resultado_usuario_byname, name='result_u_by_n'),
    path('result_u_by_s/', f_resultado_usuario_bysurename, name='result_u_by_s'),
    path('result_u_by_a/', f_resultado_usuario_byalias, name='result_u_by_a'),

    #Login Register Loguot
    path('login/', loguin_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='C:/Users/SegWay/Desktop/CoderHouse/PreentregaFinal/Entrega1_Albano/LibCatalogo/templates/LibCatalogo/register_login_logout/logout.html'), name='logout'),
]