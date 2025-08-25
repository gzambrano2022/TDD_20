from src.juego.persona import Persona
import random
class Gestor_partida:
    def __init__(self):
        self.jugadores = []
        self.jugador_actual = 0
    
    def crear_jugadores(self,cantidad):
        for i in range(cantidad):
            self.jugadores.append(Persona(i))
    def jugador_inicial(self):
        numeros = []
        cantidad_jugadores = len(self.jugadores)
        empates = []

        for i in range(cantidad_jugadores):
            numeros.append(random.randint(1,6))


        valor_maximo = max(numeros)
        for i in range(cantidad_jugadores):
            if valor_maximo == numeros[i]:
                empates.append(i)
        
        if len(empates) == 1:
            self.jugador_actual = empates[0] + 1
        else:
            self.jugador_actual = empates[random.randint(0,len(empates) -1)] + 1
        
                        
            

