class LibroNoEncontrado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

'''
SINTAXIS:
try: 
    #Bloque de código que quiero tratar de realizar

except Error: # en otros lenguajes de programación es el equivalente a catch
    #Bloque de código que quiero que se ejecute si ocurre la excepción
'''
try:
    x = 10
    y = 0
    resultado = x / y
except ZeroDivisionError: #Error que aparece al intentar dividir entre 0
    print("No podemos dividir entre cero")

#ValueError
try:
    edad = int("treinta") #Intentando forzar a un texto sea numeral
except ValueError:
    print("Favor de dar la edad en numeral")

try:
    texto = "Hola como estás?"
    numero = 22
    frase_completa = texto + numero
except TypeError:
    print("Tipos de datos distintos.")

try:
    frutas = ["frutilla", "manzanas", "platano"]
    print(frutas[5])
except IndexError:
    print("El indice no existe")

try:
    estudiante = {
        "nombre": "Pedro",
        "apellido": "Páramo"
    }
    print(estudiante["email"])
except KeyError:
    print("La clave no existe")

def dividir():
    try:
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        division = num1 / num2
        print(f"El resultado es: {division}")
    #ZeroDivision
    except ZeroDivisionError: #if tratan de dividir entre cero
        print("No podemos dividir entre cero")
    #ValueError
    except ValueError: #if tratan de poner valores distintos a enteros
        print("Solo se permiten números enteros")
    #TypeError
    except TypeError: #if no colocan el type correcto
        print("Error de tipeo")
    #Excepcion
    except Exception as e: #Atrapar errores de manera general. else haz lo siguiente
        print(f"Ocurrió un error inesperado {e}") #type(e) me da el tipo de error
    finally: #Se ejecuta SIEMPRE sin importar si hubo excepción o no
        print("¡Gracias por usar la calculadora, nos vemos pronto!") #Cerrar conexiones/archivos, liberar recursos, mensajes de cierre, etc.

dividir()

try:
    bebidas = ["cafe con leche", "chocolate", "te"]
    bebida_deseada = input("Ingrese la bebida que quiere: ")
    if bebida_deseada not in bebidas:
        raise ValueError(f"Esa bebida no está disponible") #raise -> lanzar explícitamente un excepción
    else:
        print(f"Tu bebida {bebida_deseada} está lista.")
except ValueError as e:
    print(f"Error: {e}")

try:
    palabra = input("Dinos una palabra: ")
    if palabra == "alto":
        raise ErrorEspecial("Este es el error especial que creamos")
    else:
        print(palabra)
except ErrorEspecial as e:
    print(f"Se ha capturado el error: {e}")


#Vas a crear un programa que registre usuarios para un sistema, donde se solicitan varios datos personales. Los datos deben ser validados estrictamente y, si hay algún error, el programa debe lanzar y manejar excepciones específicas. *Nombre: Debe contener solo letras y espacios, Si el nombre está vacío o contiene números o símbolos, lanzar ValueError con mensaje específico. *Edad:Debe ser un número entero entre 18 y 120.Si no es un número, lanzar TypeError.Si está fuera del rango, lanzar ValueError. *Correo electrónico: Debe contener un "@" y un "."Si no cumple, lanzar una excepción. *Contraseña: Debe tener al menos 8 caracteres, incluir al menos una mayúscula, una minúscula, un número y un símbolo especial. Si no cumple, lanzar una excepcion. * Teléfono: debe ser un número de 10 dígitos. Si ingresa algo diferente, lanzar ValueError.
#BONUS: excepcion personalizada InvalidEmailError. excepción personalizada WeakPasswordError. Al final, mostrar un resumen con todos los datos válidos ingresados. permita al usuario intentar de nuevo.