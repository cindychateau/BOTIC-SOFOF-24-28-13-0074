from django.db import models

# Create your models here.

from datetime import date

class Producto(models.Model):
    nombre = models.CharField(max_length=30) #VARCHAR(30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) #DECIMAL(10, 2)
    fecha_creacion = models.DateField(default=date.today) #Sin horas. Con horas: DateTimeField(default=datetime.now)
    disponible = models.BooleanField(default=True)