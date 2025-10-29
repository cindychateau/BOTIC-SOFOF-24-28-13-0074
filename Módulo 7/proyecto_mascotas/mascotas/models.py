from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100) #ForeignKey -> class Especie
    edad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)
    #dueno = ForeignKey -> class User

    def __str__(self):
        return f"{self.nombre} ({self.especie})"
