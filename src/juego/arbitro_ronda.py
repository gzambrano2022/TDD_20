from src.juego.contador_pintas import ContadorPintas

class Arbitro_ronda:
    """
    Clase que actúa como árbitro de la ronda en el juego de dados "Dudo".
    Su función es verificar las jugadas de los jugadores cuando deciden
    "dudar" o "calzar" una apuesta.
    """

    def dudar(self, apuesta, jugadores, jugador_actual):
        """
        Verifica la acción de 'dudar'.

        Parámetros:
        -----------
        apuesta : tuple
            Representa la apuesta realizada. 
        jugadores : list
            Lista de jugadores en la partida.
        jugador_actual : int
            Índice del jugador que decide dudar.

        Retorna:
        --------
        str
            "pierde" si el jugador que dudó pierde un dado.
            "gana" si el jugador anterior al que dudó pierde un dado.
        """
        cantidad_jugadores = len(jugadores)
        cara = apuesta[1]  # Cara que se está apostando (ej: 3, 5, etc.)
        contador_pintas = ContadorPintas()
        cantidad_dados = 0

        # Se cuentan los dados de todos los jugadores que coinciden con la cara apostada
        for i in range(cantidad_jugadores):
            cantidad_dados += contador_pintas.contar_pintas(jugadores[i].cacho.almacen, cara)

        # Si la cantidad real de dados es suficiente para cumplir la apuesta
        if cantidad_dados >= apuesta[0]:
            # El jugador que dudó pierde un dado
            jugadores[jugador_actual - 1].cacho.perder_dado()
            return "pierde"
        else:
            # Si no se cumple la apuesta, pierde el jugador anterior al que dudó
            if jugador_actual - 1 == 0:
                # Caso especial: si el jugador actual es el primero, el "anterior" es el último
                jugador_anterior = cantidad_jugadores - 1
                jugadores[jugador_anterior].cacho.perder_dado()
            else:
                jugadores[jugador_actual - 2].cacho.perder_dado()
            return "gana"
    
    def calzar(self, apuesta, jugadores, jugador_actual):
        """
        Verifica la acción de 'calzar'.

        Parámetros:
        -----------
        apuesta : tuple
            Representa la apuesta realizada. 
        jugadores : list
            Lista de jugadores en la partida.
        jugador_actual : int
            Índice del jugador que decide calzar.

        Retorna:
        --------
        str
            "gana" si el jugador que calzó acierta y gana un dado.
            "pierde" si el jugador que calzó falla y pierde un dado.
            "falla" si no se cumplen las condiciones para calzar.
        """
        cantidad_dados = 0
        cara = apuesta[1]
        cantidad_jugadores = len(jugadores)
        contador_pintas = ContadorPintas()

        # Contar todos los dados actualmente en juego
        for i in range(cantidad_jugadores):
            cantidad_dados += len(jugadores[i].cacho.almacen)

        # Reglas para permitir "calzar":
        # 1. El jugador tiene solo un dado, o
        # 2. El total de dados en juego es menor o igual a la mitad de los dados iniciales
        if len(jugadores[jugador_actual - 1].cacho.almacen) == 1 or (cantidad_jugadores * 5) / 2 >= cantidad_dados:
            pass
        else:
            return "falla"
        
        # Se cuentan cuántos dados reales coinciden con la cara apostada
        cantidad_dados = 0
        for i in range(cantidad_jugadores):
            cantidad_dados += contador_pintas.contar_pintas(jugadores[i].cacho.almacen, cara)

        # Si el número coincide exactamente con la apuesta → gana un dado
        if cantidad_dados == apuesta[0]:
            jugadores[jugador_actual - 1].cacho.ganar_dado()
            return "gana"
        else:
            # Si no coincide → pierde un dado
            jugadores[jugador_actual - 1].cacho.perder_dado()
            return "pierde"
