# ordenes/admin.py
from django.contrib import admin
from .models import Orden, DetalleOrden

# Inline para la tabla intermedia DetalleOrden
class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1  # Número de filas extra vacías para agregar rápido
    min_num = 1
    can_delete = True
    verbose_name = "Detalle de la Orden"
    verbose_name_plural = "Detalles de la Orden"

# Registro de Orden con inline de DetalleOrden
@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total', 'estado')
    list_filter = ('estado','fecha')
    search_fields = ('cliente__nombre',)
    inlines = (DetalleOrdenInline,)  # Inline agregado para ver/editar los detalles

# Registro de DetalleOrden (opcional, normalmente con inline basta)
@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'bicicleta', 'cantidad', 'precio_unitario')
    list_filter = ('orden','bicicleta')
    search_fields = ('orden__cliente__nombre','bicicleta__nombre')