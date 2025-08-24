from src.juego.contador_pintas import ContadorPintas

#Cuenta las pintas en una lista de dados tratando los ases como comodines
def test_contar_pintas():
    dados = [1,2,5,4,3,3,3,5,4,5,1,1,1,1,1] #Ejemplo con 15 dados
    pinta = 3 #Pinta que queremos contar
    contador = ContadorPintas() #Instancia del objeto ContadorPintas
    resultado = contador.contar_pintas(dados,pinta) #Llamada al metodo para contar pintas
    assert resultado == 9 #Verificacion del resultado esperado

#Cuenta las pintas en una ronda especial cuando un jugador se queda con un solo dado por primera vez
#los ases cuentan como uno solamente y no como comodines
def test_contar_pintas_en_ronda_de_un_solo_dado():
    dados = [1,2,3,4,5,3,2,1,4,3,4] #Ejemplo con 11 dados, dos jugadores con 5 dados y uno con 1 dado
    pinta = 4 #Pinta que queremos contar
    contador = ContadorPintas() #Instancia del objeto ContadorPintas
    contador.set_ronda_especial(True) #Indicador de ronda especial activa
    resultado = contador.contar_pintas(dados,pinta) #Llamada al metodo para contar pintas
    assert resultado == 3 #Verificacion del resultado esperado