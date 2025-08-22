from src.juego import dado
from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        pass

    def almacenar_dados(self):
        almacen = []

        for i in range(5):
            almacen.append(Dado())

        return almacen
