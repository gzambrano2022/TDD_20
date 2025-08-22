from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dado = Dado()
        self.almacen = []

    def almacenar_dados(self, cantidad = 5):
        for i in range(cantidad):
            self.almacen.append(self.dado.generar_valor())
        return self.almacen

    def agitar_dados(self):
        for i in range(len(self.almacen)):
            self.almacen[i] = self.dado.generar_valor()
        return self.almacen

    def perder_dado(self):
        self.almacen.pop()
        return self.almacen
