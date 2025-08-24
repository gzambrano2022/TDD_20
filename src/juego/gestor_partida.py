from src.juego.persona import Persona
class Gestor_partida:
    def __init__(self):
        self.jugadores = []
    
    def crear_jugadores(self,cantidad):
        for i in range(cantidad):
            self.jugadores.append(Persona(i))