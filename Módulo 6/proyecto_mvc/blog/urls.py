from django.urls import path
#Todo: importación de las clases de mi vista
from .views import *

urlpatterns = [
    path('', ListaPosts.as_view(), name="lista_posts"), #pública
    path('mis-posts/', MisPosts.as_view(), name="mis_posts"), #privada, solo aquellos que iniciaron sesión
    path('editar/', EditarPost.as_view(), name="editar_post"), #privada y con permisos
]