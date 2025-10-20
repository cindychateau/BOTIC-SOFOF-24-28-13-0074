from django.db import models
from clientes.models import Cliente #Importamos Cliente para poder utilizarlo
from bicicletas.models import Bicicleta

#Modelo Orden -> fecha, total, estado, cliente (Cliente)
class Orden(models.Model):
    fecha = models.DateTimeField(auto_now_add=True) #DEFAULT CURRENT_TIMESTAMP
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    estado = models.CharField(
        max_length = 20,
        choices = [('pendiente', 'Pendiente'), ('pagada', 'Pagada'), ('anulada', 'Anulada')],
        default = 'pendiente'
    ) #VARCHAR(cantidad_max_caracteres)
    cliente = models.ForeignKey(
        Cliente, #Clase con la que me estoy relacionando
        on_delete = models.CASCADE, #Al borrar mi cliente, se borran sus ordenes
        related_name = 'ordenes' #cliente.ordenes
    )

    bicicletas = models.ManyToManyField(Bicicleta, through='DetalleOrden', related_name='ordenes') #n:m

    def __str__(self):
        return f"Orden: {self.id} - Total: {self.total} - Cliente: {self.cliente.nombre}"

class DetalleOrden(models.Model): #Tabla intermediaria
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.bicicleta} en {self.orden}"