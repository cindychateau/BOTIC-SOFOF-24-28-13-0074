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
