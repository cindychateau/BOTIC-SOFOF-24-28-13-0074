from django.shortcuts import render
from .models import Receta

RECETAS = [
    Receta(
        nombre= "Spaghetti Carbonara",
        descripcion="Spagetti típico italiano",
        ingredientes= "Spaghetti, huevos, panceta, queso parmesano, pimienta",
        instrucciones= "Cocinar la pasta. Mezclar con huevos y queso. Añadir panceta frita."
    ),
    Receta(
        nombre="Tacos de Pollo",
        descripcion="Deliciosos taquitos de pollo",
        ingredientes="Tortillas, pollo, lechuga, tomate, salsa",
        instrucciones="Cocinar pollo, armar tacos con ingredientes."
    ),
]

#Inicio o Home
def home(request):
    return render(request, 'home.html') #también quieres enviar la lista de recetas

#Contacto

#Detalle de Receta