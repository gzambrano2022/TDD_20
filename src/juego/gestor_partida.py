from src.juego.persona import Persona
import random
class Gestor_partida:
    def __init__(self):
        self.jugadores = []
    
    def crear_jugadores(self,cantidad):
        for i in range(cantidad):
            self.jugadores.append(Persona(i))

    def jugador_inicial(self,lista):
        mayor = 0
        for i in range(len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor