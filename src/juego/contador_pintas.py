class ContadorPintas:

    #Metodo para contar pintas dada una lista de dados (enteros) y una pinta (entero)
    def contar_pintas(self,dados,pinta):
        cont = 0
        for dado in dados:
            if dado == 1 or dado == pinta:
                cont += 1
        return cont