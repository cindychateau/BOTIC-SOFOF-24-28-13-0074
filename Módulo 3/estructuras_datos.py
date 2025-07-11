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
