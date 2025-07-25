class CPU:
    def especificaciones(self):
        return "Procesador Intel i7"


class Computadora:
    def __init__(self):
        self.cpu = CPU() #Composición: mi computadora TIENE el cpu
    
    def mostrar_informacion(self):
        return f"Computadora con especs: {self.cpu.especificaciones()}"

mi_pc = Computadora()
print(mi_pc.mostrar_informacion())    