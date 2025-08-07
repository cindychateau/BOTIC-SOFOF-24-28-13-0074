from Vehiculo import Vehiculo
from Auto import Auto

vehiculo1 = Vehiculo("Ferrari", "Testarossa", 2025, 4) #Crea objeto
print(f"El modelo del vehiculo 1 es {vehiculo1.modelo}")
#Vehiculo.total_vehiculos = 1

vehiculo2 = Vehiculo("Yamaha", "M1", 2018, 0)
print(f"La marca del vehiculo 2 es {vehiculo2.marca}")
#Vehiculo.total_vehiculos = 2

vehiculo2.mostrar_vehiculo()

Vehiculo.cantidad_de_vehiculos()

auto1 = Auto("Suzuki", "Spresso", 2020, "ABC123", 4)
auto1.mostrar_vehiculo()