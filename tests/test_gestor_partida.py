import pytest
from src.juego.gestor_partida import Gestor_partida
from src.juego.persona import Persona

class Test_gestor:

    def test_crearjugadores(self):
        gestor = Gestor_partida()
        cantidad = 5
        gestor.crear_jugadores(cantidad)





"""
Gestor de Partida
Implementa una clase GestorPartida que:

Administre múltiples jugadores y sus dados
Determine quién inicia cada ronda
Maneje el flujo de turnos
Detecte cuándo alguien queda con un dado (para activar reglas especiales)
"""