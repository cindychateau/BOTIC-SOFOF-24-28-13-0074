from django.urls import path #Generar una ruta
from . import views #Importo views, en base a x ruta muestra y vista

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear, name='crear'),
]