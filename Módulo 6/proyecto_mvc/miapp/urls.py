#Definimos las rutas de la aplicación
from django.urls import path #Importo path, para generar una ruta
from . import views #Importo views, en base a una ruta mostrar una vista

urlpatterns = [
    path('prueba/', views.funcion_prueba, name='prueba'),
    path('hola/<str:nombre>/', views.hola, name="hola"),
    path('hola/<str:nombre>/<int:cantidad>/', views.hola_repetido, name="hola_repetido"),
    path('', views.home, name='home')
]

#http://127.0.0.1:8000/miapp/hola/alguntexto
#http://127.0.0.1:8000/miapp/hola/Elena/5
