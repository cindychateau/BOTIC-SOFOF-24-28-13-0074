from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('contacto/', views.funcion_contacto, name="contacto"),
    #path('detalle/OJO, RECIBES ALGO', views.funcion_detalle, name="detalle"),
]