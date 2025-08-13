from Cancion import Cancion

cancion1 = Cancion("APT", "Bruno Mars", 150, "Album prueba")

#print(cancion1.__duracion_seg) #-> ERROR
print(cancion1.get_duracion()) #print(150)

cancion1.set_duracion(200)
print(cancion1.get_duracion())
print(cancion1)