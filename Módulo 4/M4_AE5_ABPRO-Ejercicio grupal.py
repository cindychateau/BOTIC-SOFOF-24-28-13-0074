# Ejercicio BIKECITY - Instrucciones paso a paso
# 1. Crear excepciones personalizadas:
#    - BikeUnavailableError: se lanza si se intenta reservar una bicicleta que ya está ocupada.
#    - InvalidReservationError: se lanza si la fecha de inicio es mayor o igual que la de fin o la duración es inválida.
#
# 2. Definir la clase Bike:
#    - Atributos: modelo (texto) y estado ("disponible" o "ocupado").
#    - Método cambiar_estado(nuevo_estado): valida que el estado sea "disponible" u "ocupado" y lo asigna.
#       *Excepción 
#
# 3. Definir la clase Reservation:
#    -Atributos: bike, cliente, inicio, fin, duracion, precio, estado
#    - Definir una tarifa por hora fija (por ejemplo, 10 unidades). -> atributo de clase tarifa_por_hora = 10
#    - El constructor recibe: bike (objeto Bike), cliente (texto), inicio (datetime), fin (datetime).
#    - Validaciones al crear: **datetime hay que importarlo
#        * Si inicio >= fin: lanzar InvalidReservationError con mensaje claro.
#        * Si bike.estado != "disponible": lanzar BikeUnavailableError.
#    - Calcular la duración en horas y el precio (hint: puedes usar un método estático!)
#    - Cambiar el estado de la bicicleta a "ocupado".
#    - Guardar el estado de la reserva como "activa".
#
# 4. Agregar método finalizar() en Reservation:
#    - Cambia el estado de la reserva a "completada".
#    - Cambia el estado de la bicicleta a "disponible".
#    - Muestra (print) el total cobrado al cliente.
#
# 5. En la parte de ejecución principal (main):
#    a. Crear una bicicleta nueva e imprimirla.
#    b. Crear una reserva válida dentro de un bloque try/except/finally:
#         - Atrapar BikeUnavailableError e InvalidReservationError y mostrar el error.
#         - En finally, imprimir que se intentó la reserva.
#    c. Intentar reservar la misma bicicleta de nuevo (debe fallar con BikeUnavailableError).
#    d. Intentar crear una reserva con fechas inválidas (fin antes de inicio) para provocar InvalidReservationError.
#    e. Finalizar la reserva original y mostrar que la bicicleta vuelve a estar disponible.
#    f. Crear otra reserva ahora que la bicicleta está libre y mostrarla.
#
# 6. En cada operación importante (crear reserva, intentar reserva fallida, finalizar) usar:
#    - try/except para manejar errores esperados.
#    - finally para imprimir un mensaje tipo "Intento completado" (simula un log sencillo).
#
# 7. Al final, imprimir el estado final de la bicicleta y de la(s) reserva(s) para verificar lo sucedido.
#
# 8. Requisitos claros para el estudiante:
#    - Usar clases, excepciones, validaciones, operaciones con fechas y redondeo.
#    - No usar identificadores complejos: trabajar con el objeto Bike directamente.
#    - Mantener el programa sencillo y legible.
#
# 9. Casos mínimos que deben mostrarse al ejecutar:
#    - Reserva válida y correcta.
#    - Error al reservar una bicicleta ya ocupada.
#    - Error por fechas inválidas.
#    - Finalización de reserva y reutilización de la bicicleta.
from datetime import datetime, timedelta
import math

# --- Excepciones personalizadas ---
class BikeUnavailableError(Exception):
    pass

class InvalidReservationError(Exception):
    pass

# --- Clase Bike ---
class Bike:
    def __init__(self, modelo):
        self.modelo = modelo
        self.estado = "disponible"

    def cambiar_estado(self, nuevo_estado: str):
        if nuevo_estado not in ("disponible", "ocupado"):
            raise ValueError(f"Estado inválido: {nuevo_estado}")
        self.estado = nuevo_estado
    
    def __str__(self): #Transforma el objeto en texto cuando se necesite imprimir
        return f"Bike modelo={self.modelo} estado={self.estado}"

