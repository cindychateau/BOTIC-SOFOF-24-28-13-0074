from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50, unique=True) #unique=True sea un valor único
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True) #default=CURRENT_TIMESTAMP

    def __str__(self):
        return self.nombre