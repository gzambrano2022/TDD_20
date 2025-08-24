from src.juego.contador_pintas import ContadorPintas

def test_contar_pintas():
    dados = [1,2,5,4,3,3,3,5,4,5] #Ejemplo con 10 dados
    pinta = 3 #Pinta que queremos contar
    contador = ContadorPintas() #Instancia del objeto ContadorPintas
    resultado = contador.contar_pintas(dados,pinta) #Llamada al metodo para contar pintas
    assert resultado == 3 #Verificacion del resultado esperado