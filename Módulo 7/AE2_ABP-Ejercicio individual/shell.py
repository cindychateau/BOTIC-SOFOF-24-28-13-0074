from productos.models import Producto

producto = Producto(
    nombre = "Desodorante",
    descripcion = "Olor chocolate",
    precio = 1000,
    stock = 10
)
producto.save()

Producto.objects.create(
    nombre = "Shampoo de Mascota",
    descripcion = "Shampoo para perritos y gatitos",
    precio = 500,
    stock = 5
)

#Obtener TODOS -> Producto.objects.all()
#Obtener una lista de productos WHERE -> Producto.objects.filter()
producto1 = Producto.objects.get(id=1) #nombre = "Desodorante"
print(producto1, producto1.descripcion, producto.precio, producto1.stock)

producto1.precio = 989
producto1.save()

producto1.delete()

#AE5 - Ejercicio Individual
from productos.models import Producto

Producto.objects.create(nombre="Audífonos", descripcion="Audífonos Bluetooth", precio=120, stock=15)
Producto.objects.create(nombre="Aspiradora", descripcion="Aspiradora sin cable", precio=90, stock=5)
Producto.objects.create(nombre="Monitor", descripcion="Monitor LED 24 pulgadas", precio=130, stock=12)
Producto.objects.create(nombre="Mouse", descripcion="Mouse óptico inalámbrico", precio=25, stock=50)
Producto.objects.create(nombre="Alfombrilla", descripcion="Alfombrilla gamer RGB", precio=40, stock=8)
Producto.objects.create(nombre="Adaptador HDMI", descripcion="Adaptador a USB-C", precio=20, stock=3)

Producto.objects.all()
productos_mayores_50pesos = Producto.objects.filter(precio__gt=50)
print(productos_mayores_50pesos)

productos_empiecen_a = Producto.objects.filter(nombre__istartswith="A")
print(productos_empiecen_a)

productos_disponibles = Producto.objects.filter(disponible=True)
print(productos_disponibles)

productos_menores_100 = Producto.objects.raw("SELECT * FROM productos_producto WHERE precio < 100;")
for producto in productos_menores_100:
    print(producto.nombre, producto.precio)

bajo_stock = Producto.objects.raw("SELECT * FROM productos_producto WHERE stock < 10")
for producto in bajo_stock:
    print(producto.nombre, producto.stock)