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

'''
mascotas = Mascota.objects.all()
mascotas = Mascota.objects.filter(edad__gt=5) -> greater than
mascotas = Mascota.objects.order_by('-edad') -> descendente
mascota = Mascota.objects.get(nombre='Michi')
mascota.edad = 5
mascota.save() -> guardar un nuevo registro, guardar un cambio de un registro que ya existe
mascota.delete() -> borra registro
'''
