import pytest
from src.juego.gestor_partida import Gestor_partida
from src.juego.persona import Persona

class test_gestor:

    def test_crearjugadores(self,cantidad):
        Gestor_partida = Gestor_partida()
        for i in range(cantidad):
            Gestor_partida.jugadores.append(Persona(i))





"""
Gestor de Partida
Implementa una clase GestorPartida que:

Administre múltiples jugadores y sus dados
Determine quién inicia cada ronda
Maneje el flujo de turnos
Detecte cuándo alguien queda con un dado (para activar reglas especiales)
"""
