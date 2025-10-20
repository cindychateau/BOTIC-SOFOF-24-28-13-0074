from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) #-> ON UPDATE CURRENT_TIMESTAMP
    #perfil = PerfilCliente
    #activo = models.BooleanField(default=True) -> al eliminar este pasa a ser False. Borrado Lógico
    #ordenes = [Orden]
    def __str__(self):
        return self.nombre

class PerfilCliente(models.Model):
    cliente = models.OneToOneField(
        Cliente,
        on_delete = models.CASCADE, # Si el cliente se elimina, el perfil también se elimina
        related_name = 'perfil' #Nombre inverso -> cliente.perfil
    )
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True) #DATE() yyyy-mm-dd 2025-10-18

    def __str__(self):
        return f"Perfil de {self.cliente.nombre}"


#elena = objeto de Cliente
#elena.nombre = "Elena"
#elena.email = "elena@skillnest.com"
#elena.perfil = <Objeto de PerfilCliente>
#elena.perfil.direccion
#perfil_elena.cliente.email
