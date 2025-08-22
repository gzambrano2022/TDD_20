from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dado = Dado()

    def almacenar_dados(self):
        almacen = []

        for i in range(5):
            almacen.append(self.dado.generar_valor())

        return almacen
