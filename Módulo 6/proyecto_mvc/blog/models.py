from django.db import models
from django.contrib.auth.models import User

#Permisos por defecto que da Django: add, view, change, delete
#delete_post
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #Relación con User
    #exclusivo = models.BooleanField etc etc

    class Meta:
        #Creando permisos adicionales
        permissions = [
            ("ver_posts_exclusivos", "Ver publicaciones exclusivas")
        ]