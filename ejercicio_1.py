import random

class dado():
    def __init__(self,cantidad_caras):
        self.cantidad_caras = cantidad_caras

    def tirar(self):
        caras = random.randint(1,self.cantidad_caras)
        print("Salio", caras)
        return caras
    def varios_dados(self,cantidad_dados):
        tiradas = 0
        for i in range(0,cantidad_dados):
            print("\nsalio",random.randint(1, self.cantidad_caras))
            tiradas += 1

dado1 = dado(8)
# dado1.tirar()
dado1.varios_dados(3)