class Reservation:
    TARIFA_POR_HORA = 10

    def __init__(self, bike: Bike, cliente: str, inicio: datetime, fin: datetime):
        # Validaciones
        if inicio >= fin:
            raise InvalidReservationError("La fecha de inicio debe ser anterior a la de fin.")

        if bike.estado != "disponible":
            raise BikeUnavailableError(f"La bicicleta '{bike.modelo}' no está disponible.")

        self.bike = bike
        self.cliente = cliente
        self.inicio = inicio
        self.fin = fin
        self.duracion = self.calcular_duracion_en_horas(inicio, fin)
        self.precio = self.calcular_precio(self.duracion, Reservation.TARIFA_POR_HORA)
        self.estado = "activa"  # puede ser "activa" o "completada"

        # Al hacer la reserva, se ocupa la bicicleta
        self.bike.cambiar_estado("ocupado")

    @staticmethod
    def calcular_duracion_en_horas(inicio, fin):
        delta = fin - inicio
        horas = delta.total_seconds() / 3600
        return horas

    @staticmethod
    def calcular_precio(horas, tarifa):
        if horas <= 0:
            raise InvalidReservationError("Duración inválida para calcular precio.")
        horas_cobradas = math.ceil(horas)  # cobra por fracción hacia arriba
        return horas_cobradas * tarifa

    def finalizar(self):
        if self.estado != "activa":
            print("La reserva ya fue finalizada.")
            return

        self.estado = "completada"
        self.bike.cambiar_estado("disponible")
        print(f"Reserva de {self.cliente} finalizada. Total a cobrar: {self.precio} unidades.")
    
    def __str__(self):
        return (f"Reservation cliente={self.cliente} bike={self.bike.modelo} "
                f"inicio={self.inicio.strftime('%Y-%m-%d %H:%M')} fin={self.fin.strftime('%Y-%m-%d %H:%M')} "
                f"precio={self.precio} estado={self.estado}")

# --- Simulación ---
def main():
    print("=== ¡Bienvenido a BikeCity ===\n")

    # while True:
    #     print("Elige una opcion")
    #     print("1: Crear Bicicleta")
    #     print("2: Crear Reservacion")
    #     print("3: Devolver Bici")
    #     print("4: Salir")
    #     respuesta = input("Escribe lo que quieres hacer: ")
    #     if

    # 1. Crear una bicicleta
    bici = Bike("Urbana 2025")
    print("Bicicleta creada:", bici)

    # 2. Crear una reserva válida
    try:
        inicio = datetime.now()
        fin = inicio + timedelta(hours=1, minutes=30)  # 1.5 horas
        reserva = Reservation(bici, "Luis", inicio, fin)
        print("\nReserva creada correctamente:")
        print(reserva)
    except (BikeUnavailableError, InvalidReservationError) as e:
        print("Error al crear reserva:", e)
    finally:
        print("Intento de reserva 1 completado.\n")

    try:
        inicio2 = datetime.now() + timedelta(minutes=10)
        fin2 = inicio2 + timedelta(hours=1)
        reserva_conflictiva = Reservation(bici, "Ana", inicio2, fin2)
    except BikeUnavailableError as e:
        print("Error esperado al intentar reservar una bicicleta ocupada:", e) 
    except InvalidReservationError as e:
        print("Error de fechas:", e)
    finally:
        print("Intento de reserva 2 completado.\n")
    
    bici2 = Bike("Apache")
    try:
        # fin antes de inicio
        inicio3 = datetime.now() + timedelta(hours=2) #7:34pm
        fin3 = datetime.now() + timedelta(hours=1) #6:34pm
        reserva_invalida = Reservation(bici2, "María", inicio3, fin3)
    except BikeUnavailableError as e:
        print("Error de disponibilidad:", e)
    except InvalidReservationError as e:
        print("Error esperado de fechas inválidas:", e)
    finally:
        print("Intento de reserva 3 completado.\n")

    try:
        reserva.finalizar()
        print("Estado de la bicicleta después de finalizar:", bici)
    except Exception as e:
        print("Error al finalizar:", e)
    finally:
        print("Intento de finalización completado.\n")


main()