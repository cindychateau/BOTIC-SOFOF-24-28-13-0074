from Animal import Animal #from Archivo import Clase
from Persona import Persona
from Gato import Gato
from Perro import Perro

firulais = Animal("Firulais", "Perro")
miu = Animal("Miusita", "Gato", 7)

print(firulais.nombre)
print(miu.nombre)

miu.nombre = "Miu"
print(miu.nombre)

miu.mamifero = False

firulais.presentarse() #llamando al método
firulais.jugar(5)
print(firulais.energia, firulais.felicidad)

miu.presentarse()
miu.comer("croquetas")
print(miu.energia)
miu.dormir(2)
print(miu.energia)

#Encadenamos los 3 métodos
miu.presentarse().comer("croquetas").dormir(2)

print(Animal.nombre_veterinaria)
Animal.muestra_animalitos()

elena = Persona("Elena de Troya", miu)

elena.jugar_con_mascota(2)


print("-----------------")

garfield = Gato("Garfield", 5, "¡Odio los Lunes!", "atigrado", "corto", "naranja")

garfield.razcar_sofa()
garfield.presentarse()

oddie = Perro("Oddie", 2, "Beagle", "corto", "Woof Woof")
oddie.olfatear("zapatos").mover_colita()

Animal.muestra_animalitos()