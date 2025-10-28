nueva_lista = [x*2 for x in range(4)] #[0, 1, 2, 3]

#x = 0 x*2 = 0
#x = 1 x*2 = 2
#x = 2 2*2 = 4
#x = 3 3*2 = 6

#nueva_lista = [0, 2, 4, 6]

class Circulo:

    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return (self.radio**2)*3.14 #import math math.pi