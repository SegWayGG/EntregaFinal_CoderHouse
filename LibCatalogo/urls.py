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
from django.conf.urls import include
from LibCatalogo.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('libros/', libros, name='libros'),
    path('', inicio, name='inicio'),

    path('librosf/', libros_f, name='librosf'),

    #Urls de busquedas de libros
    path('buscar_l_by_t/', f_busqueda_lib_by_title, name='buscar_l_by_t'),
    path('result_l_by_t/', f_resultado_lib_by_title, name='result_l_by_t'),
    path('full_biblio/', read_biblioteca, name='full_biblio'),

    #Login Register Loguot
    path('login/', loguin_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='C:/Users/SegWay/Desktop/CoderHouse/PreentregaFinal/Entrega1_Albano/LibCatalogo/templates/LibCatalogo/register_login_logout/logout.html'), name='logout'),
    path('editUser/', editUser, name='editUser'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),

    path('blogDetail/<str:slug_url>', blog_detail, name='blogDetail'),
]

    