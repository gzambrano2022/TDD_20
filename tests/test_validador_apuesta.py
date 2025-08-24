from src.juego.validador_apuesta import ValidadorApuesta

#Una apuesta valida será aquella en la que aumenta la pinta o la cantidad de aparaciones de la pinta
def test_apuesta_valida():
    validador = ValidadorApuesta() #Instancia el objeto ValidadorApuesta

    #Definiremos una apuesta como un par ordenado (cantidad_de_apariciones, pinta)
    apuesta_inicial = (3,4) #tres cuartas

    apuesta_nueva1 = (3,5) #tres quintas
    apuesta_nueva2 = (4,4) #cuatro cuartas
    apuesta_nueva3 = (4,5) #cuatro quintas (caso en el que ambos aumentan tambien es valido)

    assert validador.apuesta_valida(apuesta_inicial, apuesta_nueva1) == True
    assert validador.apuesta_valida(apuesta_inicial, apuesta_nueva2) == True
    assert validador.apuesta_valida(apuesta_inicial, apuesta_nueva3) == True