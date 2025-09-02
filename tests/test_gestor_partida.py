from src.juego.gestor_partida import Gestor_partida
from unittest.mock import patch

class Test_gestor:
    """
    Clase de pruebas unitarias para `Gestor_partida`.
    Valida la correcta creación de jugadores, la elección del jugador inicial,
    el paso de turnos y la verificación de jugadores con un solo dado.
    """

    def test_crearjugadores(self):
        """
        Prueba la creación de jugadores.
        
        Caso:
        -----
        - Se crean 5 jugadores y se valida que el método no falle.
        """
        gestor = Gestor_partida()
        cantidad = 5
        gestor.crear_jugadores(cantidad)
    
    @patch("src.juego.gestor_partida.random.randint", side_effect=[2, 2, 1, 1])
    def test_jugador_inicial(self, mock_randint):
        """
        Prueba la selección del jugador inicial.

        Caso:
        -----
        - Se simula la tirada de dados con `random.randint` usando un patch.
        - Los valores simulados son [2, 2, 1].
        - Los jugadores 0 y 1 empatan con el valor máximo (2).
        - El empate se resuelve al azar, pero como el patch da un 1 extra, 
          el jugador 2 (índice 1 + 1) será el inicial.
        
        Resultado esperado:
        -------------------
        `gestor.jugador_actual` debe ser 2.
        """
        gestor = Gestor_partida()
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()
        assert gestor.jugador_actual == 2

    @patch("src.juego.gestor_partida.random.randint", side_effect=[1, 2, 3])
    def test_pasarturno(self, mock_randint):
        """
        Prueba el funcionamiento del paso de turnos con apuestas válidas e inválidas.

        Casos:
        ------
        1. Apuesta válida aumentando cantidad de dados → turno pasa correctamente.
        2. Apuesta inválida (menor que la anterior) → retorna False, no cambia turno.
        3. Apuesta válida aumentando la cara → turno avanza.
        
        Verificaciones:
        ---------------
        - Cambio correcto de `jugador_actual`.
        - Retornos True o False según validez de la apuesta.
        """
        gestor = Gestor_partida()
        gestor.apuesta_actual = [2, 4]
        apuesta_nueva = [3, 4]
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()

        # Prueba con apuesta válida (mayor cantidad de dados)
        assert gestor.jugador_actual == 3
        assert gestor.pasar_turno(apuesta_nueva) is True
        assert gestor.jugador_actual == 1

        # Prueba con apuesta inválida (menor cantidad/cara)
        apuesta_nueva = [2, 2]
        assert gestor.pasar_turno(apuesta_nueva) is False
        assert gestor.jugador_actual == 1

        # Prueba con apuesta válida (mayor cara)
        apuesta_nueva = [3, 5]
        assert gestor.pasar_turno(apuesta_nueva) is True
        assert gestor.jugador_actual == 2

    def test_verificar_un_dado(self):
        """
        Prueba la verificación de jugadores con un solo dado.

        Casos:
        ------
        - Todos los jugadores con más de un dado → retorna 0.
        - Un jugador con exactamente un dado → retorna el índice del jugador (1-based).
        
        Resultado esperado:
        -------------------
        - Con todos los jugadores con 5 dados → 0.
        - Con el jugador 3 con un dado → 3.
        """
        gestor = Gestor_partida()
        gestor.crear_jugadores(3)

        # Se inicializan los dados de los 3 jugadores (por defecto 5 cada uno)
        for i in range(3):
            gestor.jugadores[i].cacho.almacenar_dados()

        assert gestor.verificar_un_dado() == 0

        # Forzar que el jugador 3 tenga un solo dado
        gestor.jugadores[2].cacho.almacen = [1]
        assert gestor.verificar_un_dado() == 3
