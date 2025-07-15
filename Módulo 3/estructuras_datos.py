#Lista / Array /Arreglo
lista_vacia = []
lista_compras = ["leche", "manzanas", "pan"]
print(lista_compras[1]) #manzanas
print(lista_compras)
lista_compras[2] = "marraqueta"
print(lista_compras)

lista_compras.pop() #Elimina el último valor de mi lista. Eliminando marraqueta
print(lista_compras)
lista_compras.pop(0) #Enviando un valor, elimina ese índice del listado
print(lista_compras)
lista_compras.append("pollo") #Agregar el elemento al final de la lista
print(lista_compras)
lista_compras.insert(1, "sal") #Indico el indice y el valor a agregar
lista_compras.insert(1, "sal") #Indico el indice y el valor a agregar
print(lista_compras)

print(lista_compras.index("sal")) #Regresar el primer indice donde encuentra el valor dado. Si no lo encuentra da error
indice = lista_compras.index("manzanas")
lista_compras.pop(indice)
print(lista_compras)

lista_compras.remove("sal") #Va a borrar la primera ocurrencia que encuentre del valor
print(lista_compras)

lista_compras.insert(4, "carne")
print(lista_compras)
print(lista_compras[2])


verso1 = ['dale','a', 'tu', 'cuerpo']
verso2 = ['alegria', 'macarena']
estrofa = verso1 + verso2
print(estrofa)
cancion = 3 * estrofa
print(cancion)

lista_con_muchos_valores = [12, True, 1.2, "texto", ["otra", "lista"]]
print(lista_con_muchos_valores)

lista_grande = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(lista_grande[3:]) #"parto" a partir del índice 3 hasta el final de mi lista
print(lista_grande[:6]) #"Parto" desde el hasta límite 6
print(lista_grande[3:6])# "dividiendo" desde indice 3 hasta límite 6

lista_numeros = [2, 8, 1, 5, 2, 3, 1, 4]
print(len(lista_numeros)) #longitud de mi secuencia
print(max(lista_numeros)) #mayor
print(min(lista_numeros)) #menor
print(min(verso1)) #
print(sorted(lista_numeros, reverse=True)) #ordenado

cadena = ["baasdadasd", "aeaa", "iaa", "oua", "pasa"]
print(sorted(cadena, key=len))

print(lista_grande[:-1])

#Tupla: ordenada, inmutable -> no puede cambiar
tupla = ("a", "e", "i", "o", "u")
tupla_sin_p = "a", "e", "i", "o", "u"

print(tupla[2])
#tupla[2] = "j" Error TypeError

tupla = tupla + ("j", "k", "l")
print(tupla)
print(tupla[2:5])

#Diccionario: pares clave-valor
estudiante1 = {"nombre": "Elena", "apellido": "De Troya", "email": "elena@skillnest.com", "edad": 22}
estudiante2 = {
    "nombre": "Juana",
    "apellido": "De Arco",
    "email": "juana@skillnest.com",
    "edad": 30
}
print(estudiante2["edad"])

estudiante2["edad"] = 31
print(estudiante2)

estudiante2["curso"] = "Python" #Agregando un nuevo par de clave-valor
print(estudiante2)

estudiante1.pop("edad") #Eliminar el elemento con clave "edad"
print(estudiante1)

skillnest = {
    "nombre": "Skillnest",
    "fecha_inicial": "2025-07-11",
    "cursos": [
        {"nombre": "Python", "duracion": 24, "modulos": ["Modulo 1", "Modulo 2", "Modulo 3", "Modulo 4", "Modulo 5"]},
        {"nombre": "Java", "duracion": 16, "modulos": ["Fundamentos de Java", "POO", "Spring", "MVC"]}
    ]
}

skillnest["cursos"][0]["modulos"][2] = "Fundamentos de Python"

#Impresión linda
from pprint import pprint
pprint(skillnest)

ids = {1, 2, 3, 4, 1}
print(ids)

set1 = {2, 3, 4, 5, 6}
set2 = {3, 5, 6, 7, 8}

print(set1.union(set2)) #|
print(set1.intersection(set2)) #en lo que coinciden &
print(set1.difference(set2)) #en las diferencias vistas desde el primer set -
print(set2.difference(set1))
print(set1.difference(set2) | set2.difference(set1)) # Diferencia

estructura_datos = [200, 150, 300, 350]
for item in estructura_datos: #item = 350
    print(item)

for indice in range(len(estructura_datos)):
    print(indice, estructura_datos[indice])

array_bidimensional = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

array_bidimensional[0][3] = 5
print(array_bidimensional)

maestra = {
    "nombre": "Cynthia",
    "apellido": "Castillo",
    "curso": "Python"
}

for clave in maestra: #clave = "nombre", "apellido", "curso"
    print(maestra[clave])
    #print(clave)

for x in maestra.keys(): #clave
    print(x)

for u in maestra.values(): #solo valores
    print(u)

for a, b in maestra.items(): #pares de clave valor
    print(a, b, sep=" = ")