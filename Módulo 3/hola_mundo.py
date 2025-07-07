# 1. Imprime "Hola, mundo"
print("Hola, mundo")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Cynthia"
print("Hola", nombre) # con una coma
#Hola&Cynthia
print("Hola", nombre, sep="askdlak")
print("Hola, "+ nombre) #LITERAL solo pegar las cadenas

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 22
print("Hola", numero, "!") # con una coma
print("Hola "+str(numero)+"!") #Casteamos la variable número a que sea String

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "comida china"
comida2 = "sopaipillas"
print("Me encanta comer {} y {}".format(comida1, comida2)) # con .format()
comidas = "Me encanta comer {} y {}".format(comida1, comida2)
print(comidas)
print("Me encanta comer {comi1} y {comi2}".format(comi1 = "tacos", comi2 = "arepas"))
print(f"Me encanta comer '{comida1}' y {comida2}")