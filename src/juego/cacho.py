from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dado = Dado()
        self.almacen = []
        self.count = 0
        self.mostrar_dados_activado = False # no se ha usado todavía el juego abierto
        self.dados_visibles = False # estado actual de visibilidad

    def almacenar_dados(self, cantidad = 5):
        for i in range(cantidad):
            self.almacen.append(self.dado.generar_valor())
        return self.almacen

    def agitar_dados(self):
        for i in range(len(self.almacen)):
            self.almacen[i] = self.dado.generar_valor()
        return self.almacen

    def perder_dado(self):
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
