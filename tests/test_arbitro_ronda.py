from src.juego.arbitro_ronda import Arbitro_ronda
from src.juego.gestor_partida import Gestor_partida

def test_dudar():
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugador_actual = 1
    gestor.jugadores[0].cacho.almacen = [1,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,2,2,1,4]
    apuesta = (3,3)
    arbitro = Arbitro_ronda()
    assert arbitro.dudar(apuesta,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[1].cacho.almacen) == 4
    gestor.jugadores[0].cacho.almacen = [1,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,3,3,1,4]
    assert arbitro.dudar(apuesta,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[0].cacho.almacen) == 4

def test_calzar():
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugador_actual = 1
    gestor.jugadores[0].cacho.almacen = [1,2,3,4,3]
    gestor.jugadores[1].cacho.almacen = [1,2,3,4,4]
    apuesta = (3,4)
    arbitro = Arbitro_ronda()
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert gestor.jugadores[gestor.jugador_actual - 1].cacho.count == 1
    gestor.jugadores[0].cacho.almacen = [1,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,1,1,1,4]
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "pierde"
    #Debera tener count igual a 1, por lo tanto no se le quitan dados
    assert len(gestor.jugadores[gestor.jugador_actual - 1].cacho.almacen) == 5