#Bucles: un bloque de código que va a ser repetido siempre y cuando la condición se cumpla. Si no colocamos una condición correcta nos arriesgamos a tener un bucle infinito
# for (let i=2; i<7; i++) {
#     #Código a ejecutar
# }
for i in range(5): #0 - 4. NO ENTRA EN EL 5
    print(i)


for x in range(2, 7): #2 - 6. NO ENTRA EN EL 7
    print(x)

print("Afuera del bucle", x)

for numero in range(1, 10, 2): #(Comienzo, Límite, Cantidad a avanzar)
    print(numero)

print()

inicio = 2
fin = 8
paso = 3
for num in range(inicio, fin, paso):
    print(num)

print()
for z in range(5, -1, -2):
    print(z)

#Range aplicado a colecciones
lista_numeral = list(range(5))
print(lista_numeral)

#NO imprime nada
for z in range(5, -1, 2):
    print(z)

frase = "Buenos días"
for letra in frase:
    print(letra)


y = 0
while y < 3:
    print(y)
    y += 1
else:
    print("Sentencia final", y)


inicio = 1
final = 10
while inicio < final:
    print(inicio, final)
    inicio += 2
    final -= 1

# while True: #ciclo infinito
#     palabra = input("Ingresa una palabra. Si quieres salir escribe 'exit'")
#     if palabra == "exit":
#         print("Ya vas a salir")
#         break #TERMINA mi bucle
# else:
#     print("Sentencia cuando sale del while True")

for letra in "detente":
    if letra == "n":
        continue #Sáltate la n
    print(letra)

print("Fuera del bucle")

#Ciclo anidados
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j:{j}")

#Tablas de multiplicar
'''
tabla = 1
-> Tabla del 1
multiplicador = 1
-> 1 x 1 = 1
multiplicador = 2
-> 1 x 2 = 2
multiplicador = 3
-> 1 x 3 = 3
......
multiplicador = 10
-> 1 x 10 = 10

tabla = 2
-> Tabla del 2
multiplicador = 1 
'''
for tabla in range(1, 6): #Una vez por cada tabla
    print("Tabla del", tabla)
    for multiplicador in range(1, 11): #Por cada tabla yo recorro 1 -10
        print(f"{tabla} x {multiplicador} = {tabla*multiplicador}")
