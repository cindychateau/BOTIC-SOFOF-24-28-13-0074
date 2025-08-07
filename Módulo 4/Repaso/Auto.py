from Vehiculo import Vehiculo
class Auto(Vehiculo):

    def __init__(self, marca, modelo, anio, patente, puertas):
        super().__init__(marca, modelo, anio, 4)
        self.patente = patente
        self.puertas = puertas