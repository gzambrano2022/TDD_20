from src.juego.arbitro_ronda import Arbitro_ronda
from src.juego.gestor_partida import Gestor_partida

def test_dudar():
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugador_actual = 1
    gestor.jugadores[0].cacho.almacen = [4,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,2,2,4,4]
    apuesta = (3,3)
    arbitro = Arbitro_ronda()
    assert arbitro.dudar(apuesta,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[1].cacho.almacen) == 4
    gestor.jugadores[0].cacho.almacen = [4,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,3,3,4,4]
    assert arbitro.dudar(apuesta,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[0].cacho.almacen) == 4
    #Prueba para los ases
    apuesta2 = (4,5)
    gestor.jugadores[0].cacho.almacen = [5,2,1,3,3]
    gestor.jugadores[1].cacho.almacen = [5,3,1,3,4]
    assert arbitro.dudar(apuesta2,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[0].cacho.almacen) == 4
    #Prueba para mas de 2 jugadores
    gestor = Gestor_partida()
    gestor.crear_jugadores(4)
    gestor.jugador_actual = 1
    apuesta3 = (2,5)
    gestor.jugadores[0].cacho.almacen = [3,4,1,3,3]
    gestor.jugadores[1].cacho.almacen = [3,3,4,3,4]
    gestor.jugadores[2].cacho.almacen = [3,4,4,4,3]
    gestor.jugadores[3].cacho.almacen = [4,4,2,4,6]
    assert gestor.jugador_actual == 1
    assert arbitro.dudar(apuesta3,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[3].cacho.almacen) == 4
    gestor.jugador_actual = 2
    assert arbitro.dudar(apuesta3,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[0].cacho.almacen) == 4

def test_calzar():
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugador_actual = 1
    gestor.jugadores[0].cacho.almacen = [1,2,3,4,3]
    gestor.jugadores[1].cacho.almacen = [1,2,3,4,4]
    apuesta = (3,4)
    arbitro = Arbitro_ronda()
    #Mas de la mitad de dados no esta en juego por lo cual falla
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "falla"
    #Mitad de los dados en juego, por lo tanto se puede calzar
    gestor.crear_jugadores(2)
    gestor.jugadores[0].cacho.almacen = [1,2]
    gestor.jugadores[1].cacho.almacen = [5,1]
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[gestor.jugador_actual - 1].cacho.almacen) == 1
    #Un solo dado por lo cual se puede calzar
    gestor.crear_jugadores(3)
    apuesta2 = (4,6)
    gestor.jugadores[0].cacho.almacen = [5,1,1]
    gestor.jugadores[1].cacho.almacen = [6,5]
    gestor.jugadores[1].cacho.almacen = [1]
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[gestor.jugador_actual - 1].cacho.almacen) == 4