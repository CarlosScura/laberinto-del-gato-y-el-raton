'''
Pseudocodigo de las funciones.

# def imprimir_tablero(state):
#     crear matriz 4x4 con "."
#     colocar "M" en posición del ratón
#     colocar "C" en posición del gato
#     mostrar en consola

# def movimientos_validos(state, player):
#     devolver lista de posiciones dentro del tablero (no salir de 4x4)

# def aplicar_movimiento(state, move, player):
#     devolver nuevo estado con jugador movido

# def es_terminal(state):
#     True si gato == ratón (captura)
#     False en otro caso

# def evaluar(state):
#     devolver distancia Manhattan entre gato y ratón
#     (ratón quiere maximizar, gato quiere minimizar)

'''
# definimos las posiciones del gato y el raton. lo hacemos asi para que sea escalable mas adelante.

pos_gato = (0,0) # esquina superior izquierda
pos_raton = (0,4) # esquina superior derecha

# definimos el tablero como diccionario con las posiciones, tamaño y matriz.

tablero = {
    "gato": (pos_gato),
    "raton": (pos_raton),
    "tamaño": (5, 5),
}

# creamos la matriz del tablero y la anexamos al diccionario.

tablero["matriz"] = [["." for j in range(tablero["tamaño"][1])] for i in range(tablero["tamaño"][0])]

# creamos la funcion mostrar tablero.

def mostrar_tablero():
    x_gato, y_gato = tablero['gato']
    x_raton, y_raton = tablero['raton']
    filas, columnas = tablero["tamaño"]
    
    tablero["matriz"] = [["." for j in range(columnas)] for i in range(filas)]
    tablero["matriz"][x_gato][y_gato] = "G"
    tablero["matriz"][x_raton][y_raton] = "R"

    for fila in tablero["matriz"]:
        print(" ".join(fila))

# creamos la funcion para controlar los movimientos del jugador.
# usamos un for para calcular la nueva posición y verificamos que esté dentro del tablero.

def movimientos_validos(tablero, jugador):
    x, y = tablero[jugador]
    filas, columnas = tablero["tamaño"]
    movimientos = []

    for cambio_x, cambio_y in [(0,1), (0,-1), (1,0), (-1,0)]:
        nueva_x, nueva_y = x + cambio_x, y + cambio_y

        if 0 <= nueva_x < filas and 0 <= nueva_y < columnas:
            movimientos.append((nueva_x, nueva_y))

    return movimientos

# creamos la funcion para realizar el movimiento del jugador.

def aplicar_movimiento(tablero, movimiento, jugador):
    tablero[jugador] = movimiento

# creamos una funcion para controlar si el juego terminó o no.

def fin_juego(tablero, turnos):
    if tablero["gato"] == tablero["raton"]:
        return True
    else:   return False

# creamos la funcion de distancia Manhattan para evaluar el estado del juego.

def dist_manh(tablero):
    x_gato, y_gato = tablero["gato"]
    x_raton, y_raton = tablero["raton"]

    return abs(x_gato - x_raton) + abs(y_gato - y_raton)
