import time
class MiniMax:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha
        self.nodos=0
        self.nodosTotal = 0
        self.tiempoTotal = 0

    def minimax(self, estado):#selecciona la mejor jugada posible
        if estado.jugadorActual()==self.ficha:#inicia el mejor valor en -inf si es el turno de la IA (maximiza) o inf si es el del oponente (minimo)
            mejorValor=float("-inf")
        else:
            mejorValor=float("inf")
        mejorJugada=None

        for sucesor,jugada in estado.sucesores():#recorre los sucesores y las jugadas de esos sucesores
            if sucesor.jugadorActual() == self.ficha:#dependiendo de quien sea el turno llama recursivamente a min o max
                valor = self.MAX(sucesor)
            else:
                valor = self.MIN(sucesor)

            if estado.jugadorActual()==self.ficha:# dependiendo de quien sea el turno llama recursivamente a min o max
                if valor>mejorValor:
                    mejorValor=valor
                    mejorJugada=jugada
            else:
                if valor<mejorValor:
                    mejorValor=valor
                    mejorJugada=jugada

        return mejorJugada#devuelve la mejor jugada

    def MAX(self,estado):#es el turno de la ia maximiza la utilidad
        self.nodos+=1
        if estado.terminado():#si gano alguien o se quedo empate devuelve el valor de la utilidad(1,-1 o 0)
            return estado.ganador(self.ficha)

        valorMax=float("-inf")
        for sucesor,_ in estado.sucesores():#recorre los sucesores y llama recursivamente a min o max
            if sucesor.jugadorActual() == self.ficha:
                valor=self.MAX(sucesor)
            else:
                valor=self.MIN(sucesor)
            valorMax=max(valorMax,valor)
        return valorMax#devuelve el valor maximo


    def MIN(self,estado):#es el turno del oponente minimiza la utilidad
        self.nodos += 1
        if estado.terminado():
            return estado.ganador(self.ficha)

        valorMin=float("inf")
        for sucesor,_ in estado.sucesores():#recorre los sucesores y elige el minimo valor
            if sucesor.jugadorActual() == self.ficha:
                valor=self.MAX(sucesor)
            else:
                valor=self.MIN(sucesor)
            valorMin=min(valorMin,valor)
        return valorMin



    def hacerJugada(self):
        time.sleep(0.5)#pausa para que vaya mas despacio y me de tiempo a verlo
        #mide el tiempo de la juagada
        inicio = time.perf_counter_ns()
        fila,columna=self.minimax(self.estado)
        fin = time.perf_counter_ns()
        duracion=(fin-inicio)/1000

        print("Nodos explorados: " + str(self.nodos))
        print("Tiempo empleado: " + str(duracion))

        self.nodosTotal+=self.nodos
        self.tiempoTotal+=duracion

        self.estado.jugadaCoordenadas(fila,columna,self.ficha)#realiza la juugada elegida y cambia el turno
        self.estado.cambiarturno()

