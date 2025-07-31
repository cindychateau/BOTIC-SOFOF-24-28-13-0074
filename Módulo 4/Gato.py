#class Hijo(Padre):
from Animal import Animal
class Gato(Animal):

    def __init__(self, nombre, edad, sonido, raza, tipo_pelaje, color):
        super().__init__(nombre, "Gato", edad)
        self.sonido = sonido
        self.raza = raza
        self.tipo_pelaje = tipo_pelaje
        self.color = color
    
    def razcar_sofa(self):
        print(f"{self.nombre} está razcando el sofá de su casa")