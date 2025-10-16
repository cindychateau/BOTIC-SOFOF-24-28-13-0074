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