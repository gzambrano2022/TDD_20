import random

class Dado:
    """
    Clase que representa un dado de 6 caras con designaciones especiales.

    Atributos:
        designaciones: Diccionario que mapea valores numéricos a nombres.
    """
    def __init__(self):
        self.designaciones ={
            1: "As",
            2: "Tonto",
            3: "Tren",
            4: "Cuadra",
            5: "Quina",
            6: "Sexto"}

    def generar_valor(self):
        """
        Genera un valor aleatorio entre 1 y 6.
        """
        return random.randint(1,6)

    def designacion(self, valor):
        """
        Obtiene la designación (nombre) correspondiente a un valor numérico.
        """
        return self.designaciones[valor]



