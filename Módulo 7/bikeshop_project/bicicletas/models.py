from django.db import models

# Create your models here.
#Nombre de la tabla -> aplicacion_modelo
class Bicicleta(models.Model):
    #codigo = models.CharField(max_length=10, primary_key=True)
    marca = models.CharField(max_length=50) #VARCHAR(50)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2) #DECIMAL(10, 2) -> 1000000000.99
    disponible = models.BooleanField(default=True) #BOOLEAN -> TINYINT(1) 0 1
    anio = models.IntegerField()
    tipo = models.CharField(
        max_length=20,
        choices = [('mtb', 'Montaña'), ('ruta', 'Ruta'), ('bmx', 'BMX')],
        default = 'mtb'
    )

    def __str__(self):
        return f"{self.marca} {self.modelo}"