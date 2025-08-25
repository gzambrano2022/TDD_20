from src.juego.gestor_partida import Gestor_partida
from unittest.mock import patch
class Test_gestor:

    def test_crearjugadores(self):
        gestor = Gestor_partida()
        cantidad = 5
        gestor.crear_jugadores(cantidad)
    
    @patch("random.randint", side_effect=[2, 2, 1,1])
    def test_jugador_inicial(self,mock_randint):
        gestor= Gestor_partida()
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()
        assert gestor.jugador_actual == 2
        




"""
Gestor de Partida
Implementa una clase GestorPartida que:

Administre múltiples jugadores y sus dados
Determine quién inicia cada ronda
Maneje el flujo de turnos
Detecte cuándo alguien queda con un dado (para activar reglas especiales)
"""