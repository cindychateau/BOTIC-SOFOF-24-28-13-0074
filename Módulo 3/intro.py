#Para ejecutar en Mac: python3 nombre_archivo.py
#Para ejecutar en Windows: python nombre_archivo.py
print("Hola mundo!")

'''
Un comentario es una anotación
para los desarrolladores
y no afecta el funcionamiento
de mi código fuente
'''

variable1 = 1
variable1 = "uno" #"Sobrescribiendo" la variable, estoy cambiando el tipo de dato de esta
print(variable1)

print(type(variable1)) #str

#Casteo: el cambiar de tipo de dato
x = str(3) #"3" como texto
print(x)
x = int(3.3) # convierte en número entero el valor que tengo ()
print(x)
x = float(3) # 3.0
print(x)

numero = 74
print("El mejor grupo es el:" + str(numero))

texto = "Puede tener comillas dobles"
otro_texto = 'o comillas simples'

mivariable = "Elena de Troya 1"
mi_variable = "Elena de Troya"
_mivariable = "Elena de Troya"
miVariable = "Elena de Troya 2"
MIVARIABLE = "Elena de Troya 3"
mi_variable2 = "Elena de Troya"
_mi_variable_2 = "Elena de Troya"

print(mivariable)
print(miVariable)
print(MIVARIABLE)

'''
Nombres inválidos:
2miVarible
mi!variable
mi-variable
mi variable
'''

hobby1, hobby2, hobby3 = "Leer", "Dormir", "Comer"
'''
hobby1 = "Leer"
hobby2 = "Dormir"
hobby3 = "Comer"
'''
print(hobby1, hobby2, hobby3)

instructora_fav1 = instructora_fav2 = instructora_fav3 = "Cynthia Castillo"
print(instructora_fav1, instructora_fav2, instructora_fav3)
'''
instructora_fav1 = "Cynthia Castillo"
instructora_fav2 = "Cynthia Castillo"
instructora_fav3 = "Cynthia Castillo"
'''

celebridades = ["Pedro Pascal", "Kanye West", "Brad Pitt"]
a, b, c = celebridades
print(a, b, c)

nombre = input("Ingresa tu nombre completo:")
print("El nombre que ingresaste fue:", nombre)