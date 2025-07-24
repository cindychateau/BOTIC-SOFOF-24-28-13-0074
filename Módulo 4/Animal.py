#Para declarar la clase usamos la palabra reservada class. El nombre de mi clase debe ser en singular y con PascalCase
class Animal:

    #Función Constructor: Inicializa/crea el objeto.
    #Se ejecuta de manera automática cuando creo el objeto
    #self = Representa el objeto mismo que se está inicializando
    def __init__(self, nombre, tipo, edad=1, sonido="guau"):
        #self = firulais
        #nombre = "Firulais"
        #tipo = "Perro"
        #edad = 1
        #Todos los atributos con los que voy a crear el objeto
        self.nombre = nombre #firulais.nombre = "Firulais"
        self.tipo = tipo #firulais.tipo = "Perro"
        self.edad = edad #firulais.edad = 1
        self.mamifero = True