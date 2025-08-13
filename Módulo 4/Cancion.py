class Cancion:

    def __init__(self, titulo, artista, duracion_seg, album):
        self.titulo = titulo
        self.artista = artista
        self.__duracion_seg = duracion_seg #ofuscación de nombres -> se vuelve más difícil acceder a esta información fuera de clase
        self.__album = album
    
    #Getter -> Obtiene el valor de un atributo
    def get_duracion(self): #self = cancion1
        return self.__duracion_seg #return 150
    
    #Setter -> Cambiar el valor de un atributo
    def set_duracion(self, nuevo_valor):
        self.__duracion_seg = nuevo_valor
    

    #def get_album(), def set_album()
    def __str__(self):
        return f"{self.titulo}({self.artista}):{self.__duracion_seg}"