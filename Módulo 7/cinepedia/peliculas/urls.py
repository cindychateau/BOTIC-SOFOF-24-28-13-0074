from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('cine/', PeliculaListView.as_view(), name='pelicula-index')
]