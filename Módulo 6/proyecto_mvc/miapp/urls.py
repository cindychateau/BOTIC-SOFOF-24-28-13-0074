#Definimos las rutas de la aplicación
from django.urls import path #Importo path, para generar una ruta
from . import views #Importo views, en base a una ruta mostrar una vista

urlpatterns = [
    path('prueba/', views.funcion_prueba, name='prueba')
]