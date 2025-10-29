from django.urls import path #Generar una ruta
from . import views #Importo views, en base a x ruta muestra y vista

urlpatterns = [
    path('', views.home, name='home'),
    path('crear/', views.crear, name='crear'), #nuevo/nueva
    path('actualizar/<int:id>/', views.actualizar, name='actualizar'), #editar
    path('eliminar/<int:id>/', views.eliminar, name='eliminar'), #borrar
    path('detalle/<int:id>/', views.detalle, name='detalle'), #vista
]