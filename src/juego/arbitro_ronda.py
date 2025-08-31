from src.juego.contador_pintas import ContadorPintas
class Arbitro_ronda:

    def dudar(self,apuesta,jugadores,jugador_actual):
        cantidad_jugadores = len(jugadores)
        cara = apuesta[1]
        contador_pintas = ContadorPintas()
        cantidad_dados = 0
        for i in range(cantidad_jugadores):
            cantidad_dados = cantidad_dados + contador_pintas.contar_pintas(jugadores[i].cacho.almacen,cara)
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
        cara = apuesta[1]
        cantidad_jugadores = len(jugadores)
        contador_pintas = ContadorPintas()
        #Se cuentan todos los dados
        for i in range(len(jugadores)):
            cantidad_dados = cantidad_dados + len(jugadores[i].cacho.almacen)
        #Si hay mas de da mitad de dados en juego o si el jugador que quiere calzar tiene un dado entonces se podra calzar
        if len(jugadores[jugador_actual -1].cacho.almacen) == 1 or (cantidad_jugadores*5)/2 >= cantidad_dados:
            pass
        else:
            return "falla"
        
        cantidad_dados = 0
        for i in range(cantidad_jugadores):
            cantidad_dados = cantidad_dados + contador_pintas.contar_pintas(jugadores[i].cacho.almacen,cara)
        if cantidad_dados == apuesta[0]:
            jugadores[jugador_actual - 1].cacho.ganar_dado()
            return "gana"
        else:
            jugadores[jugador_actual - 1].cacho.perder_dado()
            return "pierde"