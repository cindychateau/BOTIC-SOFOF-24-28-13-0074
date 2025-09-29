from django.db import models

# Create your models here.

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    #imagen = models.ImageField(upload_to='')

    def __str__(self):
        return self.nombre