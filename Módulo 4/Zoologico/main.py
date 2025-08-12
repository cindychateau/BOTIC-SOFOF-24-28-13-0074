from Animal import Animal
from Subclases import Leon, Chimpance, Elefante, Pudu
#from Subclases import *
from funciones import *

simba = Leon("Simba", 2, "carne")
jorge_curioso = Chimpance("Jorge", 1, "bananas")
nala = Leon("Nala", 2, "carne")
dumbo = Elefante("Dumbo", 1, "cacahuates")
bambi = Pudu("Bambi", 3, "hojas")
pudin = Pudu("Pudin", 2, "hojas")
fresia = Elefante("Fresia", 51, "cacahuates")

#print(f"El animalito: {fresia.nombre} está haciendo el sonido {fresia.hacer_sonido()}")

animales_nuevos = [
    simba,
    jorge_curioso,
    nala,
    dumbo,
    bambi,
    pudin,
    fresia
]

#print(f"{simba.__class__.__name__}") -> obtiene el nombre de la clase de un objeto

# for animal in animales_nuevos:
#     guardar_animal(animal)

#print("Animales guardados correctamente en el archivo")

animales = cargar_animales()
for a in animales:
    print(f"{a.nombre} ({a.__class__.__name__}, {a.edad} años) - {a.hacer_sonido()} - Come {a.comida_favorita}")