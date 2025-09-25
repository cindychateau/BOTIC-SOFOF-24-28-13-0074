from django.shortcuts import render #Muestra una plantilla de HTML
from django.http import HttpResponse #Importo para mostrar una respuesta de http

# Create your views here.
#Funciones que definen qué mostrar al usuario

def funcion_prueba(request):
    return HttpResponse("¡Hola desde miapp!")

def hola(request, nombre):
    print(nombre)
    return HttpResponse(f"<h1>¡Hola {nombre}!</h1>")

#nombre = Elena, cantidad = 5
def hola_repetido(request, nombre, cantidad):
    respuesta = ''
    for i in range(cantidad):
        respuesta += f"<h2>¡Holis {nombre}!</h2>"
    
    return HttpResponse(respuesta)

def home(request):
    #Diccionario con la información de 1 usuario. nombre, apellido, edad
    usuario = {
        "nombre": "Elena",
        "apellido": "De Troya",
        "edad": 25
    }

    nombre = "Elena De Troya"

    return render(request, 'home.html', {"nombreCompleto": nombre, "usuario": usuario}) #Enviamos a nuestro HTML. SIEMPRE debe tener formato de diccionario

def calculadora(request, num1, num2, operacion):
    operacion = operacion.lower()
    resultado = 0
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    else:
        resultado = "Operación inválida"
    
    return HttpResponse(resultado)

def contacto(request):
    return render(request, 'contacto.html')

def estudiantes(request):
    estudiantes = [
        {"nombre": "Elena de Troya", "curso": "Java"},
        {"nombre": "Juana de Arco", "curso": "Python"},
        {"nombre": "Pablo Picasso", "curso": "MERN"},
        {"nombre": "Pedro Páramo", "curso": "Fundamentos de la Web"}
    ]
    return render(request, 'estudiantes.html', {"estudiantes":estudiantes})