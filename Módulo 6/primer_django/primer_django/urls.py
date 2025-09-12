"""
URL configuration for primer_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse #Poder generar una respuesta de http
from django.shortcuts import render #Renderizar

def saludo(request):
    return HttpResponse("¡Hola desde Django!")

def pagina_html(request):
    return render(request, "base.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo), #path("ruta/", funcion) -> 127.0.0.1/saludo
    path('plantilla/', pagina_html) #127.0.0.1/plantilla
]
