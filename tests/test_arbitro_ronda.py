from src.juego.arbitro_ronda import Arbitro_ronda
from src.juego.gestor_partida import Gestor_partida

def test_dudar():
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugadores[0].cacho.almacen = [1,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,5,2,1,4]
    apuesta = (3,3)
    arbitro = Arbitro_ronda()
    assert arbitro.dudar(apuesta,gestor.jugadores) == "pierde"

