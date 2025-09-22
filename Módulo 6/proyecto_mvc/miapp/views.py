from django.shortcuts import render #Muestra una plantilla de HTML
from django.http import HttpResponse #Importo para mostrar una respuesta de http

# Create your views here.
#Funciones que definen qué mostrar al usuario

def funcion_prueba(request):
    return HttpResponse("¡Hola desde miapp!")
