from src.juego.gestor_partida import Gestor_partida
from unittest.mock import patch
class Test_gestor:

    def test_crearjugadores(self):
        gestor = Gestor_partida()
        cantidad = 5
        gestor.crear_jugadores(cantidad)
    
    @patch("src.juego.gestor_partida.random.randint", side_effect=[2, 2, 1,1])
    def test_jugador_inicial(self,mock_randint):
        gestor= Gestor_partida()
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()
        assert gestor.jugador_actual == 2

    @patch("src.juego.gestor_partida.random.randint", side_effect=[1,2,3])
    def test_pasarturno(self,mock_randint):
        gestor= Gestor_partida()
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()
        assert gestor.jugador_actual == 3
        gestor.pasar_turno()
        assert gestor.jugador_actual == 1

    def test_verificar_un_dado(self):
        gestor= Gestor_partida()
        gestor.crear_jugadores(3)
        for i in range(3):
            gestor.jugadores[i].cacho.almacenar_dados()
        assert gestor.verificar_un_dado() == 0
        gestor.jugadores[2].cacho.almacen = [1]
        assert gestor.verificar_un_dado() == 3


"""
Gestor de Partida
Implementa una clase GestorPartida que:

Administre múltiples jugadores y sus dados
Determine quién inicia cada ronda
Maneje el flujo de turnos
Detecte cuándo alguien queda con un dado (para activar reglas especiales)
"""