class Arbitro_ronda:

    def dudar(self,apuesta,jugadores):
        cantidad_jugadores = len(jugadores)
        numero = apuesta[1]
        cantidad_dados = 0
        for i in range(cantidad_jugadores):
            cantidad_dados = cantidad_dados + jugadores[i].cacho.almacen.count(numero)
        if cantidad_dados >= apuesta[0]:
            return "pierde"
        else:
            return "gana"






