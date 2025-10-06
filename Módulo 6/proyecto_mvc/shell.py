from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from miapp.models import Producto

# Obtener el permiso para ver productos
content_type = ContentType.objects.get_for_model(Producto)
#add_producto, change_producto, view_producto, delete_producto
permission = Permission.objects.get(codename='view_producto', content_type=content_type) #Django genera automáticamente permisos para cada modelo cuando lo creas

user = User.objects.create_user('cliente2', password='contrasena123')
user.user_permissions.add(permission)

########################################################################################
from django.contrib.auth.models import User, Permission
from blog.models import Post

user1 = User.objects.create_user(username="elena", password="1234")
user2 = User.objects.create_user(username="juana", password="1234")

perm = Permission.objects.get(codename="change_post")  # permiso autogenerado por Django
user1.user_permissions.add(perm)

Post.objects.create(titulo="Primer post de Elena", contenido="Contenido del post de Elena", autor=user1)
Post.objects.create(titulo="Segundo post de Elena", contenido="Otro texto de Elena", autor=user1)
Post.objects.create(titulo="Post de Juana", contenido="Texto escrito por Juana", autor=user2)

########################################################################################

from django.contrib.auth.models import User, Permission
from blog.models import Post

user = User.objects.get(username='elena')

perm = Permission.objects.get(codename="ver_posts_exclusivos")
user.user_permissions.add(perm)
