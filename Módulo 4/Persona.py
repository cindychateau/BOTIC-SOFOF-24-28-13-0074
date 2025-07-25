class Persona:

    def __init__(self, nombre, mascota=""):
        self.nombre = nombre
        self.mascota =  mascota #Objeto de Animal
    
    def jugar_con_mascota(self, horas): #self = elena, horas = 2
        print(f"{self.nombre} está jugando con {self.mascota.nombre}")
        self.mascota.jugar(horas) #elena.miu.jugar(2)