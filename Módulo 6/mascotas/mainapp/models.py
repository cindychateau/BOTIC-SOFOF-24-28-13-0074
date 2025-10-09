from django.db import models
from django.contrib.auth.models import User

#add, view, change, delete
class Mascota(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    especie = models.CharField(max_length=20)
    descripcion = models.TextField()
    dueno = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    class Meta:
        permissions = [
            ("view_all_mascota", "Ver todas las mascotas"), #(codigo_permiso, "Nombre Visible")
        ]
