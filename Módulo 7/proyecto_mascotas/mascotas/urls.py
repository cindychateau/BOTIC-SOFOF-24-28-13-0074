from django.urls import path
from .views import *

urlpatterns = [
    path('', MascotaListView.as_view(), name='lista_mascotas'),
    path('nueva/', MascotaCreateView.as_view(), name='crear_mascota'),
    path('editar/<int:pk>/', MascotaUpdateView.as_view(), name='editar_mascota'),
    path('borrar/<int:pk>/', MascotaDeleteView.as_view(), name='borrar_mascota'),
    path('detalle/<int:pk>/', MascotaDetailView.as_view(), name='detalle_mascota'),
]