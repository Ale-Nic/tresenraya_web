from .Tablero import Tablero
from .Estado import Estado
from .Humano import Humano
from .MinMax import MiniMax
from .AlfaBeta import AlfaBeta
from .Resultados import Contador

def jugarHumano():#funcion apra que jueguen dos humano
    tablero = Tablero()
    estado = Estado(tablero)

    #asigna las fichas por defecto a cada juagdor
    fichaHumano1 = "X"
    fichaHumano2 = "O"

    #crea dos jugadores
    jugadorHumano1 = Humano(estado, fichaHumano1)
    jugadorHumano2 = Humano(estado, fichaHumano2)

    while not estado.terminado():#mientra el juego no termine alterna los turnos y cada jugador va haciendo su jugada
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador (" + fichaHumano1 +")")
            jugadorHumano1.hacerJugada()
        else:
            print("Turno del jugador (" + fichaHumano2 +")")
            jugadorHumano2.hacerJugada()

    resultado = estado.comprobar()#almacena el resultado

    linea = estado.buscarLineaGanadora()#almacena la linea ganadora si la hay
    tablero.pintar(lineaGanadora=linea)#si hay una linea ganadora pinta el tablero

    if resultado == "X":#muestra los resultados
        print("El jugador 1 (X) ha ganado")

    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    return resultado





def jugarMiniMax(fichaHumano,fichaIA):#funcion para que juegue un humano contra minMax
    tablero = Tablero()
    estado = Estado(tablero)

    #empieza el jugador que tenga la X
    if fichaHumano == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    #crea un humano y un jugador MinMax
    jugadorHumano = Humano(estado, fichaHumano)
    jugadorMiniMax = MiniMax(estado, fichaIA)

    while not estado.terminado():#mientra el juego no termine alterna los turnos y cada jugador va haciendo su jugada
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Humano " + fichaHumano)
            jugadorHumano.hacerJugada()
        else:
            print("Turno del jugador MinMax " + fichaIA)
            jugadorMiniMax.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    print("Total de nodos explorados por MiniMax: " + str(jugadorMiniMax.nodosTotal))
    print("Tiempo total empleado por MiniMax: " + str(jugadorMiniMax.tiempoTotal))


    return resultado



def jugarAlfaBeta(fichaHumano,fichaIA):#funcion para que juegue un humano contra AlfaBeta
    tablero = Tablero()
    estado = Estado(tablero)

    # empieza el jugador que tenga la X
    if fichaHumano == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    # crea un humano y un jugador AlfaBeta
    jugadorHumano = Humano(estado, fichaHumano)
    jugadorAlfaBeta = AlfaBeta(estado, fichaIA)

    while not estado.terminado():#mientra el juego no termine alterna los turnos y cada jugador va haciendo su jugada
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Humano " + fichaHumano)
            jugadorHumano.hacerJugada()
        else:
            print("Turno del jugador AlfaBeta " + fichaIA)
            jugadorAlfaBeta.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    print("Total de nodos explorados por Alfa-Beta: " + str(jugadorAlfaBeta.nodosTotal))
    print("Tiempo total empleado por Alfa-Beta: " + str(jugadorAlfaBeta.tiempoTotal))

    return resultado



def minMaxVSminMAX(fichaIA1,fichaIA2):#funcion para que jueguen dos MinMax
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaIA1 == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugador1 = MiniMax(estado, fichaIA1)
    jugador2 = MiniMax(estado, fichaIA2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador MinMax1 (" + fichaIA1 + ")")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador MinMax2 (" + fichaIA2 + ")")
            jugador2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    print("Total de nodos explorados por MiniMax1: " + str(jugador1.nodosTotal))
    print("Tiempo total empleado por MiniMax1: " + str(jugador1.tiempoTotal))
    print("\n")
    print("Total de nodos explorados por MiniMax2: " + str(jugador2.nodosTotal))
    print("Tiempo total empleado por MiniMax2: " + str(jugador2.tiempoTotal))


def AlfaBetaVSAlfaBeta(fichaIA1,fichaIA2):#funcion para que jueguen dos AlfaBeta
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaIA1 == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugador1 = AlfaBeta(estado, fichaIA1)
    jugador2 = AlfaBeta(estado, fichaIA2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador Alfa-Beta 1 (" + fichaIA1 + ")")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador Alfa-Beta 2 (" + fichaIA2 + ")")
            jugador2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    print("Total de nodos explorados por Alfa-Beta1: " + str(jugador1.nodosTotal))
    print("Tiempo total empleado por Alfa-Beta1: " + str(jugador1.tiempoTotal))
    print("\n")
    print("Total de nodos explorados por Alfa-Beta2: " + str(jugador2.nodosTotal))
    print("Tiempo total empleado por Alfa-Beta2: " + str(jugador2.tiempoTotal))



def MiniMaxVSAlfaBeta(fichaIA1,fichaIA2):#funcion para que juegue un MinMax contra un alfaBeta
    tablero = Tablero()
    estado = Estado(tablero)

    if fichaIA1 == "X":
        estado.turnoJugador = True
    else:
        estado.turnoJugador = False

    jugador1 = MiniMax(estado, fichaIA1)
    jugador2 = AlfaBeta(estado, fichaIA2)

    while not estado.terminado():
        tablero.pintar()
        print("\n")
        if estado.turnoJugador:
            print("Turno del jugador MinMax (" + fichaIA1 + ")")
            jugador1.hacerJugada()
        else:
            print("Turno del jugador Alfa-Beta (" + fichaIA2 + ")")
            jugador2.hacerJugada()

    resultado = estado.comprobar()

    linea = estado.buscarLineaGanadora()
    tablero.pintar(lineaGanadora=linea)

    if resultado == "X":
        print("El jugador 1 (X) ha ganado")
    elif resultado == "O":
        print("El jugador 2 (O) ha ganado")
    else:
        print("Empate")

    print("Total de nodos explorados por MiniMax: " + str(jugador1.nodosTotal))
    print("Tiempo total empleado por MiniMax: " + str(jugador1.tiempoTotal))
    print("\n")
    print("Total de nodos explorados por Alfa-Beta: " + str(jugador2.nodosTotal))
    print("Tiempo total empleado por Alfa-Beta: " + str(jugador2.tiempoTotal))

def mostrarResultados(archivo):#funcion para ver los resultados almacenados en el archivo
    contador=Contador(archivo)
    contador.mostrarResultados()


