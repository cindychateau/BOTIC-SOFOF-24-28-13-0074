from bicicletas.models import Bicicleta

#Crear un nuevo registro
nueva_bici = Bicicleta(
    marca = "Trek",
    modelo = "Marlin 7",
    tipo = "mtb",
    precio = 799.99,
    disponible = True,
    anio = 2023
)
nueva_bici.save() #Guardar el registo en BD

#Con create
Bicicleta.objects.create(
    marca = "Giant",
    modelo = "Trance",
    tipo = "ruta",
    precio = 1200,
    disponible = True,
    anio = 2023
)

Bicicleta.objects.create(
    marca = "Specialized",
    modelo = "Allez",
    tipo = "ruta",
    precio = 999.99,
    disponible = False,
    anio = 2022
)

#Leer registros
bicicletas = Bicicleta.objects.all() #SELECT * FROM bicicletas_bicicleta;
print(bicicletas)

#Filtrar bicicletas disponibles
disponibles = Bicicleta.objects.filter(disponible=True) #SELECT * FROM bicicletas_bicicleta WHERE disponible = 1;
print(disponibles)

#Ordenar por precio descendente
ordenadas = Bicicleta.objects.order_by('-precio') #SELECT * FROM bicicletas_bicicleta ORDER BY precio DESC;
print(ordenadas)

#Obtener 1 registro
bici1 = Bicicleta.objects.get(id=1) #SELECT * FROM bicicletas_bicicleta WHERE id = 1;
print(bici1)

#Actualizar
bici1.precio = 800
bici1.save() #UPDATE

Bicicleta.objects.filter(id=1).update(precio=851)

#Borrado
bici1.delete()

##################
# RELACIONES 1:1 #
##################
from clientes.models import Cliente, PerfilCliente

elena = Cliente.objects.create(nombre="Elena de Troya", email="elena@skillnest.com")

try:
    perfil_inexistente = elena.perfil
except PerfilCliente.DoesNotExit:
    print("El cliente aún no tiene perfil")

perfil_elena = PerfilCliente.objects.create(cliente=elena, direccion="Av. ABC 123", telefono="12345678", fecha_nacimiento="1996-10-18")

#Transacción atómica -> Las distintas acciones que se hagan deben cumplirse para que se guarde lo que trataba de hacer
#Transacción atómica -> TODO O NADA
from django.db import transaction

with transaction.atomic():
    juana = Cliente.objects.create(nombre="Juana de Arco", email="juana@skillnest.com")
    PerfilCliente.objects.create(cliente=juana, direccion="Calle Numero 5", telefono="5555555")

with transaction.atomic():
    pablo = Cliente.objects.create(nombri="Pablo Picasso", email="pablo@skillnest.com")
    PerfilCliente.objects.create(cliente=pablo, direccion="Ave. Atardecer", telefono="12340987")
try:
    with transaction.atomic():
        pedro = Cliente.objects.create(nombre="Pedro Páramo", email="pedro@skillnest.com")
        PerfilCliente.objects.create(cliente=pedro, direccion="Comala", telefoni="10101010")
except:
    print("¡Error!")

clientes = Cliente.objects.all() #SELECT * FROM clientes_cliente
for cliente in clientes:
    print(cliente.perfil.direccion) #Consulta adicional -> SELECT * FROM clientes_perfilcliente WHERE cliente_id = <id>

#SELECT * FROM clientes_cliente JOIN clientes_perfilcliente ON cliente_id = clientes_cliente.id
clientes_conperfil = Cliente.objects.select_related('perfil').all() #all() = todos los registros
for cliente in clientes_conperfil:
    print(cliente.perfil.direccion)


juana = Cliente.objects.get(email="juana@skillnest.com")
perfil_juana = juana.perfil
perfil_juana.telefono = "65555555"
perfil_juana.save()

perfil_juana.delete()

elena = Cliente.objects.get(email="elena@skillnest.com")
elena.delete()

##################
# RELACIONES 1:n #
##################
from clientes.models import Cliente
from ordenes.models import Orden

clientes = Cliente.objects.all()

juana = Cliente.objects.get(email="juana@skillnest.com")
o1 = Orden.objects.create(cliente=juana, total=1200.50)
o2 = Orden.objects.create(cliente=juana, total=850, estado='pagada')

juana.ordenes.all()
o1.cliente

ordenes_pendientes = Orden.objects.filter(estado='pendiente')
print(ordenes_pendientes)

o1.estado = 'pagada'
o1.save()

o2.delete()

ordenes = Orden.objects.select_related('cliente').all()
for orden in ordenes:
    print(orden.id, orden.cliente.nombre, orden.total)

ordenes_pagadas_concliente = Orden.objects.select_related('cliente').filter(estado='pagada') #prefetch_related
for orden in ordenes_pagadas_concliente:
    print(orden.id, orden.cliente.nombre, orden.total)

##################
# RELACIONES n:m #
##################
from clientes.models import Cliente
from bicicletas.models import Bicicleta
from ordenes.models import Orden, DetalleOrden

juana = Cliente.objects.get(email="juana@skillnest.com")
o3 = Orden.objects.create(cliente=juana, total=0)

