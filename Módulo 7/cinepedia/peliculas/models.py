from django.db import models
from django.contrib.auth.models import User #Importamos usuario para poderlo utilizar en Pelicula

class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    fecha_estreno = models.DateField()
    sinopsis = models.TextField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

#Todo: class Comentario