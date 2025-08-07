class Vehiculo:

    total_vehiculos = 0 #Atributo de clase

    def __init__(self, marca, modelo, anio, ruedas):
        #self = vehiculo2
        #marca = "Yamaha"
        #modelo =  "M1"
        #anio = 2018
        #ruedas = 0
        self.marca = marca #vehiculo2.marca = "Yamaha"
        self.modelo = modelo #vehiculo2.modelo = "M1"
        self.anio = anio #vehiculo2.anio = 2018
        self.ruedas = ruedas #vehiculo2.ruedas = 0
        Vehiculo.total_vehiculos += 1 #Aumentando la cantidad del total_vehiculos
        self.antiguedad = Vehiculo.calcula_antiguedad(anio)
    
    def mostrar_vehiculo(self): #self = vehiculo2
        #vehiculo2.marca vehiculo2.modelo (vehiculo2.anio)
        #Yamaha M1 (2018)
        print(f"{self.marca} {self.modelo} ({self.anio})")
    
    @classmethod
    def cantidad_de_vehiculos(cls): #Vehiculo
        #Vehiculos creados: Vehiculo.total_vehiculos
        #Vehiculos creados: 2
        print(f"Vehiculos creados: {cls.total_vehiculos}")
    
    @staticmethod
    def calcula_antiguedad(anio):
        return 2025 - anio