
from flask import Flask, request, jsonify, send_from_directory
from Backend.webgame import GameState, Minimax, AlfaBeta

app = Flask(__name__, static_folder='frontend', static_url_path='')

# Variables globales para la sesión del juego
estado = None
modo_juego = None

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/iniciar', methods=['POST'])
def iniciar_juego():
    global estado, modo_juego
    datos = request.json
    modo_juego = datos.get('modo')
    estado = GameState()
    return jsonify({"mensaje": f"Juego iniciado en modo {modo_juego}.", "tablero": estado.tablero})

@app.route('/movimiento', methods=['POST'])
def movimiento():
    global estado, modo_juego
    datos = request.json
    fila = datos.get('fila')
    columna = datos.get('columna')

    if estado.tablero[fila][columna] == "" and not estado.es_terminal():
        estado.tablero[fila][columna] = estado.turno

        if not estado.es_terminal():
            estado.cambiar_turno()

            if modo_juego == 'minimax':
                jugada = Minimax.elegir_jugada(estado)
                estado.tablero[jugada[0]][jugada[1]] = estado.turno
                if not estado.es_terminal():
                    estado.cambiar_turno()
            elif modo_juego == 'alfabeta':
                jugada = AlfaBeta.elegir_jugada(estado)
                estado.tablero[jugada[0]][jugada[1]] = estado.turno
                if not estado.es_terminal():
                    estado.cambiar_turno()

    return jsonify({
        "tablero": estado.tablero,
        "ganador": estado.ganador(),
        "empate": estado.es_empate(),
        "turno": estado.turno
    })

if __name__ == '__main__':
    app.run(debug=True)

