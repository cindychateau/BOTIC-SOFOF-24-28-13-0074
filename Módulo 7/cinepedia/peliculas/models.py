from django.db import models
from django.contrib.auth.models import User #Importamos usuario para poderlo utilizar en Pelicula

class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    fecha_estreno = models.DateField()
    sinopsis = models.TextField()
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    #comentarios = [Comentario]

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        ordering = ['-fecha'] #Por defecto siempre me va a ordenar los más recientes primero

    def __str__(self):
        return self.contenido