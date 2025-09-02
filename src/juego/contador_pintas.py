class ContadorPintas:

    #Metodo constructor
    def __init__(self):
        self.ronda_especial = False #Falso por defecto pues la partida empieza con 5 dados cada jugador


    def contar_pintas(self,dados,pinta):

        """
        Cuenta cuántos dados coinciden con la pinta indicada.

        Si no es ronda especial, los ases (1) cuentan como comodín para cualquier pinta.

        Parámetros:
        - dados: lista de números que representan los dados.
        - pinta: número de la pinta a contar.

        Retorna:
        - int: cantidad de dados que coinciden con la pinta.
        """

        cont = 0
        for dado in dados:
            if (dado == 1 and not self.ronda_especial) or dado == pinta:
                cont += 1
        return cont
    
    def set_ronda_especial(self, ronda_especial):
        self.ronda_especial = ronda_especial