from src.juego.gestor_partida import Gestor_partida
from unittest.mock import patch
class Test_gestor:

    def test_crearjugadores(self):
        gestor = Gestor_partida()
        cantidad = 5
        gestor.crear_jugadores(cantidad)
    
    @patch("src.juego.gestor_partida.random.randint", side_effect=[2, 2, 1,1])
    def test_jugador_inicial(self,mock_randint):
        gestor= Gestor_partida()
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()
        assert gestor.jugador_actual == 2

    @patch("src.juego.gestor_partida.random.randint", side_effect=[1,2,3])
    def test_pasarturno(self,mock_randint):
        gestor= Gestor_partida()
        gestor.apuesta_actual = [2,4]
        apuesta_nueva = [3,4]
        gestor.crear_jugadores(3)
        gestor.jugador_inicial()
        #Prueba con apuesta valida. Se aumentara la cantidad de caras
        assert gestor.jugador_actual == 3
        assert gestor.pasar_turno(apuesta_nueva) == True
        assert gestor.jugador_actual == 1
        #Prueba con apuesta invalida
        apuesta_nueva = [2,2]
        assert gestor.pasar_turno(apuesta_nueva) == False
        assert gestor.jugador_actual == 1
        #Prueba con apuesta valida. Se aumentara la cara
        apuesta_nueva = [3,5]
        assert gestor.pasar_turno(apuesta_nueva) == True
        assert gestor.jugador_actual == 2


    def test_verificar_un_dado(self):
        gestor= Gestor_partida()
        gestor.crear_jugadores(3)
        for i in range(3):
            gestor.jugadores[i].cacho.almacenar_dados()
        assert gestor.verificar_un_dado() == 0
        gestor.jugadores[2].cacho.almacen = [1]
        assert gestor.verificar_un_dado() == 3