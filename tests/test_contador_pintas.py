from src.juego.contador_pintas import ContadorPintas

#Cuenta las pintas en una lista de dados tratando los ases como comodines
def test_contar_pintas():
    dados = [1,2,5,4,3,3,3,5,4,5,1,1,1,1,1] #Ejemplo con 15 dados
    pinta = 3 #Pinta que queremos contar
    contador = ContadorPintas() #Instancia del objeto ContadorPintas
    resultado = contador.contar_pintas(dados,pinta) #Llamada al metodo para contar pintas
    assert resultado == 9 #Verificacion del resultado esperado
