import time
class AlfaBeta:
    def __init__(self, estado,ficha):
        self.estado = estado
        self.ficha = ficha
        self.nodos = 0
        self.nodosTotal = 0
        self.tiempoTotal = 0

    def AlfaBeta(self,estado):#elige la mejor jugada
        mejorValor=float("-inf")
        alfa=float("-inf")
        beta=float("inf")
        mejorJugada=None

        for sucesor,jugada in estado.sucesores():#recorre todos los sucesores y llama a min pq el sucesor sera el oponente
            valor=self.MIN(sucesor,alfa,beta)

            if valor>mejorValor:#si encuentra un valor mejor  lo actualiza
                mejorValor=valor
                mejorJugada=jugada
            alfa=max(alfa,mejorValor)#alfa toma el mejor valor que se ha encontrado hasta el momento

        return mejorJugada#devuelve la mejor jugada

    def MAX(self,estado,alfa,beta):#maximiza
        self.nodos+=1
        if estado.terminado():
            return estado.ganador(self.ficha)#si gano alguien o se quedo empate devuelve el valor de la utilidad(1,-1 o 0)

        valor=float("-inf")
        for sucesor,_ in estado.sucesores():#recorre todos los sucesores y llama a min
            valor=max(valor,self.MIN(sucesor,alfa,beta))#guarda el valor maximo de todos los sucesores

            if valor>=beta:
                return valor#si el valor ya es mayor o igual que beta no necesita seguir explorando
            alfa=max(alfa,valor)#actualiza alfa

        return valor#devuelve el mejor valor encontrado

    def MIN(self,estado,alfa,beta):#minimiza
        self.nodos += 1
        if estado.terminado():
            return estado.ganador(self.ficha)

        valor=float("inf")
        for sucesor,_ in estado.sucesores():#recorre todos los sucesores y llama a max
            valor=min(valor,self.MAX(sucesor,alfa,beta))

            if valor<=alfa:
                return valor#si el valor ya es mayor o igual que alfa no necesita seguir explorando
            beta=min(beta,valor)#actualiza beta

        return valor#devuelve el valor minimo posible

    def hacerJugada(self):
        time.sleep(0.5)#pausa para que vaya mas despacio y me de tiempo a verlo
        #mide el tiempo de la juagada
        inicio = time.perf_counter_ns()
        fila,columna=self.AlfaBeta(self.estado)
        fin = time.perf_counter_ns()
        duracion = (fin - inicio) / 1000

        print("Nodos explorados: " + str(self.nodos))
        print("Tiempo empleado: " + str(duracion))

        self.nodosTotal += self.nodos
        self.tiempoTotal += duracion


        self.estado.jugadaCoordenadas(fila,columna,self.ficha)#realiza la juugada elegida y cambia el turno
        self.estado.cambiarturno()