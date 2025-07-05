import random
import math

#BOOLEANS
mayor_edad = True
tiene_bigote = False

#NUMERALES
edad = 25 #Entero (Sin decimales)
altura = 2.05 #Flotante (Con decimales)

edad_flotante = float(edad) #Transformar mi valor en flotante
print(edad_flotante)
altura_entera = int(altura) #Tranformar mi valor en entero
print(altura_entera)

decimal = 3.56
print(int(decimal)) #3
#Round: redondear. Al valor entero más cercano
print(round(decimal)) #4
print(round(decimal, 1)) #3.6

pi = 3.14159265359
print(round(pi, 4)) #3.1416

numero_negativo = -10
print(abs(numero_negativo))

numero_alcuadrado = pow(2, 2)
print(numero_alcuadrado)

sumatoria = sum([1, 2, 3]) #Recibe una lista y regresa la sumatoria de esta
print(sumatoria)

numero_maximo = max(2, 3, 1) #Recibe n cantidad de números y regresa el mayor
print(numero_maximo)

numero_minimo = min(2, 3, 1) #Recibe n cantidad de números y regresa el menor
print(numero_minimo)

num_aleatorio = random.randint(5, 10) #Número entero aleatorio entre 5 y 10
decimal_aleatorio = random.uniform(-10, 10) #Número decimal aleatorio entre -10 y 10
print(num_aleatorio)
print(decimal_aleatorio)

'''
Genera 5 números enteros aleatorios enteros entre 10 y 10,000 usando la librería random.
Para cada número:
Muestra su valor y su tipo de dato usando la función type().
Muestra cuántos dígitos tiene utilizando len().*
Muestra el resultado con un mensaje descriptivo.
'''
num1 = random.randint(10,10000)
num2 = random.randint(10,10000)
num3 = random.randint(10,10000)
num4 = random.randint(10,10000)
num5 = random.randint(10,10000)

print(f"El valor es:{num1}, su tipo es:{type(num1)}, y la cantidad de digitos es: {len(str(num1))}")
print(f"El valor es:{num2}, su tipo es:{type(num2)}, y la cantidad de digitos es: {len(str(num2))}")
print(f"El valor es:{num3}, su tipo es:{type(num3)}, y la cantidad de digitos es: {len(str(num3))}")
print(f"El valor es:{num4}, su tipo es:{type(num4)}, y la cantidad de digitos es: {len(str(num4))}")
print(f"El valor es:{num5}, su tipo es:{type(num5)}, y la cantidad de digitos es: {len(str(num5))}")


'''
Genera 3 números aleatorios con decimales entre -100 y 100 usando random.uniform().
Para cada número realiza lo siguiente:
Muestra su valor original y su tipo de dato (type()).
Muestra su valor absoluto usando abs().
Redondea el número a 2 decimales con round().
Convierte el número redondeado a entero usando int().
¿Qué diferencia hay entre round() e int()?
'''

num1 = random.uniform(-100, 100)
num2 = random.uniform(-100, 100)
num3 = random.uniform(-100, 100)

print(f"El valor es:{num1}, su tipo es:{type(num1)}, el absoluto es: {abs(num1)}, redondeado es: {round(num1, 2)} usando int: {int(num1)}")
print(f"El valor es:{num2}, su tipo es:{type(num2)}, el absoluto es: {abs(num2)}, redondeado es: {round(num2, 2)} usando int: {int(num2)}")
print(f"El valor es:{num3}, su tipo es:{type(num3)}, el absoluto es: {abs(num3)}, redondeado es: {round(num3, 2)} usando int: {int(num3)}")

'''
Pide al usuario que ingrese dos números (enteros o decimales).
Para cada número, calcula y muestra:
La raíz cuadrada (de su valor absoluto).
Su valor elevado a la tercera potencia.
Su valor absoluto.
El redondeo hacia arriba (ceil) y hacia abajo (floor).
Luego, muestra las operaciones entre ambos números:
Suma, resta, multiplicación y división.
Máximo y mínimo de los dos números.
Potencia del primer número elevado al segundo (math.pow()).
'''
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

print("--Para el primer número--")
print(f"La raíz cuadrada (de su valor absoluto): {math.sqrt(abs(numero1))}")
print(f"Su valor elevado a la tercera potencia: {math.pow(numero1, 3)}")
print(f"Su valor absoluto: {math.fabs(numero1)}")
print(f"Redondeo hacia arriba: {math.ceil(numero1)}, Redondeo hacia abajo: {math.floor(numero1)}")

print("--Para el segundo número--")
print(f"La raíz cuadrada (de su valor absoluto): {math.sqrt(abs(numero2))}")
print(f"Su valor elevado a la tercera potencia: {math.pow(numero2, 3)}")
print(f"Su valor absoluto: {math.fabs(numero2)}")
print(f"Redondeo hacia arriba: {math.ceil(numero2)}, Redondeo hacia abajo: {math.floor(numero2)}")

print(f"Suma de ambos números: {numero1 + numero2}")
print(f"Resta de ambos números: {numero1 - numero2}")
print(f"Multiplicación de ambos números: {numero1 * numero2}")

if numero2 != 0:
    print(f"División de ambos números: {numero1 / numero2}")
else:
    print("No puedo hacer la división.")

print(f"El número máximo es: {max(numero1, numero2)}")
print(f"El número minimo es: {min(numero1, numero2)}")
print(f"Num1 elevado a la potencia de Num2 es: {math.pow(numero1, int(numero2))}")