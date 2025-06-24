
class GameState:
    def __init__(self, tablero=None, turno="X"):
        self.tablero = tablero or [["", "", ""], ["", "", ""], ["", "", ""]]
        self.turno = turno

    def copiar(self):
        return GameState([fila[:] for fila in self.tablero], self.turno)

    def cambiar_turno(self):
        self.turno = "O" if self.turno == "X" else "X"

    def jugadas_validas(self):
        movimientos = []
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == "":
                    movimientos.append((i, j))
        return movimientos

    def ganador(self):
        b = self.tablero
        lineas = [
            b[0], b[1], b[2],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]],
        ]
        for linea in lineas:
            if linea[0] != "" and linea.count(linea[0]) == 3:
                return linea[0]
        return None

    def es_empate(self):
        return self.ganador() is None and all(c != "" for fila in self.tablero for c in fila)

    def es_terminal(self):
        return self.ganador() is not None or self.es_empate()


class Minimax:
    @staticmethod
    def elegir_jugada(estado: GameState):
        ficha_ia = estado.turno

        def minimax(est: GameState, jugador: str):
            ganador = est.ganador()
            if ganador:
                return (1 if ganador == ficha_ia else -1), None
            if est.es_empate():
                return 0, None

            if jugador == ficha_ia:
                mejor_valor = float("-inf")
                mejor_jugada = None
                for i, j in est.jugadas_validas():
                    nuevo = est.copiar()
                    nuevo.tablero[i][j] = jugador
                    nuevo.cambiar_turno()
                    val, _ = minimax(nuevo, nuevo.turno)
                    if val > mejor_valor:
                        mejor_valor, mejor_jugada = val, (i, j)
                return mejor_valor, mejor_jugada
            else:
                peor_valor = float("inf")
                peor_jugada = None
                for i, j in est.jugadas_validas():
                    nuevo = est.copiar()
                    nuevo.tablero[i][j] = jugador
                    nuevo.cambiar_turno()
                    val, _ = minimax(nuevo, nuevo.turno)
                    if val < peor_valor:
                        peor_valor, peor_jugada = val, (i, j)
                return peor_valor, peor_jugada

        _, jugada = minimax(estado, estado.turno)
        return jugada


class AlfaBeta:
    @staticmethod
    def elegir_jugada(estado: GameState):
        ficha_ia = estado.turno

        def alphabeta(est: GameState, jugador: str, alfa: float, beta: float):
            ganador = est.ganador()
            if ganador:
                return (1 if ganador == ficha_ia else -1), None
            if est.es_empate():
                return 0, None

            if jugador == ficha_ia:
                valor = float("-inf")
                mejor = None
                for i, j in est.jugadas_validas():
                    nuevo = est.copiar()
                    nuevo.tablero[i][j] = jugador
                    nuevo.cambiar_turno()
                    val, _ = alphabeta(nuevo, nuevo.turno, alfa, beta)
                    if val > valor:
                        valor, mejor = val, (i, j)
                    alfa = max(alfa, valor)
                    if beta <= alfa:
                        break
                return valor, mejor
            else:
                valor = float("inf")
                mejor = None
                for i, j in est.jugadas_validas():
                    nuevo = est.copiar()
                    nuevo.tablero[i][j] = jugador
                    nuevo.cambiar_turno()
                    val, _ = alphabeta(nuevo, nuevo.turno, alfa, beta)
                    if val < valor:
                        valor, mejor = val, (i, j)
                    beta = min(beta, valor)
                    if beta <= alfa:
                        break
                return valor, mejor

        _, jugada = alphabeta(estado, estado.turno, float("-inf"), float("inf"))
        return jugada

