import random
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

'''
Genera 3 números aleatorios con decimales entre -100 y 100 usando random.uniform().
Para cada número realiza lo siguiente:
Muestra su valor original y su tipo de dato (type()).
Muestra su valor absoluto usando abs().
Redondea el número a 2 decimales con round().
Convierte el número redondeado a entero usando int().
¿Qué diferencia hay entre round() e int()?
'''