from src.juego.dado import Dado

class Cacho:
    """
    Clase que representa un conjunto de dados.

    Permite almacenar, agitar, ganar y perder dados, además de controlar
    la visibilidad de los dados para otros jugadores.

    Atributos:
        dado: Instancia de la clase Dado para generar valores aleatorios
        almacen: Lista que contiene los valores actuales de los dados
        count: Contador de dados "reservados" cuando el almacén está lleno
        mostrar_dados_activado: Indica si la función de visibilidad ya fue usado
        dados_visibles: Estado actual de visibilidad de los dados.
    """
    def __init__(self):
        self.dado = Dado()
        self.almacen = [] #
        self.count = 0
        self.mostrar_dados_activado = False
        self.dados_visibles = False

    def almacenar_dados(self, cantidad = 5):
        """
        Inicializa el almacén con nuevos dados.
        """
        for i in range(cantidad):
            self.almacen.append(self.dado.generar_valor())
        return self.almacen

    def agitar_dados(self):
        """
        Regenera todos los valores de los dados en el almacén.
        """
        for i in range(len(self.almacen)):
            self.almacen[i] = self.dado.generar_valor()
        return self.almacen

    def perder_dado(self):
        """
        Elimina un dado del almacén o reduce el contador de reservas.

        Lógica:
            -Si count > 0: reduce el contador (y añade un dado si el almacén < 5)
            -Si count == 0: elimina el último dado del almacén.
        """
        if self.count > 0:
            if len(self.almacen) < 5:
                self.almacen.append(self.dado.generar_valor())
                self.count -= 1
            else:
                self.count -= 1
        else:
            self.almacen.pop()
        return self.almacen

    def ganar_dado(self, max_dados = 5):
        """
        Añade un nuevo dado al almacén o incrementa el contador de reservas.
        """
        if len(self.almacen) < max_dados:
            self.almacen.append(self.dado.generar_valor())
        else:
            self.count += 1
        return self.almacen

    def visibilidad_dados(self):
        """"
        Función para mostrar/ocultar dados al resto de jugadores.

        Solo funciona si:
        1. El jugador tiene exactamente 1 dado.
        2. No ha usado esta función antes
        """
        if self.mostrar_dados_activado:
            return False, "Ya usaste esta función anteriormente"

        # Cambiar el estado de visibilidad
        self.dados_visibles = not self.dados_visibles
        self.mostrar_dados_activado = True

        estado = "visibles" if self.dados_visibles else "ocultos"
        return True, f"Tus dados ahora están {estado} para otros jugadores"
