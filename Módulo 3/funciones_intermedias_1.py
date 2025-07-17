#Crea la función iterarDiccionario(lista) que reciba una lista de diccionarios y recorra cada diccionario de la lista e imprima cada llave y el valor correspondiente.
'''
lista = [
    {"nombre_receta": "Galletas", "cantidad_pasos": 5, "ingredientes": ["harina", "huevo", "vainilla", "chocolate"]},
    {"nombre_receta": "Sandwich", "cantidad_pasos": 2, "ingredientes": ["pan", "mayonesa", "jamón"]},
    {"nombre_receta": "Completo", "cantidad_pasos": 3, "ingredientes": ["pan", "salchicha", "mayonesa", "palta", "tomate", "ketchup"]}
]
Primer for
elemento = {"nombre_receta": "Galletas", "cantidad_pasos": 5, "ingredientes": ["harina", "huevo", "vainilla", "chocolate"]}
frase = ""
Segundo for
clave = "nombre_receta"
valor = "Galletas"
frase = ""+ "nombre_receta - Galletas" = "nombre_receta - Galletas"
-
clave = "cantidad_pasos"
valor = 5
frase = "nombre_receta - Galletas, " + "cantidad_pasos - 5"
-
clave = "ingredientes"
valor = ["harina", "huevo", "vainilla", "chocolate"]
frase = "nombre_receta - Galletas, cantidad_pasos - 5, " + "ingredientes - ["harina", "huevo", "vainilla", "chocolate"], "
'''
def iterarDiccionario(lista):
    for elemento in lista:
        frase = ""
        for clave, valor in elemento.items():
            frase += (f"{clave} - {valor}, ")
        print(frase[:-2])


cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"},
   {"apodo": "Belipop", "pais": "España"}
]

recetas = [
    {"nombre_receta": "Galletas", "cantidad_pasos": 5, "ingredientes": ["harina", "huevo", "vainilla", "chocolate"]},
    {"nombre_receta": "Sandwich", "cantidad_pasos": 2, "ingredientes": ["pan", "mayonesa", "jamón"]},
    {"nombre_receta": "Completo", "cantidad_pasos": 3, "ingredientes": ["pan", "salchicha", "mayonesa", "palta", "tomate", "ketchup"]}
]

iterarDiccionario(recetas)


#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios. La función debe imprimir el valor almacenado para esa clave de cada diccionario que se encuentra en la lista. Por ejemplo, iterarDiccionario2(“nombre”, cantantes) debe de imprimir
def iterarDiccionario2(llave, lista): #llave = "nombre"
    for diccionario in lista: #diccionario = {"apodo": "Belipop", "pais": "España"}
        if llave in diccionario:
            print(diccionario[llave]) #"Juan Luis Guerra"
        else:
            print("No existe esa llave en el diccionario")
    '''
    for i in lista:
        try:
            print(i[llave])
        except KeyError:
            print("No existe esa llave en el diccionario")
    '''

#clave = input("Elige la clave que quieres imprimir: ")
clave = "nombre"
iterarDiccionario2(clave, cantantes)

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

chile = {
    "regiones": ["Metropolitana", "Los lagos", "Ñuble", "Los Ríos", "Tarapacá", "Araucania"],
    "comidas": ["Completos", "Empanadas", "Curanto", "Charquican", "Mote de Huesillos", "Pastel de Choclo", "Humitas"],
    "ciudades": ["Santiago", "Punta Arenas", "Talca", "Algarrobo", "Arica"]
}

#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.
def imprimirInformacion(diccionario): #diccionario = chile
    for clave, valor in diccionario.items(): #clave = "comidas", valor = ["Completos", "Empanadas", "Curanto", "Charquican", "Mote de Huesillos", "Pastel de Choclo", "Humitas"]
        print(f"{len(valor)} {clave.upper()}") #6 COMIDAS
        #sorted me va a ordenar alfabeticamente
        for x in sorted(valor): #x =  "Curanto"
            print(x)

imprimirInformacion(chile)

