from pprint import pprint
eventos = [] #Originalmente tenemos una lista vacía de eventos
usuarios = []
equipos = []

def menu():
    flag = True
    contador = 0
    while flag:
        print("Selecciona la acción que quieres realizar:")
        print("1.- Crear evento")
        print("2.- Crear usuario")
        print("3.- Crear equipo")
        print("4.- Inscribir usuario a evento")
        print("5.- Asignar usuario a equipo")
        print("6.- Consultar eventos por estado")
        print("7.- Salir")
        opcion = input("Ingresa la opción: ")

        if opcion == "1":
            print("CREAR EVENTO")
            nombre = input("Ingresa el nombre del nuevo evento: ")
            tipo = input("Ingresa el tipo del nuevo evento: ")
            fecha = input("Ingresa la fecha del nuevo evento: ")
            #estado = input("Ingresa el estado del nuevo evento: ")
            evento = {
                "nombre": nombre,
                "tipo": tipo,
                "fecha": fecha,
                "estado": "Programado",
                "usuarios": []
            }
            eventos.append(evento)

        elif opcion == "2":
            print("CREAR USUARIO")
        elif opcion == "3":
            print("CREAR EQUIPO")
        elif opcion == "4":
            print("INSCRIBIR USUARIO A EVENTO")
        elif opcion == "5":
            print("ASIGNAR USUARIO A EQUIPO")
        elif opcion == "6":
            print("CONSULTAR EVENTOS POR ESTADO")
        elif opcion == "7":
            print("SALIR")
            flag = False
        else:
            print("OPCION INVALIDA")
        contador += 1
    print(f"Se ingresó al menú {contador} veces")
    pprint(eventos)
menu()