#Para poder crear un nuevo registro de DetalleOrden necesito: Orden y Bicicleta
bici_giant = Bicicleta.objects.get(id=2)
bici_sp = Bicicleta.objects.get(id=3)

DetalleOrden.objects.create(orden=o3, bicicleta=bici_giant, cantidad=2, precio_unitario=600)
DetalleOrden.objects.create(orden=o3, bicicleta=bici_sp, cantidad=1, precio_unitario=750)

o3.bicicletas.all()
bici_sp.ordenes.all()

#DetallesOrden.objects.filter(orden=o3) -> Lista de todos los DetallesOrden de la orden 3
#[DO(orden=3, bicicleta=sp, cantidad=2, precio_unitario=600), DO(orden=3, bicicleta=giant, cantidad=1, precio_unitario=750)]
#detalle = DO(orden=3, bicicleta=giant, cantidad=1, precio_unitario=750)
#detalle.cantidad * detalle.precio_unitario = 1*750 = 750
total = sum(detalle.cantidad*detalle.precio_unitario for detalle in DetalleOrden.objects.filter(orden=o3)) #[1200, 750] = 1950
#[1200,750]
'''
lista_a_sumar = []
detalles = DetallesOrden.objects.filter(orden=o3)
for detalle in detalles:
    lista_a_sumar.append(detalle.cantidad*detalle.precio_unitario)
total = sum(lista_a_sumar)
'''
o3.total = total
o3.save()

#num = 3
#num*num for num in [1, 2, 3] -> [1, 4, 9]

##################
#   SQL + ORM.   #
##################
from clientes.models import Cliente
clientes = Cliente.objects.all() #Obtener todos los registros -> SELECT * FROM clientes_cliente;
print(clientes)

from bicicletas.models import Bicicleta
#Obteniendo todos los registros de Bicicleta donde marca = 'Giant'-> SELECT * FROM bicicletas_bicicleta WHERE marca = 'Giant'
Bicicleta.objects.filter(marca='Giant')

#Obtener todos los registros de Bicicleta donde modelo comience con A -> SELECT * FROM bicicletas_bicicleta WHERE modelo LIKE 'A%'
Bicicleta.objects.filter(modelo__startswith='A') #Case sensitive
Bicicleta.objects.filter(modelo__istartswith='a') #Case insensitive

#Obtener todos los registros de Bicicleta donde modelo termine con Z -> SELECT * FROM bicicletas_bicicleta WHERE modelo LIKE '%z'
Bicicleta.objects.filter(modelo__endswith='Z') #Case sensitive
Bicicleta.objects.filter(modelo__iendswith='Z') #Case insensitive

#Obtener todo los registros de Bicicleta donde marca tenga an-> SELECT * FROM bicicletas_bicileta WHERE marca LIKE '%an%'
Bicicleta.objects.filter(marca__contains='an')
Bicicleta.objects.filter(marca__icontains='an')

#Obtener los registros de Bicicleta donde precio es mayor a 1000 -> SELECT * FROM bicicletas_bicileta WHERE precio > 1000
Bicicleta.objects.filter(precio__gt=1000) #mayor que
Bicicleta.objects.filter(precio__gte=1000) #mayor o igual

#Obtener los registros de Bicicleta donde precio es menor a 1000 -> SELECT * FROM bicicletas_bicileta WHERE precio < 1000
Bicicleta.objects.filter(precio__lt=1000) #menor que
Bicicleta.objects.filter(precio__lte=1000) #menor o igual

#Bicicleta que anio mayor al 2022, precio menor a 1500 -> AND
Bicicleta.objects.filter(anio__gt=2022).filter(precio__lt=1500)
Bicicleta.objects.filter(anio__gt=2022, precio__lt=1500)

#OR ||
from django.db.models import Q 
Bicicleta.objects.filter(Q(anio__gt=2022) | Q(precio__lt=1500))

from ordenes.models import Orden
#Recibir una lista con la información que me regresa el query "crudo"
ordenes = Orden.objects.raw("SELECT * FROM ordenes_orden WHERE cliente_id = %s", [2]) #SELECT
for orden in ordenes: #iteración
    print(orden.id, orden.fecha, orden.total)

#Obtener solamente ciertas columnas
Cliente.objects.values("nombre", "email") #Genera un QuerySet de diccionarios SOLO con esos atributos
Cliente.objects.defer("email") #Excluyo ese campo del resultado.

#Anotaciones
from django.db.models import Count
clientes = Cliente.objects.annotate(total_ordenes=Count("ordenes"))
for cliente in clientes:
    print(cliente.nombre, cliente.total_ordenes)

#Cursor -> Operaciones más complejas
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("UPDATE ordenes_orden SET total = total*1.02 WHERE estado = %s", ['pendiente'])

#Obtener ordenes pendientes
ordenes_pendientes = Orden.objects.filter(estado='pendiente')
for orden in ordenes:
    orden.total = orden.total * 1.02
    orden.save()

#LIMIT .first() .last()
Cliente.objects.all()[:5] #LIMIT 5
Cliente.objects.all()[10:20] #LIMIT 10 - 20
