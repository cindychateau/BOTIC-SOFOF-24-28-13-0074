'''
=========================================
    Calculadora Pythonirica!
=========================================
Elige una opción:

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números (con validación de 0)
5. Calcular el cuadrado y cubo de un número
6. Contar cuántas letras tiene una palabra
7. Saber si una palabra es corta, media o larga
8. Calcular el promedio de tres números
9. Comparar tres números y decir cuál es el mayor
10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales
11. Salir de la Súper Calculadora

=========================================
Recomendaciones:
-Usar try-except
-Revisar que los números sean válidos para cada acción
-Eliminar espacios y validar que hayan ingresado una palabra en los casos de palabras
-En el promedio, redondear

BONUS:
-Uso de while para mostrar múltiples veces el menú
-Uso de while para pedir los inputs
-Contador general para saber cuántas veces ha usado el menú
-Contador individual para saber cuántas veces ha usado cada opción del menú
-Mostrar los contadores en un mensaje al salir
'''

# print("=========================================")
# print("Calculadora Pythonirica!")
# print("=========================================")
# print("Elige una opción:")
# print("")
# print("1. Sumar dos números")
# print("2. Restar dos números")
# print("3. Multiplicar dos números")
# print("4. Dividir dos números (con validación de 0)")
# print("5. Calcular el cuadrado y cubo de un número")
# print("6. Contar cuántas letras tiene una palabra")
# print("7. Saber si una palabra es corta, media o larga")
# print("8. Calcular el promedio de tres números")
# print("9. Comparar tres números y decir cuál es el mayor")
# print("10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales")
# print("11. Salir de la Súper Calculadora")
print("""=========================================
    Calculadora Pythonirica!
=========================================
Elige una opción:

1. Sumar dos números
2. Restar dos números
3. Multiplicar dos números
4. Dividir dos números (con validación de 0)
5. Calcular el cuadrado y cubo de un número
6. Contar cuántas letras tiene una palabra
7. Saber si una palabra es corta, media o larga
8. Calcular el promedio de tres números
9. Comparar tres números y decir cuál es el mayor
10. Convertir una palabra a MAYÚSCULAS, minúsculas y contar vocales
11. Salir de la Súper Calculadora""")
opcion = input("Elige una opción (1-11)")

if opcion == "1":
    #Sumar
    try:
        #Lo que queremos que se intente hacer
        num1 = float(input("Danos un número: "))
        num2 = float(input("Danos otro número: "))

        suma = num1 + num2
        print("El resultado de la suma es", suma)
    except ValueError:
        #Lo que queremos que se muestre si hay error
        print("ERROR: Ingresaste valores inválidos")

elif opcion == "2":
    #Restar
    try:
        #Lo que queremos que se intente hacer
        num1 = float(input("Danos un número: "))
        num2 = float(input("Danos otro número: "))

        resta = num1 - num2
        print("El resultado de la resta es", resta)
    except ValueError:
        #Lo que queremos que se muestre si hay error
        print("ERROR: Ingresaste valores inválidos")
elif opcion == "3":
    #Multiplicar
    try:
        #Lo que queremos que se intente hacer
        num1 = float(input("Danos un número: "))
        num2 = float(input("Danos otro número: "))

        multiplicacion = num1 * num2
        print("El resultado de la multiplicacion es", multiplicacion)
    except ValueError:
        #Lo que queremos que se muestre si hay error
        print("ERROR: Ingresaste valores inválidos")
elif opcion == "4":
    #Dividir
    try:
        #Lo que queremos que se intente hacer
        num1 = float(input("Danos un número: "))
        num2 = float(input("Danos otro número: "))

        if num2 == 0:
            print("Lo siento, no puedo dividir entre 0")
        else:
            division = num1 / num2
            print("El resultado de la division es", division)
    except ValueError:
        #Lo que queremos que se muestre si hay error
        print("ERROR: Ingresaste valores inválidos")
elif opcion == "5":
    #Cuadrado y cubo
    try:
        num = float(input("Danos un número: "))
        print(f"Cuadrado: {num ** 2}")
        print(f"Cubo: {num ** 3}")
    except ValueError:
        print("ERROR: Ingresaste valores inválidos")
elif opcion == "6":
    #Contar letras
    palabra = input("Escribe una palabra o frase: ").strip()
    if palabra == "":
        print("OYE, no ingresaste nada")
    letras_sin_espacios = palabra.replace(" ", "") #quitamos todos los espacios para tener solo letras
    print(f"La palabra/frase tiene {len(letras_sin_espacios)} letras.")
elif opcion == "7":
    #Corta-Mediana-larga
    palabra = input("Escribe una palabra: ").strip()
    if palabra == "":
        print("OYE, no ingresaste nada")
    longitud = len(palabra)
    if longitud <= 4:
        print("Es una palabra corta")
    elif longitud <= 8:
        print("Es una palabra de longitud media")
    else:
        print("Es una palabra larga")
elif opcion == "8":
    #Promedio
    try:
        num1 = float(input("Dame un número: "))
        num2 = float(input("Dame otro número: "))
        num3 = float(input("Ultimo número: "))
        promedio = (num1 + num2 + num3) / 3
        print(f"El promedio es: {round(promedio, 2)}")
    except ValueError:
        print("ERROR: Ingresaste valores inválidos")
elif opcion == "9":
    #Comparar #
    try:
        num1 = float(input("Dame un número: "))
        num2 = float(input("Dame otro número: "))
        num3 = float(input("Ultimo número: "))
        if num1 == num2 == num3:
            print("Los tres números son iguales.")
        elif num1 >= num2 and num1 >= n3:
            print(f"El mayor es {num1}")
        elif num2 >= num1 and num2 >= num3:
            print(f"El mayor es {num2}")
        else:
            print(f"El mayor es {num3}")
    except ValueError:
        print("ERROR: Ingresaste valores inválidos")
elif opcion == "10":
    #Convertir la palabra
    palabra = input("Escribe una palabra: ").strip()
    if palabra == "":
        print("OYE, no ingresaste nada")
    else:
        mayusculas = palabra.upper()
        minusculas = palabra.lower()
        vocales = sum(1 for c in palabra.lower() if c in "aeiou")
        print(f"En mayúsculas: {mayusculas}")
        print(f"En minúsculas: {minusculas}")
        print(f"Cantidad de vocales: {vocales}")
elif opcion == "11":
    #Salir, mensajito de despedida
    print("¡Adios!")
else:
    print("Opcion inválida")

