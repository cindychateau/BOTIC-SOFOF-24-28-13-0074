from Animal import Animal
from Subclases import Leon, Chimpance, Elefante, Pudu
#from Subclases import *

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

for animal in animales_nuevos:
    guardar_animal(animal)

print("Animales guardados correctamente en el archivo")
