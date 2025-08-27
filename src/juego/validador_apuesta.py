class ValidadorApuesta:
    def apuesta_valida(self, apuesta_inicial, apuesta_nueva):
        cantidad_inicial, pinta_inicial = apuesta_inicial
        cantidad_nueva, pinta_nueva = apuesta_nueva
        
        #Caso en el que se apuesta con ases dentro de una apuesta con ases (es decir, se aumenta la cantidad de ases)
        if pinta_inicial == 1 and pinta_nueva == 1 and cantidad_nueva > cantidad_inicial:
            return True
        #Caso en el que se cambia A ases (En caso de que la pinta de la apuesta se cambiara a ases, se permite rebajar el número de apariciones en curso, a la mitad de la apuesta actual más uno en caso de ser par, o a la mitad aproximado hacia arriba de ser impar.)
        elif pinta_inicial != 1 and pinta_nueva == 1:
            if cantidad_inicial % 2 == 0:
                if cantidad_nueva == (cantidad_inicial // 2 + 1):
                    return True
                #CASO DE APUESTA INVALIDA
            elif cantidad_nueva == ((cantidad_inicial + 1) // 2):
                return True
            #CASO DE APUESTA INVALIDA
        #Caso en el que se cambia DE ases (A su vez, si se está apostando por ases y se quiere cambiar de pinta, solo se permite apostar al doble más uno (o más) respecto del número de ases de la apuesta.)
        elif pinta_inicial == 1 and pinta_nueva != 1:
            if cantidad_nueva >= cantidad_inicial * 2 + 1:
                return True
            #CASO DE APUESTA INVALIDA
        #Caso en el que no hay ases involucrados (basta con que la cantidad aumente, la pinta aumente o ambas)
        elif pinta_inicial < pinta_nueva or cantidad_inicial < cantidad_nueva:
            return True
       #CASO DE APUESTA INVALIDA