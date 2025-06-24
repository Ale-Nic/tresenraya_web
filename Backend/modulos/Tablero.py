
def red(texto):#funcion para mostrar el texto en color rojo
    ROJO = "\033[31m"#codigo del rojo
    RESET = "\033[0m"#codigo para restablecer el color por defecto
    return ROJO + texto + RESET

class Tablero:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]#crea un tablero 3x3 vacio

    def pintar(self,lineaGanadora=None):#muestra el tablero la linea ganadora sera la que se pinte en rojo
        print("╔═══╦═══╦═══╗")
        for i in range(3):
            print("║ ", end="")#para cada fila del tablero pinta el borde izwuierdo y deja un espacio
            for j in range(3):
                if lineaGanadora is not None and (i,j) in lineaGanadora:#si hay una linea ganadora y la celda actual esta en esa linea la pinta en rojo
                    print(red(self.tablero[i][j]), end="")
                else:
                    print(self.tablero[i][j], end="")#si no pinta la celda en el color predeterminado
                if j<2:#pinta un separador en las columnas 0 y 1
                    print(" ║ ", end="")
                else:#pinta el separador final
                    print(" ║")
            if i<2:#pinta un separador en las linea 0 y 1
                print("╠═══╬═══╬═══╣")
        print("╚═══╩═══╩═══╝")












