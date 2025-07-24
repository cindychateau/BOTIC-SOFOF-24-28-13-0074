from Animal import Animal #from Archivo import Clase

firulais = Animal("Firulais", "Perro")
miu = Animal("Miusita", "Gato", 7, "meow")

print(firulais.nombre)
print(miu.nombre)

miu.nombre = "Miu"
print(miu.nombre)

miu.mamifero = False