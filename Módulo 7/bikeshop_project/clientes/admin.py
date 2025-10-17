from django.contrib import admin
from .models import Cliente, PerfilCliente

# Register your models here.
# admin.site.register(Cliente)
# admin.site.register(PerfilCliente)

#Desde Cliente yo pueda crear ahí mismo el Perfil del Cliente
class PerfilInline(admin.StackedInline):
    model = PerfilCliente
    can_delete = False
    verbose_name_plural = 'Perfil'

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'created_at')
    inlines = (PerfilInline,)

@admin.register(PerfilCliente)
class PerfilClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'telefono', 'direccion')

