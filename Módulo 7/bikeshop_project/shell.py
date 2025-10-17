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