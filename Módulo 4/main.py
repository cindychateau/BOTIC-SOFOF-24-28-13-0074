from Animal import Animal #from Archivo import Clase

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