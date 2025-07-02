import random #Importación de la librería random
import modulo
import paquetes.saludos
from paquetes.matematicas import suma, resta

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)

modulo.hola()
paquetes.saludos.saludar("Elena de Troya")
print(type(suma(5,3)))
print("¿Cuánto es 5+3?", suma(5,3))
print("¿Cuánto es 5-3?", resta(5,3))