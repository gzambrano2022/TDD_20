from src.juego.persona import Persona
from src.juego.validador_apuesta import ValidadorApuesta
import random

class Gestor_partida:
    """
    Clase encargada de gestionar el flujo de la partida del juego de dados "Dudo".
    Controla la creación de jugadores, turnos, apuestas y verificaciones de reglas.
    """

    def __init__(self):
        """
        Inicializa el gestor de partida con:
        - Lista de jugadores vacía.
        - Jugador actual en 0 (sin turno asignado).
        - Apuesta actual como lista vacía.
        """
        self.jugadores = []
        self.jugador_actual = 0
        self.apuesta_actual = []

    def crear_jugadores(self, cantidad):
        """
        Crea los jugadores para la partida.

        Parámetros:
        -----------
        cantidad : int
            Número de jugadores a crear.
        
        Acción:
        -------
        Limpia la lista de jugadores anterior y agrega objetos `Persona`
        numerados desde 0 hasta cantidad-1.
        """
        self.jugadores.clear()
        for i in range(cantidad):
            self.jugadores.append(Persona(i))

    def jugador_inicial(self):
        """
        Determina al jugador que comenzará la partida.

        Mecánica:
        ---------
        - Cada jugador tira un dado aleatorio (1 a 6).
        - El jugador con el valor más alto comienza.
        - Si hay empate, se elige aleatoriamente entre los empatados.

        Acción:
        -------
        Establece `self.jugador_actual` con el índice (1-based) del jugador inicial.
        """
        numeros = []
        cantidad_jugadores = len(self.jugadores)
        empates = []

        # Cada jugador tira un dado (valor aleatorio entre 1 y 6)
        for i in range(cantidad_jugadores):
            numeros.append(random.randint(1,6))

        # Se determina el valor más alto
        valor_maximo = max(numeros)

        # Se almacenan los jugadores que obtuvieron ese valor
        for i in range(cantidad_jugadores):
            if valor_maximo == numeros[i]:
                empates.append(i)
        
        # Si hay un solo ganador → inicia él
        if len(empates) == 1:
            self.jugador_actual = empates[0] + 1
        else:
            # Si hay empate → se elige al azar entre los empatados
            self.jugador_actual = empates[random.randint(0, len(empates) - 1)] + 1
    
    def pasar_turno(self, apuesta_nueva):
        """
        Pasa el turno al siguiente jugador, validando la apuesta.

        Parámetros:
        -----------
        apuesta_nueva : tuple
            Representa la nueva apuesta (cantidad_dados, cara).

        Retorna:
        --------
        bool
            False → si la apuesta no es válida.
            True → si la apuesta es válida y el turno avanza.

        Acción:
        -------
        - Si la apuesta es inválida → no cambia nada.
        - Si la apuesta es válida → se actualiza `self.apuesta_actual` 
          y se asigna el turno al siguiente jugador (o vuelve al 1 si estaba en el último).
        """
        validador = ValidadorApuesta()
        if validador.apuesta_valida(self.apuesta_actual, apuesta_nueva) == False:
            return False

        self.apuesta_actual = apuesta_nueva

        # Si el jugador actual es el último → vuelve al primero
        if self.jugador_actual == len(self.jugadores):
            self.jugador_actual = 1
            return True
        else:
            # Avanza al siguiente jugador
            self.jugador_actual = self.jugador_actual + 1
            return True
    
    def verificar_un_dado(self):
        """
        Verifica si algún jugador tiene exactamente un solo dado.

        Retorna:
        --------
        int
            - Índice del jugador que tiene un solo dado.
            - 0 si ningún jugador tiene solo un dado.
        """
        cantidad_jugadores = len(self.jugadores)
        for i in range(cantidad_jugadores):
            if len(self.jugadores[i].cacho.almacen) == 1:
                return i + 1
        return 0