from django.db import models

# Create your models here.
class Triciclo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2) #99999999.99
    disponible = models.BooleanField(default=True)
    anio = models.IntegerField() #null=True, default=2025
    created_at = models.DateTimeField(auto_now_add=True, null=True) #CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True, null=True) #CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

class Detalles(models.Model):
    triciclo = models.OneToOneField(Triciclo, on_delete=models.CASCADE, related_name='detalle')
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=30)
