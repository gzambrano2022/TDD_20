#IMPORTS
from src.juego.gestor_partida import Gestor_partida
from src.juego.arbitro_ronda import Arbitro_ronda
from src.juego.contador_pintas import ContadorPintas
from src.juego.dado import Dado

# Códigos de color
ROJO = "\033[31m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
BLANCO = "\033[37m"     
MAGENTA = "\033[35m"
RESET = "\033[0m"

# Negrita
NEGRITA = "\033[1m"

def estado_partida():
    #Impresion del estado de la partida
    print(f"{NEGRITA}{AZUL}==========Estado de la partida=========={RESET}")
    print("Cantidad de jugadores:", len(gestor_partida.jugadores))
    #Informacion para el inicio de cada ronda
    #print("Turno del jugador:", gestor_partida.jugador_actual)
    print(f"{NEGRITA}{MAGENTA}Turno del jugador: {gestor_partida.jugador_actual} {RESET}")
    print("Apuesta actual en la mesa:", gestor_partida.apuesta_actual if (not gestor_partida.apuesta_actual == (0,0)) else "No hay apuesta")

def mostrar_dados():
    #Imprimimos el estado inicial de los dados de cada jugador
    for i in range(num_jugadores):
    #Se le suma 1 al numero del jugador porque para el atributo de "jugador_actual" se maneja desde 1 en adelante pero para el "numero_jugador" se maneja desde 0 en adelante
        print("Jugador", gestor_partida.jugadores[i].numero_jugador + 1, "tiene los dados:", gestor_partida.jugadores[i].cacho.almacen)

def set_dudar(gestor_partida, arbitro_ronda):
    decision = 0
    if(gestor_partida.apuesta_actual == (0,0)):
        print("No hay apuesta previa, por lo que no se puede dudar\n")
        return False
    else:
        print("DUDO", end = " ")
        decision = arbitro_ronda.dudar(gestor_partida.apuesta_actual, gestor_partida.jugadores, gestor_partida.jugador_actual)
        print("Aseveracion correcta, jugador anterior pierde un dado" if decision == "gana" else "Aseveracion incorrecta, jugador actual pierde un dado")
                    
    #En este punto se comienza una ronda nueva, por lo tanto:
    #El si el jugador acierta al duda el jugador anterior es el que pierde el dado y por lo tanto el es quien empieza la ronda
    if(decision == "gana"):
        if (gestor_partida.jugador_actual != 1):
            gestor_partida.jugador_actual = gestor_partida.jugador_actual - 1 
        else:
            gestor_partida.jugador_actual = len(gestor_partida.jugadores) #Chequear
                    
    gestor_partida.apuesta_actual = (0,0)
    return True

def set_calzar(gestor_partida, arbitro_ronda):
    decision = decision = arbitro_ronda.calzar(gestor_partida.apuesta_actual, gestor_partida.jugadores, gestor_partida.jugador_actual)
    if decision == "falla":
        print("CALZO: Las condiciones actuales de la ronda no permiten calzar\n")
        return False
    else:
        print("CALZO: Aseveracion correcta, jugador actual gana un dado" if decision == "gana" else "CALZO: Aseveracion incorrecta, jugador actual pierde un dado")

    #En este punto se comienza una ronda nueva, por lo tanto
    gestor_partida.apuesta_actual = (0,0)
    return True

#def perder_dado


#SETUP VARIABLE Y OBJETOS
num_jugadores = 2

gestor_partida = Gestor_partida()
arbitro_ronda = Arbitro_ronda()
contador_pintas = ContadorPintas()
dado = Dado()

gestor_partida.crear_jugadores(num_jugadores)

gestor_partida.jugadores[0].cacho.almacen = [1,4,2,5,4] #Dados jugador 1
gestor_partida.jugadores[1].cacho.almacen = [4,6,3,6,2] #Dados jugador 2

gestor_partida.jugador_actual = 1     #Elegimos el jugador 1 como jugador a empezar
gestor_partida.apuesta_actual = (0,0) #Al inicio de la ronda no hay apuesta por lo tanto es (0,0)

##########################Ronda 1##########################
estado_partida()
mostrar_dados()

apuesta_nueva = (3,5) #Tres quinas
print("Apuesta jugador 1:", 3,dado.designaciones[5])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

apuesta_nueva = (4,5)
print("Apuesta jugador 2:", 4,dado.designaciones[5])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()


set_dudar(gestor_partida, arbitro_ronda)

##########################Ronda 2##########################

print("Se agitan los dados")

gestor_partida.jugadores[0].cacho.almacen = [1,1,5,4,3] #Dados jugador 1
gestor_partida.jugadores[1].cacho.almacen = [1,4,5,2] #Dados jugador 2

estado_partida()
mostrar_dados()


apuesta_nueva = (4,5)
print("Apuesta jugador 2:", 4,dado.designaciones[5])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

apuesta_nueva = (5,5)
print("Apuesta jugador 1:", 5,dado.designaciones[5])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

set_dudar(gestor_partida, arbitro_ronda)

##########################Ronda 3##########################
print("Se agitan los dados")

gestor_partida.jugadores[0].cacho.almacen = [1,4,5,6,3] #Dados jugador 1
gestor_partida.jugadores[1].cacho.almacen = [3,4,5] #Dados jugador 2

estado_partida()
mostrar_dados()


apuesta_nueva = (3,3)
print("Apuesta jugador 2:", 3,dado.designaciones[3])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

apuesta_nueva = (4,3)
print("Apuesta jugador 1:", 4,dado.designaciones[3])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

set_dudar(gestor_partida, arbitro_ronda)


##########################Ronda 4##########################

print("Se agitan los dados")

gestor_partida.jugadores[0].cacho.almacen = [2, 4, 3, 2] #Dados jugador 1
gestor_partida.jugadores[1].cacho.almacen = [6,1,5] #Dados jugador 2

estado_partida()
mostrar_dados()


apuesta_nueva = (4,2)
print("Apuesta jugador 2:", 4,dado.designaciones[2])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

apuesta_nueva = (5,2)
print("Apuesta jugador 1:", 5,dado.designaciones[2])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

set_dudar(gestor_partida, arbitro_ronda)

##########################Ronda 5##########################

print("Se agitan los dados")

gestor_partida.jugadores[0].cacho.almacen = [2, 1, 5, 4] #Dados jugador 1
gestor_partida.jugadores[1].cacho.almacen = [2,5] #Dados jugador 2

estado_partida()
mostrar_dados()

apuesta_nueva = (2,2)
print("Apuesta jugador 2:", 2,dado.designaciones[2])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

apuesta_nueva = (3,2)
print("Apuesta jugador 1:", 3,dado.designaciones[2])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

set_dudar(gestor_partida, arbitro_ronda)

##########################Ronda 6##########################

print("Se agitan los dados")

gestor_partida.jugadores[0].cacho.almacen = [3, 2, 1, 6] #Dados jugador 1
gestor_partida.jugadores[1].cacho.almacen = [5] #Dados jugador 2

estado_partida()
mostrar_dados()

apuesta_nueva = (3,3)
print("Apuesta jugador 2:", 3,dado.designaciones[3])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()

apuesta_nueva = (3,4)
print("Apuesta jugador 1:", 3,dado.designaciones[4])
gestor_partida.pasar_turno(apuesta_nueva)

estado_partida()
mostrar_dados()
set_calzar(gestor_partida, arbitro_ronda)

print(f"{NEGRITA}{ROJO}==========Fin de la partida, el jugador 2 se quedo sin dados. Jugador 1 gana=========={RESET}")