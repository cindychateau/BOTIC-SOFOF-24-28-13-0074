from django.urls import path #Importo path, para generar una ruta
from . import views #Importo views, en base a una ruta mostrar una vista

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('mascota/crear/', views.crear, name="crear"),
    path('mascota/editar/<str:nombre>/', views.editar, name="editar"), #127.0.0.1/mascota/editar/Miu
    path('mascota/detalle/<str:nombre>/', views.detalle, name="detalle"),  #127.0.0.1/mascota/detalle/Miu
    path('mascota/borrar/<str:nombre>/', views.borrar, name="borrar"),
    path('mascota/todas/', views.todas, name="todas"),
]