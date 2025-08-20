import random

class Dado:
    def __init__(self):
        self.designaciones ={
            1: "As",
            2: "Tonto",
            3: "Tren",
            4: "Cuadra",
            5: "Quina",
            6: "Sexto"}

    def generar_valor(self):
        return random.randint(1,6)

    def designacion(self, valor):
        return self.designaciones[valor]



