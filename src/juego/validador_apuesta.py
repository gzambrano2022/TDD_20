class ValidadorApuesta:
    def apuesta_valida(self, apuesta_inicial, apuesta_nueva):
        cantidad_inicial, pinta_inicial = apuesta_inicial
        cantidad_nueva, pinta_nueva = apuesta_nueva

        #La apuesta es valida si aumenta la pinta o la cantidad de apariciones de la pinta
        if pinta_nueva == 1:
            if cantidad_inicial % 2 == 0:
                if cantidad_nueva == (cantidad_inicial // 2 + 1):
                    return True
            elif cantidad_nueva == ((cantidad_inicial + 1)//2):
                return True
        elif pinta_inicial == 1:
            pass
        elif cantidad_nueva >= cantidad_inicial and pinta_nueva >= pinta_inicial:
            return True