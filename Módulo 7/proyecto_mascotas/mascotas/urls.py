from django.urls import path
from . import views #Importar todo
#from .views import MascotaListView, MascotaDetailView

urlpatterns = [
    path('', MascotaListView.as_view(), name='lista_mascotas')
]