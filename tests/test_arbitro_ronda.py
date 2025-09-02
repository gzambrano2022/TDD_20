from src.juego.arbitro_ronda import Arbitro_ronda
from src.juego.gestor_partida import Gestor_partida

def test_dudar():
    """
    Pruebas unitarias para el método `dudar` de la clase `Arbitro_ronda`.

    Casos de prueba cubiertos:
    --------------------------
    - Verificación de pérdida o ganancia de dado con 2 jugadores.
    - Prueba con ases (comodines).
    - Verificación con más de 2 jugadores en partida.
    """
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugador_actual = 1
    # Configuración inicial de los dados de los jugadores
    gestor.jugadores[0].cacho.almacen = [4,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,2,2,4,4]
    apuesta = (3,3)
    arbitro = Arbitro_ronda()

    # Caso: la apuesta es correcta → pierde el jugador anterior
    assert arbitro.dudar(apuesta,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[1].cacho.almacen) == 4

    # Caso: la apuesta es incorrecta → pierde el que dudó
    gestor.jugadores[0].cacho.almacen = [4,2,2,3,3]
    gestor.jugadores[1].cacho.almacen = [5,3,3,4,4]
    assert arbitro.dudar(apuesta,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[0].cacho.almacen) == 4

    # Prueba especial: con ases (valor 1 se cuenta como comodín)
    apuesta2 = (4,5)
    gestor.jugadores[0].cacho.almacen = [5,2,1,3,3]
    gestor.jugadores[1].cacho.almacen = [5,3,1,3,4]
    assert arbitro.dudar(apuesta2,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[0].cacho.almacen) == 4

    # Caso con más de 2 jugadores
    gestor = Gestor_partida()
    gestor.crear_jugadores(4)
    gestor.jugador_actual = 1
    apuesta3 = (2,5)
    gestor.jugadores[0].cacho.almacen = [3,4,1,3,3]
    gestor.jugadores[1].cacho.almacen = [3,3,4,3,4]
    gestor.jugadores[2].cacho.almacen = [3,4,4,4,3]
    gestor.jugadores[3].cacho.almacen = [4,4,2,4,6]

    # Jugador 1 duda → pierde el jugador anterior (jugador 4)
    assert gestor.jugador_actual == 1
    assert arbitro.dudar(apuesta3,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[3].cacho.almacen) == 4

    # Jugador 2 duda → pierde el jugador anterior (jugador 1)
    gestor.jugador_actual = 2
    assert arbitro.dudar(apuesta3,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[0].cacho.almacen) == 4


def test_calzar():
    """
    Pruebas unitarias para el método `calzar` de la clase `Arbitro_ronda`.

    Casos de prueba cubiertos:
    --------------------------
    - Fallo de calzar cuando hay más de la mitad de dados en juego.
    - Posibilidad de calzar cuando se cumple la regla de mitad de dados.
    - Posibilidad de calzar cuando un jugador solo tiene un dado.
    """
    gestor = Gestor_partida()
    gestor.crear_jugadores(2)
    gestor.jugador_actual = 1
    gestor.jugadores[0].cacho.almacen = [1,2,3,4,3]
    gestor.jugadores[1].cacho.almacen = [1,2,3,4,4]
    apuesta = (3,4)
    arbitro = Arbitro_ronda()

    # Caso: no se puede calzar porque aún hay más de la mitad de dados en juego
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "falla"

    # Caso: mitad de los dados en juego → se puede calzar
    gestor.crear_jugadores(2)
    gestor.jugadores[0].cacho.almacen = [1,2]
    gestor.jugadores[1].cacho.almacen = [5,1]
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "pierde"
    assert len(gestor.jugadores[gestor.jugador_actual - 1].cacho.almacen) == 1

    # Caso: jugador con un solo dado puede calzar
    gestor.crear_jugadores(3)
    gestor.jugadores[0].cacho.almacen = [5,1,1]
    gestor.jugadores[1].cacho.almacen = [6,5]
    gestor.jugadores[1].cacho.almacen = [1]  # Jugador con un solo dado

    # Aquí la apuesta se cumple exactamente → gana un dado
    assert arbitro.calzar(apuesta,gestor.jugadores,gestor.jugador_actual) == "gana"
    assert len(gestor.jugadores[gestor.jugador_actual - 1].cacho.almacen) == 4
