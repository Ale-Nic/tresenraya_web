from .Tablero import Tablero

class Estado:
    def __init__(self,tablero,fichaActual="X",turnoJugador=True):
        self.tablero = tablero
        self.turnoJugador=turnoJugador
        self.fichaActual=fichaActual



    def cambiarturno(self):#intercambia los turno
        self.turnoJugador=not self.turnoJugador
        if self.fichaActual=="X":
            self.fichaActual="O"
        else:
            self.fichaActual="X"


    def tableroLleno(self):#devuelve true si no quedan casillas libres
        for i in range(3):
            for j in range(3):
                if self.tablero.tablero[i][j]==" ":
                    return False
        return True

    def terminado(self):#devuelve true si algun jugador gano o se quedo en empate
        if self.tableroLleno() or self.comprobar()!=False:
            return True
        else:
            return False

    def comprobarHorizontales(self):#revisa si hay un ganador en alguna linea
        for i in range(3):
            if self.tablero.tablero[i][0]==self.tablero.tablero[i][1]==self.tablero.tablero[i][2] and self.tablero.tablero[i][0]=="O":
                return "O"
            elif self.tablero.tablero[i][0]==self.tablero.tablero[i][1]==self.tablero.tablero[i][2] and self.tablero.tablero[i][0]=="X":
                return "X"

        return False

    def comprobarVerticales(self):#revisa si hay un ganador en alguna columna
        for i in range(3):
            if self.tablero.tablero[0][i]==self.tablero.tablero[1][i]==self.tablero.tablero[2][i] and self.tablero.tablero[0][i]=="O":
                return "O"
            elif self.tablero.tablero[0][i]==self.tablero.tablero[1][i]==self.tablero.tablero[2][i] and self.tablero.tablero[0][i]=="X":
                return "X"

        return False


    def comprobarDiagonal1(self):#revisa si hay un ganador en la diagonal principal
        if self.tablero.tablero[0][0]==self.tablero.tablero[1][1]==self.tablero.tablero[2][2] and self.tablero.tablero[0][0]=="O":
            return "O"
        elif self.tablero.tablero[0][0]==self.tablero.tablero[1][1]==self.tablero.tablero[2][2] and self.tablero.tablero[0][0]=="X":
            return "X"

        return False


    def comprobarDiagonal2(self):#revisa si hay un ganador en la otra diagonal
        if self.tablero.tablero[0][2]==self.tablero.tablero[1][1]==self.tablero.tablero[2][0] and self.tablero.tablero[0][2]=="O":
            return "O"
        elif self.tablero.tablero[0][2]==self.tablero.tablero[1][1]==self.tablero.tablero[2][0] and self.tablero.tablero[0][2]=="X":
            return "X"

        return False

    def comprobar(self):#devuelve el ganador o false si no hay
        if(self.comprobarHorizontales()!=False):
            return self.comprobarHorizontales()
        elif(self.comprobarVerticales()!=False):
            return self.comprobarVerticales()
        elif(self.comprobarDiagonal1()!=False):
            return self.comprobarDiagonal1()
        elif(self.comprobarDiagonal2()!=False):
            return self.comprobarDiagonal2()
        else:
            return False

    def ganador(self,fichaIA):#es el metodo utilidad para la IA devuelve 1 si gana -1 si pierde y 0 si queda empate
        resultado=self.comprobar()
        if resultado is False:
            return 0
        if resultado== fichaIA:
            return 1
        else:
            return -1


    def movimientosValidos(self):#metodo que devuelve las casillas vacias
        movimientos=[]
        for i in range(3):
            for j in range(3):
                if self.tablero.tablero[i][j]==" ":
                    movimientos.append((i,j))
        return movimientos

    def copiarTablero(self):#crea una copia del tablero actual para poder generar sucesores si modificar el original
        tableroCopia=Tablero()
        tableroCopia.tablero=[fila[:] for fila in self.tablero.tablero]#crea una copia del tablero que no modifica el original
        return tableroCopia


    def sucesores(self):#devuelve una lista con todos los posible estados sucesores que resultarian al colocar una ficha en cada casilla vacia
        sucesores=[]

        for i,j in self.movimientosValidos():
            copia = self.copiarTablero()
            copia.tablero[i][j] = self.fichaActual

            if self.fichaActual=="X":
                ficha="O"
            else:
                ficha="X"
            nuevoEstado=Estado(tablero=copia,fichaActual=ficha,turnoJugador=not self.turnoJugador)

            sucesores.append((nuevoEstado,(i,j)))

        return sucesores



    def comprobarCasilla(self,pos):#devuevle true si una casilla esta vacia
        if self.tablero.tablero[pos[0]][pos[1]]==" ":
            return True
        else:
            return False


    def traductor(self,pos):#convierte las posiciones (1-9) introducidas por el usuario a las respectivas coordenas del tablero
        fila=(pos - 1) // 3
        columna = (pos - 1) % 3
        return fila, columna


    def jugada(self,pos,jugador):#para humano
        pos=self.traductor(pos)
        if self.comprobarCasilla(pos):
            self.tablero.tablero[pos[0]][pos[1]]=jugador

    def jugadaCoordenadas(self,fila,columna,jugador):#para ia
        if self.comprobarCasilla((fila,columna)):
            self.tablero.tablero[fila][columna]=jugador

    def jugadorActual(self):#devuelve la ficha que se esta jugando
        return self.fichaActual

    def buscarLineaGanadora(self):#funcion para devolver las casillas de la linea ganadora que se pintara en rojo
        for i in range(3):#buscar en horizontales
            if self.tablero.tablero[i][0]==self.tablero.tablero[i][1]==self.tablero.tablero[i][2] and self.tablero.tablero[i][0]!=" ":
                return [(i,0),(i,1),(i,2)]

        for i in range(3):#buscar en verticales
            if self.tablero.tablero[0][i]==self.tablero.tablero[1][i]==self.tablero.tablero[2][i] and self.tablero.tablero[0][i]!=" ":
                return [(0,i),(1,i),(2,i)]

        if self.tablero.tablero[0][0]==self.tablero.tablero[1][1]==self.tablero.tablero[2][2] and self.tablero.tablero[0][0]!=" ":
            return [(0,0),(1,1),(2,2)]

        if self.tablero.tablero[0][2]==self.tablero.tablero[1][1]==self.tablero.tablero[2][0] and self.tablero.tablero[0][2]!=" ":
            return [(0,2),(1,1),(2,0)]

        return None












