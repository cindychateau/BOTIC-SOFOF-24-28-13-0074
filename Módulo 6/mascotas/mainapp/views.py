from django.shortcuts import render, redirect
from .models import Mascota
#Todo: Importación de formulario

#Importar Modelo auth: User, authenticate, login, logout, decoradores (@login_required, @permission_required)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

#Obtener a los 2 usuarios
elena = User.objects.get(username='elena')
juana = User.objects.get(username='juana')
#Lista de mascotas
MASCOTAS = [
    Mascota(nombre = "Miu", edad = 8, especie = "Gato", descripcion = "Gatita peluda color blanca", dueno = elena),
    Mascota(nombre = "Michi", edad = 4, especie = "Gato", descripcion = "Gatita calico muy traviesa", dueno = juana),
]

def home(request):
    #Todo: filtrar las del usuario en sesión
    #Enviar contexto (mascotas)
    return render(request, 'home.html', {'mascotas': MASCOTAS})
