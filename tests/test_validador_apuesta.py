from src.juego.validador_apuesta import ValidadorApuesta
from src.juego.contador_pintas import ContadorPintas

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

def test_cambiar_a_ases():
    validador = ValidadorApuesta()
    apuesta_inicial1 = (7,3) #tres cuartas
    apuesta_inicial2 = (8,4) #ocho cuartas

    #Al cambiar a ases la apuesta se puede bajar a: La mitad + 1 si es par o la mitad redondeada hacia arriba si es impar
    apuesta_nueva1 = (4,1) #cuatro ases
    apuesta_nueva2 = (5,1) #cinco ases

    assert validador.apuesta_valida(apuesta_inicial1, apuesta_nueva1) == True
    assert validador.apuesta_valida(apuesta_inicial2, apuesta_nueva2) == True

def test_cambiar_de_ases():
    validador = ValidadorApuesta()
    apuesta_inicial1 = (4,1) #cuatro ases
    apuesta_inicial2 = (2,1) #dos ases

    apuesta_nueva1 = (9,3) #nueve trenes
    apuesta_nueva2 = (5,4) #cinco cuartas

    assert validador.apuesta_valida(apuesta_inicial1, apuesta_nueva1) == True
    assert validador.apuesta_valida(apuesta_inicial2, apuesta_nueva2) == True

def test_aumentar_apuesta_con_ases():
    validador = ValidadorApuesta()
    apuesta_inicial = (3,1) #tres ases

    apuesta_nueva1 = (4,1) #cuatro ases
    apuesta_nueva2 = (6,1) #seis ases

    assert validador.apuesta_valida(apuesta_inicial, apuesta_nueva1) == True
    assert validador.apuesta_valida(apuesta_inicial, apuesta_nueva2) == True

def test_apuestas_invalidas():
    validador = ValidadorApuesta()

    #Apostando hacia abajo sin ases invlucrados
    apuesta_inicial1 = (3,4) #tres cuartas

    apuesta_nueva11 = (3,3) #tres trenes
    apuesta_nueva12 = (2,4) #dos cuartas

    assert validador.apuesta_valida(apuesta_inicial1, apuesta_nueva11) == False
    assert validador.apuesta_valida(apuesta_inicial1, apuesta_nueva12) == False

    #Apostado cambiando A ases de forma invalida
    apuesta_inicial2 = (5,6) #cinco sextas

    apuesta_nueva21 = (6,1) #seis ases (deberia ser tres ases)
    apuesta_nueva22 = (5,1) #cinco ases (apuesta invalida directamente)

    assert validador.apuesta_valida(apuesta_inicial2, apuesta_nueva21) == False
    assert validador.apuesta_valida(apuesta_inicial2, apuesta_nueva22) == False

    #Apostando cambiando DE ases de forma invalida
    apuesta_inicial3 = (4,1)

    apuesta_nueva31 = (7,2) #siete tontos (deberia ser nueve tontos)
    apuesta_nueva32 = (3,1) #tres ases (apuesta invalida directamente)

#SOLO SE PUEDE PARTIR CON ASES CUANDO SE TIENE UN SOLO DADO
