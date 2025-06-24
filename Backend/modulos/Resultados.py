class Contador:
    def __init__(self,nombreArchivo):
        self.VictoriaHumano=0
        self.VictoriaIA=0
        self.empate=0
        self.nombreArchivo=nombreArchivo
        self.cargar()

    def resultados(self,resultado,fichaHumano,FichaIA):#metodo que incrementa las puntuaciones segun los resultados optenidos
        if resultado==fichaHumano:
            self.VictoriaHumano+=1
        elif resultado==FichaIA:
            self.VictoriaIA+=1
        else:
            self.empate+=1
        self.guardarResultados()


    def mostrarResultados(self):#muestra los resultados
        if self.nombreArchivo=="HumanoVSMinMax.txt":
            m="Humano VS MinMax"
        else:
            m="Humano VS AlfaBeta"

        print("\n")
        print("┌" + "───────────────────────────────────────────" + "┐")
        print("│" + "    Resultados " + m + "            " + "│")
        print("├" + "───────────────────────────────────────────" + "┤")
        print("│" + "                                           " + "│")
        print("│" + " Humano: "+str(self.VictoriaHumano) + "                                 " + "│")
        print("│" + " IA: " + str(self.VictoriaIA) + "                                     " + "│")
        print("│" + " Empates: " + str(self.empate) + "                                " + "│")
        print("│" + "                                           " + "│")
        print("└" + "───────────────────────────────────────────" + "┘")


    def guardarResultados(self):#guarda los resuñtados en el fichero
        with open(self.nombreArchivo,"w") as f:
            f.write(str(self.VictoriaHumano)+"\n")
            f.write(str(self.VictoriaIA)+"\n")
            f.write(str(self.empate)+"\n")

    def cargar(self):#carga los resultados contidos en el fichero

        f = open(self.nombreArchivo, "a+")
        f.seek(0)
        lineas=f.readlines()
        f.close()

        if len(lineas)>=2:
            self.VictoriaIA=int(lineas[0])
            self.empate=int(lineas[1])
        else:#aun no existe el fichero
            self.VictoriaHumano=0
            self.VictoriaIA=0
            self.empate=0

            self.guardarResultados()

