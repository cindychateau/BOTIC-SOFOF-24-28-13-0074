class Motor: #Clase
    def encender(self):
        return "Motor encendido"


class Auto:
    def __init__(self):
        self.motor = Motor() #Colaboración: Auto depende de Motor
        #atributo de Auto llamado motor
    
    def arrancar(self):
        return self.motor.encender() #Invocando al método para encender el Motor


mi_auto = Auto()
print(mi_auto.arrancar())