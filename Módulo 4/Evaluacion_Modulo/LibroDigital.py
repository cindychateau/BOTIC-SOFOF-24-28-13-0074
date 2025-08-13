from Libro import Libro

class LibroDigital(Libro):

    def __init__(self, titulo, autor, anio, estado, formato):
        super().__init__(titulo,autor,anio,estado)
        self.formato = formato