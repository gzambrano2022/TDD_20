class Arbitro_ronda:

    def dudar(self,apuesta,jugadores,jugador_actual):
        cantidad_jugadores = len(jugadores)
        numero = apuesta[1]
        cantidad_dados = 0
        for i in range(cantidad_jugadores):
            cantidad_dados = cantidad_dados + jugadores[i].cacho.almacen.count(numero) + jugadores[i].cacho.almacen.count(1)
        if cantidad_dados >= apuesta[0]:
            jugadores[jugador_actual - 1].cacho.perder_dado()
            return "pierde"
        else:
            if jugador_actual - 1 == 0:
                jugador_anterior = cantidad_jugadores - 1
                jugadores[jugador_anterior].cacho.perder_dado()
            else:
                jugadores[jugador_actual - 2].cacho.perder_dado()
            return "gana"
    
    def calzar(self,apuesta,jugadores,jugador_actual):
        #Verificacion para ver si se puede calzar
        cantidad_dados = 0
        cantidad_jugadores = len(jugadores)
        for i in range(len(jugadores)):
            cantidad_dados = cantidad_dados + len(jugadores[i].cacho.almacen)
        if len(jugadores[jugador_actual -1].cacho.almacen) == 1 or (cantidad_jugadores*5)/2 >= cantidad_dados:
            pass
        else:
            return "falla"
            
        cara = apuesta[1]
        cantidad_dados = 0
        for i in range(cantidad_jugadores):
            cantidad_dados = cantidad_dados + jugadores[i].cacho.almacen.count(cara) + jugadores[i].cacho.almacen.count(1)
        if cantidad_dados == apuesta[0]:
            jugadores[jugador_actual - 1].cacho.ganar_dado()
            return "gana"
        else:
            jugadores[jugador_actual - 1].cacho.perder_dado()
            return "pierde"