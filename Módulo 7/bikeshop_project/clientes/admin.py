from django.contrib import admin
from .models import Cliente, PerfilCliente

# Register your models here.
admin.site.register(Cliente)
admin.site.register(PerfilCliente)

#Desde Cliente yo pueda crear ahí mismo el Perfil del Cliente

