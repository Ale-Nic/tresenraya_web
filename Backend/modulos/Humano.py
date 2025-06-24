
class Humano:
    def __init__(self,estado,ficha):
        self.estado = estado
        self.tablero=estado.tablero
        self.ficha=ficha


    def hacerJugada(self):
        while True:
            pos=int(input("Introduce un movimiento " + self.ficha + ": "))
            if pos<1 or pos>9:
                print("Movimiento incorrecto debe estar entre 1 y 9")
                continue

            f,c=self.estado.traductor(pos)
            if not self.estado.comprobarCasilla((f,c)):
                print("Casilla ocupada, introduzca otra")
                continue

            self.estado.jugada(pos,self.ficha)
            self.estado.cambiarturno()
            break





