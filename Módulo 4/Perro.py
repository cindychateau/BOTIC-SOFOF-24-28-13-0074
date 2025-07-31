from Animal import Animal
class Perro(Animal):

    def __init__(self, nombre, edad, raza, pelaje, sonido):
        super().__init__(nombre, "Perro", edad)
        self.raza = raza
        self.pelaje = pelaje
        self.sonido = sonido
    
    def olfatear(self, cosa):
        print(f"{self.nombre} está olfateando {cosa}")
        return self
    
    def mover_colita(self):
        print(f"{self.nombre} está moviendo su colita, está feliz!")
        self.presentarse()
        #super().presentarse()
        return self