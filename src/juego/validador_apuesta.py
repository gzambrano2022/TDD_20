class ValidadorApuesta:
    def apuesta_valida(self, apuesta_inicial, apuesta_nueva):
        cantidad_inicial, pinta_inicial = apuesta_inicial
        cantidad_nueva, pinta_nueva = apuesta_nueva

        #La apuesta es valida si aumenta la pinta o la cantidad de apariciones de la pinta
        if cantidad_nueva > cantidad_inicial or pinta_nueva > pinta_inicial:
            return True