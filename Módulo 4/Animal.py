#Para declarar la clase usamos la palabra reservada class. El nombre de mi clase debe ser en singular y con PascalCase
class Animal:

    nombre_veterinaria = "Dogtor" #Atributo de Clase
    lista_animalitos = [] #[firulias, miu, Garfield, Oddie]

    #Función Constructor: Inicializa/crea el objeto.
    #Se ejecuta de manera automática cuando creo el objeto
    #self = Representa el objeto mismo que se está inicializando
    def __init__(self, nombre, tipo, edad=1):
        #self = firulais
        #nombre = "Firulais"
        #tipo = "Perro"
        #edad = 1
        #Todos los atributos con los que voy a crear el objeto
        self.nombre = nombre #firulais.nombre = "Firulais"
        self.tipo = tipo #firulais.tipo = "Perro"
        self.edad = edad #firulais.edad = 1
        self.mamifero = True
        self.energia = 100
        self.felicidad = 100
        Animal.lista_animalitos.append(self)
    
    #Método: función/acción que mi objeto puede realizar e invocar
    def presentarse(self): #self = miu
        #¡Hola yo soy Miu, un Gato, y tengo 7 año(s)!
        print(f"¡Hola yo soy {self.nombre}, un {self.tipo}, y tengo {self.edad} año(s)!")
        print(f"Calidad de vida de animalito: {Animal.calidad_de_vida(self.energia, self.felicidad)}")
        return self #Permite encadenamiento de métodos
    
    def comer(self, comida): #self = miu, comida = "croquetas"
        #self.energia += 5 #miu.energia = 100 + 5 = 105
        self.energia = Animal.calcula_energia(self.energia, 5)
        self.felicidad += 5 #miu.felicidad = 100 + 5 = 105
        print(f"{self.nombre} está comiendo {comida}")
        return self
    
    def jugar(self, horas): #self = firulais, horas = 5
        #Firulais estuvo jugando por 5 horas
        print(f"{self.nombre} estuvo jugando por {horas} horas")
        #self.energia -= (horas * .5) #firulais.energia = 100 - (5*.5) = 97.5
        self.energia = Animal.calcula_energia(self.energia, -(horas*.5))
        self.felicidad += (horas * .5) #firulais.felicidad = 100 + (5 * .5) = 102.5
        return self
    
    def dormir(self, horas): #self = miu, horas = 2
        if horas < 2:
            #self.energia += 1
            self.energia = Animal.calcula_energia(self.energia, 1)
        elif horas < 5:
            #self.energia += 15
            self.energia = Animal.calcula_energia(self.energia, 15)
        else:
            self.energia = 100
        print(f"{self.nombre} durmió {horas} horas")
        return self
    
    #Método de clase es algo PROPIO de la clase, es decir que NO tiene acceso a la información de un objeto específico
    @classmethod
    def muestra_animalitos(cls): #cls = Animal
        #Animal.lista_animalitos = [firulais, miu]
        for mascota in cls.lista_animalitos: 
            #animal = miu
            print(f"Nombre: {mascota.nombre}. Tipo: {mascota.tipo}. Edad: {mascota.edad}")

    #Método estático: acción/función que debo realizar para la clase SIN EMBARGO no pertenece ni mi instancia ni a mi clase. Objetivo de ayudar y organizar mi código
    @staticmethod
    def calcula_energia(energia_actual, cambio_energia): 
        suma = energia_actual + cambio_energia
        if suma <= 100:
            return suma
        else: 
            return 100

    @staticmethod
    def calidad_de_vida(energia, felicidad):
        if energia >= 70 and felicidad >= 70:
            return "BUENA"
        else:
            return "MEDIA"