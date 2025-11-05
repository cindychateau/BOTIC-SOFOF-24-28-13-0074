from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cine/', PeliculaListView.as_view(), name='pelicula-index'),
    path('cine/nueva/', PeliculaCreateView.as_view(), name='pelicula-nueva'),
    path('cine/editar/<int:pk>/', PeliculaUpdateView.as_view(), name='pelicula-editar'),
    path('pagina_sinpermisos/', pagina_sinpermisos, name='pagina_sinpermisos'),
]