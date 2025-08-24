import pytest
from src.juego.gestor_partida import Gestor_partida
from src.juego.persona import Persona
import random

class Test_gestor:

    def test_crearjugadores(self):
        gestor = Gestor_partida()
        cantidad = 5
        gestor.crear_jugadores(cantidad)

    def test_jugador_inicial(self):
        gestor= Gestor_partida()
        jugador = gestor.jugador_inicial([1,2,3,4,5])
        assert 5 == jugador





"""
Gestor de Partida
Implementa una clase GestorPartida que:

Administre múltiples jugadores y sus dados
Determine quién inicia cada ronda
Maneje el flujo de turnos
Detecte cuándo alguien queda con un dado (para activar reglas especiales)
"""