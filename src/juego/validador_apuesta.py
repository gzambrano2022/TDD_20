class ValidadorApuesta:
    def __init__(self):
        self.ronda_especial = False #Indicador para cuando el jugador queda con un solo dado
        self.ronda_obligada = False #Indicador cuando se juega una ronda obligando
        self.pinta_obligada = None  #Pinta con la que comienza el jugador que obliga

    def apuesta_valida(self, apuesta_inicial, apuesta_nueva, jugador_con_un_dado = False):
        cantidad_inicial, pinta_inicial = apuesta_inicial
        cantidad_nueva, pinta_nueva = apuesta_nueva

        #Caso en el que se juega una partida obligada
        if self.ronda_obligada:
            #Si no hay apuesta previa se permite partir con 1
            if apuesta_inicial == (0,0):
                if pinta_nueva == 1 and cantidad_nueva >= 1:
                    #Se fija la pinta
                    self.pinta_obligada = 1
                    return True
                #La pinta se fija en cualquier caso
                elif pinta_nueva > pinta_inicial and cantidad_nueva > cantidad_inicial:
                    self.pinta_obligada = pinta_nueva
                    return True
            #Si ya habia una pinta fijada antes
            elif self.pinta_obligada is not None:
                if pinta_nueva != self.pinta_obligada:
                    #Solo los jugadores con un dado pueden cambiar la pinta
                    if(jugador_con_un_dado and cantidad_nueva > cantidad_inicial):
                        self.pinta_obligada = pinta_nueva
                        return True
                    return False
    
        
        #Caso en el que se comienza una ronda nueva (no hay apuesta inicial)
        #if apuesta_inicial == (0,0) and self.ronda_especial == True and pinta_nueva == 1 and cantidad_nueva >= 1:
        #    return True
        
        #Caso en el que se apuesta con ases dentro de una apuesta con ases (es decir, se aumenta la cantidad de ases)
        elif pinta_inicial == 1 and pinta_nueva == 1 and cantidad_nueva > cantidad_inicial:
            return True
        #Caso en el que se cambia A ases (En caso de que la pinta de la apuesta se cambiara a ases, se permite rebajar el número de apariciones en curso, a la mitad de la apuesta actual más uno en caso de ser par, o a la mitad aproximado hacia arriba de ser impar.)
        elif pinta_inicial != 1 and pinta_nueva == 1:
            if cantidad_inicial % 2 == 0:
                if cantidad_nueva == (cantidad_inicial // 2 + 1):
                    return True
                else:
                    return False #CASO DE APUESTA INVALIDA
            elif cantidad_nueva == ((cantidad_inicial + 1) // 2):
                return True
            else:
                return False #CASO DE APUESTA INVALIDA

        #Caso en el que se cambia DE ases (A su vez, si se está apostando por ases y se quiere cambiar de pinta, solo se permite apostar al doble más uno (o más) respecto del número de ases de la apuesta.)
        elif pinta_inicial == 1 and pinta_nueva != 1:
            if cantidad_nueva >= cantidad_inicial * 2 + 1:
                return True
            else:
                return False #CASO DE APUESTA INVALIDA
            
        #Caso en el que no hay ases involucrados (basta con que la cantidad aumente, la pinta aumente o ambas)
        elif apuesta_inicial == (0,0):
            return pinta_inicial < pinta_nueva and cantidad_inicial < cantidad_nueva
        elif pinta_inicial < pinta_nueva or cantidad_inicial < cantidad_nueva:
            return True
        else:
            return False #CASO DE APUESTA INVALIDA