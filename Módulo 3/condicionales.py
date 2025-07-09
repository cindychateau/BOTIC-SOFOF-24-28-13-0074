x = 20
if x > 10: #20 > 10
    print("El número ingresado es mayor a 10")
else:
    print("El número es menor a 10")

print("----------")

edad_infante = 4 #snake_case variables y funciones
if edad_infante < 2: #4 < 2
    print("El infante es un bebesito")
elif edad_infante < 5: #4 < 5
    print("El infante es un toddler")
else:
    print("El infante es un niño")

#&& and 
temperatura = 20
esta_lloviendo = False #True o False
if temperatura > 18 and not esta_lloviendo: #! not -------- not CONDICIONAL = CONDICIONAL == False
    print("Salgamos al parque a pasear!")
else:
    print("Quedémonos en casa a descansar!")

#|| or
edad = 17
permiso_padres = False
if edad >= 18 or permiso_padres:
    print("Ya puedes obtener tu licencia de manejo")


x = 1
y = 2
z = 3

if x > 2 or y > 2 or z > 2:
    print("Alguno de los números es mayor a 2")

# > < >= <= == !=
# and or not

#() */ +-
matematicas = 50 + 2 / 10 * (12 - 1)


'''
ADIVINA ADIVINADOR
Pide al usuario que ingrese un número del 1 al 10.
Crea un número aleatorio mágico ;)

Muestra un mensaje especial según si:
Le atinó,
Estuvo cerca (a 1 número de distancia),
Falló por mucho.
*Si conoces sobre bucles, bucle para pedirle el número hasta que lo adivine*
'''
# try:
#     numero = int(input("Dame un número:"))
# except ValueError:
#     print("Lo que ingresaste no fue válido")

'''
MOOD DEL DÍA
Pide al usuario que ingrese su estado de ánimo (feliz, triste, cansado, emocionado).
Según la respuesta, muestra un mensaje motivador o divertido.
'''


'''
3 NUMERITOS
Pide tres números. Según sus valores y la suma total, el programa mostrará un mensaje. Solo una opción se mostrará, la primera que cumpla:

Si todos los números son 0: mostrar "Todos los números son cero."
Si algún número es negativo: mostrar "Tienes al menos un número negativo."
Si los tres números son iguales a 100: mostrar "¡Triple 100!"
Si todos los números son iguales: mostrar "Todos los números son iguales."
Si la suma es mayor a 300: mostrar "La suma es altísima."
Si la suma está entre 201 y 300: mostrar "La suma es alta."
Si la suma está entre 101 y 200: mostrar "La suma es media."
Si la suma es 100 o menos: mostrar "La suma es baja."
En cualquier otro caso (no debería ocurrir, pero por buenas prácticas): mostrar "Caso no contemplado. Misterio sin resolver"
'''
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

suma = num1 + num2 + num3

if num1 == num2 == num3 == 0: #num1 == 0 and num2 == 0 and num3 == 0
    print("Todos los números son cero.")
elif num1 < 0 or num2 < 0 or num3 < 0:
    print("Tienes al menos un número negativo.")
elif num1 == num2 == num3 == 100:
    print("¡Triple 100!")
elif num1 == num2 == num3: #num1 == num2 and num2 == num3
    print("Todos los números son iguales.")
elif suma > 300:
    print("La suma es ALTISIMA")
elif suma > 200:
    print("La suma es alta...")
elif suma > 100:
    print("la suma es media")
elif suma <= 100:
    print("La suma es baja.")
else:
    print("Caso no contemplado. Misterio sin resolver")






