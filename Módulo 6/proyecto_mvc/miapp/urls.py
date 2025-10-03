#Definimos las rutas de la aplicación
from django.urls import path #Importo path, para generar una ruta
from . import views #Importo views, en base a una ruta mostrar una vista
from django.contrib.auth import views as auth_views #Vistas pre-creadas que Django tiene para que yo utilice

urlpatterns = [
    path('prueba/', views.funcion_prueba, name='prueba'),
    path('hola/<str:nombre>/', views.hola, name="hola"),
    path('hola/<str:nombre>/<int:cantidad>/', views.hola_repetido, name="hola_repetido"),
    path('', views.home, name='home'),
    path('calculadora/<int:num1>/<int:num2>/<str:operacion>/', views.calculadora,name="calculadora"),
    path('contacto/', views.contacto, name="contacto"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('productos/', views.productos, name="productos"),
    path('productos/<int:indice>', views.producto, name="producto"),
    path('contacto_exito/', views.contacto_exito, name="contacto_exito"),
    path('login/', views.login_view, name="login"),
    #path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
]

#http://127.0.0.1:8000/miapp/hola/alguntexto
#http://127.0.0.1:8000/miapp/hola/Elena/5
