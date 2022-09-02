class encriptador():
    encriptar= {
        "a": "0",
        "e": "1",
        "i": "2",
        "o": "3",
        "u": "4",
    }

    def __init__(self,palabras):
        self.palabras= palabras
        self.lista = []
    
    def encriptar(self):
        for letra in self.palabras:
            if letra == "a":
                self.lista.append("0")
            elif letra == "e":
                self.lista.append("1")
            elif letra == "i":
                self.lista.append("2")
            elif letra == "o":
                self.lista.append("3")
            elif letra == "u":
                self.lista.append("4")
            else:
                self.lista.append(letra)
        print(self.lista)

pollo = encriptador("murcielago")
pollo.encriptar()   

