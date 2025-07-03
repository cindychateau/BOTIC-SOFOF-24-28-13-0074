import random #Importa un módulo: random

print('¡Bienvenido a Python!') #Imprimiendo '¡Bienvenido a Python!'

print('Este es un bucle que imprime 10 veces')
for num in range(1, 11): #Bucle empezando 1 - 11 (no me incluye el 11) # i < 11
    print(f'num es: {num}')

semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
dia = random.choice(semana)

print(f'Hoy es: {dia}')

if dia == 'Lunes':
    print('¡Comenzamos la semana con toda la actitud!')
elif(dia == 'Viernes'):
    print('¡Listos para un fin de semana!')
else:
    print('¿Qué día es?')