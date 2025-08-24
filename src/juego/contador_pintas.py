class ContadorPintas:

    #Metodo constructor
    def __init__(self):
        self.ronda_especial = False #Falso por defecto pues la partida empieza con 5 dados cada jugador

    #Metodo para contar pintas dada una lista de dados (enteros) y una pinta (entero)
    def contar_pintas(self,dados,pinta):
        cont = 0
        for dado in dados:
            if (dado == 1 and not self.ronda_especial) or dado == pinta:
                cont += 1
        return cont
    
    def set_ronda_especial(self, ronda_especial):
        self.ronda_especial = ronda_especial