from Subclases import Leon, Chimpance, Elefante, Pudu
def guardar_animal(animal):
    try:
        archivo = open("zoo.txt", "a")
        archivo.write(f"{animal.__class__.__name__},{animal.nombre},{animal.edad},{animal.comida_favorita}\n")
    except FileNotFoundError:
        print("Archivo no existe.")
    except IOError:
        print("No se puede leer/escribir el archivo")
    finally:
        archivo.close()
'''
archivo = 'Leon,Alex,10,filete
Leon,Simba,2,carne
Chimpance,Jorge,1,bananas
Leon,Nala,2,carne
Elefante,Dumbo,1,cacahuates
Pudu,Bambi,3,hojas
Pudu,Pudin,2,hojas
Elefante,Fresia,51,cacahuates'

lineas = [
 0   Leon,Alex,10,filete
 1   Leon,Simba,2,carne
 2   Chimpance,Jorge,1,bananas
 3   Leon,Nala,2,carne
 4   Elefante,Dumbo,1,cacahuates
 5   Pudu,Bambi,3,hojas
 6   Pudu,Pudin,2,hojas
 7   Elefante,Fresia,51,cacahuates
]

linea = Leon,Simba,2,carne
datos = [
  0  Leon,
  1  Simba,
  2  2,
  3  carne
]
'''
def cargar_animales():
    animales = []
    try:
        with open("zoo.txt", "r") as archivo:
            lineas = archivo.readlines() #Genera una lista con el contenido
            for linea in lineas:
                datos = linea.strip().split(",")
                clase, nombre, edad, comida = datos
                if clase == "Leon":
                    animal = Leon(nombre, edad, comida)
                elif clase == "Elefante":
                    animal = Elefante(nombre, edad, comida)
                elif clase == "Chimpance":
                    animal = Chimpance(nombre, edad, comida)
                else:
                    animal = Pudu(nombre, edad, comida)
                
                animales.append(animal)
    except FileNotFoundError:
        print("Archivo no existe.")
    except IOError:
        print("No se puede leer/escribir el archivo")

    return animales