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
