#r = leer, w = sobreescribir, a = editar (add)
try:
    recetario = open("recetario.txt", "w", encoding= "utf-8") #w -> crea el archivo si no existe, y si existe sobre escribe el contenido
    recetario.write("Empanada de Pino \n") #\n un salto de línea
    recetario.write("Pastel de Choclo \n")
except FileNotFoundError: #El archivo no se encuentra/no existe 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r") #permisos de lectura
    contenido = recetario.read() #read -> lee todo el contenido
    print("Recetario actual: \n", contenido)
except FileNotFoundError: #El archivo no se encuentra/no existe 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r")
    recetas = recetario.readlines() #readlines -> Me regresa el contenido como lista
    #print(recetas)
    print("Receta en indice 1:", recetas[1])
except FileNotFoundError: #El archivo no se encuentra/no existe 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "a") #a -> agregar al final del archivo, respetando el contenido original de este
    recetario.write("Ensalada\n")
    recetario.write("Mote con huesillos\n")
except FileNotFoundError: #El archivo no se encuentra/no existe 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r+") #r+ -> permite leer y escribir
    contenido_existente = recetario.read()
    recetario.seek(0) #seek-> posiciona en el caracter indicado
    recetario.write("MI RECETARIO \n" + contenido_existente)
except FileNotFoundError: #El archivo no se encuentra/no existe 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()

try:
    recetario = open("recetario.txt", "r")
    lineas = recetario.readlines() #Regresa el contenido como si fuera una lista
    '''
    lineas = [
        "Empanada",
        "Pastel",
        "Ensalada",
        "Mote"
    ]
    '''
    print("Lista de recetas: \n")
    for linea in lineas:
        print("Receta: ", linea)
except FileNotFoundError: #El archivo no se encuentra/no existe 
    print("El archivo no se encuentra")
except IOError:
    print("No se pudo leer/modificar el archivo")
finally:
    recetario.close()