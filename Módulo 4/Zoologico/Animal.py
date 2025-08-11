class Animal:

    def __init__(self, name, age, food):
        #self = animal1
        #name = "Pedro", age = 5, food = "croquetas"
        self.nombre = name #animal1.nombre = "Pedro"
        self.edad = age #animal1.edad = 5
        self.comida_favorita = food #animal1.comida_favorita = "croquetas"
    
    #Método Abstracto -> No tiene una definición. Se debe de implementar en la clase hija
    def hacer_sonido(self):
        raise NotImplementedError 