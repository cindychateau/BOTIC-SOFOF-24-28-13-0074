from django.db import models
from clientes.models import Cliente #Importamos Cliente para poder utilizarlo

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

    def __str__(self):
        return f"Orden: {self.id} - Total: {self.total} - Cliente: {self.cliente.nombre}"

