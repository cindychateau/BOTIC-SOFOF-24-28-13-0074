class TarjetaCredito:

   #Incluye en este método valores por default
   def __init__(self, saldo_pagar=0, limite_credito=10000, intereses=.02):
       self.saldo_pagar = saldo_pagar
       self.limite_credito = limite_credito
       self.intereses = intereses

   def compra(self, monto):
       #TU CODIGO: aumenta el saldo_pagar. Siempre y cuando no haya llegado al limite_credito
        pass
  

   def pago(self, monto):
       #TU CODIGO: disminuye el saldo_pagar
        pass
  

   def mostrar_info_tarjeta(self):
       #TU CODIGO: imprimir en consola el saldo
        pass
  

   def cobrar_interes(self):
       #TU CODIGO: saldo_pagar = saldo_pagar*intereses
       pass