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
    
    #Sobreescritura/Anulación
    def presentarse(self):
        print(f"*El gato te ve, te analiza, te ignora por un momento*")
        print(f"Hola, no te había visto ahí: me llamo {self.nombre}, soy un {self.tipo}, y mi raza es la dueña del universo.")
        #super().presentarse()
        return self
    
    def ir_al_baño(self):
        print("Va a su caja, razca la arena y va al baño")