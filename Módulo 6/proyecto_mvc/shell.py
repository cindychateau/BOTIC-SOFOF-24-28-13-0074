from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from miapp.models import Producto

# Obtener el permiso para ver productos
content_type = ContentType.objects.get_for_model(Producto)
#add_producto, change_producto, view_producto, delete_producto
permission = Permission.objects.get(codename='view_producto', content_type=content_type) #Django genera automáticamente permisos para cada modelo cuando lo creas

user = User.objects.create_user('cliente2', password='contrasena123')
user.user_permissions.add(permission)